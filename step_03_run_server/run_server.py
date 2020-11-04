import sys

from step_03_run_server.botcontext import BotContext
from step_03_run_server.const import STATIC_DIR
from step_03_run_server.load_pool_data import PoolData
from step_03_run_server.ner_stuff import checkDistrict, checkDay, populateContext, handle_user_request
from step_03_run_server.nn_stuff import getResponse, predict_class, intents

sys.path.append('./')

from flask import Flask, render_template, request, session

poolData = PoolData()

app = Flask(__name__, static_folder=STATIC_DIR)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    return handle_user_request()


if __name__ == "__main__":
    app.config["SECRET_KEY"] = "i am just secret"
    app.run()
