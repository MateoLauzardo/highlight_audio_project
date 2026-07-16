#NOTE: THIS PURPOSE OF FILE IS: reads current clipboard content


import time

# library to access the clipboard
import pyperclip
from pynput.keyboard import Controller, Key


# keyboard controller used to simulate Ctrl+C
_keyboard = Controller()



#SECTION - COPY TEXT FROM CLIPBOARD -> actually presses Ctrl+C, then reads what landed on the clipboard
def copy_text():

    # actually simulate Ctrl+C so the CURRENT selection is copied
    with _keyboard.pressed(Key.ctrl):
        _keyboard.press('c')
        _keyboard.release('c')

    # give the OS a moment to put the selection on the clipboard
    time.sleep(0.1)

    # the text that is copied
    tmp_value = pyperclip.paste()
    
    return tmp_value
