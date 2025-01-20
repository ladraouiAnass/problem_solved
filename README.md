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
```
Input:

    millennium-falcon.json: Contains ship autonomy, routes, and the mission's starting planet.
    empire.json: Specifies bounty hunter schedules and the countdown limit.

Output:

    Prints the probability of reaching the destination within the given constraints.

Backend

The core logic for computing probabilities is implemented in the Django application.
Features:

    Processes JSON input files to determine constraints and travel paths.
    Calculates the probability of success considering all travel and capture possibilities.

Key File:

    apps.py in the myapp app.

Frontend

A simple client interface for users to interact with the calculator.
Features:

    Allows users to upload millennium-falcon.json and empire.json files.
    Displays the calculated probability of success.

Access:

http://127.0.0.1:8080/

Examples
Input:
millennium-falcon.json:

{
  "autonomy": 6,
  "departure": "Tatooine",
  "arrival": "Endor",
  "routes_db": "universe.db"
}

empire.json:

{
  "countdown": 9,
  "bounty_hunters": [
    { "planet": "Hoth", "day": 6 },
    { "planet": "Tatooine", "day": 2 }
  ]
}

Output:

When using the CLI or frontend, the probability of success is displayed. For example:

Probability of success: 0.333

Installation

    Clone the repository:

git clone https://github.com/yourusername/millennium-falcon-calculator.git
cd millennium-falcon-calculator

    Install dependencies:

pip install -r requirements.txt

    Start the backend server:

python manage.py runserver

    Access the frontend: Visit http://127.0.0.1:8080/.

Testing

Run tests to validate the implementation:

pytest tests/

Future Improvements

    Add support for real-time galaxy maps.
    Introduce a more interactive frontend with detailed path visualizations.
    Optimize computation for larger datasets.

Contributing

Contributions are welcome! Please follow these steps:

    Fork the repository.
    Create a new branch: git checkout -b feature-name.
    Commit your changes: git commit -m 'Add new feature'.
    Push to the branch: git push origin feature-name.
    Open a Pull Request.

License

This project is licensed under the MIT License. See the LICENSE file for details.


You can copy and paste this directly into your `README.md` file in your GitHub repository. Replace placeholders like `yourusername` and add additional project details where needed.


