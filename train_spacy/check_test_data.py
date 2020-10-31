import sys

from train_spacy.spacy_ner_training_data import TRAINING_DATA

sys.path.append('./')



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

not_found = []
for t in TRAINING_DATA:
    # print("sentence: ", t[0])
    sent = t[0]

    for ent in t[1].items():
        # print("    entities:  ", ent)
        for e in ent[1]:
            # print("                 e: ", e)
            start = e[0]
            end = e[1]
            distr = sent[start:end]
            # print("                district: ", sent[start:end])
            found = False
            for n in names:
                if n == distr or n.lower() == distr:
                    found = True
            if not found:
                for z in zipCode:
                    if str(z) == distr:
                        found = True
            if not found:
                print("       '", distr, "' NOT  found in sentence '", sent, "', start: " + str(start) + ", end: " + str(end))
                not_found.append(distr)

# print("############################################################")
# print("not found .........")
# for n in not_found:
#     print("notfound:  ", n)
