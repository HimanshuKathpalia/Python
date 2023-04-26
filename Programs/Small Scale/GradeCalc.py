'''
Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.'''

**************************************************************************************************************************

# Prompt user for input of score
score = float(input("Enter Score: "))

# Check if score is out of range
if(score<0.0 or score>1.0):
    print("Error")
# Check if score is A grade or higher
elif(score>= 0.9):
    print("A")
# Check if score is B grade or higher
elif(score>= 0.8):
    print("B")
# Check if score is C grade or higher
elif(score>= 0.7):
    print("C")
# Check if score is D grade or higher
elif(score>= 0.6):
    print("D")
# If score is lower than D grade, print F grade
else:
    print("F")
