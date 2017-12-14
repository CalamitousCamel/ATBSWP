#!python3
'''Madlibs takes in specifically formatted .txt files and prompts the user
    to generate a mad lib story'''
from os import path, getcwd, chdir, listdir, mkdir
from datetime import datetime
import re
import shelve


def checkYN():
    # asks For Y/N input and returns with boolean T/F For repeatability
    check = None
    while check is None:
        check = input().lower()
        if check == 'y' or check == 'yes':
            return True
        elif check == 'n'or check == 'no':
            return False
        else:
            print("This is a 'yes' or 'no' question")
            check = None


def askForPath(inputMsg):
    print(inputMsg)
    newPath = input()
    while path.isdir(newPath) is False:
        print('please enter a valid path')
        newPath = input()
    return path.abspath(newPath)


lib = re.compile(r'\|(.*?)\|')

# if exist, open defaults file. if no, create one in CWD
print('\n**Welcome to madLibs**\n**********************\n')
defaultPath = shelve.open('.\\settings\\defaults')
try:
    searchFolder = defaultPath['searchFolder']
    defaultPath.close()
# If a default is not set yet
except KeyError:
    searchFolder = getcwd()
chdir(searchFolder)
print('The madLib files in ' + searchFolder + ' are:')

# creates a dictionary that stores filenames w/out .txt for user ease
while True:
    fileDict = {}
    for file in listdir(searchFolder):
        if file.endswith('.txt'):
            fileDict[file[0:-4]] = file

    if fileDict == {}:
        print("...there don't seem to be any madLibs files in " +
              searchFolder +
              ". Would you like to specify a different location?")
        cont = checkYN()
        if cont is False:
            print('EXITING PROGRAM')
            exit()
        elif cont is True:
            searchFolder = askForPath('please specify a new file location:')
            print('saving ' + searchFolder + ' as new default location')
            defaultPath['searchFolder'] = searchFolder
            defaultPath.close()
            chdir(searchFolder)
    else:
        break


# get input for file and make it a path so it can open as a file
for _ in fileDict.keys():
    print(_)
print('Type the name of the file you wish to open')
while True:
    try:
        libFile = path.abspath(fileDict[input()])
        break
    except KeyError:
        pass
    print("That selection doesn't seem to be on the list. Please try again")

# create a directory for the saved stories
if path.isdir(path.join('..', 'storyFiles')) is False:
    mkdir(path.join('..', 'storyFiles'))
story = open(libFile)
libStory = story.read()
story.close()

# the actual regex iterator
for match in lib.finditer(libStory):
    print('enter a(n) ' + str(match.group(1)) + ': ', end='')
    libStory = lib.sub(input(), libStory, count=1)

print(libStory)
print('\ndo you want to save this story?')
optsave = checkYN()

if optsave is True:
    fileName = "{:%y-%m-%d_%H.%M}".format(datetime.now())
    storyFile = open('..\\storyFiles\\' + fileName + '.txt', 'w')
    storyFile.write(libStory)
    storyFile.close()
