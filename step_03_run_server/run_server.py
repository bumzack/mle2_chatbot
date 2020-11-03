import sys

from step_03_run_server.botcontext import BotContext
from step_03_run_server.const import STATIC_DIR
from step_03_run_server.load_pool_data import pool_data
from step_03_run_server.ner_stuff import checkDistrict, checkDay, populateContext
from step_03_run_server.nn_stuff import getResponse, predict_class, intents

sys.path.append('./')

from flask import Flask, render_template, request, session

for p in pool_data:
    print('name:  ' + p["name"] + ' \n       address: ' + p["address"] + ',  district:   "' + p["district"] + '", auslastung_today' +
          p["auslastung_today"] + '", auslastung_tomorrow' + p["auslastung_tomorrow"] + '')

app = Flask(__name__, static_folder=STATIC_DIR)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    ctx = BotContext()

    if not session.get("context") is None:
        data = session.get("context")
        ctx.data = data
        print("====== context.data =======")
        print(ctx.data)
        print("===========================")
    else:
        print("====== no context on session object found =======")

    userText = request.args.get('msg')
    ints = predict_class(userText)

    district = checkDistrict(userText)
    if not district is None:
        ctx.data["district"] = district

    day = checkDay(userText)
    if not day is None:
        ctx.data["day"] = day

    # contains a random response depending on the intent found
    response = getResponse(ints, intents)
    populateContext(ctx, response)

    print("response: " + response["response"])
    session["context"] = ctx.data

    return response


if __name__ == "__main__":
    app.config["SECRET_KEY"] = "i am just secret"
    app.run()
