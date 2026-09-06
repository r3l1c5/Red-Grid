         _____                         _____
      __|__   |__  ______  _____    __|___  |__  _____   ____  _____
     |     |     ||   ___||     \  |   ___|    ||     | |    ||     \
     |     \     ||   ___||      \ |   |  |    ||     \ |    ||      \
     |__|\__\  __||______||______/ |______|  __||__|\__\|____||______/
        |_____|                       |_____|

## Red Grid
### Malware Simulation Lab for Cybersecurity Education

Red-Grid is a **Python-based malware simulation lab** built to demonstrate common malware behaviors through safe, controlled, and non-destructive command-line simulations.

The project is designed for **cybersecurity students, beginners, and security researchers** who want to understand malware concepts without executing harmful activity on a real system.

---

## What Red-Grid Demonstrates

Red-Grid provides simulations for 10 common malware categories:

| #  | Simulation                  | Concept Demonstrated                  |
| -- | --------------------------- | ------------------------------------- |
| 1  | **Keylogger**               | Keystroke monitoring                  |
| 2  | **Ransomware**              | File encryption and recovery concepts |
| 3  | **Worm**                    | Self-replication and propagation      |
| 4  | **Stealer**                 | Data collection                       |
| 5  | **Trojan**                  | Hidden malicious behavior             |
| 6  | **Rootkit**                 | File and process concealment          |
| 7  | **Backdoor**                | Unauthorized access                   |
| 8  | **Adware**                  | Unwanted advertising                  |
| 9  | **File Infector**           | File infection concepts               |
| 10 | **Bash Persistence Script** | Startup persistence                   |

> **Safety:** All current simulations are non-destructive. They demonstrate concepts through controlled terminal output and do not perform real malware activity.

---

## Key Features

* Python-based command-line interface
* 10 malware behavior simulations
* Modular project architecture
* Beginner-friendly code structure
* Automated virtual environment setup
* Minimal Python dependencies
* Linux-focused execution
* Non-destructive simulation design
* Simple menu-driven workflow

---

## Requirements

* **Linux**
* **Python 3.12+**
* **Git**

---

## Installation

Clone the repository:

```bash
git clone https://github.com/R3L1C5/Red_Grid.git
cd Red_Grid
```

Start the lab:

```bash
./run.sh
```

The launcher automatically creates a Python virtual environment and installs the required dependencies.

---

## Usage

After launching Red-Grid, the main menu provides the available simulations:

```text
1. Keylogger
2. Ransomware
3. Worm
4. Stealer
5. Trojan
6. Rootkit
7. Backdoor
8. Adware
9. File Infector
10. Bash Persistence Script
0. Exit
```

Select a number and press **Enter** to run the corresponding simulation.

---

## Project Structure

```text
Red_Grid/
├── malware_simulation_lab.py
├── modules/
│   ├── __init__.py
│   ├── adware.py
│   ├── backdoor.py
│   ├── bash_persistence.py
│   ├── file_infector.py
│   ├── keylogger.py
│   ├── ransomware.py
│   ├── rootkit.py
│   ├── stealer.py
│   ├── trojan.py
│   └── worm.py
├── requirements.txt
├── run.sh
├── .gitignore
├── LICENSE
└── README.md
```

### Architecture

The project uses a simple modular design:

```text
User
  │
  ▼
malware_simulation_lab.py
  │
  ├── Keylogger Simulation
  ├── Ransomware Simulation
  ├── Worm Simulation
  ├── Stealer Simulation
  ├── Trojan Simulation
  ├── Rootkit Simulation
  ├── Backdoor Simulation
  ├── Adware Simulation
  ├── File Infector Simulation
  └── Bash Persistence Simulation
```

Each malware category is implemented as an independent Python module with a standardized `simulate()` interface.

---

## Learning Objectives

Red-Grid provides hands-on practice with:

* Malware categories and behavior
* Python modules and package organization
* CLI application development
* Menu-driven program design
* Function-based architecture
* Python virtual environments
* Dependency management
* Linux command-line workflows
* Safe cybersecurity experimentation

---

## Safety & Ethics

Red-Grid is intentionally designed as a **simulation-only cybersecurity project**.

The current implementation does **not**:

* Capture real keystrokes
* Encrypt or modify user files
* Collect real credentials
* Create system persistence
* Propagate across systems
* Establish remote shells
* Modify system configuration
* Perform destructive actions

Use Red-Grid only for **authorized cybersecurity education, research, and laboratory environments**.

---

## License

This project is distributed under the **MIT License**. See the `LICENSE` file for details.

## Author

**R3L1C5**
