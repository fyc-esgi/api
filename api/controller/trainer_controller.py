from controller.pokemon_controller import PokemonController


class TrainerController:
    """Trainer class controller """
    trainers = []
    trainer_att = ['name', 'pokemons', 'title']

    @staticmethod
    def add_trainer(json: dict) -> int:
        if not TrainerController.is_trainer(json):
            return -1
        if TrainerController.get_index(json['name']) != -1:
            return -2
        for pokemon in json['pokemons']:
            if not PokemonController.pokemon_exist(pokemon['name']):
                return -3
        TrainerController.trainers.append(json)
        return 1

    @staticmethod
    def update_trainer(json: dict) -> int:
        if not TrainerController.is_trainer(json):
            return -1
        for pokemon in json['pokemons']:
            if not PokemonController.pokemon_exist(pokemon['name']):
                return -3
        index = TrainerController.get_index(json['name'])
        if index == -1:
            return -2
        TrainerController.trainers[index] = json
        return 1

    @staticmethod
    def delete_trainer(trainer_name: str) -> int:
        index = TrainerController.get_index(trainer_name)

        if index == -1:
            return -1
        del TrainerController.trainers[index]
        return 1

    @staticmethod
    def get_all() -> list:
        return TrainerController.trainers

    @staticmethod
    def get_index(trainer_name) -> int:
        for index, trainer in enumerate(TrainerController.trainers):
            if trainer['name'] == trainer_name:
                return index
        return -1

    @staticmethod
    def is_trainer(json: dict) -> bool:
        for train_att in TrainerController.trainer_att:
            if train_att not in json:
                return False
        return True

    @staticmethod
    def delete_pokemon(pokemon_name):
        for trainer in TrainerController.trainers:
            for index, pokemon in enumerate(trainer['pokemons']):
                if pokemon['name'] == pokemon_name:
                    del trainer['pokemons'][index]
