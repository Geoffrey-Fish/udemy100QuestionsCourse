#Here I will store all my accumulated points.
#This is the first time that I have planned and coded an Idea all by myself!

# Pickle is for storing data in a relative simple manner.
import pickle

# The "with" command is a build in tool that allows to open a file with a separate name,
#work in that file, and no need of closing, or double accessing of the data file.
with open('speicher.data','rb') as content: #content is the local name of the data file
    pos = [] #local buffer for the stored data
    while True: #iteration through the stored data
        plus = pickle.load(content) # plus is the whole list of the stored data
        if plus is None: #simple break check for safety measures
            break
        pos.append(plus) #here, the local buffer gets filled

#now I assign the stored data to the variables Iĺl be working with- simple, aint it?
exercise_number ,points,date_is = [pos[i] for i in (0,1,2)] 

#Here "starts" the Programm, showing where I am with the information of my exercises from udemy so far.
print("Your last Exercise number was: ",exercise_number)
print("Your score so far: ",points)
print("Last used: ",date_is)
###########
#print("interim:You have 0.5 points saved from prevous missions!")
###########
# Now, I give information about my progress in the course.
exeadd = int(input("At wich exercise are you right now? "))
pointadd = int(input("how many points did you get? "))
date = str(input("And todays date is? "))

# Here Iḿ adding my information to the working variables.
exercise_number = exeadd
points += pointadd
date_is = date

# this is a fuckery and Im working on it-this must get better.
#see further down for more explanation.
liste = []
liste.append(exercise_number)
liste.append(points)
liste.append(date)

# Iḿ quite talkative, am I ? :-)
print("Tank you!")
print("Your actual exercise is number: ", exercise_number)
print("Your score so far is: ",points)
print("Last saved at: ",date_is)

# The with thinggy again-so cool.
# As mentioned, here I use the liste list for saving every information in the same order as
# I pull them at the beginning
with open('speicher.data','wb') as keep:
    for i in liste:
        pickle.dump(i,keep)
    pickle.dump(None,keep) #Here is the None failsafe.will be put at the end after iterating through the list.

# Thatś it! My very first, self made, google-fu-ed Programm!!!
# Jeff the tryharder, 03.12.21
#V1.0
