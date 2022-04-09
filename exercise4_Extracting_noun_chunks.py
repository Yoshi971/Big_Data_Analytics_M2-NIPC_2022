#Created by Roxanne Pradillon

import spacy
from Chapter01.dividing_into_sentences import read_text_file

print("Extracting noun chunk")

#Read in the sherlock_holmes_1.txt file
text = read_text_file("Chapter01/sherlock_holmes_1.txt")

#Initialize the spacy engine and then use it to process the text
nlp = spacy.load('en_core_web_md')
doc = nlp(text)

print("out the chunks:")
for noun_chunk in doc.noun_chunks:
    print(noun_chunk.text)