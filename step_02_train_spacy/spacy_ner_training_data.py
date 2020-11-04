# training data
DATA = [
    ("Who is Shaka Khan?", {"entities": [(7, 17, "PERSON")]}),
    ("Margareten is a district in Vienna?", {"entities": [(0, 10, "VIE_DIS")]}),
    ("Floridsdorf is my hood?", {"entities": [(0, 11, "VIE_DIS")]}),

    ("The people in Innere Stadt are a little bit different.", {"entities": [(14, 26, "VIE_DIS")]}),
    ("The people in Leopoldstadt are a little bit different.", {"entities": [(14, 26, "VIE_DIS")]}),
    ("The people in Landstraße are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("The people in Wieden are a little bit different.", {"entities": [(14, 20, "VIE_DIS")]}),
    ("The people in Margareten are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("The people in Mariahilf are a little bit different.", {"entities": [(14, 23, "VIE_DIS")]}),
    ("The people in Neubau are a little bit different.", {"entities": [(14, 20, "VIE_DIS")]}),
    ("The people in Josefstadt are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("The people in Alsergrund are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("The people in Favoriten are a little bit different.", {"entities": [(14, 23, "VIE_DIS")]}),
    ("The people in Simmering are a little bit different.", {"entities": [(14, 23, "VIE_DIS")]}),
    ("The people in Meidling are a little bit different.", {"entities": [(14, 22, "VIE_DIS")]}),
    ("The people in Hietzing are a little bit different.", {"entities": [(14, 22, "VIE_DIS")]}),
    ("The people in Penzing are a little bit different.", {"entities": [(14, 21, "VIE_DIS")]}),
    ("The people in Rudolfsheim-Fünfhaus are a little bit different.", {"entities": [(14, 34, "VIE_DIS")]}),
    ("The people in Ottakring are a little bit different.", {"entities": [(14, 23, "VIE_DIS")]}),
    ("The people in Hernals are a little bit different.", {"entities": [(14, 21, "VIE_DIS")]}),
    ("The people in Währing are a little bit different.", {"entities": [(14, 21, "VIE_DIS")]}),
    ("The people in Döbling are a little bit different.", {"entities": [(14, 21, "VIE_DIS")]}),
    ("The people in Brigittenau are a little bit different.", {"entities": [(14, 25, "VIE_DIS")]}),
    ("The people in Floridsdorf are a little bit different.", {"entities": [(14, 25, "VIE_DIS")]}),
    ("The people in Donaustadt are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("The people in Liesing are a little bit different.", {"entities": [(14, 21, "VIE_DIS")]}),

    ("The mayor has his office in the district named Innere Stadt.", {"entities": [(47, 59, "VIE_DIS")]}),
    ("The people in Leopoldstadt are a little bit different.", {"entities": [(14, 26, "VIE_DIS")]}),
    ("Most of the time I am not in in the district called Landstraße.", {"entities": [(52, 62, "VIE_DIS")]}),
    ("I didn't know Wieden until 5 minutes ago.", {"entities": [(14, 20, "VIE_DIS")]}),
    ("The people in Margareten are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("My father used to work near a street which name is quite similar to Mariahilf.", {"entities": [(68, 77, "VIE_DIS")]}),
    ("The buildings in Neubau are ugly.", {"entities": [(17, 23, "VIE_DIS")]}),
    ("Most of the parks in Josefstadt are not very human friendly.", {"entities": [(21, 31, "VIE_DIS")]}),
    ("I don't know where the district Alsergrund is.", {"entities": [(32, 42, "VIE_DIS")]}),
    ("Favoriten probably has the worst reputation of all of them.", {"entities": [(0, 9, "VIE_DIS")]}),
    ("I don't like Simmering.", {"entities": [(13, 22, "VIE_DIS")]}),
    ("The name Meidling is part a greats song by Alkbottle.", {"entities": [(9, 17, "VIE_DIS")]}),
    ("Don't care about Hietzing at all.", {"entities": [(17, 25, "VIE_DIS")]}),
    ("I drive through Penzing all the time.", {"entities": [(16, 23, "VIE_DIS")]}),
    ("Where is Rudolfsheim-Fünfhaus?", {"entities": [(9, 29, "VIE_DIS")]}),
    ("The markets in Ottakring are nice.", {"entities": [(15, 24, "VIE_DIS")]}),
    ("Hernals sounds like the german word for neck.", {"entities": [(0, 7, "VIE_DIS")]}),
    ("What ever happens in Währing stays in Währing.", {"entities": [(21, 28, "VIE_DIS"), (38, 45, "VIE_DIS")]}),
    ("I only pass through Döbling in a car.", {"entities": [(20, 27, "VIE_DIS")]}),
    ("Why is Brigittenau written with an i instead of an e.", {"entities": [(7, 18, "VIE_DIS")]}),
    ("The people in Floridsdorf are a little bit different.", {"entities": [(14, 25, "VIE_DIS")]}),
    ("Donaustadt are a little bit different.", {"entities": [(0, 10, "VIE_DIS")]}),
    ("There are no book shops in Liesing.", {"entities": [(27, 34, "VIE_DIS")]}),

    ("The district Innere Stadt has the zipcode 1010.", {"entities": [(13, 25, "VIE_DIS"), (42, 46, "VIE_DIS")]}),
    ("The district Leopoldstadt has the zipcode 1020.", {"entities": [(13, 25, "VIE_DIS"), (42, 46, "VIE_DIS")]}),
    ("The district Landstraße has the zipcode 1030.", {"entities": [(13, 23, "VIE_DIS"), (40, 44, "VIE_DIS")]}),
    ("The district Wieden has the zipcode 1040.", {"entities": [(13, 19, "VIE_DIS"), (36, 40, "VIE_DIS")]}),
    ("The district Margareten has the zipcode 1050.", {"entities": [(13, 23, "VIE_DIS"), (40, 44, "VIE_DIS")]}),
    ("The district Mariahilf has the zipcode 1060.", {"entities": [(13, 22, "VIE_DIS"), (39, 43, "VIE_DIS")]}),
    ("The district Neubau has the zipcode 1070.", {"entities": [(13, 19, "VIE_DIS"), (36, 40, "VIE_DIS")]}),
    ("The district Josefstadt has the zipcode 1080.", {"entities": [(13, 23, "VIE_DIS"), (40, 44, "VIE_DIS")]}),
    ("The district Alsergrund has the zipcode 1090.", {"entities": [(13, 23, "VIE_DIS"), (40, 44, "VIE_DIS")]}),
    ("The district Favoriten has the zipcode 1100.", {"entities": [(13, 22, "VIE_DIS"), (39, 43, "VIE_DIS")]}),
    ("The district Simmering has the zipcode 1110.", {"entities": [(13, 22, "VIE_DIS"), (39, 43, "VIE_DIS")]}),
    ("The district Meidling has the zipcode 1120.", {"entities": [(13, 21, "VIE_DIS"), (38, 42, "VIE_DIS")]}),
    ("The district Hietzing has the zipcode 1130.", {"entities": [(13, 21, "VIE_DIS"), (38, 42, "VIE_DIS")]}),
    ("The district Penzing has the zipcode 1140.", {"entities": [(13, 20, "VIE_DIS"), (37, 41, "VIE_DIS")]}),
    ("The district Rudolfsheim-Fünfhaus has the zipcode 1150.", {"entities": [(13, 33, "VIE_DIS"), (50, 54, "VIE_DIS")]}),
    ("The district Ottakring has the zipcode 1160.", {"entities": [(13, 22, "VIE_DIS"), (39, 43, "VIE_DIS")]}),
    ("The district Hernals has the zipcode 1170.", {"entities": [(13, 20, "VIE_DIS"), (37, 41, "VIE_DIS")]}),
    ("The district Währing has the zipcode 1180.", {"entities": [(13, 20, "VIE_DIS"), (37, 41, "VIE_DIS")]}),
    ("The district Döbling has the zipcode 1190.", {"entities": [(13, 20, "VIE_DIS"), (37, 41, "VIE_DIS")]}),
    ("The district Brigittenau has the zipcode 1200.", {"entities": [(13, 24, "VIE_DIS"), (41, 45, "VIE_DIS")]}),
    ("The district Floridsdorf has the zipcode 1210.", {"entities": [(13, 24, "VIE_DIS"), (41, 45, "VIE_DIS")]}),
    ("The district Donaustadt has the zipcode 1220.", {"entities": [(13, 23, "VIE_DIS"), (40, 44, "VIE_DIS")]}),
    ("The district Liesing has the zipcode 1230.", {"entities": [(13, 20, "VIE_DIS"), (37, 41, "VIE_DIS")]}),

    ("Innere Stadt", {"entities": [(0, 12, "VIE_DIS")]}),
    ("Leopoldstadt", {"entities": [(0, 12, "VIE_DIS")]}),
    ("Landstraße", {"entities": [(0, 10, "VIE_DIS")]}),
    ("Wieden", {"entities": [(0, 6, "VIE_DIS")]}),
    ("Margareten", {"entities": [(0, 10, "VIE_DIS")]}),
    ("Mariahilf", {"entities": [(0, 9, "VIE_DIS")]}),
    ("Neubau", {"entities": [(0, 6, "VIE_DIS")]}),
    ("Josefstadt", {"entities": [(0, 10, "VIE_DIS")]}),
    ("Alsergrund", {"entities": [(0, 10, "VIE_DIS")]}),
    ("Favoriten", {"entities": [(0, 9, "VIE_DIS")]}),
    ("Simmering", {"entities": [(0, 9, "VIE_DIS")]}),
    ("Meidling", {"entities": [(0, 8, "VIE_DIS")]}),
    ("Hietzing", {"entities": [(0, 8, "VIE_DIS")]}),
    ("Penzing", {"entities": [(0, 7, "VIE_DIS")]}),
    ("Rudolfsheim-Fünfhaus", {"entities": [(0, 20, "VIE_DIS")]}),
    ("Ottakring", {"entities": [(0, 9, "VIE_DIS")]}),
    ("Hernals", {"entities": [(0, 7, "VIE_DIS")]}),
    ("Währing", {"entities": [(0, 7, "VIE_DIS")]}),
    ("Döbling", {"entities": [(0, 7, "VIE_DIS")]}),
    ("Brigittenau", {"entities": [(0, 11, "VIE_DIS")]}),
    ("Floridsdorf", {"entities": [(0, 11, "VIE_DIS")]}),
    ("Donaustadt", {"entities": [(0, 10, "VIE_DIS")]}),
    ("Liesing", {"entities": [(0, 7, "VIE_DIS")]}),

    ("1010", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1020", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1030", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1040", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1050", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1060", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1070", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1080", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1090", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1100", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1110", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1120", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1130", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1140", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1150", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1160", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1170", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1180", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1190", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1210", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1220", {"entities": [(0, 4, "VIE_DIS")]}),
    ("1230", {"entities": [(0, 4, "VIE_DIS")]}),

    ("The district Innere Stadt should not be mistaken with Leopoldstadt.", {"entities": [(13, 25, "VIE_DIS"), (54, 66, "VIE_DIS")]}),
    ("Leopoldstadt is the opposite of Favoriten in regards to life quality.", {"entities": [(0, 12, "VIE_DIS"), (32, 41, "VIE_DIS")]}),
    ("If you ever been to Landstraße going to Simmering is not worth it.", {"entities": [(20, 30, "VIE_DIS"), (40, 49, "VIE_DIS")]}),
    ("The technical university is in Wieden, but the veterinary university is in Floridsdorf.",
     {"entities": [(31, 37, "VIE_DIS"), (75, 86, "VIE_DIS")]}),
    ("Moving to Margareten is like working in the Josefstadt.", {"entities": [(10, 20, "VIE_DIS"), (44, 54, "VIE_DIS")]}),
    ("Mariahilf has the best shops, compored to Ottakring where you can only buy food.",
     {"entities": [(0, 9, "VIE_DIS"), (42, 51, "VIE_DIS")]}),
    ("Neubau has as many letters as Josefstadt.", {"entities": [(0, 6, "VIE_DIS"), (30, 40, "VIE_DIS")]}),
    ("Josefstadt is named after Jesus father, but not Meidling.", {"entities": [(0, 10, "VIE_DIS"), (48, 56, "VIE_DIS")]}),
    ("The main reason Alsergrund exists is to make the people living in the Innere Stadt laugh.",
     {"entities": [(16, 26, "VIE_DIS"), (70, 82, "VIE_DIS")]}),
    ("In Favoriten nobody cares about Simmering.", {"entities": [(3, 12, "VIE_DIS"), (32, 41, "VIE_DIS")]}),
    ("In Simmering everybod cares about and hates Favoriten at the same time.", {"entities": [(3, 12, "VIE_DIS"), (44, 53, "VIE_DIS")]}),
    ("Meidling has a zipcode with the same checksum as Wieden.", {"entities": [(0, 8, "VIE_DIS"), (49, 55, "VIE_DIS")]}),
    ("The offices in Hietzing are older than those in Hernals.", {"entities": [(15, 23, "VIE_DIS"), (48, 55, "VIE_DIS")]}),

    ("The streets in Penzing are great, compared to those in Brigittenau", {"entities": [(15, 22, "VIE_DIS"), (55, 66, "VIE_DIS")]}),
    ("The district Rudolfsheim-Fünfhaus is the district with longest name, Wieden has one of the shortest names.",
     {"entities": [(13, 33, "VIE_DIS"), (69, 75, "VIE_DIS")]}),
    ("The brewery in Ottakring is world famous, all the other breweries in Margareten are unknown.",
     {"entities": [(15, 24, "VIE_DIS"), (69, 79, "VIE_DIS")]}),
    ("The train station in Hernals was built by Wagner, just like those in Meidling.",
     {"entities": [(21, 28, "VIE_DIS"), (69, 77, "VIE_DIS")]}),
    ("Währing is one of the few districts which as an umlaut in its name.", {"entities": [(0, 7, "VIE_DIS")]}),
    ("Renting an apartment in Döbling is twice  as expensive compared to Favoriten.",
     {"entities": [(24, 31, "VIE_DIS"), (67, 76, "VIE_DIS")]}),
    ("The way Brigittenau is pronounced is completely different from Liesing.", {"entities": [(8, 19, "VIE_DIS"), (63, 70, "VIE_DIS")]}),
    ("Floridsdorf is the best hood in Vienna, Donaustadt the wortst.", {"entities": [(0, 11, "VIE_DIS"), (40, 50, "VIE_DIS")]}),
    ("Donaustadt can be seen as the dumb brother of Floridsdorf.", {"entities": [(0, 10, "VIE_DIS"), (46, 57, "VIE_DIS")]}),
    ("The way the mafia appears to take over Liesing is nothing compared to the gang wars in Neubau .",
     {"entities": [(39, 46, "VIE_DIS"), (87, 93, "VIE_DIS")]}),
    ("The people in Leopoldstadt are a little bit different.", {"entities": [(14, 26, "VIE_DIS")]}),
    ("Most of the time I am not in in the district called Landstraße.", {"entities": [(52, 62, "VIE_DIS")]}),
    ("I didn't know Wieden until 5 minutes ago.", {"entities": [(14, 20, "VIE_DIS")]}),
    ("The people in Margareten are a little bit different.", {"entities": [(14, 24, "VIE_DIS")]}),
    ("My father used to work near a street which name is quite similar to Mariahilf.", {"entities": [(68, 77, "VIE_DIS")]}),
    ("The buildings in Neubau are ugly.", {"entities": [(17, 23, "VIE_DIS")]}),
    ("Most of the parks in Josefstadt are not very human friendly.", {"entities": [(21, 31, "VIE_DIS")]}),
    ("I don't know where the district Alsergrund is.", {"entities": [(32, 42, "VIE_DIS")]}),
    ("Favoriten probably has the worst reputation of all of them.", {"entities": [(0, 9, "VIE_DIS")]}),
    ("I don't like Simmering.", {"entities": [(13, 22, "VIE_DIS")]}),
    ("The name Meidling is part a greats song by Alkbottle.", {"entities": [(9, 17, "VIE_DIS")]}),
    ("Don't care about Hietzing at all.", {"entities": [(17, 25, "VIE_DIS")]}),
    ("I drive through Penzing all the time.", {"entities": [(16, 23, "VIE_DIS")]}),
    ("Where is Rudolfsheim-Fünfhaus?", {"entities": [(9, 29, "VIE_DIS")]}),
    ("The markets in Ottakring are nice.", {"entities": [(15, 24, "VIE_DIS")]}),
    ("Hernals sounds like the german word for neck.", {"entities": [(0, 7, "VIE_DIS")]}),
    ("What ever happens in Währing stays in Währing.", {"entities": [(21, 28, "VIE_DIS"), (38, 45, "VIE_DIS")]}),
    ("I only pass through Döbling in a car.", {"entities": [(20, 27, "VIE_DIS")]}),
    ("Why is Brigittenau written with an i instead of an e.", {"entities": [(7, 18, "VIE_DIS")]}),
    ("The people in Floridsdorf are a little bit different.", {"entities": [(14, 25, "VIE_DIS")]}),
    ("Donaustadt are a little bit different.", {"entities": [(0, 10, "VIE_DIS")]}),
    ("There are no book shops in Liesing.", {"entities": [(27, 34, "VIE_DIS")]}),
    ("Innere Stadt is also a district in Vienna?", {"entities": [(0, 12, "VIE_DIS")]}),
    ("I like London and Berlin.", {"entities": [(7, 13, "LOC"), (18, 24, "LOC")]}),

    ("Kombibad Döbling", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Familienbad Währinger Park", {"entities": [(0, 26, "POOL_NAME")]}),
    ("Familienbad Augarten", {"entities": [(0, 20, "POOL_NAME")]}),
    ("Badeschiff Wien", {"entities": [(0, 15, "POOL_NAME")]}),
    ("Familienbad Stammersdorf", {"entities": [(0, 24, "POOL_NAME")]}),
    ("Familienbad Strebersdorf", {"entities": [(0, 24, "POOL_NAME")]}),
    ("Strandbad Stadlau", {"entities": [(0, 17, "POOL_NAME")]}),
    ("Stadionbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Familienbad Herderplatz", {"entities": [(0, 23, "POOL_NAME")]}),
    ("Stadthallenbad", {"entities": [(0, 14, "POOL_NAME")]}),
    ("Schönbrunner Bad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Familienbad Hofferplatz", {"entities": [(0, 23, "POOL_NAME")]}),
    ("Familienbad-Hugo-Wolf-Park", {"entities": [(0, 26, "POOL_NAME")]}),
    ("Familienbad Gudrunstraße", {"entities": [(0, 24, "POOL_NAME")]}),
    ("Familienbad Schweizergarten", {"entities": [(0, 27, "POOL_NAME")]}),
    ("Hallenbad Floridsdorf", {"entities": [(0, 21, "POOL_NAME")]}),
    ("Höpflerbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Ottakringerbad", {"entities": [(0, 14, "POOL_NAME")]}),
    ("Krapfenwaldl Bad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Theresienbad", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Neuwaldegger Bad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("PSO-Sommerbad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Sommerbad Hadersdorf-Weidlingau", {"entities": [(0, 31, "POOL_NAME")]}),
    ("Dianabad", {"entities": [(0, 8, "POOL_NAME")]}),
    ("Bundesbad Alte Donau", {"entities": [(0, 20, "POOL_NAME")]}),
    ("Kombibad Großfeldsiedlung", {"entities": [(0, 25, "POOL_NAME")]}),
    ("Brausebad Friedrich-Kaiser-Gasse", {"entities": [(0, 32, "POOL_NAME")]}),
    ("Amalienbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Kombibad Donaustadt", {"entities": [(0, 19, "POOL_NAME")]}),
    ("Apostelbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Familienbad Reinlgasse", {"entities": [(0, 22, "POOL_NAME")]}),
    ("Strandbad Angelibad", {"entities": [(0, 19, "POOL_NAME")]}),
    ("Kongreßbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Strandbad Alte Donau", {"entities": [(0, 20, "POOL_NAME")]}),
    ("Hallenbad Brigittenau", {"entities": [(0, 21, "POOL_NAME")]}),
    ("Einsiedlerbad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Laaerbergbad", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Strandbad Gänsehäufel", {"entities": [(0, 21, "POOL_NAME")]}),
    ("Hermannbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Penzinger Bad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Liesinger Bad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Schafbergbad", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Hietzinger Bad", {"entities": [(0, 14, "POOL_NAME")]}),
    ("Jörgerbad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Therme Wien", {"entities": [(0, 11, "POOL_NAME")]}),
    ("Kombibad Simmering", {"entities": [(0, 18, "POOL_NAME")]}),
    ("Straßenbahnerbad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Polizeibad", {"entities": [(0, 10, "POOL_NAME")]}),

    ("Amalienbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Angelibad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Apostelbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Badeschiff", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Brausebad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Bundesbad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Dianabad", {"entities": [(0, 8, "POOL_NAME")]}),
    ("Einsiedlerbad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Familienbad", {"entities": [(0, 11, "POOL_NAME")]}),
    ("Gänsehäufel", {"entities": [(0, 11, "POOL_NAME")]}),
    ("Hadersdorf-Weidlingau", {"entities": [(0, 21, "POOL_NAME")]}),
    ("Hallenbad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Hallenbad Hütteldorf", {"entities": [(0, 20, "POOL_NAME")]}),
    ("Hermannbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Hietzinger Bad", {"entities": [(0, 14, "POOL_NAME")]}),
    ("Höpflerbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Jörgerbad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Kombibad", {"entities": [(0, 8, "POOL_NAME")]}),
    ("Kongreßbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Krapfenwaldl", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Laaerbergbad", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Liesinger Bad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Neuwaldegger Bad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Ottakringerbad", {"entities": [(0, 14, "POOL_NAME")]}),
    ("Penzinger Bad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Polizeibad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("PSO-Sommerbad", {"entities": [(0, 13, "POOL_NAME")]}),
    ("Schafbergbad", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Schönbrunner Bad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Sommerbad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Stadionbad", {"entities": [(0, 10, "POOL_NAME")]}),
    ("Stadlau", {"entities": [(0, 7, "POOL_NAME")]}),
    ("Stadthallenbad", {"entities": [(0, 14, "POOL_NAME")]}),
    ("Strandbad", {"entities": [(0, 9, "POOL_NAME")]}),
    ("Straßenbahnerbad", {"entities": [(0, 16, "POOL_NAME")]}),
    ("Theresienbad", {"entities": [(0, 12, "POOL_NAME")]}),
    ("Therme", {"entities": [(0, 6, "POOL_NAME")]}),

    ("Alte Donau", {"entities": [(0, 10, "POOL_LOC")]}),
    ("Augarten", {"entities": [(0, 8, "POOL_LOC")]}),
    ("Friedrich-Kaiser-Gasse", {"entities": [(0, 22, "POOL_LOC")]}),
    ("Großfeldsiedlung", {"entities": [(0, 16, "POOL_LOC")]}),
    ("Gudrunstraße", {"entities": [(0, 12, "POOL_LOC")]}),
    ("Herderplatz", {"entities": [(0, 11, "POOL_LOC")]}),
    ("Hofferplatz", {"entities": [(0, 11, "POOL_LOC")]}),
    ("Hugo-Wolf-Park", {"entities": [(0, 14, "POOL_LOC")]}),
    ("Schweizergarten", {"entities": [(0, 15, "POOL_LOC")]}),
    ("Stammersdorf", {"entities": [(0, 12, "POOL_LOC")]}),
    ("Strebersdorf", {"entities": [(0, 12, "POOL_LOC")]}),
    ("Währinger Park", {"entities": [(0, 14, "POOL_LOC")]})
]


def training_data_lower_case():
    newTrainData = []
    for text, ent in DATA:
        text = text.lower()
        newTrainData.append((text, ent))
    return newTrainData


TRAINING_DATA = DATA + training_data_lower_case()

if __name__ == "__main__":
    print("training data")