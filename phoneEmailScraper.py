#! python3
# pulls phone numbers and email addresses from text copied to the clipboard

import pyperclip, re

phoneRegex= re.compile(r'''(?i)										# note the inline ignorecase function
							(?<!\w)(?P<c>\d)?						# country code accounting for whitespace
							\D?										# spacer
							\(?(?P<a>\d{3})?\)?						# 3 digit area code incl. optional bracket notation
							\D?								
							(?P<n1>\d{3})\D?(?P<n2>\d{4})				# 7 digit phone number
							((\D*(x|extension)\D{,3}(?P<ext>\d+)))?	# extension matching within written sentence matches common extension identifiers with numbers at most 3 spaces afterwards. Matches a flexible distance away from the initial phone number to account for differing scentence structure 
		    			''',re.X)	

emailRegex= re.compile(r'''
			(\S+\@\S+) #matches any non-whitespace character on either side of the @
			''',re.X)

#copiedText= str(pyperclip.paste())
copiedText = "if 16138346612 834 6612 then if 834 6612 then if 1 613 834 6612 ext. 244 then if (613)8346612 X 244 then if 834 6612 next then 834 6612  this is a block of text that includes a number 8346612 with the extension 224  more text for the number 1 (613) 834 6612 with the extension 224  or the other number 834 6612. call that, oh ask for x 2244. there is also some email's I want you to have: 234554@registereduser.ca or call him at 1 306 265 4455 ext. 88 or xxlcose_xx@86canada.ec.gc.ca" 
phoneMatch=[]
emailMatch=[]

for number in phoneRegex.finditer(copiedText):
		phoneNum= str(number.group('n1')+'.'+number.group('n2'))
		if number.group('a') != None:
			phoneNum = str(number.group('a')+'.'+phoneNum)
		if number.group('c') != None:
			phoneNum = str(number.group('c')+'.'+phoneNum)
		if number.group('ext') !=None:
			phoneNum += str(' ext.'+number.group('ext'))
		phoneMatch.append(phoneNum)

for email in emailRegex.findall(copiedText):
	emailMatch.append(email)

allMatch='\nphone numbers found: '+str(len(phoneMatch))
'''####################DEBUG#########################	
print('\nphone numbers found: '+str(len(phoneMatch)))
for n in phoneMatch:
	print(n)

print('\nemails matched: '+str(len(emailMatch)))
for n in emailMatch:
	print(n)
'''


pyperclip.copy(allMatch)

'''TODO
imort text from clipboard
search text for info
format info into readable text
export to clipboard
throw error if none detected (try/except function?)
'''
