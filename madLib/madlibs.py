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
#TODO    saveAs File with deafault being name of libFile+date/Time

def checkYN() 
    ask for Y/N input and return with boolean T/F for repeatability 
    

#TODO open(shelfFile for storing last used searchFolder)

print('**Welcome to madLibs**')
#TODO
searchFolder = path.join('pathFromShelFile')



while #TODO loop 
print('searching ' + searchFolder + ' for madLibs files')

try:
#TODO
fileList = regex search searchFolder

except #TODO nofile error:
    print("there don't seem to be any madLib files in" + searchFolder + ". Would you like to specify a different location?")
    cont = checkYN()
    print('set new location to default?')
    default = checkYN()
#TODO searchFolder = regex to path.abspath(path.join(input('please specify a new file location:\n')))
    if cont and default and path.isdir(searchFolder) is True:
        print('saving searchFolder as new default location')
#TODO   open shelve and save settings
    elif path.isdir(searchFolder) is not True
#TODO    print warning and retry filepath
    elif cont is False:
        break
#TODO
for n in len(fileList):
    print(str(n+1) + '. ' + fileList[n] + '\n')
    libFile = input('Enter the number of the file you wish to open:\n' )
chwd(searchfolder)
if path.isdir(path.join)
mkdir(path.join('.', 'storyFiles')
copy(libfile) to storyFile
open(storyFile,-w)

for each regex match (Noun|Adverb|Adjective|Verb):
    input('enter a '+ [match]) 
    write to file regex replace [match] With [input]
    
print(storyFile)
print('do you want to save this story?')
optsave = checkYN()

if optsave is True:
    fileName = regex to path.abspath(path.join(input('specify a file name or leave blank to save using timestamp: \n'))
        while path.isfile(fileName) is True: 
            fileName = input('please choose another name, ' + fileName + ' is taken: \n')
        saveAs(fileName)
