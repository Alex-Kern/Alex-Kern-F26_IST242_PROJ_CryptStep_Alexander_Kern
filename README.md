# CryptStep

A turn-based grid puzzle and dungeon crawler built in Python using Pygame-CE.

## Core Concept
* **Genre:** Top-down turn-based grid crawler
* **Core Loop:** Navigate a 15x15 grid; every player step triggers enemy movement and trap ticks.
* **Win Condition:** Collect all 3 relics and reach the exit stairs.
* **Loss Condition:** Player HP drops to 0.

## Planned Architecture
* `logic.py` — Python game state, movement, combat, and win/loss rules (zero Pygame dependencies).
* `rendering.py` — Pygame-CE graphics rendering and HUD overlays.
* `main.py` — Application entry point and event loop.
* `constants.py` — Grid dimensions, tile sizes, and color/display configuration.
* `test_logic.py` — Pytest covering movement, combat, and state edge cases.

## Planned Controls
* **Arrow Keys / WASD:** Move one tile (North, South, East, West)
* **R:** Restart level
* **ESC:** Quit game