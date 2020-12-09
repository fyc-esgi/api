from flask import Flask, jsonify

from route.pokemon_router import pokemon_api
from route.trainer_router import trainer_api

app = Flask(__name__)

app.register_blueprint(pokemon_api)
app.register_blueprint(trainer_api)


@app.route('/', methods=['GET'])
def default():
    return jsonify({'test': 'Hello world'})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
