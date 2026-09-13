# 2048 Game

A graphical implementation of the **2048 game developed in Python using Pygame**.

This project was developed as part of my university studies to practice Python programming, matrix manipulation, game logic, and graphical interfaces.

## How It Works

The game uses a **4x4 grid** where numbered tiles can be moved using the arrow keys.

When two tiles with the same value collide, they merge into a single tile with their combined value.

After each valid movement, a new tile with the value **2 or 4** is randomly generated in an empty position.

The objective is to combine the tiles until reaching **2048**.

## Controls

Use the arrow keys to move the tiles:

* **↑** Move Up
* **↓** Move Down
* **←** Move Left
* **→** Move Right

## Features

* 4x4 game grid
* Graphical interface using Pygame
* Keyboard controls
* Random generation of 2 and 4 tiles
* Tile movement and merging
* Different colors for each tile value
* Victory detection when reaching 2048
* Game Over detection when no moves are available

## Project Structure

```text
2048-game/
│
├── src/
│   └── game_2048.py
│
└── README.md
```

## Requirements

* Python 3
* Pygame

Install Pygame using:

```bash
pip install pygame
```

Or install the project dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

Run the game with:

```bash
python src/game_2048.py
```

Use the **arrow keys** to move the tiles and try to reach 2048.

## Technologies

* Python
* Pygame

## Author

University project developed for programming practice.

