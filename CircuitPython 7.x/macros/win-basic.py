# MACROPAD Hotkeys example: Basic Windows Shit

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Windows Basic', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x0de05e, 'Cut', [Keycode.CONTROL, 'x']),
        (0x0de05e, 'Copy', [Keycode.CONTROL, 'c']),
        (0x0de05e, 'Paste', [Keycode.CONTROL, 'v']),
        # 2nd row ----------
        (0x0de05e, 'Sel All', [Keycode.CONTROL, 'a']),
        (0x0de05e, 'Undo', [Keycode.CONTROL, 'z']),
        (0x0de05e, 'Rfresh', [Keycode.CONTROL, 'r']),
        # 3rd row ----------
        (0x770de0, 'New Tab', [Keycode.CONTROL, 't']),
        (0x770de0, 'New Win', [Keycode.CONTROL, 'n']),
        (0x770de0, 'Task', [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE,]),
        # 4th row ----------
        (0x770de0, 'Lock', [Keycode.WINDOWS, 'l']),
        (0x770de0, 'Vol+', [Keycode.CONTROL, Keycode.F3]),
        (0x770de0, 'Vol-', [Keycode.CONTROL, Keycode.F3]),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}