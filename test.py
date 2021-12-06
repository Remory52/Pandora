import spacy

nlp = spacy.load("en_core_web_md")

while True:
    line = input("Sentence: ")
    if line == "q":
        break

    result = nlp(line)

    for token in result:
        print(token.text, token.pos_, token.dep_)
        #print(token.similarity, token.subtree)