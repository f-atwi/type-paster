from time import sleep
import keyboard
import pyperclip

def type_clipboard():
    for line in pyperclip.paste().split('\r\n'):
        keyboard.write(line)
        keyboard.send('enter')
        keyboard.send('home')
    keyboard.send('backspace')

paste_hotkey = 'esc+v'
exit_hotkey = 'esc+q'
keyboard.add_hotkey(paste_hotkey, type_clipboard, suppress=True)
keyboard.wait(exit_hotkey, suppress=True)
