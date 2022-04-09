#Created by Roxanne Pradillon 

print("###Finding references – anaphora resolution")

#Import spacy and neuralcoref
import spacy
import neuralcoref

#Load the spaCy engine and add neuralcoref to its pipeline:
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

#process the following short text:
text = "Earlier this year, Olga appeared on a new song.She was featured on one of the tracks. The singer isassuring that her next album will be worth the wait."

print("\n#process the text usingspaCy and then output the result:")
doc = nlp(text)
print(doc._.coref_resolved)

#Let's use the following short text
text = "Deepika has a dog. She loves him. The movie star has always been fond of animals."

#add neuralcoref to the spacy
neuralcoref.add_to_pipe(nlp, conv_dict={'Deepika':['woman']})

print("\n#Process the result:")
doc = nlp(text)
print(doc._.coref_resolved)


