# Elementary Cellular Automaton

This project is a Python implementation of an Elementary Cellular Automaton. It simulates the behavior of cellular automata 
following the rules defined by [elementary cellular automaton theory](https://en.wikipedia.org/wiki/Elementary_cellular_automaton).

## Features

- Implementations for various cellular automaton rules.
- Visualization of the automaton evolution.
- Customizable rule sets for experimentation.

## Installation

**Prerequisite:** Ensure [Poetry](https://python-poetry.org/docs/#installation) is installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/PetrFridrich/ElementaryCellularAutomaton.git
   ```
2.  Navigate to the project directory:
    ```bash
    cd ElementaryCellularAutomaton
    ```
3. Install the dependencies with Poetry:
    ```bash 
    poetry install
    ```
This will install all required dependencies as defined in pyproject.toml.

## Project Structure

The project is organized as follows:

<pre>
ElementaryCellularAutomaton/
├── src/                                    # Folder with source codes
│   ├── __main__.ipynb                      # Main script to run the cellular automaton
│   └── elementary_cellular_automaton.py    # Implementation of cellular automaton
├── .gitignore                              # Git ignore file
├── pyproject.toml                          # Poetry project configuration and dependencies
└── README.md                               # This README file
</pre>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

