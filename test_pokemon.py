import unittest

from pokemon import Charizard, Gengar, Pokemon


class PokemonBehaviorTests(unittest.TestCase):
    def test_unknown_attack_raises_value_error(self):
        pikachu = Charizard()
        with self.assertRaises(ValueError):
            pikachu.use_attack("Thunderbolt", Gengar())

    def test_protect_defense_starts_and_reduces_damage(self):
        attacker = Charizard()
        defender = Gengar()

        attacker.use_attack("Protect", defender)
        self.assertTrue(attacker.protected)

        defender.hp = 100
        attacker.use_attack("Flamethrower", defender)
        self.assertLess(defender.hp, 100)


if __name__ == "__main__":
    unittest.main()
