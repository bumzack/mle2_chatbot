import sys

import spacy

from step_03_run_server.const import MODEL_DIR, TODAY, TOMORROW


sys.path.append('./')

print("Loading from: '", MODEL_DIR, "'")
nlp_spacy_districts = spacy.load(MODEL_DIR)

nlp_spacy_full = spacy.load(SPACY_MODEL)


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
                print("checkDay: found TODAY")
                return TODAY
            if d.lower() == TOMORROW:
                print("checkDay: found TOMORROW")
                return TOMORROW
