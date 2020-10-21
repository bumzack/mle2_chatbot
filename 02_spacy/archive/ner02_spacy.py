# https://spacy.io/usage/linguistic-features#section-named-entities

# python3 -m 02_spacy download en_core_web_sm
# python3 -m 02_spacy download en_core_web_md
from random import shuffle

import spacy
from spacy.tokens import Span


nlp = spacy.load("en_core_web_sm")
s = "Autonomous cars shift insurance liability toward manufacturers"

doc = nlp(s)
print("Entities  autonomous cars:    ", [(ent.text, ent.label_) for ent in doc.ents])
print("Tokens    autonomous cars:     ", [(t.text, t.ent_type_, t.ent_iob) for t in doc])

print("\n\n tokens   nur doc  \n\n")




s = "Where is an open pool in Margareten?"
pool= nlp(s)
print("Entities    pool      ", [(ent.text, ent.label_) for ent in pool.ents])
print("Tokens pool           ", [(t.text, t.ent_type_, t.ent_iob) for t in pool])


# print("\n\n Named entities doc.ents \n\n")
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)
# displacy.serve(doc, style="dep")
#
# print("\n\n   token vectors   \n\n")
# nlp = 02_spacy.load("en_core_web_md")
# tokens = nlp("dog cat banana afskfsd")
# for token in tokens:
#     print(token.text, token.has_vector, token.vector_norm, token.is_oov)
#
#
#
# print("\n\n   similarity vectors   \n\n")
# nlp = 02_spacy.load("en_core_web_md")  # make sure to use larger model!
# tokens = nlp("dog cat banana")
# for token1 in tokens:
#     for token2 in tokens:
#         print(token1.text, token2.text, token1.similarity(token2))
#
# print("\n\n   knowledge base   \n\n")
# from 02_spacy.kb import KnowledgeBase
# # load the model and create an empty KB
# nlp = 02_spacy.load('en_core_web_sm')
# kb = KnowledgeBase(vocab=nlp.vocab, entity_vector_length=3)
# # adding entities
# kb.add_entity(entity="Q1004791", freq=6, entity_vector=[0, 3, 5])
# kb.add_entity(entity="Q42", freq=342, entity_vector=[1, 9, -3])
# kb.add_entity(entity="Q5301561", freq=12, entity_vector=[-2, 4, 2])
# # adding aliases
# kb.add_alias(alias="Douglas", entities=["Q1004791", "Q42", "Q5301561"], probabilities=[0.6, 0.1, 0.2])
# kb.add_alias(alias="Douglas Adams", entities=["Q42"], probabilities=[0.9])
# print()
# print("Number of entities in KB:",kb.get_size_entities()) # 3
# print("Number of aliases in KB:", kb.get_size_aliases()) # 2
#
# print("----------------------------------------")
# print("lighning tour")
# print("----------------------------------------")
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# apple = doc[0]
# print("Fine-grained POS tag  ", apple.text, apple.pos_, apple.pos)
# print("Coarse-grained POS tag", apple.tag_, apple.tag)
# print("Word shape", apple.shape_, apple.shape)
# print("Alphabetic characters?", apple.is_alpha)
# print("Punctuation mark?", apple.is_punct)
#
# billion = doc[10]
# print("Digit?", billion.is_digit)
# print("Like a number?", billion.like_num)
# print("Like an email address?", billion.like_email)
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp("Peach emoji is where it has always been. Peach is the superior "
#           "emoji. It's outranking eggplant 🍑 ")
# print(doc[0].text)          # 'Peach'
# print(doc[1].text)          # 'emoji'
# print(doc[-1].text)         # '🍑'
# print(doc[17:19].text)      # 'outranking eggplant'
#
# noun_chunks = list(doc.noun_chunks)
# print(noun_chunks[0].text)  # 'Peach emoji'
#
# sentences = list(doc.sents)
# assert len(sentences) == 3
# print(sentences[1].text)    # 'Peach is the superior emoji.'

print("----------------------------------------")
print("named entities")
print("----------------------------------------")
nlp = spacy.load("en_core_web_sm")
print("San Francisco considers banning sidewalk delivery robots")
doc = nlp("San Francisco considers banning sidewalk delivery robots")
for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
#
# print("FB is hiring a new VP of global policy")
#
# doc = nlp("FB is hiring a new VP of global policy")
# doc.ents = [Span(doc, 0, 1, label="ORG")]
# for ent in doc.ents:
#     print(ent.text, ent.start_char, ent.end_char, ent.label_)

# print("----------------------------------------")
# print(" word verctors similaritites  ")
# print("----------------------------------------")
# nlp = 02_spacy.load("en_core_web_md")
# doc = nlp("Apple and banana are similar. Pasta and hippo aren't.")
# #
# # apple = doc[0]
# # banana = doc[2]
# # pasta = doc[6]
# # hippo = doc[8]
# #
# # print("apple <-> banana", apple.similarity(banana))
# # print("pasta <-> hippo", pasta.similarity(hippo))
# # print(apple.has_vector, banana.has_vector, pasta.has_vector, hippo.has_vector)
#
# print("----------------------------------------")
# print(" syntactic dependenices  ")
# print("----------------------------------------")
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp("When Sebastian Thrun started working on self-driving cars at Google "
#           "in 2007, few people outside of the company took him seriously.")
#
# dep_labels = []
# for token in doc:
#     while token.head != token:
#         dep_labels.append(token.dep_)
#         token = token.head
# print(dep_labels)
#
# print("----------------------------------------")
# print(" noun chunks  ")
# print("----------------------------------------")
# print("Autonomous cars shift insurance liability toward manufacturers")
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
# for chunk in doc.noun_chunks:
#     print("text ' {}',   root.text {},   root.dep_ {},   root.head.text {} ".format(chunk.text, chunk.root.text,
#                                                                                     chunk.root.dep_,
#                                                                                     chunk.root.head.text))

# print("----------------------------------------")
# print(" dependecy tree")
# print("----------------------------------------")
# nlp = 02_spacy.load("en_core_web_sm")
# print("Autonomous cars shift insurance liability toward manufacturers")
# doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
# i = 1
# for token in doc:
#     print(" i = {}".format(i))
#     print(token.text, token.dep_, token.head.text, token.head.pos_,
#           [child for child in token.children])
#     print("\n")
#
# from 02_spacy.symbols import nsubj, VERB
#
# print("----------------------------------------")
# print(" possible verbs")
# print("----------------------------------------")
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp("Autonomous cars shift insurance liability toward manufacturers")
# print("Autonomous cars shift insurance liability toward manufacturers")
# # Finding a verb with a subject from below — good
# verbs = set()
# for possible_subject in doc:
#     if possible_subject.dep == nsubj and possible_subject.head.pos == VERB:
#         verbs.add(possible_subject.head)
# print("possible verbs  ", verbs)
#
# s = "San Francisco considers banning sidewalk delivery robots"
# s = "Where is a public pool in Margareten"
#
# print("----------------------------------------")
# print(" Accessing entity annotations")
# print("----------------------------------------")
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp(s)
#
# # document level
# ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
# print(ents)
#
# # token level
# ent_san = [doc[0].text, doc[0].ent_iob_, doc[0].ent_type_]
# ent_francisco = [doc[1].text, doc[1].ent_iob_, doc[1].ent_type_]
# print(ent_san)  # ['San', 'B', 'GPE']
# print(ent_francisco)  # ['Francisco', 'I', 'GPE']
#
# print("all")
# for x in doc:
#     entx = [x.text, x.ent_iob_, x.ent_type_]
#     print(entx)
#     print("\n")
#
# fb_ent = Span(doc, 6, 7, label="GPE")  # create a Span for the new entity
# doc.ents = list(doc.ents) + [fb_ent]
#
# ents = [(e.text, e.start_char, e.end_char, e.label_) for e in doc.ents]
# print('After', ents)
# # [('fb', 0, 2, 'ORG')] 🎉
#
#
# text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."
#
# nlp = 02_spacy.load("en_core_web_sm")
# doc = nlp(text)
# # displacy.serve(doc, style="ent")
#
# print("----------------------------------------")
# print(" model training")
# print("----------------------------------------")
#
# train_data = [
#     ("Uber blew through $1 million a week", [(0, 4, 'ORG')]),
#     ("Android Pay expands to Canada", [(0, 11, 'PRODUCT'), (23, 30, 'GPE')]),
#     ("Spotify steps up Asia expansion", [(0, 8, "ORG"), (17, 21, "LOC")]),
#     ("Google Maps launches location sharing", [(0, 11, "PRODUCT")]),
#     ("Google rebrands its business apps", [(0, 6, "ORG")]),
#     ("look what i found on google! 😂", [(21, 27, "PRODUCT")])]
#
# TRAIN_DATA = [
#     ("Uber blew through $1 million a week", {"entities": [(0, 4, "ORG")]}),
#     ("Google rebrands its business apps", {"entities": [(0, 6, "ORG")]}),
#     ("Android Pay expands to Canada", {"entities": [(0, 11, 'PRODUCT'), (23, 30, 'GPE')]}),
#     ("Spotify steps up Asia expansion", {"entities": [(0, 8, "ORG"), (17, 21, "LOC")]}),
#     ("Google Maps launches location sharing", {"entities": [(0, 11, "PRODUCT")]}),
#     ("Margareten is a district in Vienna", {"entities": [(0, 10, "GPE")]}),
#     ("Margarete is a common name in the good old times", {"entities": [(0, 9, "PERSON")]}),
#     ("look what i found on google! 😂", {"entities": [(21, 27, "PRODUCT")]})
# ]
#
# nlp = 02_spacy.load("en_core_web_sm")  # 02_spacy.blank("en")
# optimizer = nlp.begin_training()
# for i in range(20):
#     shuffle(TRAIN_DATA)
#     for text, annotations in TRAIN_DATA:
#         nlp.update([text], [annotations], sgd=optimizer)
# nlp.to_disk("./model_grg")
#
# doc = nlp("Google expands to canada")
# for x in doc:
#     entx = [x.text, x.ent_iob_, x.ent_type_]
#     print(entx)
#     print("\n")
#
#
# doc = nlp("Margareten is a district i like")
# for x in doc:
#     entx = [x.text, x.ent_iob_, x.ent_type_]
#     print(entx)
#     print("\n")
