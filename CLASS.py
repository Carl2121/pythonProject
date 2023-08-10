class Pokemon:
    pokemons = []

    def __init__(self):
        self.name = input("Enter Pokemon: ")
        self.cp = int(input("Enter Combat Power: "))
        Pokemon.pokemons.append(self)

    @classmethod
    def display_all(cls):
        for pokemon in cls.pokemons:
            print("I got a", pokemon.name, "with a combat power of", pokemon.cp)


while True:
    new_pokemon = Pokemon()
    choice = input("Do you want to enter another Pokemon? (y/n): ")
    if choice.lower() == 'n':
        break

Pokemon.display_all()


