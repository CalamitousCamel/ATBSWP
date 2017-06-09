#! python3
# a version of str.strip() but with regex.
import re

# pattern matches the leading and trailng space in any string
defaultChar = re.compile(r'(^\s*\b)(.*)(\b\s*$)')

def rStrip(toStrip,char=defaultChar):
	# if no char arg then strip whitespace by returning matching group 2 only
	if char is defaultChar:	
		newString = re.sub(char,r'\2',toStrip)
	else:
		newString = re.sub(char,'',toStrip)
	print(newString)

rStrip('   this is a test   ','[asi]')	