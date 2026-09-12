"""Controlled adware behavior simulation for Red-Grid.

This module does not perform real adware activity.

It simulates common adware characteristics by:

* creating a dedicated laboratory directory
* generating fake advertising configuration
* simulating repeated advertisement events
* recording simulated tracking/telemetry events
* producing a behavioral report

All generated data stays inside the local `redgrid_lab` directory.
"""

from **future** import annotations

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

def _timestamp() -> str:
"""Return a readable timestamp."""
return datetime.now().isoformat(timespec="seconds")

def _create_lab() -> None:
"""Create the isolated simulation directory."""
ADWARE_DIR.mkdir(parents=True, exist_ok=True)

def _write_json(filename: str, data) -> Path:
"""Write simulation data as JSON."""
path = ADWARE_DIR / filename

```
with path.open("w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

return path
```

def _generate_configuration() -> Path:
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
"tracking_enabled": True,
"external_network_access": False,
"persistence_enabled": False,
}

```
return _write_json("simulated_config.json", configuration)
```

def _simulate_ad_events(count: int = 5) -> list[dict]:
"""Generate simulated advertisement events."""
events = []

```
for event_id in range(1, count + 1):
    advertisement = random.choice(FAKE_ADS)

    event = {
        "event_id": event_id,
        "timestamp": _timestamp(),
        "event": "ADVERTISEMENT_DISPLAYED",
        "campaign": advertisement["campaign"],
        "title": advertisement["title"],
        "category": advertisement["category"],
        "simulated": True,
    }

    events.append(event)

    print(
        f"[+] Simulated advertisement #{event_id}: "
        f"{advertisement['title']}"
    )

    time.sleep(0.2)

return events
```

def _simulate_tracking(events: list[dict]) -> list[dict]:
"""Generate harmless fake telemetry events."""
telemetry = []

```
fake_pages = [
    "/home",
    "/products",
    "/search",
    "/offers",
    "/checkout",
]

for index, event in enumerate(events, start=1):
    record = {
        "event_id": index,
        "timestamp": _timestamp(),
        "event": "SIMULATED_PAGE_TRACKING",
        "page": random.choice(fake_pages),
        "campaign": event["campaign"],
        "simulated": True,
    }

    telemetry.append(record)

return telemetry
```

def _generate_report(events: list[dict], telemetry: list[dict]) -> Path:
"""Create a human-readable behavioral report."""
report = ADWARE_DIR / "behavior_report.txt"

```
lines = [
    "Red-Grid Adware Simulation Report",
    "=" * 36,
    "",
    "Simulation status: SAFE / SIMULATED",
    f"Generated: {_timestamp()}",
    "",
    "Observed simulated behavior:",
    "",
    f"- Advertisement events: {len(events)}",
    f"- Tracking events:       {len(telemetry)}",
    "- Real advertisements:   No",
    "- External network:      No",
    "- Persistence:            No",
    "- Real browser changes:   No",
    "",
    "Behavior represented:",
    "- Repeated advertisement delivery",
    "- Campaign identification",
    "- Basic user-interest tracking",
    "- Advertising telemetry collection",
    "",
    "All generated artifacts are contained inside:",
    str(ADWARE_DIR.resolve()),
    "",
]

report.write_text("\n".join(lines), encoding="utf-8")

return report
```

def simulate() -> None:
"""Run the controlled adware behavior simulation."""
print("Adware Behavior Simulation")
print("=" * 28)

```
print()
print("[SIMULATION] Initializing isolated laboratory environment...")

_create_lab()

configuration = _generate_configuration()

print(f"[+] Created simulated configuration: {configuration}")

print()
print("[SIMULATION] Simulating advertisement delivery...")

events = _simulate_ad_events()

print()
print("[SIMULATION] Simulating advertising telemetry...")

telemetry = _simulate_tracking(events)

telemetry_file = _write_json(
    "simulated_telemetry.json",
    telemetry,
)

events_file = _write_json(
    "advertisement_events.json",
    events,
)

report = _generate_report(events, telemetry)

print()
print("[+] Advertisement events recorded.")
print(f"[+] Event log: {events_file}")
print(f"[+] Telemetry log: {telemetry_file}")
print(f"[+] Behavior report: {report}")

print()
print("[SIMULATION] No real advertising, tracking, persistence,")
print("[SIMULATION] browser modification, or network communication occurred.")
```

:::("")]

// end of code?
