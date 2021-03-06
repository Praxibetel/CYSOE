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
    cysoe_icon = Path(str(os.path.dirname( __file__ )) + '/assets/cysoe.png')
elif platform == 'win32':
    cysoe_icon = Path(str(os.path.dirname( __file__ )) + '/assets/cysoe.ico')

cats = ['Dark Fantasy', 'Fantasy Adventure', 'Sci-fi Adventure', 'Modern Adventure', 'Horror', 'Love & Dating', 'Mystery/Thriller', 'Edutainment', 'Fan Fiction', 'Everything Else']
mats = ['1 - (G) All ages', '2 - Young children', '3 - (PG) Most children', '4 - Young teens', '5 - (PG-13) Older teens', '6 - Young adults', '7 - (R) Adults']
diffs = ['1 - no possible way to lose', '2 - walk in the park', '3 - trek through the forest', '4 - march in the swamp', '5 - run through the jungle', '6 - living in detroit', '7 - walking into mordor', '8 - licking your elbow']
tags = ['Action Adventure', 'Animal Perspective', 'Anti-Hero', 'Based Off A True Story', 'Biblical', 'Contest Entry', 'CYOA Movie', 'Drama', 'Dystopia', 'Edgelord', 'Family Friendly', 'Fantasy', 'Female Protagonist', 'Foreign Language', 'Grimdark', 'Historical', 'Horror', 'Humor', 'LGBT', 'Mystery', 'Part Of A Series', 'Poetry', 'Post-apocalyptic', 'Previously Featured', 'Psychological', 'Puzzle', 'Quiz', 'Romance', 'RPG', 'Science Fiction', 'Serious', 'Socially Important', 'Spiritual', 'Sports', 'Superhero', 'Supernatural', 'Thriller', 'Villain Protagonist', 'War', 'Western', 'Zombie']

cysoe_optn  = dict()
cysoe_optn['input-width'     ] = 144
cysoe_optn['input-heigt'     ] = 10
cysoe_optn['output-width'    ] = 140
cysoe_optn['output-heigt'    ] = 30
cysoe_optn['output-font'     ] = 'Courier'
cysoe_optn['output-font-size'] = 10
cysoe_optn['opm-flow-manual' ] = 'None'
cysoe_optn['opm-resinsight'  ] = 'None'
cysoe_optn['edit-command'    ] = 'None'


#-----------------------------------------------#
# PRE-PROCESSING                                #
#-----------------------------------------------#
#-----------------------------------------------#
# GUI                                           #
#-----------------------------------------------#

mainmenu   = [['File',  ['New', 'Open', 'Save', 'Save As', 'Export / Format']],
              ['Edit',  ['Pages', 'Variables', 'Scripts', 'Items', 'Preferences'],],
              ['Help',  ['CYSOE Documentation', 'CYS Script Documentation', 'Advanced Editor Forum', 'About'],] ]

proplayout = [[sg.Menu(mainmenu)],
          [sg.Text('Storygame Properties')],
          [sg.Text('Title:'), sg.Input(key='-TITLE-')],
          [sg.Text('Description:'), sg.Input(key='-DESC-')],
          [sg.Text('Category:'), sg.Combo(cats, enable_events=True, key='-CAT-')],
          [sg.Text('Maturity:'), sg.Combo(mats, enable_events=True, key='-MAT-')],
          [sg.Text('Difficulty:'), sg.Combo(diffs, enable_events=True, key='-DIFF-')],
          [sg.Text('Tags:'), sg.Combo(tags, enable_events=True, key='-TAGS-')],
          [sg.Button('Save'), sg.Button('Save and Exit')]]

window = sg.Window('CYS Offline Editor', proplayout, icon=cysoe_icon)

#-----------------------------------------------#
# EVENT LOOP AND CALLBACKS                      #
#-----------------------------------------------#

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
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
