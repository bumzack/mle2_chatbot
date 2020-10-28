import sys
sys.path.append('./')

from spacy_ner_training_data import  TRAIN_DATA

names = [
    "Innere Stadt",
    "Leopoldstadt",
    "Landstraße",
    "Wieden",
    "Margareten",
    "Mariahilf",
    "Neubau",
    "Josefstadt",
    "Alsergrund",
    "Favoriten",
    "Simmering",
    "Meidling",
    "Hietzing",
    "Penzing",
    "Rudolfsheim-Fünfhaus",
    "Ottakring", "Hernals", "Währing",
    "Döbling",
    "Brigittenau",
    "Floridsdorf",
    "Donaustadt",
    "Liesing"
]

zipCode = [
    1010,
    1020,
    1030,
    1040,
    1050,
    1060,
    1070,
    1080,
    1090,
    1100,
    1110,
    1120,
    1130,
    1140,
    1150,
    1160,
    1170,
    1180,
    1190,
    1200,
    1210,
    1220,
   1230
]

for t in TRAIN_DATA:
    print("sentence: %s".format(t))
