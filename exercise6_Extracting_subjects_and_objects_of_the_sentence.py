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
            
#The dative object function
def get_dative_phrase(doc):
    for token in doc:
        if ("dative" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            return doc[start:end]
            
#prepositional object function
def get_prepositional_phrase_objs(doc):
    prep_spans = []
    for token in doc:
        if ("pobj" in token.dep_):
            subtree = list(token.subtree)
            start = subtree[0].i
            end = subtree[-1].i + 1
            prep_spans.append(doc[start:end])
    return prep_spans

print("loop through the sentences and print out their subjects and objects")
for sentence in sentences:
    doc = nlp(sentence)
    subject_phrase = get_subject_phrase(doc)
    object_phrase = get_object_phrase(doc)
    dative_phrase = get_dative_phrase(doc)
    prepositional_phrase = get_prepositional_phrase_objs(doc)
    print(subject_phrase)
    print(object_phrase)
    print(dative_phrase)
    print(prepositional_phrase)
    
