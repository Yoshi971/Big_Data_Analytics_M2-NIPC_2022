#Created by Roxanne Pradillon

import spacy

print("###Extracting noun chunks : there is more")

def process(model):

    #Load the spacy engine
    nlp = spacy.load('en_core_web_sm')

    #Set the sentence
    sentence = "All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balancedmind."

    #Process the sentence with the spacy engine
    doc = nlp(sentence)

    print("#look at the noun chunks in this sentence:")
    for noun_chunk in doc.noun_chunks:
        print(noun_chunk.text)

    print("#them out together with the noun chunks:")
    for noun_chunk in doc.noun_chunks:
        print(noun_chunk.text, "\t", noun_chunk.start, "\t",
          noun_chunk.end)
          
    print("#print out the sentence where the noun chunk belongs:")
    for noun_chunk in doc.noun_chunks:
        print(noun_chunk.text, "\t", noun_chunk.sent)

    print("#noun chunk:")
    for noun_chunk in doc.noun_chunks:
        print(noun_chunk.text, "\t", noun_chunk.root.text)
    
    #process noun chunk using spacy
    other_span = "emotions"
    other_doc = nlp(other_span)

    print("#compare it to the noun chunks in the sentence:")
    for noun_chunk in doc.noun_chunks:
        print(noun_chunk.similarity(other_doc))
    

process('en_core_web_sm')

#Medium spacy model
print("\n###run this code with the new model")
process('en_core_web_md')

