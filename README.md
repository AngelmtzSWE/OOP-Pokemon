# OOP Pokémon Battle Arena

A compact Python project designed to showcase object-oriented programming principles in a clear and approachable way. The game simulates a turn-based Pokémon battle with a reusable base class, specialized subclasses, and encapsulated combat logic.

## What this project demonstrates
- Inheritance with distinct Pokémon subclasses
- Encapsulation through behavior and state management
- Composition by attaching move lists to each Pokémon
- Clean Python class design using dataclasses and type hints
- Basic game flow logic for a turn-based system

## Included Pokémon
- Charizard
- Blastoise
- Gengar
- Venusaur

## Project structure
- `pokemon.py` – core battle logic and class definitions
- `test_pokemon.py` – lightweight regression tests for move handling and defense mechanics

## Run the game

```bash
python pokemon.py
```

## Gameplay flow
1. Player 1 selects a Pokémon
2. Player 2 selects a Pokémon
3. Players alternate taking turns
4. Moves apply damage, defense, healing, or status effects
5. The battle ends when one Pokémon reaches 0 HP



## Potential next upgrades
- Add type effectiveness and weaknesses
- Include AI-controlled enemy logic
- Expand the roster with more Pokémon
- Add a battle history display or leaderboard

