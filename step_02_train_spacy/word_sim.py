from __future__ import unicode_literals, print_function

import sys

from step_03_run_server.const import SPACY_MODEL

sys.path.append('./')

import spacy


def word_sim(w1: str, w2: str):
    doc1 = nlp_spacy_full(w1)
    doc2 = nlp_spacy_full(w2)
    sim = doc1.similarity(doc2)
    print("simularity between: {} and {}: {}".format(w1, w2, sim))


if __name__ == "__main__":
    nlp_spacy_full = spacy.load(SPACY_MODEL)

    word_sim("Heiligenstadt", "Heilgenstadt")
    word_sim("Heiligenstadt", "Heiligenstad")
    word_sim("Heiligenstadt", "Heilgenstad")
