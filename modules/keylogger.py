"""Controlled keylogger behavior simulation for the Red-Grid Malware Simulation Lab.

This module does not access the real keyboard, install hooks, capture user input,
or transmit data. It generates synthetic keystrokes and demonstrates the
collection and reporting concepts associated with keyloggers.
"""

from __future__ import annotations

import json
import time
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
KEYLOGGER_DIR = LAB_ROOT / "keylogger"

SAMPLE_ID = "REDGRID-KEYLOGGER-001"

SYNTHETIC_INPUT = [
    ("user", "hello_redgrid"),
    ("password", "[SIMULATED_PASSWORD]"),
    ("command", "whoami"),
    ("search", "cybersecurity lab"),
    ("note", "training session"),
]


def _utc_timestamp() -> str:
    """Return an ISO-8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


def _write_json(path: Path, data: object) -> None:
    """Write JSON data to a laboratory artifact."""
    path.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8",
    )


def _create_configuration() -> Path:
    """Create a configuration artifact describing the safe simulation boundary."""
    config = {
        "simulation": True,
        "component": "keylogger",
        "sample_id": SAMPLE_ID,
        "input_source": "synthetic_data",
        "real_keyboard_capture": False,
        "keyboard_hook_installed": False,
        "credential_capture": False,
        "persistence_enabled": False,
        "external_network_access": False,
        "data_transmission": False,
        "purpose": "educational malware-behavior simulation",
    }

    path = KEYLOGGER_DIR / "simulated_config.json"
    _write_json(path, config)

    return path


def _generate_events() -> list[dict[str, object]]:
    """Generate synthetic keystroke-collection events."""
    events: list[dict[str, object]] = []

    print()
    print("[SIMULATION] Generating synthetic keystroke activity...")

    for sequence, (input_type, value) in enumerate(
        SYNTHETIC_INPUT,
        start=1,
    ):
        event = {
            "event_id": sequence,
            "timestamp": _utc_timestamp(),
            "source": "synthetic_input",
            "input_type": input_type,
            "value": value,
            "real_keyboard_input": False,
        }

        events.append(event)

        print(
            f"[+] Synthetic input #{sequence}: "
            f"{input_type} -> {value}"
        )

        time.sleep(0.15)

    return events


def _create_collection_report(events: list[dict[str, object]]) -> Path:
    """Create a defender-oriented report from simulated collection events."""
    report = KEYLOGGER_DIR / "behavior_report.txt"

    report.write_text(
        "Red-Grid Keylogger Simulation Report\n"
        "====================================\n\n"
        "Simulation status: SAFE / SIMULATED\n"
        f"Sample ID: {SAMPLE_ID}\n\n"
        "Behavior represented:\n"
        "- Synthetic keystroke collection\n"
        "- Input categorization\n"
        "- Local event logging\n"
        "- Collected-data reporting\n\n"
        "Safety boundaries:\n"
        "- Real keyboard input captured: No\n"
        "- Keyboard hook installed: No\n"
        "- Credential capture: No\n"
        "- Persistence created: No\n"
        "- External network communication: No\n"
        "- Data transmitted externally: No\n\n"
        f"Simulated input events: {len(events)}\n\n"
        "Defender observation points:\n"
        "- Unexpected input-capture components\n"
        "- Suspicious local keystroke logs\n"
        "- Persistence associated with input-capture software\n"
        "- Unexpected outbound communication containing collected data\n",
        encoding="utf-8",
    )

    return report


def simulate() -> None:
    """Run the controlled keylogger behavior simulation."""
    print()
    print("Keylogger Behavior Simulation")
    print("==============================")
    print()
    print("[SIMULATION] Initializing isolated laboratory environment...")

    KEYLOGGER_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    config_path = _create_configuration()
    print(f"[+] Created simulated configuration: {config_path}")

    events = _generate_events()

    event_path = KEYLOGGER_DIR / "synthetic_keystroke_events.json"
    _write_json(event_path, events)

    report_path = _create_collection_report(events)

    print()
    print("[SIMULATION] Simulated collection completed.")
    print(f"[+] Event log: {event_path}")
    print(f"[+] Behavior report: {report_path}")
    print()
    print(
        "[SIMULATION] No real keyboard input was captured, "
        "no keyboard hook was installed, and no data was transmitted."
    )


if __name__ == "__main__":
    simulate()