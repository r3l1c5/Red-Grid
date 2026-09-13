"""Controlled adware behavior simulation for Red-Grid.

This module does not perform real adware activity.

It simulates common adware characteristics by:
- creating a dedicated laboratory directory
- generating fake advertising configuration
- simulating repeated advertisement events
- recording simulated tracking/telemetry events
- producing a behavioral report

All generated data stays inside the local Red-Grid lab directory.
"""

import json
import random
import time
from datetime import datetime
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
ADWARE_DIR = LAB_ROOT / "adware"


FAKE_ADS = [
    {
        "campaign": "SIM-001",
        "title": "Limited Time Offer",
        "category": "Shopping",
    },
    {
        "campaign": "SIM-002",
        "title": "You Won a Prize!",
        "category": "Scam Advertisement",
    },
    {
        "campaign": "SIM-003",
        "title": "Recommended Product",
        "category": "Product Promotion",
    },
    {
        "campaign": "SIM-004",
        "title": "Special Browser Offer",
        "category": "Software Promotion",
    },
]


def _timestamp():
    """Return a readable timestamp."""
    return datetime.now().isoformat(timespec="seconds")


def _create_lab():
    """Create the isolated simulation directory."""
    ADWARE_DIR.mkdir(parents=True, exist_ok=True)


def _write_json(filename, data):
    """Write simulation data as JSON."""
    path = ADWARE_DIR / filename

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return path


def _generate_configuration():
    """Create a fake adware configuration file."""
    configuration = {
        "simulation": True,
        "component": "adware",
        "sample_id": "REDGRID-ADWARE-001",
        "ad_frequency_seconds": 5,
        "target_categories": [
            "shopping",
            "software",
            "promotions",
        ],
        "tracking_enabled": False,
        "simulated_tracking": True,
        "external_network_access": False,
        "persistence_enabled": False,
    }

    return _write_json("simulated_config.json", configuration)


def _simulate_ad_events(count=5):
    """Generate simulated advertisement events."""
    events = []

    for event_id in range(1, count + 1):
        advertisement = random.choice(FAKE_ADS)

        event = {
            "event_id": event_id,
            "timestamp": _timestamp(),
            "campaign": advertisement["campaign"],
            "title": advertisement["title"],
            "category": advertisement["category"],
            "displayed": True,
            "external_network_request": False,
        }

        events.append(event)

        print(
            f"[+] Simulated advertisement #{event_id}: "
            f"{advertisement['title']}"
        )

        time.sleep(0.2)

    return events


def _simulate_telemetry(events):
    """Generate simulated local telemetry records."""
    telemetry = []

    for event in events:
        telemetry.append(
            {
                "timestamp": event["timestamp"],
                "event_id": event["event_id"],
                "category": event["category"],
                "interaction": "simulated_view",
                "real_user_tracking": False,
                "external_transmission": False,
            }
        )

    return telemetry


def _generate_report(events, telemetry):
    """Create a defender-oriented behavioral report."""
    report_path = ADWARE_DIR / "behavior_report.txt"

    report = (
        "Red-Grid Adware Simulation Report\n"
        "=================================\n\n"
        "Simulation status: SAFE / SIMULATED\n"
        "Sample ID: REDGRID-ADWARE-001\n\n"
        "Simulated behavior:\n"
        "- Advertisement generation\n"
        "- Repeated advertisement display events\n"
        "- Synthetic telemetry generation\n"
        "- Local behavioral logging\n\n"
        "Safety boundaries:\n"
        "- Real user tracking: No\n"
        "- External network communication: No\n"
        "- Data transmission: No\n"
        "- Persistence: No\n"
        "- Real system modification: No\n\n"
        f"Advertisement events generated: {len(events)}\n"
        f"Telemetry events generated: {len(telemetry)}\n\n"
        "Defender observation points:\n"
        "- Unexpected advertisement processes\n"
        "- Suspicious telemetry collection\n"
        "- Unexpected persistence mechanisms\n"
        "- Unexpected outbound network requests\n"
    )

    report_path.write_text(
        report,
        encoding="utf-8",
    )

    return report_path


def simulate():
    """Run the controlled adware behavior simulation."""
    print()
    print("Adware Behavior Simulation")
    print("===========================")
    print()
    print("[SIMULATION] Initializing isolated laboratory environment...")

    _create_lab()

    config_path = _generate_configuration()
    print(f"[+] Simulation configuration: {config_path}")

    print()
    print("[SIMULATION] Generating advertisement events...")

    events = _simulate_ad_events()

    event_path = _write_json(
        "advertisement_events.json",
        events,
    )

    telemetry = _simulate_telemetry(events)

    telemetry_path = _write_json(
        "simulated_telemetry.json",
        telemetry,
    )

    report_path = _generate_report(
        events,
        telemetry,
    )

    print()
    print(f"[+] Advertisement log: {event_path}")
    print(f"[+] Telemetry log: {telemetry_path}")
    print(f"[+] Behavior report: {report_path}")
    print()
    print(
        "[SIMULATION] No real tracking, external network "
        "communication, persistence, or system modification occurred."
    )


if __name__ == "__main__":
    simulate()