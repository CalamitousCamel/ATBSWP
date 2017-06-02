#! python3
# pulls phone numbers and email addresses from text copied to the clipboard

import pyperclip, re

phoneRegex= re.compile(r'''(?i)										# note the inline ignorecase function
							(?<!\w)(?P<c>\d)?						# country code accounting for whitespace
							\D?										# spacer
							\(?(?P<a>\d{3})?\)?						# 3 digit area code incl. optional bracket notation
							\D?								
							(?P<n1>\d{3})\D?(?P<n2>\d{4})			# 7 digit phone number
							((\D*(x|extension)\D{,3}(?P<ext>\d+)))?	# extension matching. Matches a flexible distance away from the initial phone number to account for differing scentence structure 
		    			''',re.X)	

emailRegex= re.compile(r'''
			(\S+\@\S+) 												# matches any non-whitespace character on either side of the @
			''',re.X)

copiedText= str(pyperclip.paste())
phoneMatch=[]
emailMatch=[]

for number in phoneRegex.finditer(copiedText):						# this if-mess translates each various phone number match into it's own string (accounting for differing/missing notation) and appends it to a list of phone numbers
		phoneNum= str(number.group('n1')+'.'+number.group('n2'))
		if number.group('a') != None:
			phoneNum = str(number.group('a')+'.'+phoneNum)
		if number.group('c') != None:
			phoneNum = str(number.group('c')+'.'+phoneNum)
		if number.group('ext') !=None:
			phoneNum += str(' ext.'+number.group('ext'))
		phoneMatch.append(phoneNum)

for email in emailRegex.findall(copiedText):						# finds and appends emails into a list
	emailMatch.append(email)

allMatch='\nphone numbers found: '+str(len(phoneMatch))+'\n'		# begins each section with a report on how many of each match was found in the text and then pipes a comma delimited string "list" into allMatch
for n in phoneMatch:
	allMatch+=n+', '

allMatch+=('\nemails found: '+str(len(emailMatch))+'\n')
for n in emailMatch:
	allMatch+=n+', '

pyperclip.copy(allMatch)

