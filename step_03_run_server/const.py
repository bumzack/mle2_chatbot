import os

spacy_model_dir = "../data/sapcy_ner_trained_model"
# spacy_model_simple_dir = "../data/spacy_simple"

# TODO use en_core_web_lg
SPACY_MODEL = "en_core_web_sm"

TOMORROW = "tomorrow"
TODAY = "today"

STATIC_DIR = os.path.abspath('./static')
print("STATIC DIR   ", STATIC_DIR)

POOL_NAME = 2
ADDRESS = 3
DISTRICT = 5
AUSLASTUNG_TODAY = 7
AUSLASTUNG_TOMORROW = 9

MODEL_DIR = spacy_model_dir