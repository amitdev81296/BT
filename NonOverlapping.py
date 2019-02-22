from bcl import bcl
import nltk


def find_category(verb):
    count = 0
    for b in bcl.bloom:
        if verb in b:
            return bcl.level[str(count)]
        count = count + 1

input_question = raw_input("Please Enter A Question : ")

tokens = nltk.word_tokenize(input_question)
tagged = nltk.pos_tag(tokens)

for t in tagged:
    if t[1] == 'VB':
        category = find_category(t[0])
        print("\nExtracted Verb : " + str(t[0]))
        print("\nBloom's Classification Level : " + str(category))
