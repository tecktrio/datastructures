import keyboard

x = 'a'
y = 'b'
keyboard.add_hotkey(x,lambda:keyboard.write(y))


keyboard.wait()
