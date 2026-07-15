

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

def on_click(x, y, button, pressed):
    
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
            
            
            #TODO - we will pass text later on to AI agent 
            text = copy_text()
            print("Text: ", text)
            
            
                
    

    
# Start the listener that runs continuously
def start_listener():
    # mouse listener runs in the background — .start() does NOT block
    mouse = Listener(on_click=on_click)
    mouse.start()

    # keyboard listener blocks forever, keeping the whole program alive
    with keyboard.Listener(on_press=listen_for_on_off_toggle) as listener:
        listener.join() # sits and waits forever so program doesnt quit
    
    