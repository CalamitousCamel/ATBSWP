#! python3
# a version of str.strip() nut with regex. For reasons.
import re

toStrip = '   this is a test   '
char = '(^\s*\b)(?:.*)(\b\s*$)'
def rStrip(toStrip,char):
	re.sub(toStrip,char)
