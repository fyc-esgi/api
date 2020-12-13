from flask import Flask, jsonify
from flask_cors import CORS
from flask_prometheus_metrics import register_metrics
from prometheus_client import make_wsgi_app

from route.pokemon_router import pokemon_api
from route.trainer_router import trainer_api
from werkzeug import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware

app = Flask(__name__)
CORS(app)

app.register_blueprint(pokemon_api)
app.register_blueprint(trainer_api)


@app.route('/', methods=['GET'])
def default():
    return jsonify({'test': 'Hello world'})


if __name__ == '__main__':
    # provide app's version and deploy environment/config name to set a gauge metric
    register_metrics(app, app_version="v0.1.2", app_config="staging")

    # Plug metrics WSGI app to your main app with dispatcher
    dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})

    run_simple(hostname="0.0.0.0", port=5050, application=dispatcher)
