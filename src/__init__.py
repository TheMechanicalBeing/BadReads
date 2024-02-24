from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def initial():
        return "Hello world!"

    return app