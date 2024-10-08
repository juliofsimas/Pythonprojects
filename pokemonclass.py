


class Pokemon:
    def __init__(self, name, pokemon_type, level=1):
        # These are the attributes of each Pokémon
        self.name = name           # The name of the Pokémon
        self.pokemon_type = pokemon_type  # The type of the Pokémon (e.g., Fire, Water, Grass)
        self.level = level         # The Pokémon's level (default is 1)
        self.hp = level * 10       # The Pokémon's HP (Hit Points), based on level

    # Method 1: Display Pokémon info
    def display_info(self):
        print(f"{self.name} is a {self.pokemon_type}-type Pokémon at level {self.level} with {self.hp} HP.")

    # Method 2: Level up the Pokémon
    def level_up(self):
        self.level += 1
        self.hp = self.level * 10  # Update HP as well when leveling up
        print(f"{self.name} leveled up to level {self.level}! HP is now {self.hp}.")

    # Method 3: Attack another Pokémon
    def attack(self, other_pokemon):
        damage = self.level * 5    # Damage is based on the attacker's level
        other_pokemon.hp -= damage  # The other Pokémon loses HP
        print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
        if other_pokemon.hp <= 0:
            print(f"{other_pokemon.name} has fainted!")
        else:
            print(f"{other_pokemon.name} has {other_pokemon.hp} HP left.")

Charmander = Pokemon('Charmander', 'Fire')
Pikachu = Pokemon('Pikachu,'Eletric')

Charmander.display_info

Charmander.level_up

print(pikachu)

