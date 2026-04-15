from flask import Flask
from flask_cors import CORS
from .routes import file_route


def create_app() -> Flask:
    app = Flask(__name__)

    CORS(app)

    app.register_blueprint(file_route)

    return app



if __name__ == "__main__":

    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)