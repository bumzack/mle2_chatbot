from typing import Optional

import spacy

from step_03_run_server.const import SPACY_MODEL

THRESHOLD_SIMILARITY = 0.8

nlp_spacy_full = spacy.load(SPACY_MODEL)

district_zip_mapping = {
    "1": 1010,
    "2": 1020,
    "3": 1030,
    "4": 1040,
    "5": 1050,
    "6": 1060,
    "7": 1070,
    "8": 1080,
    "9": 1090,
    "10": 1100,
    "11": 1110,
    "12": 1120,
    "13": 1130,
    "14": 1140,
    "15": 1150,
    "16": 1160,
    "17": 1170,
    "18": 1180,
    "19": 1190,
    "20": 1200,
    "21": 1210,
    "22": 1220,
    "23": 1230
}

district_name_mapping = {
    "Innere Stadt": 1010,
    "Leopoldstadt": 1020,
    "Landstraße": 1030,
    "Wieden": 1040,
    "Margareten": 1050,
    "Mariahilf": 1060,
    "Neubau": 1070,
    "Josefstadt": 1080,
    "Alsergrund": 1090,
    "Favoriten": 1100,
    "Simmering": 1110,
    "Meidling": 1120,
    "Hietzing": 1130,
    "Penzing": 1140,
    "Rudolfsheim-Fünfhaus": 1150,
    "Ottakring": 1160,
    "Hernals": 1170,
    "Währing": 1180,
    "Döbling": 1190,
    "Brigittenau": 1200,
    "Floridsdorf": 1210,
    "Donaustadt": 1220,
    "Liesing": 1230
}


def word_sim(w1: str, w2: str):
    doc1 = nlp_spacy_full(w1)
    doc2 = nlp_spacy_full(w2)
    sim = doc1.similarity(doc2)
    # print("simularity between: {} and {}: {}".format(w1, w2, sim))
    return sim


def find_best_district_match(district: str) -> Optional[str]:
    max_sim = 0
    max_sim_district = None
    for d in district_name_mapping:
        sim = word_sim(d, district)
        if sim > max_sim:
            max_sim = sim
            max_sim_district = d

    if max_sim > THRESHOLD_SIMILARITY and not max_sim_district is None:
        return max_sim_district

    # find by zipcode
    for name, zipcode in district_name_mapping.items():
        if str(zipcode) == str(district):
            return name

    return None
