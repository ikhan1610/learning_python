#! python3
    # mcb.pyw - Saves and loads pieces of text to the clipboard.
    # Usage: python mcb.pyw save <keyword> - Saves clipboard to keyword.
    #        python mcb.pyw delete <keyword> - Removes keyword from the list .
    #        python mcb.pyw <keyword> - Loads keyword to clipboard.
    #        python mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
    else:
        pyperclip.copy("Wrong keyword. It can't be deleted.")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for keyword in list(mcbShelf.keys()):
            del mcbShelf[keyword]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        pyperclip.copy(f"No '{sys.argv[1]}' keyword available in the list")
else:
    pyperclip.copy(f"'{sys.argv[1]}' command is unavailable.")


mcbShelf.close()
