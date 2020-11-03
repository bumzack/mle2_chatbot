import csv
import os
import sys

import spacy

from step_03_run_server.nn_stuff import getResponse, predict_class
from step_03_run_server.zip_mapping import district_mapping

TOMORROW = "tomorrow"
TODAY = "today"

STATIC_DIR = os.path.abspath('./static')
print("STATIC DIR   ", STATIC_DIR)

POOL_NAME = 2
ADDRESS = 3
DISTRICT = 5
AUSLASTUNG_TODAY = 7
AUSLASTUNG_TOMORROW = 9
