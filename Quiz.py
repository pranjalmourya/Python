Name = input("Enter participantname: ")
print(f"Hello! {Name}, Welcome to my computer Quiz")

playing = input("Do you want to play? ")
if playing.lower() != 'yes':
    quit()

print("Okay! Let's play: ")

Score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit' :
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory' :
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphic processing unit' :
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == 'power supply unit' :
    Score += 1
    print("Correct!")
else:
    print("Incorrect!")    

print(f"Your Score is: {Score}" ) 
print(f"You got {Score} question correctly")   
print(f"You got {(Score/4)*100}% question correctly")   


    