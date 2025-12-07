#To read the contents of a file, you must first open it. 
# You can read the contents of a text file line by line, 
# or you can read the entire contents of the file at once.

#The program print_countries.py opens a text file, reads its 
# contents line by line, and prints the contents of each line. 
# Analize the program code. Then, run the program.

with open('countries.txt', 'r') as file:
    for line in file:
        print(line, end='')