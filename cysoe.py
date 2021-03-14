#===============================================#
# CYS Offline Editor (CYSOE) by Hunter Browning #
# Start: 02/21/2021                             #
# Version: ALPHA 0.0.1                          #
#===============================================#
#-----------------------------------------------#
# IMPORT                                        #
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
    cysoe_icon = Path(str(os.path.dirname(__file__)) + '/assets/cysoe.png')
elif platform == 'win32':
    cysoe_icon = Path(str(os.path.dirname(__file__)) + '/assets/cysoe.ico')

cats = ['Dark Fantasy', 'Fantasy Adventure', 'Sci-fi Adventure', 'Modern Adventure', 'Horror',
        'Love & Dating', 'Mystery/Thriller', 'Edutainment', 'Fan Fiction', 'Everything Else']

mats = ['1 - (G) All ages', '2 - Young children', '3 - (PG) Most children',
        '4 - Young teens', '5 - (PG-13) Older teens', '6 - Young adults', '7 - (R) Adults']

diffs = ['1 - no possible way to lose', '2 - walk in the park', '3 - trek through the forest', '4 - march in the swamp',
         '5 - run through the jungle', '6 - living in detroit', '7 - walking into mordor', '8 - licking your elbow']

tags = ['Action Adventure', 'Animal Perspective', 'Anti-Hero', 'Based Off A True Story', 'Biblical',
        'Contest Entry', 'CYOA Movie', 'Drama', 'Dystopia', 'Edgelord', 'Family Friendly', 'Fantasy', 'Female Protagonist',
        'Foreign Language', 'Grimdark', 'Historical', 'Horror', 'Humor', 'LGBT', 'Mystery',
        'Part Of A Series', 'Poetry', 'Post-apocalyptic', 'Previously Featured', 'Psychological', 'Puzzle', 'Quiz',
        'Romance', 'RPG', 'Science Fiction', 'Serious', 'Socially Important', 'Spiritual', 'Sports', 'Superhero',
        'Supernatural', 'Thriller', 'Villain Protagonist', 'War', 'Western', 'Zombie']

pages = []

#-----------------------------------------------#
# PRE-PROCESSING                                #
#-----------------------------------------------#
#-----------------------------------------------#
# GUI                                           #
#-----------------------------------------------#

# Menubar
menubar = [['File',  ['New', 'Open', 'Save', 'Save As', 'Export / Format']],
           ['Edit',  ['Pages', 'Variables', 'Scripts', 'Items', 'Preferences'], ],
           ['Help',  ['CYSOE Documentation', 'CYS Script Documentation', 'Advanced Editor Forum', 'About'], ]]

# Layouts
storygame_properties_layout = [[sg.T('Title:'), sg.Input(key='-TITLE-')],
                               [sg.T('Description:'), sg.Input(key='-DESC-')],
                               [sg.T('Category:'), sg.Combo(
                                   cats, enable_events=True, key='-CAT-')],
                               [sg.T('Maturity:'), sg.Combo(
                                   mats, enable_events=True, key='-MAT-')],
                               [sg.T('Difficulty:'), sg.Combo(
                                   diffs, enable_events=True, key='-DIFF-')],
                               [sg.T('Tags:'), sg.Combo(tags, enable_events=True, key='-TAGS-')]]

items_layout = [[sg.B('Create New Item')],
                [sg.T('ID#'), sg.B('Test')]]

variables_layout = [[sg.B('Create New Variable')],
                    [sg.T('Variable'), sg.T('Min'), sg.T('Max'),
                     sg.T('Start'), sg.T('Disp. On Pg.')],
                    [sg.B('SCORE'), sg.T('-'), sg.T('-'), sg.T('-'), sg.T('No')]]

scripts_layout = [[sg.B('Global Page Script')],
                  [sg.B('Global Link Script')]]

chapters_and_pages_layout = [[sg.B('New Chapter')],
                             [sg.T('ID'), sg.T('Chapter Title'),
                              sg.T('Chapter Start Page')],
                             [sg.T('1'), sg.Input(key='-CH_TITLE-'),
                              sg.Combo(pages, key='-CH_START-')],
                             [sg.B('Save Changes To Chapter'),
                              sg.B('Delete Entire Chapter')],
                             [sg.T('Pages in Chapter 1')],
                             [sg.B('Create New Page')]]

main_window_layout = [[sg.Menu(menubar)],
                      [sg.TabGroup([[sg.Tab('Storygame Properties', storygame_properties_layout), sg.Tab(
                          'Chapters & Pages', chapters_and_pages_layout),
                          sg.Tab('Items', items_layout),
                          sg.Tab('Variables', variables_layout),
                          sg.Tab('Scripts', scripts_layout)]])],
                      [sg.B('Save'), sg.B('Save and Exit')]]

initial_popup_layout = [[sg.B('New'), sg.B('Open'), sg.B('Exit')]]

# Windows
init_pop = sg.Window('CYSOE', initial_popup_layout, icon=cysoe_icon,
                     resizable=True, grab_anywhere=True)

main = sg.Window('CYS Offline Editor', main_window_layout,
                 icon=cysoe_icon, resizable=True, grab_anywhere=True)

#-----------------------------------------------#
# EVENT LOOP AND CALLBACKS                      #
#-----------------------------------------------#

while True:
    event, values = init_pop.read()
    print(event, values)
    if event == 'New':
        print('Creating new project directory...')
        break
    elif event == 'Open':
        print('Opening existing project directory...')
        break
    elif event in ('Exit', sg.WIN_CLOSED):
        print('Exiting...')
        exit()

while True:
    event, values = main.read()
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

main.close()
