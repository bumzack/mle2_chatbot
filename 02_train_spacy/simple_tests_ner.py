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

    sentence = "I want to go to a public pool in Döbling or in Margareten maybe to Wieden or everyday is great in  Hernals, but Simmering sucks - where apple dont live in the U.K, but is worth $1 billion"
    pool = nlp2(sentence)

    for token in pool:
        print("newly trained       ", token.text, token.lemma_, token.pos_)

    print("Tokens newly trained    ", [(t.text, t.ent_type_, t.ent_iob) for t in pool])
    print("Entities newly trained ", [(ent.text, ent.label_) for ent in pool.ents])

    print("\n\n\n\n")

    nlp = spacy.load("en_core_web_lg")
    pool_standard = nlp(sentence)
    for token in pool_standard:
        print("standard  ", token.text, token.lemma_, token.pos_)

    print("Tokens standard  ", [(t.text, t.ent_type_, t.ent_iob) for t in pool_standard])
    print("Entities standard ", [(ent.text, ent.label_) for ent in pool_standard.ents])

    apple = "Apple is looking at buying U.K. startup for $1 billion"
    apple_doc = nlp(apple)



    for ent in apple_doc.ents:
        print("ent apple standard: ", ent.text, ent.start_char, ent.end_char, ent.label_)

    apple_doc2 = nlp2(apple)

    for ent in apple_doc2.ents:
        print("ent apple newly trained : ", ent.text, ent.start_char, ent.end_char, ent.label_)
