print("Welcome to the Quiz Game!")

playing = input ("Do you wanna start the game? Answer by typing yes or no \n")

if playing.lower() != "yes":
    quit()

print("Ok! Let's play :) ")
score = 0

#Question 1

answer = input ("What does CPU stand for? \n")
if answer.lower() == "central processing unit":
    print ("Correct! :) ")
    score = score + 1
else:
    print ("Incorrect! :( ")

#Question 2
    
answer = input ("What does GPU stand for? \n")
if answer.lower() == "graphics processing unit":
    print ("Correct! :) ")
    score += 1
else:
    print ("Incorrect! :( ")

#Question 3
    
answer = input ("What does RAM stand for? \n")
if answer.lower() == "random access memory":
    print ("Correct! :) ")
    score += 1
else:
    print ("Incorrect! :( ")

#Question 4
    
answer = input ("What does ROM stand for? \n")
if answer.lower() == "read only memory":
    print ("Correct! :) ")
    score += 1
else:
    print ("Incorrect! :( ")

print ("Congrats! You got " + str(score) + " questions correct!\n")
print ("You got " + str((score / 4 ) * 100) + "%. ")