class PokemonController:
    """Pokemon class controller """
    pokemons = []
    pok_attributes = ['name', 'element_type', 'hp', 'attack', 'defense', 'speed']

    @staticmethod
    def addPokemon(json: dict) -> int:
        if not PokemonController.is_pokemon(json):
            return -1
        if PokemonController.get_index(json['name']) != -1:
            return -2
        PokemonController.pokemons.append(json)
        return 1

    @staticmethod
    def updatePokemon(json: dict) -> int:
        if not PokemonController.is_pokemon(json):
            return -1
        index = PokemonController.get_index(json['name'])
        if index == -1:
            return -2
        PokemonController.pokemons[index] = json
        return 1

    @staticmethod
    def deletePokemon(pokemon_name: str) -> int:
        index = PokemonController.get_index(pokemon_name)

        if index == -1:
            return -1
        del PokemonController.pokemons[index]
        return 1

    @staticmethod
    def getAll() -> list:
        return PokemonController.pokemons

    @staticmethod
    def get_index(pokemon_name) -> int:
        for index, pokemon in enumerate(PokemonController.pokemons):
            if pokemon['name'] == pokemon_name:
                return index
        return -1

    @staticmethod
    def is_pokemon(json: dict) -> bool:
        for pok_att in PokemonController.pok_attributes:
            if pok_att not in json:
                return False
        return True

    @staticmethod
    def pokemon_exist(pokemon_name) -> bool:
        return False if PokemonController.get_index(pokemon_name) == -1 else True
