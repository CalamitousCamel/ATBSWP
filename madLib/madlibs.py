#!python3
'''Madlibs takes in specifically formatted .txt files and prompts the user
    to generate a mad lib story'''


#TODO
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
from os import path
import re
import sys
import shelve

def saveAs(fileName, default=libFile+timestamp)
    saveAs File with deafault being name of libFile+date/Time


def checkYN():
    #asks For Y/N input and returns with boolean T/F For repeatability 
    check = None
    while check == None:    
        check = input().lower()
        if check == 'y' or check == 'yes':
            return True
        elif check == 'n'or check == 'no':
            return False
        else:
            print("This is a 'yes' or 'no' question")
            check = None

def askForPath(inputMsg)
    returns regex fixed path from user input
    searchFolder = regex to path.abspath(path.join(input()))



print('**Welcome to madLibs**')
#TODO open(shelfFile for storing last used searchFolder)
#TODO
searchFolder = path.join('pathFromShelFile')



while #TODO loop 
print('searching ' + searchFolder + ' for madLibs files')

try:
#TODO
fileList = regex search searchFolder
#returns file.txt
#possible make abspath here 

except #TODO nofile error:
    print("there don't seem to be any madLibs files in" + searchFolder + ". Would you like to specify a different location?")
    cont = checkYN()
    if cont is False:
        EXIT PROGRAM
#TODO 
    searchFolder = input('please specify a new file location:\n')
    if cont and path.isdir(searchFolder) is True:
        print('saving' + searchFolder + ' as new default location')
#TODO   open shelve and save settings
    elif path.isdir(searchFolder) is not True
#TODO    print warning and retry filepath

#TODO
for n in len(fileList):
    enumFileList += (str(n+1) + '. ' + fileList[n] + '\n')
    #possible print index and key instead of making whole new variable

print(enumFileList)
index = input('Enter the number of the file you wish to open:\n' )
chwd(searchfolder)
libfile =  open(fileList[index]) #need to add this to a path
if path.isdir(path.join('.', 'storyFiles')) is not True:
    mkdir(path.join('.', 'storyFiles'))
copy(libfile) to storyFile
open(storyFile,-w)

for each regex match (Noun|Adverb|Adjective|Verb) in storyFile:
    input('enter a '+ [match]) 
    write to file regex replace [match] With [input()]
    
print(storyFile)
print('do you want to save this story?')
optsave = checkYN()

if optsave is True:
    fileName = askForPath('specify a file name or leave blank to save using timestamp: \n')
        while path.isfile(fileName) is True: 
            fileName = input('please choose another name, ' + fileName + ' is taken: \n')
        saveAs(fileName)
