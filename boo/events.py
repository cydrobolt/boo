import random, time
from pykeyboard import PyKeyboardEvent, PyKeyboard

k = PyKeyboard()

class KeyboardBoo(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)

        self.space_pressed = True

    def tap(self, keycode, character, press):
        # press is boolean; True for press, False for release
        if press == True:
            # on release
            if character == ' ':
                # if space pressed
                self.space_pressed = True
                return

            if character in ['b', 'o', 'Return'] or keycode == k.backspace_key:
                # exclude 'boo' from keypress to
                # avoid recursive boos
                return

            o_nums = random.randint(3, 8)
            k.tap_key(k.backspace_key)

            if self.space_pressed == True:
                self.space_pressed = False
                k.tap_key('b')
                return

            k.tap_key('o')
            return False
