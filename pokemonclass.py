# Stabilshing classes
class Pokemon:
    def __init__(self, name, pokemon_type, level=1):
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level
        self.hp = level * 10

    # Method to display pokemon information
    def display_info(self):
        print(f"{self.name} is a {self.pokemon_type}-type Pokémon at level {self.level} with {self.hp} HP.")

    # Exemple how to use this method
    #pikachu = Pokemon("Pikachu", "Electric",level= 2)
    #pikachu.display_info()
    # Expected response = Pikachu is a Eletric Pokémon at Level 2 with 20 HP. 

    # Method to level up your pokemon
    def level_up(self):
        self.level += 1
        self.hp = self.level * 10  # update HP
        print(f"{self.name} leveled up to level {self.level}! HP is now {self.hp}.")

    #expected results
    #picachu leveld up to level 3! hp is now 30

    # Method to attack other pokemon
    def attack(self, other_pokemon):
        damage = self.level * 5  # The damage is realative to your level
        other_pokemon.hp -= damage  # The hp drew from the other pokemon
        print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
        if other_pokemon.hp <= 0:
            print(f"{other_pokemon.name} has fainted!")
        else:
            print(f"{other_pokemon.name} has {other_pokemon.hp} HP left.")

# Tests

# Creating pokemons
charmander = Pokemon("Charmander", "fire", level=5)
squirtle = Pokemon("Squirtle", "water", level=4)

# Showing informations
print("=== Initial informations ===")
charmander.display_info()
squirtle.display_info()

# Charmander hit Squirtle
print("\n=== Battle 1: Charmander hit Squirtle ===")
charmander.attack(squirtle)

# Squirtle hit back
print("\n=== Battle 2: Squirtle hit Charmander ===")
squirtle.attack(charmander)

# Charmander leveled up
print("\n=== Charmander level up ===")
charmander.level_up()

# Showing information after level up
print("\n=== Information after level up ===")
charmander.display_info()
