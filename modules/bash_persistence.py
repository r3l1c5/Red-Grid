import json
from datetime import datetime, timezone
from pathlib import Path


LAB_ROOT = Path("redgrid_lab")
PERSISTENCE_DIR = LAB_ROOT / "bash_persistence"


def utc_timestamp():
    return datetime.now(timezone.utc).isoformat()


def create_lab_environment():
    PERSISTENCE_DIR.mkdir(parents=True, exist_ok=True)


def write_config():
    config = {
        "simulation": True,
        "component": "bash_persistence",
        "sample_id": "REDGRID-BASH-PERSISTENCE-001",
        "target_scope": str(PERSISTENCE_DIR),
        "real_shell_modification": False,
        "real_startup_modification": False,
        "real_crontab_modification": False,
        "real_profile_modification": False,
        "real_persistence": False,
        "command_execution": False,
        "external_network_access": False,
    }

    config_path = PERSISTENCE_DIR / "simulated_config.json"

    with config_path.open("w", encoding="utf-8") as file:
        json.dump(config, file, indent=4)


def simulate_persistence_mechanisms():
    mechanisms = [
        {
            "mechanism": "bashrc",
            "location": "~/.bashrc",
            "status": "SIMULATED",
            "action": "A startup command would be represented here.",
        },
        {
            "mechanism": "profile",
            "location": "~/.profile",
            "status": "SIMULATED",
            "action": "A login startup command would be represented here.",
        },
        {
            "mechanism": "cron",
            "location": "user crontab",
            "status": "SIMULATED",
            "action": "A scheduled persistence entry would be represented here.",
        },
    ]

    result = {
        "timestamp": utc_timestamp(),
        "simulation_only": True,
        "mechanisms": mechanisms,
    }

    output_path = PERSISTENCE_DIR / "simulated_persistence.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    return result


def write_report(result):
    report_path = PERSISTENCE_DIR / "behavior_report.txt"

    lines = [
        "RED-GRID BASH PERSISTENCE SIMULATION",
        "=" * 42,
        "",
        "Purpose:",
        "Simulate how a persistence-focused threat may abuse shell startup",
        "locations without modifying the real operating system.",
        "",
        "Simulated persistence mechanisms:",
        "- Bash configuration (.bashrc)",
        "- Login profile (.profile)",
        "- User crontab",
        "",
        "Safety controls:",
        "- No real shell configuration was modified.",
        "- No real crontab entry was created.",
        "- No startup command was executed.",
        "- No command execution was performed.",
        "- No persistence was established.",
        "- No external network communication occurred.",
        "",
        "Defender observation points:",
        "- Unexpected changes to shell startup files.",
        "- Suspicious commands executed during shell initialization.",
        "- Unexpected user-level scheduled tasks.",
        "- New or modified startup entries.",
        "- Shell configuration changes occurring without user intent.",
        "",
        f"Generated: {result['timestamp']}",
    ]

    with report_path.open("w", encoding="utf-8") as file:
        file.write("\n".join(lines))


def simulate():
    create_lab_environment()
    write_config()

    result = simulate_persistence_mechanisms()
    write_report(result)

    print("\n[BASH PERSISTENCE SIMULATION]")
    print("-" * 35)
    print("Status: SIMULATED")
    print("Real shell modification: DISABLED")
    print("Real persistence: DISABLED")
    print(f"Artifacts: {PERSISTENCE_DIR}")
    print("Simulation completed successfully.")


if __name__ == "__main__":
    simulate()