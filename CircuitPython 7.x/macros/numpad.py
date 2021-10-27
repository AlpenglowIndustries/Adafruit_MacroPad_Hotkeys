# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x870000, '1', ['1']),
        (0x873b00, '2', ['2']),
        (0x876300, '3', ['3']),
        # 2nd row ----------
        (0x873b00, '4', ['4']),
        (0x876300, '5', ['5']),
        (0x00870b, '6', ['6']),
        # 3rd row ----------
        (0x876300, '7', ['7']),
        (0x00870b, '8', ['8']),
        (0x006a87, '9', ['9']),
        # 4th row ----------
        (0x00870b, '*', ['*']),
        (0x006a87, '0', ['0']),
        (0x580087, '#', ['#']),
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}