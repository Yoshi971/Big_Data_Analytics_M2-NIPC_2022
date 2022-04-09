#Created by Roxanne Pradillon

import spacy

print("Getting the dependency parse")

#Load the sentence to be parsed
sentence = 'I have seldom heard him mention her under any other name.'

#Load the spacy engine
nlp = spacy.load('en_core_web_sm')

#Process the sentence using the spacy engine:
doc = nlp(sentence)

print("\nThe dependency information : ")
for token in doc:
    print(token.text, "\t", token.dep_, "\t", spacy.explain(token.dep_)) 

print("\nexplore the dependency parse structure: Token class : ")
for token in doc:
    print(token.text)
    ancestors = [t.text for t in token.ancestors]
    print(ancestors)

print("\nTo see all the children token, use the following code : ")
for token in doc:
    print(token.text)
    children = [t.text for t in token.children]
    print(children)

print("\nSee the subtree that the token is in : ")
for token in doc:
    print(token.text)
    subtree = [t.text for t in token.subtree]
    print(subtree)