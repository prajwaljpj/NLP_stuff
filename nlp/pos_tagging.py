#!/usr/bin/env python3

import nltk


nltk.download('tagsets')
# nltk.help.upenn_tagset()
text = nltk.word_tokenize('There is a cup on the table Asha, can you pick up the cup')
tagged = nltk.pos_tag(text)
print(tagged)
