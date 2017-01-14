from pymouse import PyMouse
from pykeyboard import PyKeyboard
import webbrowser, time, signal, sys

from events import KeyboardBoo

m = PyMouse()
k = PyKeyboard()
kb_boo = KeyboardBoo()

def is_halloween_in_january():
    return time.strftime("%d") in ["13", "14"] and time.strftime("%m") == "01"

def type_slowly(text):
    for char in text:
        k.tap_key(char)
        if char == ' ':
            time.sleep(0.6)
        else:
            time.sleep(0.4)

def spook():
    if not is_halloween_in_january():
        return

    # initialize keyboard listener
    kb_boo.run()

def handle_sigint(a, b):
    # stop listening
    kb_boo.state = False

    # run surprise
    webbrowser.open_new_tab('https://google.com')
    time.sleep(3)
    # press Ctrl+L to go to address bar
    k.press_key(k.control_key)
    k.tap_key('l')
    k.release_key(k.control_key)
    time.sleep(1)
    type_slowly('https://www.youtube.com/v/wxBO6KX9qTA?autoplay=true')
    time.sleep(1)
    k.tap_key('Return')

    sys.exit(0)

# register signal handler
signal.signal(signal.SIGINT, handle_sigint)
