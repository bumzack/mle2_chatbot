from __future__ import unicode_literals, print_function

import sys

SPACY_BASE_MODEL = "en_core_web_sm"

sys.path.append('./')

import spacy

if __name__ == "__main__":
    spacy_model_dir = "../data/sapcy_ner_trained_model"
    # spacy_model_simple_dir = "../data/spacy_simple"

    model_dir = spacy_model_dir
    print("Loading from: '", model_dir,"'")
    nlp2 = spacy.load(model_dir)
    nlp_spacy_full = spacy.load(SPACY_BASE_MODEL)

    # sentence = "in döbling"
    # district = nlp2(sentence)
    #
    # for token in district:
    #     print("district   newly trained       ", token.text, token.lemma_, token.pos_)
    #
    # print("district Tokens newly trained    ", [(t.text, t.ent_type_, t.ent_iob) for t in district])
    # print("district Entities newly trained ", [(ent.text, ent.label_) for ent in district.ents])
    #
    # print("\n\n\n\n")

    sentence = "i am bored today"
    day = nlp_spacy_full(sentence)

    # for token in day:
    #     print("looking for day       ", token.text, token.lemma_, token.pos_)

    # print("looking for day     ", [(t.text, t.ent_type_, t.ent_iob) for t in day])
    print("looking for day ents ", [(ent.text, ent.label_) for ent in day.ents])

    print("\n\n\n\n")

