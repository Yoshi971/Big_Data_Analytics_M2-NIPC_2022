#Created by Roxanne Pradillon 

print("Extracting subjects and objects of the sentence")

import spacy

#Load the spacy engine:
nlp = spacy.load('en_core_web_sm')

#list of sentences processed
sentences=["The big black cat stared at the small dog.","Jane watched her brother in the evenings."]

#subject function
def get_subject_phrase(doc):
    for token in doc:
        if ("subj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]

#direct object function
def get_object_phrase(doc):
    for token in doc:
        if ("dobj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]

print("loop through the sentences and print out their subjects and objects")
for sentence in sentences:
    doc = nlp(sentence)
    subject_phrase = get_subject_phrase(doc)
    object_phrase = get_object_phrase(doc)
    print(subject_phrase)
    print(object_phrase)
    
