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

    # Método para subir de nível
    def level_up(self):
        self.level += 1
        self.hp = self.level * 10  # Atualiza os HP
        print(f"{self.name} leveled up to level {self.level}! HP is now {self.hp}.")

    # Método para atacar outro Pokémon
    def attack(self, other_pokemon):
        damage = self.level * 5  # O dano é baseado no nível
        other_pokemon.hp -= damage  # O outro Pokémon perde HP
        print(f"{self.name} attacks {other_pokemon.name} for {damage} damage!")
        if other_pokemon.hp <= 0:
            print(f"{other_pokemon.name} has fainted!")
        else:
            print(f"{other_pokemon.name} has {other_pokemon.hp} HP left.")

# Testando os métodos

# Criando dois Pokémon
charmander = Pokemon("Charmander", "fire", level=5)
squirtle = Pokemon("Squirtle", "water", level=4)

# Exibindo informações dos Pokémon
print("=== Informações Iniciais ===")
charmander.display_info()
squirtle.display_info()

# Charmander ataca Squirtle
print("\n=== Batalha 1: Charmander ataca Squirtle ===")
charmander.attack(squirtle)

# Squirtle ataca de volta
print("\n=== Batalha 2: Squirtle ataca Charmander ===")
squirtle.attack(charmander)

# Charmander sobe de nível
print("\n=== Charmander sobe de nível ===")
charmander.level_up()

# Exibindo informações após o level up
print("\n=== Informações após o level up ===")
charmander.display_info()
