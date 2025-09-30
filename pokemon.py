class Attack:
    def __init__(self, name, power, effect):
        self.name = name
        self.power = power
        self.effect = effect

class Pokemon:
    def __init__(self, attack, defence, type, attacks, hp=100):
        self.attack = attack
        self.defence = defence
        self.type = type
        self.attacks = attacks
        self.hp = hp
        self.protected = False
        self.status = None

    def use_attack(self, attack_name, target):
        for atk in self.attacks:
            if atk.name == attack_name:
                print(f"{self.__class__.__name__} used {atk.name}!")
                print(f"Effect: {atk.effect}, Power: {atk.power}")

                if atk.effect == "damage":
                    damage = (atk.power * self.attack) // (target.defence * 2)
                    damage = max(5, damage)

                    if target.protected:
                        damage //= 2
                        target.protected = False
                        print(f"{target.__class__.__name__} was protected! Damage reduced.")

                    target.hp -= damage
                    target.hp = max(0, target.hp)
                    print(f"{target.__class__.__name__} took {damage} damage!")
                    print(f"{target.__class__.__name__}'s HP is now {target.hp}")

                elif atk.effect == "defence":
                    self.protected = True
                    print(f"{self.__class__.__name__} is protected and will take less damage next turn.")

                elif atk.effect == "heal":
                    healed = 15
                    self.hp = min(100, self.hp + healed)
                    print(f"{self.__class__.__name__} healed for {healed} HP!")
                    print(f"{self.__class__.__name__}'s HP is now {self.hp}")

                elif atk.effect == "status":
                    target.status = "asleep"
                    print(f"{target.__class__.__name__} is now asleep!")

                return
        print(f"{attack_name} not found!")

class Charizard(Pokemon):
    def __init__(self):
        flamethrower = Attack("Flamethrower", 90, "damage")
        protect = Attack("Protect", 0, "defence")
        fly = Attack("Fly", 70, "damage")
        super().__init__(attack=84, defence=78, type="Fire/Flying", attacks=[flamethrower, protect, fly])

class Blastoise(Pokemon):
    def __init__(self):
        hydro_pump = Attack("Hydro Pump", 110, "damage")
        protect = Attack("Protect", 0, "defence")
        ice_beam = Attack("Ice Beam", 90, "damage")
        super().__init__(attack=83, defence=100, type="Water", attacks=[hydro_pump, protect, ice_beam])

class Gengar(Pokemon):
    def __init__(self):
        shadow_ball = Attack("Shadow Ball", 80, "damage")
        hypnosis = Attack("Hypnosis", 0, "status")
        sludge_bomb = Attack("Sludge Bomb", 90, "damage")
        super().__init__(attack=65, defence=60, type="Ghost/Poison", attacks=[shadow_ball, hypnosis, sludge_bomb])

class Venusaur(Pokemon):
    def __init__(self):
        solar_beam = Attack("Solar Beam", 120, "damage")
        leech_seed = Attack("Leech Seed", 0, "heal")
        razor_leaf = Attack("Razor Leaf", 55, "damage")
        super().__init__(attack=82, defence=83, type="Grass/Poison", attacks=[solar_beam, leech_seed, razor_leaf])

def choose_pokemon(player_number):
    print(f"\nPlayer {player_number}, choose your Pokémon:")
    print("1. Charizard")
    print("2. Blastoise")
    print("3. Gengar")
    print("4. Venusaur")

    while True:
        try:
            choice = int(input("Enter 1, 2, 3, or 4: "))
            if choice == 1:
                return Charizard()
            elif choice == 2:
                return Blastoise()
            elif choice == 3:
                return Gengar()
            elif choice == 4:
                return Venusaur()
            else:
                print("Invalid number. Please choose between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def battle(pokemon1, pokemon2):
    print("\n🔥 The battle begins! 🔥")
    print(f"{pokemon1.__class__.__name__} VS {pokemon2.__class__.__name__}\n")

    current_player = 1

    while pokemon1.hp > 0 and pokemon2.hp > 0:
        attacker = pokemon1 if current_player == 1 else pokemon2
        defender = pokemon2 if current_player == 1 else pokemon1

        if attacker.status == "asleep":
            print(f"{attacker.__class__.__name__} is asleep and skips the turn!")
            attacker.status = None
        else:
            print(f"\n{attacker.__class__.__name__}'s turn")
            print("Choose an attack:")

            for i, atk in enumerate(attacker.attacks):
                print(f"{i + 1}. {atk.name}")

            while True:
                try:
                    choice = int(input("Enter 1, 2, or 3: "))
                    if 1 <= choice <= len(attacker.attacks):
                        selected_attack = attacker.attacks[choice - 1]
                        attacker.use_attack(selected_attack.name, defender)
                        break
                    else:
                        print("Invalid choice. Please enter a number from the list.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        if defender.hp <= 0:
            print(f"\n💀 {defender.__class__.__name__} fainted! {attacker.__class__.__name__} wins!")
            break

        current_player = 2 if current_player == 1 else 1

# Start the game
print("⚔️ Welcome to the Python Pokémon Battle Arena! ⚔️")
player1_pokemon = choose_pokemon(1)
player2_pokemon = choose_pokemon(2)
battle(player1_pokemon, player2_pokemon)
