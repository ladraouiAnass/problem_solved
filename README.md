# Millennium Falcon Odds Calculator

## Project Overview

This project calculates the odds that the Millennium Falcon reaches Endor in time to save the galaxy. The solution consists of three main components:

1. **CLI (Command-Line Interface):** A Python script (`cli.py`) to compute the success probability directly from the terminal.
2. **Backend:** A Django application (`apps.py` in the `myapp` app) that serves as the core computational engine.
3. **Frontend:** A simple client interface hosted on `http://127.0.0.1:8080/` that allows users to upload JSON files and view results.

---

## Problem Description

The Millennium Falcon must:
- Navigate through the galaxy with limited autonomy for Hyperspace jumps.
- Avoid or mitigate capture by bounty hunters who may be present on specific planets during specific days.
- Reach Endor before the Death Star destroys it within a given countdown.

The probability of success considers fuel stops, bounty hunter encounters, and travel constraints. For detailed examples, refer to the **Examples** section below.

---

## Solution Components

### CLI

The `cli.py` script allows you to compute the probability directly from the terminal.

#### Usage:
```bash
python cli.py path_to/millennium-falcon.json path_to/empire.json
