# https://github.com/explosion/spaCy/blob/master/examples/training/train_ner.py

# !/usr/bin/env python
# coding: utf8
"""Example of training spaCy's named entity recognizer, starting off with an
existing model or a blank model.
For more details, see the documentation:
* Training: https://spacy.io/usage/training
* NER: https://spacy.io/usage/linguistic-features#named-entities
Compatible with: spaCy v2.0.0+
Last tested with: v2.2.4
"""
from __future__ import unicode_literals, print_function

import sys

from train_spacy.spacy_ner_training_data import TRAINING_DATA

sys.path.append('./')

import random

import spacy



nlp = spacy.blank("en")
optimizer = nlp.begin_training()
for i in range(20):
    random.shuffle(TRAINING_DATA)
    for text, annotations in TRAINING_DATA:
        nlp.update([text], [annotations], sgd=optimizer)
nlp.to_disk("../data/spacy_simple")

print("DONE")
