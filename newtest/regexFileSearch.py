import os
import re


# ask user for input and display search folder
folder = os.getcwd()
print("you are seraching in " + folder)
usrInput = input("Please enter your RegEx search terms ")
usrSearch = re.compile(usrInput)


# look for and open anything with a .txt extension
for file in os.listdir(os.getcwd()):
    print(file)
    if file.endswith('.txt'):
        with open(file) as f:
            currentFile = f.read()
        print(currentFile)
# apply regex to file and print matches as they come up
        for match in usrSearch.findall(currentFile):
            print("match in " + file + ":")
            print(match)
        
