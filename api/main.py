from flask import Flask, jsonify
from flask_cors import CORS
from route.pokemon_router import pokemon_api
from route.trainer_router import trainer_api


app = Flask(__name__)
CORS(app)

app.register_blueprint(pokemon_api)
app.register_blueprint(trainer_api)


@app.route('/', methods=['GET'])
def default():
    return jsonify({'test': 'Hello world'})


if __name__ == '__main__':
    app.run("0.0.0.0", port=5050)
