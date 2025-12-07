#The array contains the student's test results. 
# A value of True indicates that the student answered the question correctly, 
# while a value of False indicates an incorrect answer. 
# Write a program that prints information about the test results:

#Number of questions:
#Number of correct answers:
#Number of incorrect answers:
#Percentage of correct answers:

test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

qnum = len(test_results)
correct = 0
incorrect = 0
for answer in test_results:
    if answer == True:
        correct = correct + 1
    elif answer == False:
        incorrect = incorrect + 1

percentage = (correct / qnum)*100
percentage = round(percentage)
print(f'Number of questions: {qnum}')
print(f'Number of correct answers: {correct}')
print(f'Number of incorrect answers: {incorrect}')
print(f'Percentage of correct answers: {percentage}%')