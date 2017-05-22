#1 python3
# add wikipedia markup for bulleted lists to list-formatted text
import pyperclip

cliplist= pyperclip.paste()
split=cliplist.split('\n')
for n in range(len(split)):
		split[n] = '* '+split[n]
newlist= '\n'.join(split)

pyperclip.copy(newlist)


