#! python3
# Copying and Pasting messages from clipboard to email body, based on a small key phrase in the command line.

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'iftar': """Sajeer bhai, is it possible to make an iftar invitation ?"""}



import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mClip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for '+keyphrase+' has been copied to the clipboard')
else:
    print('There is no text for '+keyphrase)


