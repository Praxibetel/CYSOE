#-----------------------------------------------#
# CYS Offline Editor (CYSOE) by Hunter Browning #
# Start: 02/21/2021                             #
# Version: ALPHA 0.0.0                          #
#-----------------------------------------------#

import PySimpleGUI as sg
import json
import os
from sys import platform
from pathlib import Path

#-----------------------------------------------#
# CONSTANTS                                     #
#-----------------------------------------------#

if platform == 'linux' or platform == 'linux2':
    cysoe_icon = Path(str(os.path.dirname( __file__ )) + '/cysoe.png')
elif platform == 'win32':
    cysoe_icon = Path(str(os.path.dirname( __file__ )) + '/cysoe.ico')

#-----------------------------------------------#
# PRE-PROCESSING                                #
#-----------------------------------------------#
#-----------------------------------------------#
# GUI                                           #
#-----------------------------------------------#
layout = [[sg.Text('Storygame Properties')],
          [sg.Text('Title:'), sg.Input(key='-TITLE-')],
          [sg.Text('Description:'), sg.Input(key='-DESC-')],
          [sg.Text('Category:'), sg.Input(key='-CAT-')],
          [sg.Text('Maturity:'), sg.Input(key='-MAT-')],
          [sg.Text('Difficulty:'), sg.Input(key='-DIFF-')],
          [sg.Text('Tags:'), sg.Input(key='-TAGS-')],
          [sg.Button('Save'), sg.Button('Save and Exit')]]

window = sg.Window('CYS Offline Editor', layout, icon=cysoe_icon)

#-----------------------------------------------#
# EVENT LOOP AND CALLBACKS                      #
#-----------------------------------------------#

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED):
        print('Exiting...')
        break
    elif event == 'Save':
        outfile = open(os.path.dirname(__file__) + '/cysoe.json', 'w+')
        json.dump(values, outfile, indent=4)
        outfile.close()
        print('Saved')
    elif event == 'Save and Exit':
        outfile = open(os.path.dirname(__file__) + '/cysoe.json', 'w+')
        json.dump(values, outfile, indent=4)
        outfile.close()
        print('Saved\nExiting...')
        break

window.close()
