# MACROPAD Hotkeys example: Microsoft Edge web browser for Windows

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                      # REQUIRED dict, must be named 'app'
    'name' : 'Kicad-PCB', # Application name
    'macros' : [             # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000dff, '3D View', [Keycode.ALT, '3']),        # 3D Viewer
        (0x000dff, 'Save', [Keycode.CONTROL, 's']),       # Save
        (0x000dff, 'Undo', [Keycode.CONTROL, 'z']),       # Undo
        # 2nd row ----------
        (0x06bf0c, 'Pref.', [Keycode.CONTROL, ',']),      # Prefrences
        (0x06bf0c, '+Zoom', [Keycode.F1]),                # Zoom In
        (0x06bf0c, '-Zoom', [Keycode.F2]),                # Zoom Out
        # 3rd row ----------
        (0xfcf400, 'FP Edit', [Keycode.CONTROL, 'e']),    # Footprint Editor
        (0xfcf400, '+FP', ['o']),                         # Add Footprint
        (0xfcf400, '+Track', ['x']),                      # Add Track
        # 4th row ----------
        (0xfc6500, 'Rotate', ['r']),                      # Rotate
        (0xfc6500, 'Flip', ['f']),                        # Flip
        (0xfc6500, 'Move', [Keycode.CONTROL, 'm']),       # Move Exactly
        # Encoder button ---
        (0x000000, '', [Keycode.CONTROL, 'w']) # Close tab
    ]
}