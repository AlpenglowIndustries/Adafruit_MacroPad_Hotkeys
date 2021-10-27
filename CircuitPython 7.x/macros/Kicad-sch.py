# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Kicad-Schematic', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x7d00fa, 'Save', [Keycode.CONTROL, 's']),      # Save
        (0x7d00fa, 'Undo', [Keycode.CONTROL, 'z']),      # Undo
        (0x7d00fa, 'Pref.', [Keycode.CONTROL, ',']),     # Prefrences
        # 2nd row ----------
        (0x000dff, '+Sym', ['a']),      # Add Symbol
        (0x000dff, '+Pwr', ['p']),      # Add Power
        (0x000dff, 'No Conn', ['q']),   # No Connection Flag
        # 3rd row ----------
        (0x06bf0c, 'Dupl', ['c']),      # Duplicate
        (0x06bf0c, 'Move', ['m']),      # Move
        (0x06bf0c, 'Rotate', ['r']),    # Rotate
        # 4th row ----------
        (0xfcf400, '+Label', ['l']),   # Add Label
        (0xfcf400, 'Wire', ['w']),     # Add wire
        (0xfcf400, 'Value', ['v']),    # Edit Symbol Value
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}