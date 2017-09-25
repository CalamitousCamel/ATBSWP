#! python3
# pulls phone numbers and email addresses from text copied to the clipboard

import pyperclip
import re
'''
phoneRegex:
# country code accounting for whitespace
# spacer
# 3 digit area code incl. optional bracket notation
# spacer
# 7 digit phone number in 2 seperate capture groups
# Matches most common extension notation a flexible distance
  away from the initial phone number
'''
phoneRegex = re.compile(r'''
    (?i)
    (?<!\w)(?P<c>\d)?
    \D?
    \(?(?P<a>\d{3})?\)?
    \D?
    (?P<n1>\d{3})\D?(?P<n2>\d{4})
    ((\D*(x|extension)\D{,3}(?P<ext>\d+)))?
''', re.X)

# matches any non-whitespace character on either side of the @
emailRegex = re.compile(r'''(\S+\@\S+)''', re.X)


copiedText = str(pyperclip.paste())
phoneMatch = []
emailMatch = []

'''this if-mess translates each various phone number match into it's own
string (accounting for differing/missing notation) and appends
it to a list of phone numbers'''
for number in phoneRegex.finditer(copiedText):
    phoneNum = str(number.group('n1') + '.' + number.group('n2'))
    if number.group('a'):
        phoneNum = str(number.group('a') + '.' + phoneNum)
    if number.group('c'):
        phoneNum = str(number.group('c') + '.' + phoneNum)
    if number.group('ext'):
        phoneNum += str(' ext.' + number.group('ext'))
    phoneMatch.append(phoneNum)

# finds and appends emails into a list
for email in emailRegex.findall(copiedText):
    emailMatch.append(email)

'''begins each section with a report on how many of each match was
found in the text and then pipes a comma delimited string "list" to allMatch'''
allMatch = '\nphone numbers found: ' + str(len(phoneMatch)) + '\n'
for n in phoneMatch:
    allMatch += n + ', '

allMatch += ('\nemails found: ' + str(len(emailMatch)) + '\n')
for n in emailMatch:
    allMatch += n + ', '

pyperclip.copy(allMatch)
