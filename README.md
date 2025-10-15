# Study Reminders - ScriptingAssignmet2

A Python package that automates creating and sending personalized study reminders for students.  


## Overview

The **study_reminders** package manages student information, generates personalized reminders, simulates sending them, logs all operations, and can schedule automatic daily delivery.

It demonstrates modular programming, file handling, and basic automation in Python.


## Features

- Manage student information stored in a JSON file (`students.json`)
- Generate personalized course reminders
- Simulate sending reminders (prints to console)
- Log sent reminders with timestamps
- Schedule automated daily reminders using the `schedule` library
- Modular, reusable, and easy to extend


## Installation

1. Clone or download this project.
2. Open a terminal in the project folder.
3. Install the package locally (in editable mode):

```bash
pip install -e .
```

## How to run
Use the command:

```bash
study-reminders
```

This will then show up:

```bash
Welcome to the Study Reminders automation system!

1. Send reminders once (manual test)
2. Run daily scheduler
```

Choose **1** to send reminders immediately or **2** to run the scheduled daily delivery.


## Logging
All reminders are recorded in *reminder_log.txt* with timestamps.


## Dependencies

- Python 3.8+

- schedule

Install automatically via `pip install -e .`


