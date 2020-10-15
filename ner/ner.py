import ssl

import nltk
# https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed
from nltk import word_tokenize, pos_tag

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

ex = 'I am going to eat one cone of ice-cream tomorrow'


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


sent = preprocess(ex)
print("sentence: {}", ex)
print("processed: {}", sent)

pattern = 'NP: {<DT>?<JJ>*<NN>}'

cp = nltk.RegexpParser(pattern)
cs = cp.parse(sent)
print("chunk parsers {}", cs)

print("--------------------------------------------------")
print("--------------------------------------------------")
print("labels")

for sent in nltk.sent_tokenize(ex):
    for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
        if hasattr(chunk, 'label'):
            print(chunk.label(), ' '.join(c[0] for c in chunk))

from nltk.chunk import tree2conlltags, ne_chunk
from pprint import pprint

iob_tagged = tree2conlltags(cs)
print("iob_tagged ")
pprint(iob_tagged)

ne_tree = ne_chunk(nltk.pos_tag(nltk.word_tokenize(ex)))
print("ne_tree ")
print(ne_tree)

sentence = "Mark and John are working at Google."
pprint(tree2conlltags(ne_chunk(pos_tag(word_tokenize(sentence)))))


print("tree2conlltags ")
pprint(tree2conlltags(ne_chunk(pos_tag(word_tokenize(ex)))))
