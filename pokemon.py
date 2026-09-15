"""Pokemon battle simulation demonstrating object-oriented programming in Python.

This project models a small turn-based battle system using classes, inheritance,
and composition. It is intentionally lightweight and readable so it can serve as
an introductory portfolio example for demonstrating core OOP principles.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Attack:
    """Represents a single move used by a Pokémon during battle."""

    name: str
    power: int
    effect: str

    def __str__(self) -> str:
        return self.name


class Pokemon:
    """Base class for all Pokémon in the battle arena."""

    def __init__(
        self,
        name: str,
        attack: int,
        defence: int,
        type_: str,
        attacks: list[Attack],
        hp: int = 100,
    ) -> None:
        self.name = name
        self.attack = attack
        self.defence = defence
        self.type = type_
        self.attacks = attacks
        self.hp = hp
        self.protected = False
        self.status = None

    def get_attack(self, attack_name: str) -> Attack:
        for attack in self.attacks:
            if attack.name.lower() == attack_name.lower():
                return attack
        raise ValueError(f"{attack_name} is not an available move for {self.name}.")

    def take_damage(self, amount: int) -> None:
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} took {amount} damage!")
        print(f"{self.name}'s HP is now {self.hp}")

    def heal(self, amount: int = 15) -> None:
        self.hp = min(100, self.hp + amount)
        print(f"{self.name} healed for {amount} HP!")
        print(f"{self.name}'s HP is now {self.hp}")

    def use_attack(self, attack_name: str, target: "Pokemon") -> None:
        attack = self.get_attack(attack_name)
        print(f"{self.name} used {attack.name}!")
        print(f"Effect: {attack.effect}, Power: {attack.power}")

        if attack.effect == "damage":
            damage = max(5, (attack.power * self.attack) // (target.defence * 2))

            if target.protected:
                damage //= 2
                target.protected = False
                print(f"{target.name} was protected! Damage reduced.")

            target.take_damage(damage)

        elif attack.effect == "defence":
            self.protected = True
            print(f"{self.name} is guarding and will take less damage next turn.")

        elif attack.effect == "heal":
            self.heal()

        elif attack.effect == "status":
            target.status = "asleep"
            print(f"{target.name} is now asleep!")

        else:
            raise ValueError(f"Unsupported attack effect: {attack.effect}")

    def __str__(self) -> str:
        return self.name


class Charizard(Pokemon):
    def __init__(self) -> None:
        super().__init__(
            name="Charizard",
            attack=84,
            defence=78,
            type_="Fire/Flying",
            attacks=[
                Attack("Flamethrower", 90, "damage"),
                Attack("Protect", 0, "defence"),
                Attack("Fly", 70, "damage"),
            ],
        )


class Blastoise(Pokemon):
    def __init__(self) -> None:
        super().__init__(
            name="Blastoise",
            attack=83,
            defence=100,
            type_="Water",
            attacks=[
                Attack("Hydro Pump", 110, "damage"),
                Attack("Protect", 0, "defence"),
                Attack("Ice Beam", 90, "damage"),
            ],
        )


class Gengar(Pokemon):
    def __init__(self) -> None:
        super().__init__(
            name="Gengar",
            attack=65,
            defence=60,
            type_="Ghost/Poison",
            attacks=[
                Attack("Shadow Ball", 80, "damage"),
                Attack("Hypnosis", 0, "status"),
                Attack("Sludge Bomb", 90, "damage"),
            ],
        )


class Venusaur(Pokemon):
    def __init__(self) -> None:
        super().__init__(
            name="Venusaur",
            attack=82,
            defence=83,
            type_="Grass/Poison",
            attacks=[
                Attack("Solar Beam", 120, "damage"),
                Attack("Leech Seed", 0, "heal"),
                Attack("Razor Leaf", 55, "damage"),
            ],
        )


def choose_pokemon(player_number: int) -> Pokemon:
    print(f"\nPlayer {player_number}, choose your Pokémon:")
    pokemon_options = {
        1: Charizard,
        2: Blastoise,
        3: Gengar,
        4: Venusaur,
    }

    for number, pokemon_class in pokemon_options.items():
        print(f"{number}. {pokemon_class.__name__}")

    while True:
        try:
            choice = int(input("Enter 1, 2, 3, or 4: "))
            if choice in pokemon_options:
                return pokemon_options[choice]()
            print("Invalid number. Please choose between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")


class BattleArena:
    """Coordinates the turn-based battle flow between two Pokémon."""

    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2

    def run(self) -> None:
        print("\n🔥 The battle begins! 🔥")
        print(f"{self.pokemon1.name} VS {self.pokemon2.name}\n")

        current_player = 1

        while self.pokemon1.hp > 0 and self.pokemon2.hp > 0:
            attacker = self.pokemon1 if current_player == 1 else self.pokemon2
            defender = self.pokemon2 if current_player == 1 else self.pokemon1

            if attacker.status == "asleep":
                print(f"{attacker.name} is asleep and skips the turn!")
                attacker.status = None
            else:
                print(f"\n{attacker.name}'s turn")
                print("Choose an attack:")

                for index, attack in enumerate(attacker.attacks, start=1):
                    print(f"{index}. {attack.name}")

                while True:
                    try:
                        choice = int(input("Enter a move number: "))
                        if 1 <= choice <= len(attacker.attacks):
                            selected_attack = attacker.attacks[choice - 1]
                            attacker.use_attack(selected_attack.name, defender)
                            break
                        print("Invalid choice. Please enter a number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

            if defender.hp <= 0:
                print(f"\n💀 {defender.name} fainted! {attacker.name} wins!")
                break

            current_player = 2 if current_player == 1 else 1


def battle(pokemon1: Pokemon, pokemon2: Pokemon) -> None:
    """Backward-compatible wrapper for the battle loop."""
    BattleArena(pokemon1, pokemon2).run()


def main() -> None:
    """Launch the command-line Pokémon battle simulator."""
    print("⚔️ Welcome to the Python Pokémon Battle Arena! ⚔️")
    player1_pokemon = choose_pokemon(1)
    player2_pokemon = choose_pokemon(2)
    battle(player1_pokemon, player2_pokemon)


if __name__ == "__main__":
    main()
