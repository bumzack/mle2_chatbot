import csv
import sys

import spacy

from step_03_run_server.nn_stuff import getResponse, predict_class, POOL_NAME, AUSLASTUNG_TODAY, ADDRESS, AUSLASTUNG_TOMORROW, DISTRICT, \
    TODAY, TOMORROW, STATIC_DIR
from step_03_run_server.zip_mapping import district_mapping

sys.path.append('./')

from flask import Flask, render_template, request, session
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
import pickle
from keras.models import load_model

model = load_model('../data/chatbot_model.h5')
import json

intents = json.loads(open('../input_data/intents.json').read())
words = pickle.load(open('../data/words.pkl', 'rb'))
classes = pickle.load(open('../data/classes.pkl', 'rb'))

# ######################################################################
# load spacy NER model
# ######################################################################
spacy_model_dir = "../data/sapcy_ner_trained_model"
# spacy_model_simple_dir = "../data/spacy_simple"


pool_data = []
# ########### laod csv
with open('../data/SCHWIMMBADOGD.csv', newline='') as csvfile:
    pool_data_tmp = csv.reader(csvfile, delimiter=',')
    i = 0
    for row in pool_data_tmp:
        if i == 0:
            break
        i = i + 1
        print(
            'name:  ' + row[POOL_NAME] + ' \n       address: ' + row[ADDRESS] + ',  district:   "' + row[DISTRICT] + '", auslastung_today' +
            row[AUSLASTUNG_TODAY] + '')
        pos_comma = row[ADDRESS].find(",")
        add = row[ADDRESS][pos_comma + 1:]
        dist = district_mapping[row[DISTRICT]]
        entry = {
            "name": row[POOL_NAME],
            "address": add,
            "district": dist,
            "auslastung_today": row[AUSLASTUNG_TODAY],
            "auslastung_tomorrow": row[AUSLASTUNG_TOMORROW],
        }
        pool_data.append(entry)

for p in pool_data:
    print('name:  ' + p["name"] + ' \n       address: ' + p["address"] + ',  district:   "' + p["district"] + '", auslastung_today' +
          p["auslastung_today"] + '", auslastung_tomorrow' + p["auslastung_tomorrow"] + '')

model_dir = spacy_model_dir
print("Loading from: '", model_dir, "'")
nlp_spacy_districts = spacy.load(model_dir)

# TODO use en_core_web_lg
nlp_spacy_full = spacy.load("en_core_web_sm")

app = Flask(__name__, static_folder=STATIC_DIR)


class BotContext:
    def __init__(self):
        self.data = {
            "intent_greeting": None,
            "intent_goodbye": None,
            "intent_thanks": None,
            "intent_noanswer": None,
            "intent_options": None,
            "intent_user_bored": None,
            "intent_pool_today": None,
            "intent_pool_tomorrow": None,
            "intent_pool_where": None,
            "intent_user_not_happy": None,
            "intent_user_approve": None,
            "day": None,
            "district": None
        }


@app.route("/")
def home():
    return render_template("index.html")


def populateContext(ctx, response):
    if response["tag"] == 'intent_pool_today':
        print("adding 'today' to ctx ")
        ctx.data["intent_day"] = True
        ctx.data["day"] = 'today'

    if response["tag"] == 'intent_pool_tomorrow':
        print("adding 'tomorrow' to ctx ")
        ctx.data["intent_day"] = True
        ctx.data["day"] = 'tomorrow'

    if response["tag"] == 'intent_pool_where':
        print("adding 'tomorrow' to ctx ")
        ctx.data["intent_pool_where"] = True


def checkDistrict(userText):
    spacy_districts = nlp_spacy_districts(userText)

    print("=========  checkDistrict entities ===========")
    print("district Entities newly trained ", [(ent.text, ent.label_) for ent in spacy_districts.ents])
    print("=========  checkDistrict  END districts entities ===========")
    districts = []
    for ent in spacy_districts.ents:
        if ent.label_ == "VIE_DIS":
            districts.append(ent.text)

    print("=========  checkDistrict: filtered districts entities ===========")
    print("filtered districts ", [d for d in districts])
    print("=========  checkDistrict END filtered  districts entities ===========")

    ner = nlp_spacy_full(userText)
    print("=========  checkDistrict NER ===========")
    for token in ner:
        print("found ner:   ", token.text, token.lemma_, token.pos_)
    print("=========  checkDistrict END NER ===========")

    if len(districts) > 0:
        return districts[0]

    return None


def checkDay(userText):
    spacy_days = nlp_spacy_full(userText)
    print("=========  checkDate NER  ===========")
    days = []
    for ent in spacy_days.ents:
        print("ent.text " + ent.text + ",     ent.label_:  " + ent.label_)
        if ent.label_ == "DATE":
            days.append(ent.text)
    print("=========  checkDate END NER ===========")

    if len(days) > 0:
        for d in days:
            if d.lower() == TODAY:
                return TODAY
            if d.lower() == TOMORROW:
                return TOMORROW


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
