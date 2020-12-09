from flask import Flask, request, jsonify

from pokemon_controller import PokemonController

app = Flask(__name__)


@app.route('/', methods=['GET'])
def default():
    return jsonify({'test': 'Hello world'})


@app.route('/pokemon', methods=['POST'])
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


@app.route('/pokemon', methods=['PUT'])
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


@app.route('/pokemon', methods=['DELETE'])
def delete_pokemon():
    action = PokemonController.deletePokemon(request.get_json()['name'])
    if action == 1:
        return jsonify({'message': 'Successfully deleted'}), 200
    elif action == -1:
        return jsonify({'message': "Doesn't exist."}), 400
    else:
        return jsonify({'message': 'Bad request'}), 400


@app.route('/pokemon', methods=['GET'])
def get_all_pokemon():
    return jsonify({'data': PokemonController.getAll()}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
