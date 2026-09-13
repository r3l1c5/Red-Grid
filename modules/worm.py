"""Controlled worm behavior simulation for the Red-Grid laboratory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
WORM_DIR = LAB_ROOT / "worm"
HOSTS_DIR = WORM_DIR / "simulated_hosts"

CONFIG_FILE = WORM_DIR / "simulated_config.json"
PROPAGATION_FILE = WORM_DIR / "simulated_propagation.json"
REPORT_FILE = WORM_DIR / "behavior_report.txt"


SIMULATED_HOSTS = {
    "HOST-001": {
        "address": "10.0.0.101",
        "status": "reachable",
    },
    "HOST-002": {
        "address": "10.0.0.102",
        "status": "reachable",
    },
    "HOST-003": {
        "address": "10.0.0.103",
        "status": "reachable",
    },
    "HOST-004": {
        "address": "10.0.0.104",
        "status": "reachable",
    },
}


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create fake hosts used exclusively by the simulation."""
    HOSTS_DIR.mkdir(parents=True, exist_ok=True)

    for host_id, host_info in SIMULATED_HOSTS.items():
        host_dir = HOSTS_DIR / host_id
        host_dir.mkdir(parents=True, exist_ok=True)

        host_config = {
            "host_id": host_id,
            "address": host_info["address"],
            "status": host_info["status"],
            "simulation": True,
        }

        config_path = host_dir / "host_config.json"

        config_path.write_text(
            json.dumps(host_config, indent=4),
            encoding="utf-8",
        )


def write_config() -> None:
    """Write explicit worm simulation safety configuration."""
    config = {
        "simulation": True,
        "component": "worm",
        "sample_id": "REDGRID-WORM-001",
        "propagation_mode": "simulated",
        "target_scope": str(HOSTS_DIR),
        "real_network_scanning": False,
        "real_network_connections": False,
        "real_exploitation": False,
        "real_propagation": False,
        "persistence_enabled": False,
        "external_network_access": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def discover_simulated_hosts() -> list[Path]:
    """Discover only fake hosts created by the laboratory."""
    return sorted(
        path
        for path in HOSTS_DIR.iterdir()
        if path.is_dir()
    )


def simulate_propagation(host_path: Path) -> dict:
    """Simulate worm propagation to a fake laboratory host."""
    host_config_path = host_path / "host_config.json"

    host_config = json.loads(
        host_config_path.read_text(encoding="utf-8")
    )

    propagation_marker = {
        "simulation": True,
        "infected": True,
        "infection_method": "simulated_propagation",
        "timestamp": utc_timestamp(),
    }

    marker_path = host_path / "simulated_infection.json"

    marker_path.write_text(
        json.dumps(propagation_marker, indent=4),
        encoding="utf-8",
    )

    return {
        "host_id": host_config["host_id"],
        "address": host_config["address"],
        "operation": "simulated_propagation",
        "network_connection": False,
        "exploitation": False,
        "status": "SIMULATED",
        "timestamp": utc_timestamp(),
    }


def write_propagation_log(events: list[dict]) -> None:
    """Write simulated propagation events."""
    propagation = {
        "simulation": True,
        "component": "worm",
        "event_count": len(events),
        "events": events,
        "real_network_activity": False,
        "real_propagation": False,
        "timestamp": utc_timestamp(),
    }

    PROPAGATION_FILE.write_text(
        json.dumps(propagation, indent=4),
        encoding="utf-8",
    )


def write_report(events: list[dict]) -> None:
    """Write a defender-oriented worm behavior report."""
    report = f"""Red-Grid Worm Simulation Report
================================

Simulation status: SAFE / SIMULATED

Component:
    Worm behavior simulation

Simulated host environment:
    {HOSTS_DIR}

Hosts processed:
    {len(events)}

Real network scanning:
    No

Real network connections:
    No

Real exploitation:
    No

Real propagation:
    No

Persistence:
    No

External network communication:
    No

Simulation behavior:
    Red-Grid created a collection of synthetic hosts and simulated
    propagation between those hosts.

    Each simulated infection is represented by a local JSON artifact
    inside the corresponding laboratory host directory.

Safety boundary:
    The host addresses are synthetic data. They were not scanned,
    contacted, exploited, or modified over a real network.

Defender observation points:
    - Unexpected host-to-host propagation
    - Rapid creation of similar files across systems
    - Repeated process or service activity
    - Suspicious network discovery behavior
    - Multiple systems showing similar compromise indicators
    - Unusual authentication or execution patterns
    - Repeated connections between previously unrelated hosts

Red-Grid did not scan the real network, establish network connections,
exploit systems, or propagate outside the laboratory environment.
"""

    REPORT_FILE.write_text(report, encoding="utf-8")


def simulate() -> None:
    """Demonstrate controlled worm propagation behavior."""
    print()
    print("Worm Behavior Simulation")
    print("========================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()

    print(f"[+] Created simulated hosts: {HOSTS_DIR}")
    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print()

    print("[SIMULATION] Discovering simulated hosts...")

    hosts = discover_simulated_hosts()

    print(f"[+] Discovered {len(hosts)} simulated hosts.")
    print()

    print("[SIMULATION] Simulating worm propagation...")

    events = []

    for host_path in hosts:
        event = simulate_propagation(host_path)
        events.append(event)

        print(
            f"[+] Simulated propagation: "
            f"{event['host_id']} ({event['address']})"
        )

    write_propagation_log(events)
    write_report(events)

    print()
    print("[+] Propagation log:", PROPAGATION_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No real network scanning, connections, exploitation, "
        "or propagation occurred."
    )
    print()


if __name__ == "__main__":
    simulate()