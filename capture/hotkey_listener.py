 

from typing import Callable

from pynput import keyboard
from pynput.mouse import Listener, Button
from capture.clipboard_listener import copy_text








# SECTION - button for user to turn the program on and off 
status = True

def listen_for_on_off_toggle(key):
    
    global status
    
    #!SECION - if button is z, toggle status
    if key == keyboard.KeyCode.from_char('z'):
        # NOTE this toggles the status between True and False
        status = not status 






# SECTION - mouse click listener, when user highlights and lets go, we will read the clipboard content
press_pos = None

def on_click(x: int, y: int, button: Button, pressed: bool, on_text: Callable):

    if status == True:

        global press_pos

        # if not left click, ignore
        if button != Button.left:
            return

        # if pressed set position
        if pressed:
            press_pos = (x, y)

        # represent stops being pressed
        else:

            # if same position as when pressed, ignore
            if (x,y) == press_pos:
                print("Mouse position is the same as when pressed. No action taken.")
                return


            text = copy_text()
            print(f"Retrieved text: {text}")


            # on_text is a function that is passed in from main.py, which is make_audio_from_text
            on_text(text)
            
       
            
            
                
    

    
# SECTION - start the mouse listener, and also start a keyboard listener to keep the program alive
def start_listener(on_text):
    # pynput only ever calls on_click with (x, y, button, pressed).
    # so we wrap it in a lambda that tacks on our on_text function,
    # smuggling it in without breaking pynput's fixed signature.
    mouse = Listener(on_click=lambda x, y, button, pressed: on_click(x, y, button, pressed, on_text))
    mouse.start()

    # keyboard listener blocks forever, keeping the whole program alive
    with keyboard.Listener(on_press=listen_for_on_off_toggle) as listener:
        listener.join() # sits and waits forever so program doesnt quit
    
    