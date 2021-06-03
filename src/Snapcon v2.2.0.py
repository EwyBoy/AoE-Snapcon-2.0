import os
import keyboard
import pyautogui
import Tkinter

from ConfigParser import SafeConfigParser

mode = False
label = Tkinter.Label(text='Placeholder Text', font=('Times New Roman', '18'), fg='white', bg='black')
config = SafeConfigParser(allow_no_value=True)

print 'AoE - Snapcon version 2.2.0'
print 'Developed by: EwyBoy 03.18.2018\n'
print 'License: The MIT License Copyright (c) <2018> <EwyBoy> Permission is hereby granted, \n' \
      'free of charge, to any person obtaining a copy of this software and associated documentation files (the \n' \
      '"Software"), to deal in the Software without restriction, including without limitation the rights to use, \n' \
      'copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit \n' \
      'persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright \n' \
      'notice and this permission notice shall be included in all copies or substantial portions of the Software. THE \n' \
      'SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO \n' \
      'THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE \n' \
      'AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF \n' \
      'CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER \n' \
      'DEALINGS IN THE SOFTWARE.\n'


# Writes the config file if there is not already one generated
def write_file():
    config.write(open('keybindings.ini', 'w'))


# Checks if there is not an existing keybindings file
# If not, it is generating the default one
if not os.path.exists('keybindings.ini'):
    print ('Generating keybindings.ini file')

    config.add_section('keybindings')

    config.set('keybindings', '# Switch Mode')
    config.set('keybindings', 'key0', '`')

    config.set('keybindings', '# House | Barracks')
    config.set('keybindings', 'key1', '1')

    config.set('keybindings', '# Mill | Archery Range')
    config.set('keybindings', 'key2', '2')

    config.set('keybindings', '# Farm | Stable')
    config.set('keybindings', 'key3', '3')

    config.set('keybindings', '# Mining Camp | Siege Workshop')
    config.set('keybindings', 'key4', '4')

    config.set('keybindings', '# Lumber Camp | Wooden Wall')
    config.set('keybindings', 'key5', '5')

    config.set('keybindings', '# Blacksmith | Wooden Tower')
    config.set('keybindings', 'key6', '6')

    config.set('keybindings', '# Market	Stone | Wall')
    config.set('keybindings', 'key7', '7')

    config.set('keybindings', '# University | Stone Tower')
    config.set('keybindings', 'key8', '8')

    config.set('keybindings', '# Monastery | Cannon Tower')
    config.set('keybindings', 'key9', '9')

    config.set('keybindings', '# Town Center | Castle')
    config.set('keybindings', 'key10', '0')

    config.set('keybindings', '# Dock | Wooden Gate')
    config.set('keybindings', 'key11', '-')

    config.set('keybindings', '# Wonder | Stone Gate')
    config.set('keybindings', 'key12', '=')

    write_file()

# else we read the one we have
else:
    print ('Loading keybindings.ini file')
    config.read('keybindings.ini')


# Grabs the mode and executes the key combo to build requested building
def build(getMode, key1, key2, name1, name2):
    if getMode:
        pyautogui.typewrite('s')
        pyautogui.typewrite(key1)
        print('Build ' + name1)
    else:
        pyautogui.typewrite('a')
        pyautogui.typewrite(key2)
        print('Build ' + name2)


# Draws the UI-Overlay
def funcOverlay():
    label.master.geometry("+0+250")
    label.master.overrideredirect(True)
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)

    if mode:
        label.configure(text='Military Mode')
    else:
        label.configure(text='Building Mode')
    label.update()
    label.pack()


# Flips the MODE boolean and tells the UI-overlay to update it's label
def switchMode():
    global mode
    mode ^= True
    pyautogui.typewrite('')
    pyautogui.typewrite('')
    funcOverlay()
    if mode:
        label.configure(text='Military Mode')
        print('Military Mode')
    else:
        label.configure(text='Building Mode')
        print('Building Mode')


# Have to Switch mode twice to get the UI to render properly
# Don't ask why, cause if I knew why it would NOT be done like this
print('Firing up overlay UI and testing modes:')
switchMode()
print('Military Mode Confirmed Working')
switchMode()
print('Building Mode Confirmed Working')


# Main loop that handles key presses
def funcLoop():
    global mode

    while True:
        try:
            # Toggles between normal and military buildings using the '|' (pipe) key
            if keyboard.is_pressed(config.get('keybindings', 'key0')):
                switchMode()

            # <1> # Build House / Barracks
            elif keyboard.is_pressed(config.get('keybindings', 'key1')):
                build(mode, 'q', 'q', 'Barracks', 'House')

            # <2> # Build Mill / Archer Range
            elif keyboard.is_pressed(config.get('keybindings', 'key2')):
                build(mode, 'w', 'w', "Archer Range", "Mill")

            # <3> # Build Farm / Stable
            elif keyboard.is_pressed(config.get('keybindings', 'key3')):
                build(mode, 'e', 'a', "Stable", 'Farm')

            # <4> # Build Mining Camp / Siege Workshop
            elif keyboard.is_pressed(config.get('keybindings', 'key4')):
                build(mode, 'r', 'e', "Siege Workshop", 'Mining Camp')

            # <5> # Build Lumber Camp / Wooden Wall
            elif keyboard.is_pressed(config.get('keybindings', 'key5')):
                build(mode, 's', 'r', "Wooden Wall", 'Lumber Camp')

            # <6> # Build Blacksmith / Wooden Tower
            elif keyboard.is_pressed(config.get('keybindings', 'key6')):
                build(mode, 'a', 's', 'Wooden Tower', 'Blacksmith')

            # <7> # Market / Build Stone Wall
            elif keyboard.is_pressed(config.get('keybindings', 'key7')):
                build(mode, 'd', 'd', 'Stone Wall', 'Market')

            # <8> # Build University / Stone Tower
            elif keyboard.is_pressed(config.get('keybindings', 'key8')):
                build(mode, 'f', 'g', 'Stone Tower', 'University')

            # <9> # Build Monastery / Cannon Tower
            elif keyboard.is_pressed(config.get('keybindings', 'key9')):
                build(mode, 'g', 'f', "Cannon Tower", 'Monastery')

            # <0> # Build Town Center / Castle
            elif keyboard.is_pressed(config.get('keybindings', 'key10')):
                build(mode, 'c', 'z', 'Castle', 'Town Center')

            # <+> # Build Build Dock / Wooden Gate
            elif keyboard.is_pressed(config.get('keybindings', 'key11')):
                build(mode, 'x', 't', 'Wooden Gate', 'Build Dock')

            # <\> # Build Wonder / Stone Gate
            elif keyboard.is_pressed(config.get('keybindings', 'key12')):
                build(mode, 'z', 'x', 'Stone Gate', 'Wonder')

            else:
                pass
        except:
            break


# Main method
if __name__ == '__main__':
    write_file()
    funcLoop()
    funcOverlay()
