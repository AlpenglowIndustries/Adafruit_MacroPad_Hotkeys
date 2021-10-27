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
        (0x770de0, 'Tindie', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'https://www.tindie.com/orders/\n']), # Tindie orders in new tab
        (0x770de0, 'Yarn', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'https://www.weebly.com/app/store/users/44315549/sites/294261841826241486/#/store/orders\n']), # Alpenglow Yarn orders in new tab
        (0x770de0, 'AlpInd', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'https://www.weebly.com/app/store/users/44315549/sites/686100740128112971/#/store/orders\n']), # Alpenglow Industries orders in new tab
        # 4th row ----------
        (0x770de0, 'Twitter', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                           'https://twitter.com/alpenglowind\n']),   # Alpenglow Twitter in new tab
        (0x770de0, 'Ytube', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                            'https://www.youtube.com/channel/UCo8j_W8OaqIE78o4_Z4OagQ\n']),   # Alpenglow YouTube in new tab
        (0x770de0, 'Hacks', [Keycode.CONTROL, 't', -Keycode.COMMAND,
                             'https://hackaday.io/alpenglow\n']), # Hack-a-Day in new tab
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}