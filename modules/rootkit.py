"""Controlled rootkit behavior simulation for the Red-Grid laboratory."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
ROOTKIT_DIR = LAB_ROOT / "rootkit"

CONFIG_FILE = ROOTKIT_DIR / "simulated_config.json"
OBJECTS_FILE = ROOTKIT_DIR / "simulated_objects.json"
DETECTION_FILE = ROOTKIT_DIR / "detection_results.json"
REPORT_FILE = ROOTKIT_DIR / "behavior_report.txt"


SIMULATED_OBJECTS = [
    {
        "object_id": "OBJ-001",
        "object_type": "process",
        "name": "simulated_service",
        "visible_to_normal_view": True,
    },
    {
        "object_id": "OBJ-002",
        "object_type": "file",
        "name": "simulated_driver.dat",
        "visible_to_normal_view": True,
    },
    {
        "object_id": "OBJ-003",
        "object_type": "service",
        "name": "SimulatedUpdateService",
        "visible_to_normal_view": True,
    },
    {
        "object_id": "OBJ-004",
        "object_type": "process",
        "name": "simulated_hidden_process",
        "visible_to_normal_view": False,
    },
    {
        "object_id": "OBJ-005",
        "object_type": "file",
        "name": "simulated_hidden_file.dat",
        "visible_to_normal_view": False,
    },
]


def utc_timestamp() -> str:
    """Return the current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment() -> None:
    """Create the isolated rootkit laboratory directory."""
    ROOTKIT_DIR.mkdir(parents=True, exist_ok=True)


def write_config() -> None:
    """Write explicit rootkit simulation safety configuration."""
    config = {
        "simulation": True,
        "component": "rootkit",
        "sample_id": "REDGRID-ROOTKIT-001",
        "dataset": "synthetic_objects",
        "real_os_objects_modified": False,
        "real_process_hiding": False,
        "real_file_hiding": False,
        "kernel_modification": False,
        "driver_installation": False,
        "registry_modification": False,
        "persistence_enabled": False,
        "external_network_access": False,
        "created_at": utc_timestamp(),
    }

    CONFIG_FILE.write_text(
        json.dumps(config, indent=4),
        encoding="utf-8",
    )


def create_object_dataset() -> None:
    """Create a synthetic representation of system objects."""
    dataset = {
        "simulation": True,
        "generated_at": utc_timestamp(),
        "objects": SIMULATED_OBJECTS,
    }

    OBJECTS_FILE.write_text(
        json.dumps(dataset, indent=4),
        encoding="utf-8",
    )


def simulate_normal_view() -> list[dict]:
    """Return objects visible through a simulated normal inspection."""
    return [
        obj
        for obj in SIMULATED_OBJECTS
        if obj["visible_to_normal_view"]
    ]


def simulate_deep_view() -> list[dict]:
    """Return all objects through a simulated deeper inspection."""
    return list(SIMULATED_OBJECTS)


def compare_views(
    normal_view: list[dict],
    deep_view: list[dict],
) -> list[dict]:
    """Identify objects missing from the simulated normal view."""
    normal_ids = {
        obj["object_id"]
        for obj in normal_view
    }

    hidden_objects = []

    for obj in deep_view:
        if obj["object_id"] not in normal_ids:
            hidden_objects.append(
                {
                    "object_id": obj["object_id"],
                    "object_type": obj["object_type"],
                    "name": obj["name"],
                    "detection": "SIMULATED_HIDDEN_OBJECT",
                }
            )

    return hidden_objects


def write_detection_results(
    normal_view: list[dict],
    deep_view: list[dict],
    hidden_objects: list[dict],
) -> None:
    """Write simulated detection comparison results."""
    results = {
        "simulation": True,
        "timestamp": utc_timestamp(),
        "normal_view_count": len(normal_view),
        "deep_view_count": len(deep_view),
        "hidden_object_count": len(hidden_objects),
        "hidden_objects": hidden_objects,
        "real_system_inspection": False,
    }

    DETECTION_FILE.write_text(
        json.dumps(results, indent=4),
        encoding="utf-8",
    )


def write_report(
    normal_view: list[dict],
    deep_view: list[dict],
    hidden_objects: list[dict],
) -> None:
    """Write a defender-oriented rootkit behavior report."""
    report = f"""Red-Grid Rootkit Simulation Report
===================================

Simulation status: SAFE / SIMULATED

Component:
    Rootkit behavior simulation

Synthetic objects:
    {len(deep_view)}

Objects visible through simulated normal inspection:
    {len(normal_view)}

Objects absent from simulated normal inspection:
    {len(hidden_objects)}

Real process hiding:
    No

Real file hiding:
    No

Kernel modification:
    No

Driver installation:
    No

Registry modification:
    No

Persistence:
    No

External network communication:
    No

Simulation behavior:
    Red-Grid created a synthetic system-object dataset containing
    objects that are either visible or hidden from a simulated
    inspection method.

    A second simulated inspection provides a broader view and
    identifies objects missing from the normal view.

    This demonstrates the defensive concept of discrepancies
    between different sources of system information.

Safety boundary:
    No real operating-system objects were hidden, modified,
    deleted, or manipulated.

Defender observation points:
    - Differences between independent system inventories
    - Unexpected processes or services
    - Files absent from one inspection method but present in another
    - Suspicious drivers or kernel components
    - Integrity mismatches
    - Unexpected system-level modifications
    - Discrepancies between user-space and lower-level telemetry

Red-Grid did not hide real processes, files, services, drivers,
registry entries, or kernel objects.
"""

    REPORT_FILE.write_text(
        report,
        encoding="utf-8",
    )


def simulate() -> None:
    """Demonstrate controlled rootkit behavior."""
    print()
    print("Rootkit Behavior Simulation")
    print("===========================")
    print()

    print("[SIMULATION] Initializing isolated laboratory environment...")

    create_lab_environment()
    write_config()
    create_object_dataset()

    print(f"[+] Simulation configuration: {CONFIG_FILE}")
    print(f"[+] Synthetic object dataset: {OBJECTS_FILE}")
    print()

    print("[SIMULATION] Performing simulated normal inspection...")

    normal_view = simulate_normal_view()

    print(
        f"[+] Normal inspection discovered "
        f"{len(normal_view)} objects."
    )

    print()
    print("[SIMULATION] Performing simulated deep inspection...")

    deep_view = simulate_deep_view()

    print(
        f"[+] Deep inspection discovered "
        f"{len(deep_view)} objects."
    )

    hidden_objects = compare_views(
        normal_view,
        deep_view,
    )

    print()
    print("[SIMULATION] Comparing inspection results...")

    for obj in hidden_objects:
        print(
            f"[+] Simulated hidden object detected: "
            f"{obj['object_type']} -> {obj['name']}"
        )

    write_detection_results(
        normal_view,
        deep_view,
        hidden_objects,
    )

    write_report(
        normal_view,
        deep_view,
        hidden_objects,
    )

    print()
    print("[+] Detection results:", DETECTION_FILE)
    print("[+] Behavior report:", REPORT_FILE)
    print()
    print(
        "[SIMULATION] No real processes, files, services, drivers, "
        "registry entries, or kernel objects were hidden or modified."
    )
    print()


if __name__ == "__main__":
    simulate()