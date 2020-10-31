from __future__ import unicode_literals, print_function

import sys

sys.path.append('./')

import spacy

if __name__ == "__main__":
    spacy_model_dir = "../data/sapcy_ner_trained_model"
    spacy_model_simple_dir = "../data/spacy_simple"

    model_dir = spacy_model_dir
    print("Loading from: '", model_dir,"'")
    nlp2 = spacy.load(model_dir)


    sentence = "in döbling"
    district = nlp2(sentence)

    for token in district:
        print("district   newly trained       ", token.text, token.lemma_, token.pos_)

    print("district Tokens newly trained    ", [(t.text, t.ent_type_, t.ent_iob) for t in district])
    print("district Entities newly trained ", [(ent.text, ent.label_) for ent in district.ents])

    print("\n\n\n\n")

