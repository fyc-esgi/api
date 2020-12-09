from flask import Blueprint, jsonify, request

from controller.pokemon_controller import PokemonController

pokemon_api = Blueprint('pokemon_api', __name__)


@pokemon_api.route('/pokemon', methods=['POST'])
def add_pokemon():
    action = PokemonController.addPokemon(request.get_json())
    if action == 1:
        return jsonify({'message': 'Successfully created'}), 201
    elif action == -1:
        return jsonify({'message': "Wrong attributes, needs : 'name', 'element_type', 'hp', 'attack', 'defense' and "
                                   "'speed'."}), 400
    elif action == -2:
        return jsonify({'message': 'Already exists'}), 400
    else:
        return jsonify({'message': 'Bad request'}), 400


@pokemon_api.route('/pokemon', methods=['PUT'])
def update_pokemon():
    action = PokemonController.updatePokemon(request.get_json())
    if action == 1:
        return jsonify({'message': 'Successfully updated'}), 200
    elif action == -1:
        return jsonify({'message': "Wrong attributes, needs : 'name', 'element_type', 'hp', 'attack', 'defense' and "
                                   "'speed'."}), 400
    elif action == -2:
        return jsonify({'message': "Doesn't exist."}), 404
    else:
        return jsonify({'message': 'Bad request'}), 400


@pokemon_api.route('/pokemon', methods=['DELETE'])
def delete_pokemon():
    action = PokemonController.deletePokemon(request.get_json()['name'])
    if action == 1:
        return jsonify({'message': 'Successfully deleted'}), 200
    elif action == -1:
        return jsonify({'message': "Doesn't exist."}), 400
    else:
        return jsonify({'message': 'Bad request'}), 400


@pokemon_api.route('/pokemon', methods=['GET'])
def get_all_pokemon():
    return jsonify({'data': PokemonController.getAll()}), 200