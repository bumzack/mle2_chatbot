import sys

import spacy
from flask import session, request

from step_03_run_server.botcontext import BotContext
from step_03_run_server.const import MODEL_DIR, TODAY, TOMORROW, SPACY_MODEL
from step_03_run_server.nn_stuff import predict_class, getResponse, intents

sys.path.append('./')

print("Loading from: '", MODEL_DIR, "'")
nlp_spacy_districts = spacy.load(MODEL_DIR)

nlp_spacy_full = spacy.load(SPACY_MODEL)


def populateContext(ctx, response):
    if response["tag"] == 'intent_pool_today':
        print("adding 'today' to ctx ")
        ctx.setIntentPoolToday()
        ctx.setDay(TODAY)

    if response["tag"] == 'intent_pool_tomorrow':
        print("adding 'tomorrow' to ctx ")
        ctx.setIntentPoolTomorrow()
        ctx.setDay(TOMORROW)

    if response["tag"] == 'intent_pool_where':
        print("adding 'intent_pool_where' to ctx ")
        ctx.setIntentPoolWhere()

    if response["tag"] == 'intent_greeting':
        print("adding 'intent_greeting' to ctx ")
        ctx.setIntentGreeting()

    if response["tag"] == 'intent_goodbye':
        print("adding 'intent_goodbye' to ctx ")
        ctx.setIntentGoodBye()

    if response["tag"] == 'intent_thanks':
        print("adding 'intent_thanks' to ctx ")
        ctx.setIntentThanks()

    if response["tag"] == 'intent_noanswer':
        print("adding 'intent_noanswer' to ctx ")
        ctx.setIntentNoanswer()

    if response["tag"] == 'intent_options':
        print("adding 'intent_options' to ctx ")
        ctx.setIntentOptions()

    if response["tag"] == 'intent_user_bored':
        print("adding 'intent_user_bored' to ctx ")
        ctx.setIntentUSerBored()

    if response["tag"] == 'intent_user_not_happy':
        print("adding 'intent_user_not_happy' to ctx ")
        ctx.setIntentUseNotHappy()

    if response["tag"] == 'intent_user_approve':
        print("adding 'intent_user_approve' to ctx ")
        ctx.setIntentUserApprove()


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
                print("checkDay: found TODAY")
                return TODAY
            if d.lower() == TOMORROW:
                print("checkDay: found TOMORROW")
                return TOMORROW


def extract_infos_from_user_input(ctx: BotContext, userText: str):
    district = checkDistrict(userText)
    if not district is None:
        ctx.setDistrict(district)
    day = checkDay(userText)
    if not day is None:
        ctx.setDay(day)


def get_context():
    ctx = BotContext()
    if not session.get("context") is None:
        data = session.get("context")
        ctx.data = data
        ctx.print_context("at beginning of request")
    else:
        print("====== no context on session object found =======")
    return ctx


def handle_user_request():
    ctx = get_context()

    userText = request.args.get('msg')
    ints = predict_class(userText)

    extract_infos_from_user_input(ctx, userText)

    # contains a random response depending on the intent found
    response = getResponse(ints, intents)
    populateContext(ctx, response)
    # print("response: " + response["response"])
    session["context"] = ctx.data

    ctx.print_context("ctx at end of method")

    return response
