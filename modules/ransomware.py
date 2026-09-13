"""Controlled ransomware behavior simulation for the Red-Grid laboratory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
RANSOMWARE_DIR = LAB_ROOT / "ransomware"
VICTIM_DIR = RANSOMWARE_DIR / "victim_files"

CONFIG_FILE = RANSOMWARE_DIR / "simulated_config.json"
IMPACT_FILE = RANSOMWARE_DIR / "simulated_impact.json"
REPORT_FILE = RANSOMWARE_DIR / "behavior_report.txt"


SAMPLE_FILES = {
    "document_01.txt": (
        "Red-Grid ransomware simulation document.\n"
        "This file exists only inside the controlled laboratory.\n"
    ),
    "document_02.txt": (
        "Synthetic research document for ransomware behavior analysis.\n"
        "No real user data is stored here.\n"
    ),
    "research_notes.txt": (
        "Laboratory notes:\n"
        "- Malware behavior simulation\n"
        "- Defensive analysis\n"
        "- Incident response training\n"
    ),
}


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create the isolated ransomware laboratory environment."""
    VICTIM_DIR.mkdir(parents=True, exist_ok=True)

    for filename, content in SAMPLE_FILES.items():
        file_path = VICTIM_DIR / filename

        if not file_path.exists():
            file_path.write_text(content, encoding="utf-8")


def write_config() -> None:
    """Write explicit safety and simulation configuration."""
    config = {
        "simulation": True,
        "component": "ransomware",
        "sample_id": "REDGRID-RANSOMWARE-001",
        "target_scope": str(VICTIM_DIR),
        "real_user_files": False,
        "real_encryption": False,
        "reversible_operation": True,
        "persistence_enabled": False,
        "external_network_access": False,
        "ransom_payment": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def discover_lab_files() -> list[Path]:
    """Discover files only inside the dedicated laboratory directory."""
    files = []

    for file_path in VICTIM_DIR.iterdir():
        if file_path.is_file():
            files.append(file_path)

    return sorted(files)


def simulate_impact(file_path: Path) -> dict:
    """
    Apply a reversible simulation marker to a laboratory file.

    No encryption is performed. The original content is preserved inside
    the file using a clearly identifiable simulation format.
    """
    original_content = file_path.read_text(encoding="utf-8")

    simulated_content = (
        "[RED-GRID SIMULATED RANSOMWARE STATE]\n"
        "[REAL ENCRYPTION: FALSE]\n"
        "[LAB-ONLY FILE]\n\n"
        f"{original_content}"
    )

    file_path.write_text(
        simulated_content,
        encoding="utf-8",
    )

    return {
        "filename": file_path.name,
        "operation": "simulated_file_lock",
        "encryption_performed": False,
        "reversible": True,
        "timestamp": utc_timestamp(),
        "status": "SIMULATED",
    }


def recover_file(file_path: Path) -> bool:
    """Restore a file modified by the simulation."""
    content = file_path.read_text(encoding="utf-8")

    marker = (
        "[RED-GRID SIMULATED RANSOMWARE STATE]\n"
        "[REAL ENCRYPTION: FALSE]\n"
        "[LAB-ONLY FILE]\n\n"
    )

    if not content.startswith(marker):
        return False

    original_content = content[len(marker):]
    file_path.write_text(original_content, encoding="utf-8")

    return True


def write_impact_log(events: list[dict]) -> None:
    """Write simulated ransomware impact information."""
    impact = {
        "simulation": True,
        "component": "ransomware",
        "event_count": len(events),
        "events": events,
        "external_network_communication": False,
        "real_encryption": False,
        "timestamp": utc_timestamp(),
    }

    IMPACT_FILE.write_text(
        json.dumps(impact, indent=4),
        encoding="utf-8",
    )


def write_report(events: list[dict], recovered_count: int) -> None:
    """Write a defender-oriented ransomware behavior report."""
    report = f"""Red-Grid Ransomware Simulation Report
======================================

Simulation status: SAFE / SIMULATED

Component:
    Ransomware behavior simulation

Target scope:
    {VICTIM_DIR}

Files targeted:
    {len(events)}

Files recovered:
    {recovered_count}

Real encryption:
    No

Real user files modified:
    No

Persistence:
    No

External network communication:
    No

Ransom payment:
    No

Simulation behavior:
    The laboratory created synthetic victim files and simulated the
    file-impact stage associated with ransomware.

    Instead of cryptographically encrypting files, Red-Grid applied
    a clearly identifiable and reversible simulation marker.

Safety boundary:
    Only files created inside the dedicated Red-Grid ransomware
    laboratory directory were processed.

Defender observation points:
    - Unexpected modification of multiple files
    - Rapid changes across many files
    - Suspicious file-processing activity
    - Ransomware-related process behavior
    - Creation of ransom-note-like artifacts
    - Potential attempts to disable recovery mechanisms
    - Suspicious encryption-related activity

Red-Grid did not perform real encryption, modify arbitrary user files,
establish persistence, contact external infrastructure, or request
ransom payment.
"""

    REPORT_FILE.write_text(report, encoding="utf-8")


def simulate() -> None:
    """Demonstrate controlled ransomware behavior."""
    print()
    print("Ransomware Behavior Simulation")
    print("==============================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()

    print(f"[+] Created laboratory files: {VICTIM_DIR}")
    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print()

    print("[SIMULATION] Discovering laboratory victim files...")

    lab_files = discover_lab_files()

    print(f"[+] Discovered {len(lab_files)} laboratory files.")
    print()

    print("[SIMULATION] Simulating ransomware file impact...")

    events = []

    for file_path in lab_files:
        event = simulate_impact(file_path)
        events.append(event)

        print(f"[+] Simulated impact: {file_path.name}")

    write_impact_log(events)

    print()
    print("[SIMULATION] Simulated recovery operation...")

    recovered_count = 0

    for file_path in lab_files:
        if recover_file(file_path):
            recovered_count += 1
            print(f"[+] Recovered laboratory file: {file_path.name}")

    write_report(events, recovered_count)

    print()
    print("[+] Impact log:", IMPACT_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No real encryption, arbitrary file modification, "
        "persistence, network communication, or ransom payment occurred."
    )
    print()


if __name__ == "__main__":
    simulate()