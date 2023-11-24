#! python3

# Automated form filler

#1. Click the first text field of the form.
#2. Move through the form, typing information into each field.
#3. Click the Submit button.
#4. Repeat the process with the next set of data

import pyautogui
import time

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
 'robocop': 4, 'comments': 'Tell Bob I said hi.'},
 {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4,
 'comments': 'n/a'},
 {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
 {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
 ]
pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

# TODO: Give the user a chance to kill the script.
for person in formData:
    # give user chance to kill the script
    time.sleep(5)
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')

    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t', '\t'])

# TODO: Fill out the Name Field.
    pyautogui.write(person['name'] + '\t')
# TODO: Fill out the Greatest Fear(s) field.
    pyautogui.write(person['fear'] + '\t')
# TODO: Fill out the Source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.write(['down', '\t'] , 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down', '\t'] , 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down', '\t'] , 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down', '\t'] , 0.5)
# TODO: Fill out the RoboCop field.
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t'] , 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t'] , 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t'] , 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t'] , 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t'] , 0.5)


# TODO: Fill out the Additional Comments field.
    pyautogui.write(person['comments'] + '\t')
# TODO: Click Submit.
    time.sleep(0.5) # Wait for the button to activate.
    pyautogui.press('enter')
# TODO: Wait until form page has loaded.
    print('Submitted form.')
    time.sleep(5)
# TODO: Click the Submit another response link.
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
