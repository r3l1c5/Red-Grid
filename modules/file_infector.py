"""Controlled file-infector behavior simulation for the Red-Grid laboratory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
INFECTOR_DIR = LAB_ROOT / "file_infector"
TARGET_DIR = INFECTOR_DIR / "target_files"

CONFIG_FILE = INFECTOR_DIR / "simulated_config.json"
INFECTION_FILE = INFECTOR_DIR / "simulated_infections.json"
REPORT_FILE = INFECTOR_DIR / "behavior_report.txt"


SAMPLE_FILES = {
    "document_01.txt": (
        "Red-Grid synthetic document 01.\n"
        "This file belongs exclusively to the laboratory.\n"
    ),
    "document_02.txt": (
        "Red-Grid synthetic document 02.\n"
        "No real user data is contained in this file.\n"
    ),
    "research_notes.txt": (
        "Red-Grid laboratory research notes.\n"
        "File-infector behavior simulation.\n"
    ),
}


SIMULATION_MARKER = (
    "\n"
    "[RED-GRID SIMULATED FILE INFECTOR MARKER]\n"
    "[SIMULATION ONLY - NO EXECUTABLE CODE]\n"
)


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create the isolated file-infector laboratory."""
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    for filename, content in SAMPLE_FILES.items():
        file_path = TARGET_DIR / filename

        if not file_path.exists():
            file_path.write_text(
                content,
                encoding="utf-8",
            )


def write_config() -> None:
    """Write explicit file-infector simulation safety configuration."""
    config = {
        "simulation": True,
        "component": "file_infector",
        "sample_id": "REDGRID-FILE-INFECTOR-001",
        "target_scope": str(TARGET_DIR),
        "target_file_type": "synthetic_text_files",
        "real_user_files": False,
        "executable_code_injection": False,
        "binary_modification": False,
        "self_replication": False,
        "real_propagation": False,
        "persistence_enabled": False,
        "external_network_access": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def discover_target_files() -> list[Path]:
    """Discover only files inside the dedicated laboratory directory."""
    return sorted(
        path
        for path in TARGET_DIR.iterdir()
        if path.is_file()
    )


def simulate_infection(file_path: Path) -> dict:
    """
    Apply a harmless simulation marker to a laboratory file.

    No executable code is inserted and no binary files are modified.
    """
    content = file_path.read_text(encoding="utf-8")

    if SIMULATION_MARKER.strip() in content:
        return {
            "filename": file_path.name,
            "operation": "already_simulated",
            "status": "SKIPPED",
            "timestamp": utc_timestamp(),
        }

    modified_content = content + SIMULATION_MARKER

    file_path.write_text(
        modified_content,
        encoding="utf-8",
    )

    return {
        "filename": file_path.name,
        "operation": "simulated_infection",
        "code_injected": False,
        "self_replication": False,
        "status": "SIMULATED",
        "timestamp": utc_timestamp(),
    }


def write_infection_log(events: list[dict]) -> None:
    """Write simulated file-infection events."""
    infection_log = {
        "simulation": True,
        "component": "file_infector",
        "event_count": len(events),
        "events": events,
        "executable_code_injected": False,
        "real_propagation": False,
        "timestamp": utc_timestamp(),
    }

    INFECTION_FILE.write_text(
        json.dumps(infection_log, indent=4),
        encoding="utf-8",
    )


def write_report(events: list[dict]) -> None:
    """Write a defender-oriented file-infector report."""
    infected_count = sum(
        1
        for event in events
        if event["status"] == "SIMULATED"
    )

    report = f"""Red-Grid File Infector Simulation Report
===========================================

Simulation status: SAFE / SIMULATED

Component:
    File-infector behavior simulation

Target directory:
    {TARGET_DIR}

Files processed:
    {len(events)}

Files marked as simulated:
    {infected_count}

Real user files modified:
    No

Executable code injected:
    No

Binary files modified:
    No

Self-replication:
    No

Real propagation:
    No

Persistence:
    No

External network communication:
    No

Simulation behavior:
    Red-Grid created synthetic text files inside a dedicated
    laboratory directory and applied a harmless simulation marker.

    The marker represents the conceptual idea of a file being
    modified by an infector without inserting executable code.

Safety boundary:
    Only files created by this module inside the dedicated
    laboratory directory were processed.

Defender observation points:
    - Unexpected modifications to executable or document files
    - Repeated modification of multiple files
    - Changes to file hashes or integrity metadata
    - Unexpected changes immediately after process execution
    - Suspicious modification timestamps
    - Processes accessing large numbers of files
    - Unexpected code injection into executable files

Red-Grid did not inject executable code, modify binary files,
replicate across the system, modify user files, or communicate
with external infrastructure.
"""

    REPORT_FILE.write_text(
        report,
        encoding="utf-8",
    )


def simulate() -> None:
    """Demonstrate controlled file-infector behavior."""
    print()
    print("File Infector Behavior Simulation")
    print("=================================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()

    print(f"[+] Created laboratory files: {TARGET_DIR}")
    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print()

    print("[SIMULATION] Discovering laboratory target files...")

    target_files = discover_target_files()

    print(
        f"[+] Discovered {len(target_files)} "
        "synthetic target files."
    )
    print()

    print("[SIMULATION] Simulating file infection...")

    events = []

    for file_path in target_files:
        event = simulate_infection(file_path)
        events.append(event)

        print(
            f"[+] Simulated infection: "
            f"{file_path.name}"
        )

    write_infection_log(events)
    write_report(events)

    print()
    print("[+] Infection log:", INFECTION_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No executable code was injected, no binary files "
        "were modified, and no real user files were accessed."
    )
    print()


if __name__ == "__main__":
    simulate()