# Find the url's which starts with http:// or https://

#TODO: Create a regex that matches url's which starts with http:// or https://

#TODO: Find URL matches in the clipboard

#TODO: Print the matched URL's onto the clipboard

import pyperclip, re

#Create a regex that matches url's which starts with http:// or https://
urlRegex = re.compile(r'[http|https]+\:\/\/[a-zA-Z0-9./?+%:,&_=-]+')

#Find URL matches in the clipboard
urls = pyperclip.paste()
#print("urls: ", urls)
matches = []
for group in urlRegex.findall(urls):
    matches.append(group)
#print("matches: ", matches)
#Print the matched URL's onto the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n\n'.join(matches))
else:
    print('No url with http:// or https:// were found')








