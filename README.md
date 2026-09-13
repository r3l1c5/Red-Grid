         _____                         _____
      __|__   |__  ______  _____    __|___  |__  _____   ____  _____
     |     |     ||   ___||     \  |   ___|    ||     | |    ||     \
     |     \     ||   ___||      \ |   |  |    ||     \ |    ||      \
     |__|\__\  __||______||______/ |______|  __||__|\__\|____||______/
        |_____|                       |_____|

## Red Grid
### Malware Simulation Lab for Cybersecurity Education

Red-Grid
Malware Simulation Lab for Cybersecurity Education

Red-Grid is a Python-based malware simulation lab designed to demonstrate common malware behaviors through safe, controlled, and non-destructive simulations.

The project is intended for cybersecurity students, beginners, and security researchers who want hands-on experience with malware concepts without executing harmful activity on a real system.

Important: Red-Grid is a simulation environment. The included modules do not implement real malware capabilities such as credential theft, real keylogging, destructive encryption, network propagation, persistence, or command-and-control communication.

What Red-Grid Demonstrates

Red-Grid currently contains 10 independent malware behavior simulations:

#	Simulation	Concept Demonstrated
1	Keylogger	Simulated keystroke collection and event logging
2	Ransomware	Simulated file impact, encryption concepts, and recovery
3	Worm	Simulated host discovery and propagation concepts
4	Stealer	Simulated collection of sensitive-data categories
5	Trojan	Simulated deceptive payload delivery
6	Rootkit	Simulated hidden process and file detection
7	Backdoor	Simulated unauthorized command-access concepts
8	Adware	Simulated advertising and telemetry behavior
9	File Infector	Simulated file infection using harmless markers
10	Bash Persistence	Simulated shell and scheduled-task persistence concepts

All simulations operate within controlled scenarios and use synthetic or project-local data.

Key Features
Python-based command-line interface
10 independent malware behavior simulations
Modular project architecture
Standardized simulate() interface
Beginner-friendly Python implementation
Menu-driven execution
Controlled synthetic data
Project-local simulation artifacts
No third-party Python dependencies
Cross-platform Python launcher
Linux/macOS shell launcher
Non-destructive simulation design
Clear safety boundaries for cybersecurity education
Requirements
Python 3.12 or newer
Git
Linux or macOS if using run.sh
Windows can run the Python launcher directly

Red-Grid currently uses Python's standard library only.

No external Python packages are required.

Installation

Clone the repository:

git clone https://github.com/R3L1C5/Red-Grid.git
cd Red-Grid
Linux / macOS

Make the launcher executable:

chmod +x run.sh

Start Red-Grid:

./run.sh

The launcher creates a local Python virtual environment if one does not already exist.

Windows

Run the main launcher directly:

python malware_simulation_lab.py

If your system uses the py launcher:

py malware_simulation_lab.py

No third-party dependencies need to be installed.

Usage

After launching Red-Grid, the main menu provides the available simulations:

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

Select a module number and press Enter.

Each simulation runs independently and returns control to the main menu after completion.

Simulation Output

Some modules generate controlled artifacts for demonstration purposes.

These artifacts are stored under:

redgrid_lab/

For example, the ransomware and file-infector simulations create synthetic files inside their own project-local directories.

These files are not real user documents and are not intended to represent actual malware impact.

The redgrid_lab/ directory is excluded from Git through .gitignore.

Project Structure
Red-Grid/
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
├── .gitignore
├── LICENSE
├── README.md
└── run.sh

Runtime-generated directories such as:

redgrid_lab/
__pycache__/
.venv/

are intentionally excluded from version control.

Architecture

Red-Grid uses a simple modular architecture:

                         User
                           |
                           v
              malware_simulation_lab.py
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
     Keylogger        Ransomware          Worm
     Simulation       Simulation        Simulation
          |
          +--------------------------------+
          |                |               |
          v                v               v
       Stealer          Trojan          Rootkit
       Simulation      Simulation       Simulation
          |
          +----------------+----------------+
                           |
              +------------+------------+
              |            |            |
              v            v            v
          Backdoor       Adware     File Infector
          Simulation    Simulation   Simulation
                           |
                           v
                  Bash Persistence
                     Simulation

Each module exposes a standardized:

simulate()

entry point.

The main launcher imports the modules and maps them to menu options.

This design keeps each malware concept isolated and makes the project easier to understand, test, and extend.

Module Safety Design

Red-Grid intentionally separates malware concepts from real malware capabilities.

Keylogger

The keylogger module uses predefined synthetic input rather than capturing keyboard events.

It does not:

Install keyboard hooks
Monitor the real keyboard
Capture real passwords
Capture credentials
Record user activity
Ransomware

