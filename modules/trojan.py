"""Controlled Trojan behavior simulation for the Red-Grid laboratory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
TROJAN_DIR = LAB_ROOT / "trojan"
PAYLOAD_DIR = TROJAN_DIR / "simulated_payload"

CONFIG_FILE = TROJAN_DIR / "simulated_config.json"
EXECUTION_FILE = TROJAN_DIR / "simulated_execution.json"
REPORT_FILE = TROJAN_DIR / "behavior_report.txt"


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create the isolated Trojan laboratory environment."""
    PAYLOAD_DIR.mkdir(parents=True, exist_ok=True)


def write_config() -> None:
    """Write explicit Trojan simulation safety configuration."""
    config = {
        "simulation": True,
        "component": "trojan",
        "sample_id": "REDGRID-TROJAN-001",
        "payload_type": "benign_simulated_payload",
        "deception_simulated": True,
        "real_program_execution": False,
        "arbitrary_command_execution": False,
        "persistence_enabled": False,
        "external_network_access": False,
        "c2_communication": False,
        "system_modification": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def create_simulated_payload() -> Path:
    """Create a harmless payload description artifact."""
    payload = {
        "simulation": True,
        "payload_id": "REDGRID-PAYLOAD-001",
        "payload_name": "Benign Training Payload",
        "purpose": "Demonstrate Trojan payload execution concept",
        "actual_execution": False,
        "actions": [
            "Display simulated payload activation",
            "Generate local training telemetry",
            "Write a behavior event",
        ],
        "dangerous_actions": False,
        "timestamp": utc_timestamp(),
    }

    payload_file = PAYLOAD_DIR / "payload_manifest.json"

    payload_file.write_text(
        json.dumps(payload, indent=4),
        encoding="utf-8",
    )

    return payload_file


def simulate_delivery(payload_file: Path) -> dict:
    """Simulate deceptive delivery of a Trojan payload."""
    return {
        "stage": "delivery",
        "timestamp": utc_timestamp(),
        "artifact": str(payload_file),
        "delivery_method": "simulated_deceptive_launcher",
        "real_delivery": False,
        "status": "SIMULATED",
    }


def simulate_execution(payload_file: Path) -> dict:
    """Simulate activation without executing arbitrary code."""
    return {
        "stage": "execution",
        "timestamp": utc_timestamp(),
        "artifact": str(payload_file),
        "execution_type": "simulated_payload_activation",
        "actual_code_execution": False,
        "arbitrary_command_execution": False,
        "status": "SIMULATED",
    }


def write_execution_log(events: list[dict]) -> None:
    """Write simulated Trojan execution events."""
    execution = {
        "simulation": True,
        "component": "trojan",
        "event_count": len(events),
        "events": events,
        "system_modified": False,
        "external_communication": False,
        "timestamp": utc_timestamp(),
    }

    EXECUTION_FILE.write_text(
        json.dumps(execution, indent=4),
        encoding="utf-8",
    )


def write_report(events: list[dict]) -> None:
    """Write a defender-oriented Trojan behavior report."""
    report = f"""Red-Grid Trojan Simulation Report
==================================

Simulation status: SAFE / SIMULATED

Component:
    Trojan behavior simulation

Payload directory:
    {PAYLOAD_DIR}

Simulation stages:
    {len(events)}

Real program execution:
    No

Arbitrary command execution:
    No

System modification:
    No

Persistence:
    No

External network communication:
    No

C2 communication:
    No

Simulation behavior:
    Red-Grid simulated the Trojan lifecycle by representing a
    deceptive delivery mechanism followed by activation of a
    harmless training payload.

    The payload is represented by a local manifest and telemetry
    artifacts. No executable malicious payload was launched.

Safety boundary:
    The simulation does not execute arbitrary code, modify the
    operating system, establish persistence, communicate with
    external infrastructure, or provide remote access.

Defender observation points:
    - Unexpected execution of unfamiliar applications
    - Programs masquerading as legitimate software
    - Suspicious parent-child process relationships
    - Unexpected file creation following application execution
    - Attempts to establish persistence
    - Unexpected network connections after execution
    - Suspicious payload staging behavior

Red-Grid did not execute arbitrary commands, modify system files,
establish persistence, communicate with C2 infrastructure, or
provide remote access.
"""

    REPORT_FILE.write_text(
        report,
        encoding="utf-8",
    )


def simulate() -> None:
    """Demonstrate controlled Trojan behavior."""
    print()
    print("Trojan Behavior Simulation")
    print("==========================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()

    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print()

    print("[SIMULATION] Preparing benign simulated payload...")

    payload_file = create_simulated_payload()

    print(f"[+] Created payload manifest: {payload_file}")
    print()

    print("[SIMULATION] Simulating deceptive delivery...")

    delivery_event = simulate_delivery(payload_file)

    print("[+] Simulated payload delivery.")

    print()
    print("[SIMULATION] Simulating payload activation...")

    execution_event = simulate_execution(payload_file)

    print("[+] Simulated payload activation.")
    print("[+] No actual executable payload was launched.")

    events = [
        delivery_event,
        execution_event,
    ]

    write_execution_log(events)
    write_report(events)

    print()
    print("[+] Execution log:", EXECUTION_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No arbitrary code execution, persistence, system "
        "modification, C2 communication, or remote access occurred."
    )
    print()


if __name__ == "__main__":
    simulate()