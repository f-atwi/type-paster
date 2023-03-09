import keyboard
import pyperclip

def type_clipboard():
    keyboard.write(pyperclip.paste())

keyboard.add_hotkey('ctrl+alt+v', type_clipboard)

keyboard.wait("ctrl+alt+q")
