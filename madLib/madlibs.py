#!python3
'''Madlibs takes in specifically formatted .txt files and prompts the user
    to generate a mad lib story'''
from os import path, getcwd, chdir, listdir, mkdir
from datetime import datetime
import re
import shelve
# TODO
'''
search dir for .txt file
if no .txt, ask to change search dir
ask to and save as default search dir
regex .txt for match Noun|Adverb|Adjective|Verb
for each match promt user for [match]
replace match with user input
read out new file
promt user to 'save as' in a  saved story subdir
use input as filename and save file to story subdir
'''

'''
def saveAs(fileName, default=str(libFile + "{:%y-%m-%d_%H.%M}".format(datetime.now()))):
   pass
    saveAs File with deafault being name of libFile + date / Time
    this may be a process of printing the whole story to a variable,
    then replacing the regex matches with user inputs, then opening
    it as a new file.
'''


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

# TODO if exist, open defaults file. if no, create one in CWD
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


# TODO get input for file and make it a path so it can open as a file
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


if path.isdir(path.join('..', 'storyFiles')) is False:
    mkdir(path.join('..', 'storyFiles'))
story = open(libFile)
libStory = story.read()
story.close()

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


'''A vacation is when you take a trip to some |Adjective| place with your
|Adjective| family. Usually you go to some place that is near a/an |Noun|
or up on a/an |Noun|. A good vacation place is one where you can ride
|Plural Noun|, play |Adverb| or go hunting for |Plural Noun|. I like
to spend my time |Verb| or |Verb|. When parents go on a vacation, they
spend their time eating three |Plural Noun| a day, and fathers play golf,
and mothers sit around |Verb ending in -ing|. Last summer, my little brother
fell in a/an |Noun| and got poison |Noun (plant)| all over his |Body Part|.
My family is going to go to (the) |Noun|, and I will practice |Verb|. Parents
need vacations more than kids because parents are always very |Adjective| and
because they have to work |Number| hours every day all year making enough
|Plural Noun| to pay for the vacation.'''
