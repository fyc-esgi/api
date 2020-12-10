from flask import Blueprint, jsonify, request

from controller.trainer_controller import TrainerController

trainer_api = Blueprint('trainer_api', __name__)


@trainer_api.route('/trainer', methods=['POST'])
def add_trainer():
    action = TrainerController.addTrainer(request.get_json())
    if action == 1:
        return jsonify({'message': 'Successfully created'}), 201
    elif action == -1:
        return jsonify({'message': "Wrong attributes, needs : 'name', 'pokemons', 'title'."}), 400
    elif action == -2:
        return jsonify({'message': 'Already exists'}), 400
    elif action == -3:
        return jsonify({'message': "One of trainer's pokemon do not exist."}), 400
    else:
        return jsonify({'message': 'Bad request'}), 400


@trainer_api.route('/trainer', methods=['PUT'])
def update_trainer():
    action = TrainerController.updateTrainer(request.get_json())
    if action == 1:
        return jsonify({'message': 'Successfully updated'}), 200
    elif action == -1:
        return jsonify({'message': "Wrong attributes, needs : 'name', 'pokemons', 'title'."}), 400
    elif action == -2:
        return jsonify({'message': "Trainer doesn't exist."}), 404
    elif action == -3:
        return jsonify({'message': "One of trainer's pokemon do not exist."}), 400
    else:
        return jsonify({'message': 'Bad request'}), 400


@trainer_api.route('/trainer', methods=['DELETE'])
def delete_trainer():
    action = TrainerController.deleteTrainer(request.get_json()['name'])
    if action == 1:
        return jsonify({'message': 'Successfully deleted'}), 200
    elif action == -1:
        return jsonify({'message': "Doesn't exist."}), 400
    else:
        return jsonify({'message': 'Bad request'}), 400


@trainer_api.route('/trainer', methods=['GET'])
def get_all_trainer():
    return jsonify({'data': TrainerController.getAll()}), 200
