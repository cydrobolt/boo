import random
from pykeyboard import PyKeyboardEvent, PyKeyboard

k = PyKeyboard()

class KeyboardBoo(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

    def tap(self, keycode, character, press):
        # press is boolean; True for press, False for release
        if press == False:
            # if releasing
            # o_nums = random.randint(3, 8)
            k.type_string('boo')
