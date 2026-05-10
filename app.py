import os
from flask import Flask, jsonify, render_template


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("config.Config")


    @app.get("/")
    def home():
        return render_template("index.html"), 200


    @app.get("/health")
    def health():
        return jsonify(status="ok"), 200

    return app


app = create_app()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=app.config["DEBUG"])
