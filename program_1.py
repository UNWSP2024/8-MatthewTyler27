#Matthew Tyler
#10/24/25
#Initials

def initials_generator(personsName):

    personsInitials = ""
    #Divide personsName by first/middle/last
    names = personsName.split()

    for name in names:
        #Get first letter of names
        personsInitials += name[0].upper() + ". "

    return personsInitials.strip()


personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)
