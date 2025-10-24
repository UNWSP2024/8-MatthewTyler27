#Matthew Tyler
#10/24/25
#Word Seperator

def word_separator(sentence):

    new_sentence = ""
    #Keep first letter the same
    new_sentence = sentence[0]

    for letter in sentence[1:]:
        #check if letter is uppercase
        if letter.isupper():
            #add space and make lowercase
            new_sentence +=  " " + letter.lower()
        else:
            #Continue adding the letters to new sentence
            new_sentence += letter
    #Add Period
    new_sentence = new_sentence + "."


    return new_sentence.strip()

# Example usage
sentence = "StopAndSmellTheRoses"
new_sentence = word_separator(sentence)
print(new_sentence)
