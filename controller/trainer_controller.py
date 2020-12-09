from controller.pokemon_controller import PokemonController


class TrainerController:
    """Trainer class controller """
    trainers = []
    trainer_att = ['name', 'pokemons', 'title']

    @staticmethod
    def addTrainer(json: dict) -> int:
        if not TrainerController.is_trainer(json):
            return -1
        if TrainerController.get_index(json['name']) != -1:
            return -2
        TrainerController.trainers.append(json)
        return 1

    @staticmethod
    def updateTrainer(json: dict) -> int:
        if not TrainerController.is_trainer(json):
            return -1
        index = TrainerController.get_index(json['name'])
        if index == -1:
            return -2
        TrainerController.trainers[index] = json
        return 1

    @staticmethod
    def deleteTrainer(trainer_name: str) -> int:
        index = TrainerController.get_index(trainer_name)

        if index == -1:
            return -1
        del TrainerController.trainers[index]
        return 1

    @staticmethod
    def getAll() -> list:
        return TrainerController.trainers

    @staticmethod
    def get_index(trainer_name) -> int:
        for index, trainer in enumerate(TrainerController.trainers):
            if trainer['name'] == trainer_name:
                return index
        return -1

    @staticmethod
    def pokemon_exist(pokemon_name) -> bool:
        return False if PokemonController.get_index(pokemon_name) == -1 else True

    @staticmethod
    def is_trainer(json: dict) -> bool:
        for train_att in TrainerController.trainer_att:
            if train_att not in json:
                return False
        return True