The ransomware module operates on synthetic files created inside the Red-Grid runtime directory.

It does not:

Encrypt real user files
Search arbitrary directories
Destroy data
Modify unrelated files
Demand real payment

The simulated operation is reversible.

Worm

The worm module uses predefined fictional hosts to demonstrate propagation concepts.

It does not:

Scan real networks
Connect to remote systems
Exploit vulnerabilities
Propagate between machines
Download or execute remote payloads
Stealer

The stealer module works with synthetic demonstration data.

It does not access:

Browser databases
Password stores
Real credentials
Authentication tokens
Payment information
Private user files
Trojan

The Trojan module demonstrates deceptive delivery and payload concepts using a benign simulated payload manifest.

It does not:

Execute malicious payloads
Execute arbitrary commands
Establish persistence
Create remote access
Communicate with command-and-control infrastructure
Rootkit

The rootkit module demonstrates the concept of hidden objects using a synthetic dataset.

It does not:

Hide real processes
Hide real files
Modify the operating system
Install drivers
Modify the kernel
Modify security configuration
Backdoor

The backdoor module demonstrates command-access concepts using a predefined local command queue.

It does not:

Open network listeners
Create sockets for remote access
Execute arbitrary shell commands
Establish command-and-control communication
Provide a remote shell
Create persistence
Adware

The adware module demonstrates simulated advertisements and synthetic telemetry.

It does not:

Contact external advertising services
Track real users
Send telemetry over the network
Install browser extensions
Create persistence
File Infector

The file-infector module operates only on synthetic text files created inside the Red-Grid runtime directory.

It adds a harmless simulation marker and does not inject executable code.

It does not:

Modify real user files
Modify executable binaries
Inject executable code
Self-replicate
Spread between systems
Bash Persistence

The Bash persistence module demonstrates common persistence concepts such as shell startup files and scheduled tasks using simulation output.

It does not modify:

.bashrc
.profile
Actual crontab entries
Startup configuration
System persistence mechanisms
Safety Boundaries

The current Red-Grid implementation does not perform the following real-world actions:

Real keyboard capture
Credential theft
Real secret collection
Destructive file encryption
Modification of arbitrary user files
Real network scanning
Network propagation
Exploitation of remote systems
Command-and-control communication
Network listeners
Remote shells
Arbitrary command execution
Real persistence
Process hiding
File hiding
Kernel modification
Driver installation
Security configuration modification

The project is intentionally limited to controlled simulations and synthetic data.

Testing

Each module can be tested independently.

Keylogger
python -m modules.keylogger
Ransomware
python -m modules.ransomware
Worm
python -m modules.worm
Stealer
python -m modules.stealer
Trojan
python -m modules.trojan
Rootkit
python -m modules.rootkit
Backdoor
python -m modules.backdoor
Adware
python -m modules.adware
File Infector
python -m modules.file_infector
Bash Persistence
python -m modules.bash_persistence
Syntax Validation

Check the main launcher:

python -m py_compile malware_simulation_lab.py

Check the modules:

python -m py_compile modules/*.py

On Windows PowerShell, all Python files can also be compiled with:

Get-ChildItem modules\*.py | ForEach-Object {
    python -m py_compile $_.FullName
}

python -m py_compile malware_simulation_lab.py
Learning Objectives

Red-Grid provides practical experience with:

Malware behavior concepts
Malware simulation design
Python modules and packages
CLI application development
Menu-driven applications
Function-based architecture
Python virtual environments
Standard-library-only Python development
Linux command-line workflows
Cross-platform Python execution
Controlled cybersecurity experimentation
Defensive security concepts
Safe laboratory design
Why This Project Exists

Understanding malware does not require building operational malware.

Red-Grid focuses on the behavioral and analytical side of malware by reproducing simplified versions of common techniques in a controlled environment.

This makes it possible to study questions such as:

What does a keylogger conceptually collect?
How does ransomware behavior differ from normal file modification?
How does malware propagation work conceptually?
What types of information might an infostealer target?
Why is persistence important to malware?
What makes rootkit behavior difficult to detect?
How can defenders identify suspicious behavior?

The goal is to understand these concepts while keeping the implementation safe and non-destructive.

Ethical Use

Red-Grid is intended for:

Cybersecurity education
Malware behavior research
Defensive security training
Authorized laboratory environments
Security portfolio development
Interview and technical learning

Run the project only on systems and environments where you have appropriate authorization.

Do not modify the project to introduce harmful functionality or deploy it against systems without authorization.
---

## License

This project is distributed under the **MIT License**. See the `LICENSE` file for details.

## Author

**R3L1C5**
