import sys

import spacy
from flask import session, request

from step_03_run_server.botcontext import BotContext
from step_03_run_server.const import MODEL_DIR, TODAY, TOMORROW, SPACY_MODEL
from step_03_run_server.district_utils import find_best_district_match
from step_03_run_server.nn_stuff import predict_class, getResponse, intents
from step_03_run_server.pool_data import PoolData

sys.path.append('./')

poolData = PoolData()

# print("Loading from: '", MODEL_DIR, "'")
nlp_spacy_districts = spacy.load(MODEL_DIR)
nlp_spacy_full = spacy.load(SPACY_MODEL)


def populateContext(ctx, response):
    if response["tag"] == 'intent_pool_today':
        # print("adding 'today' to ctx ")
        ctx.setIntentPoolToday()
        ctx.setDay(TODAY)

    if response["tag"] == 'intent_pool_tomorrow':
        # print("adding 'tomorrow' to ctx ")
        ctx.setIntentPoolTomorrow()
        ctx.setDay(TOMORROW)

    if response["tag"] == 'intent_pool_where':
        # print("adding 'intent_pool_where' to ctx ")
        ctx.setIntentPoolWhere()

    if response["tag"] == 'intent_greeting':
        # print("adding 'intent_greeting' to ctx ")
        ctx.setIntentGreeting()

    if response["tag"] == 'intent_goodbye':
        # print("adding 'intent_goodbye' to ctx ")
        ctx.setIntentGoodBye()

    if response["tag"] == 'intent_thanks':
        # print("adding 'intent_thanks' to ctx ")
        ctx.setIntentThanks()

    if response["tag"] == 'intent_noanswer':
        # print("adding 'intent_noanswer' to ctx ")
        ctx.setIntentNoanswer()

    if response["tag"] == 'intent_options':
        # print("adding 'intent_options' to ctx ")
        ctx.setIntentOptions()

    if response["tag"] == 'intent_user_bored':
        # print("adding 'intent_user_bored' to ctx ")
        ctx.setIntentUSerBored()

    if response["tag"] == 'intent_user_not_happy':
        # print("adding 'intent_user_not_happy' to ctx ")
        ctx.setIntentUseNotHappy()

    if response["tag"] == 'intent_user_approve':
        # print("adding 'intent_user_approve' to ctx ")
        ctx.setIntentUserApprove()


def checkDistrict(userText):
    spacy_districts = nlp_spacy_districts(userText)

    print("=========  checkDistrict entities ===========")
    print("district Entities newly trained ", [(ent.text, ent.label_) for ent in spacy_districts.ents])
    print("=========  checkDistrict  END districts entities ===========")
    districts = []
    for ent in spacy_districts.ents:
        if ent.label_ == "VIE_DIS":
            d = find_best_district_match(ent.text)
            if not d is None:
                districts.append(d)

    print("=========  checkDistrict: filtered districts entities ===========")
    print("filtered districts ", [d for d in districts])
    print("=========  checkDistrict END filtered  districts entities ===========")

    if len(districts) > 0:
        print("found a district: {}".format(districts[0]))
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
    # has user entered a district?
    district = checkDistrict(userText)
    if not district is None:
        print("setting district to {}".format(district))
        ctx.setDistrict(district)

    # has user entered a "date" (today or tomorrow) ?
    day = checkDay(userText)
    if not day is None:
        print("setting day to {}".format(day))
        ctx.setDay(day)


def get_context():
    ctx = BotContext()
    if not session.get("context") is None:
        data = session.get("context")
        ctx.data = data
        ctx.print_context("at beginning of request")
    # else:
    # print("====== no context on session object found =======")
    return ctx


def response_based_on_context_and_intent(ctx: BotContext, intent: str) -> str:
    response = ""
    if ctx.hasDay() and not ctx.hasDistrict():
        print("ctx.hasDay() and not ctx.hasDistrict()")
        response = "You want to go to a pool {}, but i don't know where! Tell me the zip code or name of a district!".format(ctx.getDay())
    elif not ctx.hasDay() and ctx.hasDistrict():
        print("elif not ctx.hasDay() and ctx.hasDistrict()")
        response = "You want to go to a pool in {}, but i don't know when! Tell me when you want to go - today or tomorrow?".format(
            ctx.getDistrict())
    elif ctx.getShownPools() and intent == "intent_user_approve":
        print("ctx.getShownPools() and intent ==  intent_user_approve")
        response = "I am happy you are happy :-)"
    elif ctx.getShownPools() and intent == "intent_user_not_happy":
        print("ctx.getShownPools() and intent ==  intent_user_not_happy")
        response = "Oh - that's not good - maybe choose another district or day?"
    elif ctx.getShownPools() and intent == "intent_goodbye":
        print("ctx.getShownPools() and intent ==  intent_goodbye")
        response = "bye!"
    elif ctx.getShownPools() and intent == "intent_user_bored":
        print("ctx.getShownPools() and intent ==  intent_user_bored")
        response = "Sorry you're bored - I already showed you some addresses of public pools!"
    elif ctx.hasDay() and ctx.hasDistrict():
        print("ctx.hasDay() and ctx.hasDistrict()")
        # ctx.print_context("before calling get_pools_for_day_and_district")
        # print("calling   get_pools_for_day_and_district  with day {} and district {}".format(ctx.getDay(), ctx.getDistrict()))
        data = poolData.get_pools_for_day_and_district(ctx.getDay(), ctx.getDistrict())
        if data is None:
            return "I am sorry - but i couldn't find any data for your choice: day: {}, district: {}".format(ctx.getDay(),
                                                                                                             ctx.getDistrict())
        response = "Nice! - i found the following pools for you: " + data
        response = response + "<br><br>Are you happy with this information?"
        ctx.setShownPools(True)

    return response


def handle_user_request():
    ctx = get_context()

    userText = request.args.get('msg')
    ints = predict_class(userText)

    print("userText: {}".format(userText))
    extract_infos_from_user_input(ctx, userText)

    # contains a random response depending on the intent found
    default_response_based_on_intent = getResponse(ints, intents)

    # if there is a better repsonse with more specific feedback, than solely based on the intent, overwrite the response text
    response_ner = response_based_on_context_and_intent(ctx, default_response_based_on_intent["tag"])
    if response_ner != "":
        default_response_based_on_intent["response"] = response_ner

    populateContext(ctx, default_response_based_on_intent)
    # print("response: " + response["response"])
    session["context"] = ctx.data

    ctx.print_context("ctx at end of method")

    return default_response_based_on_intent
