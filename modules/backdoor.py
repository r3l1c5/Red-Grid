"""Controlled backdoor behavior simulation for the Red-Grid laboratory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
BACKDOOR_DIR = LAB_ROOT / "backdoor"

CONFIG_FILE = BACKDOOR_DIR / "simulated_config.json"
COMMAND_LOG_FILE = BACKDOOR_DIR / "simulated_command_log.json"
REPORT_FILE = BACKDOOR_DIR / "behavior_report.txt"


SIMULATED_COMMANDS = [
    {
        "command_id": 1,
        "command": "system_info",
        "description": "Request simulated system information",
    },
    {
        "command_id": 2,
        "command": "list_files",
        "description": "Request simulated file listing",
    },
    {
        "command_id": 3,
        "command": "status",
        "description": "Request simulated implant status",
    },
    {
        "command_id": 4,
        "command": "disconnect",
        "description": "Terminate the simulated session",
    },
]


SIMULATED_RESPONSES = {
    "system_info": {
        "hostname": "REDGRID-LAB-HOST",
        "platform": "SIMULATED-WINDOWS",
        "user": "lab_user",
    },
    "list_files": {
        "files": [
            "training_document.txt",
            "simulation_config.json",
            "analysis_notes.txt",
        ]
    },
    "status": {
        "implant_status": "SIMULATED_ACTIVE",
        "network_connection": False,
        "persistence": False,
    },
    "disconnect": {
        "session_status": "SIMULATED_DISCONNECTED",
    },
}


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create the isolated backdoor laboratory directory."""
    BACKDOOR_DIR.mkdir(parents=True, exist_ok=True)


def write_config() -> None:
    """Write explicit backdoor simulation safety configuration."""
    config = {
        "simulation": True,
        "component": "backdoor",
        "sample_id": "REDGRID-BACKDOOR-001",
        "command_source": "predefined_local_queue",
        "real_listener": False,
        "network_socket": False,
        "external_network_access": False,
        "c2_communication": False,
        "arbitrary_command_execution": False,
        "shell_execution": False,
        "persistence_enabled": False,
        "remote_access": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def simulate_command(command: dict) -> dict:
    """Process a predefined command without executing system commands."""
    command_name = command["command"]

    response = SIMULATED_RESPONSES.get(
        command_name,
        {"status": "UNKNOWN_SIMULATED_COMMAND"},
    )

    return {
        "command_id": command["command_id"],
        "command": command_name,
        "description": command["description"],
        "timestamp": utc_timestamp(),
        "source": "local_simulated_c2_queue",
        "execution": "SIMULATED",
        "response": response,
    }


def write_command_log(events: list[dict]) -> None:
    """Write simulated C2 command activity."""
    command_log = {
        "simulation": True,
        "component": "backdoor",
        "event_count": len(events),
        "events": events,
        "network_connection": False,
        "external_c2": False,
        "timestamp": utc_timestamp(),
    }

    COMMAND_LOG_FILE.write_text(
        json.dumps(command_log, indent=4),
        encoding="utf-8",
    )


def write_report(events: list[dict]) -> None:
    """Write a defender-oriented backdoor behavior report."""
    report = f"""Red-Grid Backdoor Simulation Report
====================================

Simulation status: SAFE / SIMULATED

Component:
    Backdoor behavior simulation

Command events:
    {len(events)}

Real network listener:
    No

Real network socket:
    No

External C2 communication:
    No

Remote access:
    No

Shell execution:
    No

Arbitrary command execution:
    No

Persistence:
    No

Simulation behavior:
    Red-Grid simulated a backdoor command-and-control workflow
    using a predefined local command queue.

    Commands were processed by a controlled dispatcher and returned
    predefined synthetic responses.

    No operating-system commands were executed.

Safety boundary:
    The simulation does not create a listening service, open network
    sockets, contact a C2 server, accept remote connections, execute
    shell commands, or establish persistence.

Defender observation points:
    - Unexpected listening services
    - Suspicious outbound connections
    - Persistent command-and-control communication
    - Unusual parent-child process relationships
    - Repeated beacon-like activity
    - Unexpected command execution
    - Persistence associated with remote-access components

Red-Grid did not create a network backdoor or provide actual remote
command execution.
"""

    REPORT_FILE.write_text(
        report,
        encoding="utf-8",
    )


def simulate() -> None:
    """Demonstrate controlled backdoor behavior."""
    print()
    print("Backdoor Behavior Simulation")
    print("============================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()

    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print()

    print("[SIMULATION] Loading predefined command queue...")

    events = []

    for command in SIMULATED_COMMANDS:
        print(
            f"[+] Simulated command received: "
            f"{command['command']}"
        )

        event = simulate_command(command)
        events.append(event)

        print("[+] Simulated response generated.")

    write_command_log(events)
    write_report(events)

    print()
    print("[+] Command log:", COMMAND_LOG_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No network listener, external C2 connection, "
        "remote access, shell execution, or persistence occurred."
    )
    print()


if __name__ == "__main__":
    simulate()