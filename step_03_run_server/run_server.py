import sys

from step_03_run_server.const import STATIC_DIR
from step_03_run_server.ner_stuff import handle_user_request
from step_03_run_server.nn_stuff import predict_class

sys.path.append('./')

from flask import Flask, render_template

app = Flask(__name__, static_folder=STATIC_DIR)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    return handle_user_request()


if __name__ == "__main__":
    # the first response usually takes some time - fake one request
    ints = predict_class("dummy")

    app.config["SECRET_KEY"] = "i am just secret"
    app.run()
