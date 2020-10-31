import os
import random
import sys

import nltk
import numpy as np
import spacy

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

STATIC_DIR = os.path.abspath('./static')
print("STATIC DIR   ", STATIC_DIR)

# ######################################################################
# load spacy NER model
# ######################################################################
spacy_model_dir = "../data/sapcy_ner_trained_model"
spacy_model_simple_dir = "../data/spacy_simple"
model_dir = spacy_model_dir
print("Loading from: '", model_dir, "'")
nlp_spacy_districts = spacy.load(model_dir)
nlp_spacy_full = spacy.load("en_core_web_lg")

app = Flask(__name__, static_folder=STATIC_DIR)


def clean_up_sentence(sentence):
    # tokenize the pattern - splitting words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stemming every word - reducing to base form
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# return bag of words array: 0 or 1 for words that exist in sentence

def bag_of_words(sentence, words, show_details=True):
    # tokenizing patterns

    sentence_words = clean_up_sentence(sentence)
    # bag of words - vocabulary matrix
    bag = [0] * len(words)
    for s in sentence_words:
        for i, word in enumerate(words):
            if word == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % word)
    return np.array(bag)


def predict_class(sentence):
    # filter below  threshold predictions
    p = bag_of_words(sentence, words, show_details=True)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    #  print("getResponse     list_of_intents ", list_of_intents)
    serverlog = []
    result = None
    for i in list_of_intents:
        if i['tag'] == tag:
            msg1 = "getResponse  predicted class:  " + str(ints)
            msg2 = "getResponse     found intent: " + str(i)
            serverlog.append(msg1 + "\n")
            serverlog.append(msg2 + "\n")
            print("getResponse  predicted class: %s", ints)
            print("getResponse     found intent: %s ", i)
            result = random.choice(i['responses'])
            break

    response = {
        'response': result,
        'serverlog': serverlog,
        'tag': tag
    }

    return response


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
    districts = nlp_spacy_districts(userText)

    print("=========  districts ===========")
    for token in districts:
        print("found districts: ", token.text, token.lemma_, token.pos_)
    print("=========  END districts ===========")

    print("=========  districts entities ===========")
    print("Entities newly trained ", [(ent.text, ent.label_) for ent in districts.ents])
    print("=========  END districts entities ===========")



    ner = nlp_spacy_full(userText)
    print("=========  NER ===========")
    for token in ner:
        print("found ner:   ", token.text, token.lemma_, token.pos_)
    print("=========  END NER ===========")

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

    # contains a random response depending on the intent found
    response = getResponse(ints, intents)
    populateContext(ctx, response)

    district = checkDistrict(userText)

    print("response: " + response["response"])
    session["context"] = ctx.data
    return response


if __name__ == "__main__":
    app.config["SECRET_KEY"] = "i am just secret"
    app.run()
