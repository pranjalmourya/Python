[1mdiff --git a/Quiz.py b/Quiz.py[m
[1mindex 3e7523e..66c1844 100644[m
[1m--- a/Quiz.py[m
[1m+++ b/Quiz.py[m
[36m@@ -1 +1,45 @@[m
[31m-print("pranjal")[m
\ No newline at end of file[m
[32m+[m[32mName = input("Enter participantname: ")[m
[32m+[m[32mprint(f"Hello! {Name}, Welcome to my computer Quiz")[m
[32m+[m
[32m+[m[32mplaying = input("Do you want to play? ")[m
[32m+[m[32mif playing.lower() != 'yes':[m
[32m+[m[32m    quit()[m
[32m+[m
[32m+[m[32mprint("Okay! Let's play: ")[m
[32m+[m
[32m+[m[32mScore = 0[m
[32m+[m
[32m+[m[32manswer = input("What does CPU stand for? ")[m
[32m+[m[32mif answer.lower() == 'central processing unit' :[m
[32m+[m[32m    Score += 1[m
[32m+[m[32m    print("Correct!")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("Incorrect!")[m
[32m+[m
[32m+[m[32manswer = input("What does RAM stand for? ")[m
[32m+[m[32mif answer.lower() == 'random access memory' :[m
[32m+[m[32m    Score += 1[m
[32m+[m[32m    print("Correct!")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("Incorrect!")[m
[32m+[m
[32m+[m[32manswer = input("What does GPU stand for? ")[m
[32m+[m[32mif answer.lower() == 'graphic processing unit' :[m
[32m+[m[32m    Score += 1[m
[32m+[m[32m    print("Correct!")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("Incorrect!")[m
[32m+[m
[32m+[m[32manswer = input("What does PSU stand for? ")[m
[32m+[m[32mif answer.lower() == 'power supply unit' :[m
[32m+[m[32m    Score += 1[m
[32m+[m[32m    print("Correct!")[m
[32m+[m[32melse:[m
[32m+[m[32m    print("Incorrect!")[m[41m    [m
[32m+[m
[32m+[m[32mprint(f"Your Score is: {Score}" )[m[41m [m
[32m+[m[32mprint(f"You got {Score} question correctly")[m[41m   [m
[32m+[m[32mprint(f"You got {(Score/4)*100}% question correctly")[m[41m   [m
[41m+[m
[41m+[m
[41m+    [m
\ No newline at end of file[m
