#Matthew Tyler
#10/24/25
#Capital Quiz

import random

midwest_states = ["Minnesota", "Wisconsin", "Iowa", "Michigan", 
"North Dakota","South Dakota", "Nebraska", "Kansas", "Missouri",
"Illinois", "Indiana", "Ohio"]

midwest_Capitals = {"Minnesota": "St. paul", "Wisconsin": "Madison", "Iowa": "Des Moines", "Michigan": "Lansing", 
"North Dakota": "Bismarck","South Dakota": "Pierre", "Nebraska": "Lincoln", "Kansas": "Topeka", "Missouri": "Jefferson City",
"Illinois": "Springfield", "Indiana": "Indianapolis", "Ohio": "Columbus"}


def Captital_quiz():
    state = random.choice(midwest_states)
    quiz = input("What is the capital of:" + state )
    if midwest_Capitals[state] == quiz:
        print("Correct!")
    else:
        print("Sorry, inncorrect")

Captital_quiz()
