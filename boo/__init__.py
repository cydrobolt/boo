from pymouse import PyMouse
from pykeyboard import PyKeyboard
import webbrowser, time

m = PyMouse()
k = PyKeyboard()

def spook():
    webbrowser.open_new_tab('https://google.com')
    time.sleep(3)
    k.tap_key('F6')
    time.sleep(1)
    k.type_string('hackclub.com')
    time.sleep(1)
    k.tap_key('Return')
