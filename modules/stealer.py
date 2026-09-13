"""Controlled information-stealer behavior simulation for Red-Grid."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
STEALER_DIR = LAB_ROOT / "stealer"

CONFIG_FILE = STEALER_DIR / "simulated_config.json"
COLLECTION_FILE = STEALER_DIR / "simulated_collection.json"
REPORT_FILE = STEALER_DIR / "behavior_report.txt"


SYNTHETIC_DATA = [
    {
        "record_id": 1,
        "data_type": "username",
        "source": "synthetic_application",
        "value": "demo_user",
    },
    {
        "record_id": 2,
        "data_type": "password",
        "source": "synthetic_application",
        "value": "[SIMULATED_PASSWORD]",
    },
    {
        "record_id": 3,
        "data_type": "email",
        "source": "synthetic_application",
        "value": "demo@example.invalid",
    },
    {
        "record_id": 4,
        "data_type": "session_token",
        "source": "synthetic_application",
        "value": "[SIMULATED_TOKEN]",
    },
    {
        "record_id": 5,
        "data_type": "credit_card",
        "source": "synthetic_payment_form",
        "value": "[SIMULATED_PAYMENT_DATA]",
    },
]


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create the isolated stealer laboratory directory."""
    STEALER_DIR.mkdir(parents=True, exist_ok=True)


def write_config() -> None:
    """Write explicit safety and simulation configuration."""
    config = {
        "simulation": True,
        "component": "stealer",
        "sample_id": "REDGRID-STEALER-001",
        "data_source": "synthetic_dataset",
        "real_credentials": False,
        "browser_access": False,
        "credential_store_access": False,
        "filesystem_discovery": False,
        "real_secret_collection": False,
        "data_transmission": False,
        "external_network_access": False,
        "persistence_enabled": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def simulate_collection() -> list[dict]:
    """Simulate collection from a predefined synthetic dataset."""
    events = []

    for item in SYNTHETIC_DATA:
        event = {
            "event_id": item["record_id"],
            "timestamp": utc_timestamp(),
            "data_type": item["data_type"],
            "source": item["source"],
            "value": item["value"],
            "collection_status": "SIMULATED",
        }

        events.append(event)

    return events


def write_collection_log(events: list[dict]) -> None:
    """Write simulated data-collection events."""
    collection = {
        "simulation": True,
        "component": "stealer",
        "event_count": len(events),
        "events": events,
        "real_data_collected": False,
        "data_transmitted": False,
        "timestamp": utc_timestamp(),
    }

    COLLECTION_FILE.write_text(
        json.dumps(collection, indent=4),
        encoding="utf-8",
    )


def write_report(events: list[dict]) -> None:
    """Write a defender-oriented information-stealer report."""
    report = f"""Red-Grid Information Stealer Simulation Report
================================================

Simulation status: SAFE / SIMULATED

Component:
    Information-stealer behavior simulation

Synthetic dataset:
    {len(events)} records

Real credentials collected:
    No

Browser data accessed:
    No

Credential stores accessed:
    No

Real secrets collected:
    No

Filesystem discovery:
    No

External network communication:
    No

Data transmission:
    No

Persistence:
    No

Simulation behavior:
    Red-Grid used a predefined synthetic dataset representing
    information that a real information stealer might attempt to
    collect from a compromised system.

    The dataset contains fake usernames, passwords, email addresses,
    session tokens, and payment information.

    Sensitive synthetic values are represented by placeholders rather
    than realistic credentials or usable secrets.

Safety boundary:
    All collected values originated from the Red-Grid source code.
    No browser, operating-system credential store, application database,
    filesystem search, or external service was accessed.

Defender observation points:
    - Unexpected access to browser data
    - Unexpected access to credential stores
    - Suspicious access to application databases
    - Collection of authentication artifacts
    - Collection of payment-related information
    - Unexpected staging of sensitive information
    - Suspicious outbound data transmission

Red-Grid did not access real credentials, browser information,
credential stores, personal files, or external infrastructure.
"""


    REPORT_FILE.write_text(
        report,
        encoding="utf-8",
    )


def simulate() -> None:
    """Demonstrate controlled information-stealer behavior."""
    print()
    print("Information Stealer Behavior Simulation")
    print("========================================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()

    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print()

    print("[SIMULATION] Loading synthetic data source...")

    events = simulate_collection()

    print(f"[+] Loaded {len(events)} synthetic records.")
    print()

    print("[SIMULATION] Simulating data collection...")

    for event in events:
        print(
            f"[+] Simulated collection: "
            f"{event['data_type']} from {event['source']}"
        )

    write_collection_log(events)
    write_report(events)

    print()
    print("[+] Collection log:", COLLECTION_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No real credentials, browser data, credential stores, "
        "personal files, or external services were accessed."
    )
    print()


if __name__ == "__main__":
    simulate()