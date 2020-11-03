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

from step_02_train_spacy.spacy_ner_training_data import TRAINING_DATA
from step_03_run_server.const import SPACY_MODEL

sys.path.append('./')

import random
import warnings
from pathlib import Path

import plac
import spacy
from spacy.util import minibatch, compounding


@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int),
)
def main(model=None, output_dir=None, n_iter=100):
    """Load the model, set up the pipeline and train the entity recognizer."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank("en")  # create blank Language class
        print("Created blank 'en' model")

    # create the built-in pipeline components and add them to the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if "ner" not in nlp.pipe_names:
        ner = nlp.create_pipe("ner")
        nlp.add_pipe(ner, last=True)
    # otherwise, get it so we can add labels
    else:
        ner = nlp.get_pipe("ner")

    # add labels
    for _, annotations in TRAINING_DATA:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    # get names of other pipes to disable them during training
    pipe_exceptions = ["ner", "trf_wordpiecer", "trf_tok2vec"]
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe not in pipe_exceptions]
    # only train NER
    with nlp.disable_pipes(*other_pipes), warnings.catch_warnings():
        # show warnings for misaligned entity spans once
        warnings.filterwarnings("once", category=UserWarning, module='step_02_train_spacy')

        # reset and initialize the weights randomly – but only if we're
        # training a new model
        if model is None:
            nlp.begin_training()
        for itn in range(n_iter):
            print("iter " + str(itn) + "/" + str(n_iter))
            random.shuffle(TRAINING_DATA)
            losses = {}
            # batch up the examples using spaCy's minibatch
            batches = minibatch(TRAINING_DATA, size=compounding(4.0, 32.0, 1.001))
            for batch in batches:
                texts, annotations = zip(*batch)
                nlp.update(
                    texts,  # batch of texts
                    annotations,  # batch of annotations
                    drop=0.5,  # dropout - make it harder to memorise data
                    losses=losses,
                )
            print("Losses", losses)

    # test the trained model
    for text, _ in TRAINING_DATA:
        doc = nlp(text)
        print("TrainData  Entities", [(ent.text, ent.label_) for ent in doc.ents])
        print("TrainData  Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        for text, _ in TRAINING_DATA:
            doc = nlp2(text)
            print("TrainData2  Entities", [(ent.text, ent.label_) for ent in doc.ents])
            print("TrainData2  Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])


if __name__ == "__main__":
    spacy_model_dir = "../data/sapcy_ner_trained_model"
    train = True

    if train:
        main(SPACY_MODEL, spacy_model_dir, 100)

    # test the saved model
    print("Loading from", spacy_model_dir)
    nlp2 = spacy.load(spacy_model_dir)

    s = "Autonomous cars shift insurance liability toward manufacturers"
    auto_cars = nlp2(s)
    # print("\n\nUUUU Entities", [(ent.text, ent.label_) for ent in auto_cars.ents])
    # print("\n\nUUUU Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in auto_cars])

    for token in auto_cars:
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        #       token.shape_, token.is_alpha, token.is_stop)
        print(token.text, token.lemma_, token.pos_)
    #
    # s = "Where is an open pool in Margareten?"
    #
    #
    # doc = nlp2(s)
    # print("NEW  Entities", [(ent.text, ent.label_) for ent in doc.ents])
    # print("NEW  Tokens", [(t.text, t.ent_type_, t.ent_iob) for t in doc])
    #
    # nlp = spacy.load("en_core_web_lg")
    # pool_standard = nlp(s)
    # print("Entities default ", [(ent.text, ent.label_) for ent in pool_standard.ents])
    # print("Tokens default ", [(t.text, t.ent_type_, t.ent_iob) for t in pool_standard])

    print("\n\n\n\nDONE")
