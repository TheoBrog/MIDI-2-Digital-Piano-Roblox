import mido
from pynput.keyboard import Controller, Key

keyboard = Controller()

# Exemplo de dicionário: nota -> (tecla, precisa_shift)
note_to_key = {
    36: ('1', False),
    37: ('1', True),
    38: ('2', False),
    39: ('2', True),
    40: ('3', False),
    41: ('4', False),
    42: ('4', True),
    43: ('5', False),
    44: ('5', True),
    45: ('6', False),
    46: ('6', True),
    47: ('7', False),
    48: ('8', False),
    49: ('8', True),
    50: ('9', False),
    51: ('9', True),
    52: ('0', False),
    53: ('q', False),
    54: ('q', True),
    55: ('w', False),
    56: ('w', True),
    57: ('e', False),
    58: ('e', True),
    59: ('r', False),
    60: ('t', False),
    61: ('t', True),
    62: ('y', False),
    63: ('y', True),
    64: ('u', False),
    65: ('i', False),
    66: ('i', True),
    67: ('o', False),
    68: ('o', True),
    69: ('p', False),
    70: ('p', True),
    71: ('a', False),
    72: ('s', False),
    73: ('s', True),
    74: ('d', False),
    75: ('d', True),
    76: ('f', False),
    77: ('g', False),
    78: ('g', True),
    79: ('h', False),
    80: ('h', True),
    81: ('j', False),
    82: ('j', True),
    83: ('k', False),
    84: ('l', False),
    85: ('l', True),
    86: ('z', False),
    87: ('z', True),
    88: ('x', False),
    89: ('c', False),
    90: ('c', True),
    91: ('v', False),
    92: ('v', True),
    93: ('b', False),
    94: ('b', True),
    95: ('n', False),
    96: ('m', False)
}

print("Portas MIDI disponíveis:")
for port in mido.get_input_names():
    print(f" - {port}")

port_name = mido.get_input_names()[0]
print(f"\nUsando porta: {port_name}")

with mido.open_input(port_name) as inport:
    print("\nAguardando notas MIDI... (Ctrl+C para sair)")
    for msg in inport:
        if msg.type == 'note_on' and msg.velocity > 0:
            note = msg.note
            print(f"Nota pressionada: {note}")
            if note in note_to_key:
                key, need_shift = note_to_key[note]
                print(f"Pressionando tecla: {'Shift + ' if need_shift else ''}{key}")
                if need_shift:
                    with keyboard.pressed(Key.shift):
                        keyboard.press(key)
                        keyboard.release(key)
                else:
                    keyboard.press(key)
                    keyboard.release(key)