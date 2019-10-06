#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.0),
    on Sun Oct  6 14:40:10 2019
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.0'
expName = 'mf_amp'  # from the Builder filename that created this script
expInfo = {'participant ID': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant ID'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jtf/projects/inprogress/mf_amp/exp_files_f19/mf_amp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0.765,0.765,0.765], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "hold"
holdClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to the Language, Symbols, and Emotion study! Please wait until a researcher says you may begin.',
    font='Verdana',
    pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
begin_key = keyboard.Keyboard()
import random 
import pandas as pd
import numpy as np
import webbrowser

globalClock = core.Clock()
routineClock = core.Clock()

# Reading in the CSVs

words = pd.read_csv("condition_files/words4exp.csv")
symbols = pd.read_csv("condition_files/symbols.csv")
memtask_words = pd.read_csv("condition_files/mem_task_words.csv")

# Generating word lists

unique_cats = {k:None for k in words.category.unique()} 

for k,v in unique_cats.items():
    unique_cats[k] = list(words[words.category == k].index.values)

full_amp_words = {k:None for k in unique_cats.keys() if k != "neutral"} 
full_ldt_words = {k:None for k in unique_cats.keys()} 

for k,v in unique_cats.items():
    if "." in str(k):
        full_amp_words[k] = random.sample(unique_cats[k],7)
        full_ldt_words[k] = [x for x in unique_cats[k] if x not in full_amp_words[k]]
    if k == "nonword":
        full_amp_words[k] = random.sample(unique_cats[k],10)
        full_ldt_words[k] = [x for x in unique_cats[k] if x not in full_amp_words[k]]
    if k =="control":
        full_amp_words[k] = unique_cats[k]
    if k == "neutral":
        full_ldt_words[k] = unique_cats[k]

amp_primes = [] 
amp_symbols = range(0,82) 

for k,v in full_amp_words.items():     
    for i in v:
        amp_primes.append(i)

# Pulling the words, correct answers, and categories for all of the indices for our moral words plus our ten nonword controls 

AMP_words = words.loc[amp_primes].words.values 
AMP_corr_ans = words.loc[amp_primes].correct_amp.values 
AMP_category = words.loc[amp_primes].category.values
AMP_masks = words.loc[amp_primes].masks.values

#pulling the nonwords and masks for our targets that weren't selected to be included in the prime 

AMP_symbols = symbols.loc[amp_symbols].symbol.values

# df1 is the words that will be used as primes and their associated categories and correct answers  

df1 = pd.DataFrame(
    {'words': AMP_words.tolist(),
    'corr_ans': AMP_corr_ans.tolist(),
    'category': AMP_category.tolist(),
    'masks': AMP_masks.tolist()
    })

# df2 is the nonwords that will be used as targets and their associated masks  

df2 = pd.DataFrame(
    {'symbols': AMP_symbols.tolist()
    })  

# Shuffling the words once and then generating four   

primes_rep1 = df1.sample(frac=1).reset_index(drop=True) 
targets_rep1 = df2.sample(frac=1).reset_index(drop=True)  
primes_rep2 = df1.sample(frac=1).reset_index(drop=True) 
targets_rep2 = df2.sample(frac=1).reset_index(drop=True)  
primes_rep3 = df1.sample(frac=1).reset_index(drop=True) 
targets_rep3 = df2.sample(frac=1).reset_index(drop=True)  
primes_rep4 = df1.sample(frac=1).reset_index(drop=True) 
targets_rep4 = df2.sample(frac=1).reset_index(drop=True)  

# Concatenating all of the primes and targets and writing them to condition files.

rep1 = pd.concat([primes_rep1,targets_rep1], axis = 1)
rep1.to_csv("condition_files/AMP_rep1.csv")

rep2 = pd.concat([primes_rep2,targets_rep2], axis = 1)
rep2.to_csv("condition_files/AMP_rep2.csv")

rep3 = pd.concat([primes_rep3,targets_rep3], axis = 1)
rep3.to_csv("condition_files/AMP_rep3.csv")

rep4 = pd.concat([primes_rep4,targets_rep4], axis = 1)
rep4.to_csv("condition_files/AMP_rep4.csv") 

# Concatenating all of the reps horizontally  

df_full = pd.concat([rep1,rep2,rep3,rep4], axis = 0)

# Writing AMP conditions to CSV

df_full.reset_index(inplace=True, drop=True)
df_full.to_csv("condition_files/AMP_conditions.csv")

# Generating LDT word list

ldt_wordlist = [] 

for k,v in full_ldt_words.items():
    if k != "control":
        for i in v:
            ldt_wordlist.append(i)

# Pulling the words, correct answers, categories, & masks for all of the indices for our words 

LDT_words = words.loc[ldt_wordlist].words.values 
LDT_corr = words.loc[ldt_wordlist].correct_ldt.values 
LDT_category = words.loc[ldt_wordlist].category.values 
LDT_masklist = words.loc[ldt_wordlist].masks.values

df_ldt = pd.DataFrame(
    {'words': LDT_words.tolist(),
    'corr_ans': LDT_corr.tolist(),
    'category': LDT_category.tolist(),
    'mask': LDT_masklist.tolist()     })

df_ldt.to_csv("condition_files/LDT_conditions.csv")

# Creating the list for the memory task

memtask_wordlist = memtask_words.words.values
memtask_cats = memtask_words.category.values
seen = pd.DataFrame(
    {'words': AMP_words.tolist(),
     'corr_ans': ['right'] * 82,
     'category': AMP_category.tolist()
    })

unseen = pd.DataFrame(
    {'words': memtask_wordlist.tolist(),
     'corr_ans': ['left'] * 50,
     'category': memtask_cats.tolist()
    })

seen_selection = seen.sample(n=50)
memtask_final = pd.concat([seen_selection,unseen], axis = 0)
memtask_final = memtask_final.sample(frac=1).reset_index(drop=True)

memtask_final.to_csv("condition_files/memtask_conditions.csv")

# Initialize components for Routine "instr_main"
instr_mainClock = core.Clock()
instr_2 = visual.TextStim(win=win, name='instr_2',
    text='The goal of this experiment is to better understand how people interpret symbols and understand language',
    font='Verdana',
    pos=(0, 0), height=.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_3 = visual.TextStim(win=win, name='instr_3',
    text='You will be asked to complete four different tasks, followed by a short survey.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_4 = visual.TextStim(win=win, name='instr_4',
    text='Before we begin, please make sure your fingers are on the correct keys.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_5 = visual.TextStim(win=win, name='instr_5',
    text='Your right index finger should be on the left arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_6 = visual.TextStim(win=win, name='instr_6',
    text='Your right ring finger should be on the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
position_reminder = visual.ImageStim(
    win=win,
    name='position_reminder', 
    image='images/keyboard_diagram.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
instr_7 = visual.TextStim(win=win, name='instr_7',
    text='If you are ready to begin please press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_instr = keyboard.Keyboard()

# Initialize components for Routine "instr_LDT"
instr_LDTClock = core.Clock()
instr_LDT1 = visual.TextStim(win=win, name='instr_LDT1',
    text='In this task, you will see a selection of real words and nonsense words.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_LDT2 = visual.TextStim(win=win, name='instr_LDT2',
    text='You will see a real word or a nonsense word quickly followed by a string of "&" symbols\n',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_LDT3 = visual.TextStim(win=win, name='instr_LDT3',
    text='Upon seeing the "&" symbols, you should decide as quickly as possible whether you saw a real word or nonsense word',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_LDT4 = visual.TextStim(win=win, name='instr_LDT4',
    text='If you think you saw a real word, press the RIGHT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_LDT5 = visual.TextStim(win=win, name='instr_LDT5',
    text='If you think you saw a nonsense word, press the LEFT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_LDT6 = visual.TextStim(win=win, name='instr_LDT6',
    text='Please make sure your fingers are in the correct place',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='images/keyboard_diagram.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
keyboard_reminder_LDT = visual.ImageStim(
    win=win,
    name='keyboard_reminder_LDT', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
instr_LDT7 = visual.TextStim(win=win, name='instr_LDT7',
    text='The words may be difficult to see, but please do the best you can',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_LT8 = visual.TextStim(win=win, name='instr_LT8',
    text="Let's do a practice round",
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
instr_LDT9_ = visual.TextStim(win=win, name='instr_LDT9_',
    text='When you are ready to begin, press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_LDT_instr = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
LDT_fix_cross = visual.ImageStim(
    win=win,
    name='LDT_fix_cross', 
    image='images/crosshair.png', mask=None,
    ori=0, pos=(0, 0), size=[.05,.05],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "LDT_prac"
LDT_pracClock = core.Clock()
LDT_word_prac = visual.TextStim(win=win, name='LDT_word_prac',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
LDT_mask_prac = visual.TextStim(win=win, name='LDT_mask_prac',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_LDT_prac = keyboard.Keyboard()
key_reminder_3 = visual.ImageStim(
    win=win,
    name='key_reminder_3', units='deg', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "instr_LDT_2"
instr_LDT_2Clock = core.Clock()
instr_LDT9 = visual.TextStim(win=win, name='instr_LDT9',
    text='Great job!',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_LDT10 = visual.TextStim(win=win, name='instr_LDT10',
    text='Remember that LEFT is nonsense word and RIGHT is real word.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr_LDT11 = visual.TextStim(win=win, name='instr_LDT11',
    text='If you are ready to begin, please press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
resp_LDT_ready = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
LDT_fix_cross = visual.ImageStim(
    win=win,
    name='LDT_fix_cross', 
    image='images/crosshair.png', mask=None,
    ori=0, pos=(0, 0), size=[.05,.05],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "LDT_trial"
LDT_trialClock = core.Clock()
LDT_word_trial = visual.TextStim(win=win, name='LDT_word_trial',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
LDT_mask_trial = visual.TextStim(win=win, name='LDT_mask_trial',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_LDT_trial = keyboard.Keyboard()
key_reminder = visual.ImageStim(
    win=win,
    name='key_reminder', units='deg', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "LDT_feedback"
LDT_feedbackClock = core.Clock()
LDT_rating = visual.RatingScale(win=win, name='LDT_rating', scale = "To what extent did you respond randomly in this task?",
choices=None, 
low=1, 
high=7, 
pos=[0,0],
precision=1, 
labels=["Not at all","Somewhat","Completely"], 
tickMarks=None, 
showValue=False,
showAccept=True,
acceptPreText='Click a value', 
acceptText='Accept?', 
acceptSize=1.0,
tickHeight=1.0, 
marker='slider',
markerStart=4, 
textSize=1.0,
stretch = 1.5, 
textColor='Black', 
textFont='Helvetica Bold',
disappear=True)
LDT_feedback_inst = visual.TextStim(win=win, name='LDT_feedback_inst',
    text='You will now respond to a question. Please note that your response to this question is completely anonymous and will not affect your SONA credit in any way.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instr_symbol"
instr_symbolClock = core.Clock()
instr_sym1 = visual.TextStim(win=win, name='instr_sym1',
    text='In this task, you will see a selection of symbols.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_sym2 = visual.TextStim(win=win, name='instr_sym2',
    text='You will be asked to rate whether each symbol you see makes you feel pleasant or unpleasant.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_sym3 = visual.TextStim(win=win, name='instr_sym3',
    text='If the symbol made you feel pleasant, press the RIGHT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_sym4 = visual.TextStim(win=win, name='instr_sym4',
    text='If the symbol made you feel unpleasant, press the LEFT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_sym5 = visual.TextStim(win=win, name='instr_sym5',
    text='The symbol will look something like this.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
logo_example = visual.ImageStim(
    win=win,
    name='logo_example', 
    image='images/symbols/symbol_1.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
instr_sym6 = visual.TextStim(win=win, name='instr_sym6',
    text='Remember that you will press RIGHT if the symbol made you feel pleasant and LEFT if the symbol made you feel unpleasant.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
logo_prac_layout_reminder = visual.ImageStim(
    win=win,
    name='logo_prac_layout_reminder', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
instr_sym7 = visual.TextStim(win=win, name='instr_sym7',
    text='First, we will do a brief practice round.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_sym8 = visual.TextStim(win=win, name='instr_sym8',
    text='When you are ready to begin, press the RIGHT arrow key.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
resp_sym_rate = keyboard.Keyboard()

# Initialize components for Routine "symbol_prac"
symbol_pracClock = core.Clock()
img_logo_prac = visual.ImageStim(
    win=win,
    name='img_logo_prac', 
    image='images/symbols/symbol_2.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mask_logo_prac = visual.ImageStim(
    win=win,
    name='mask_logo_prac', units='height', 
    image='images/symbols/mask.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_reminder_logo_prac = visual.ImageStim(
    win=win,
    name='key_reminder_logo_prac', units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sym_resp_1 = keyboard.Keyboard()

# Initialize components for Routine "instr_symbol2"
instr_symbol2Clock = core.Clock()
instr_sym9 = visual.TextStim(win=win, name='instr_sym9',
    text='Great job!',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_sym10 = visual.TextStim(win=win, name='instr_sym10',
    text='Remember that LEFT is unpleasant and RIGHT is pleasant.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sym_layout_reminder = visual.ImageStim(
    win=win,
    name='sym_layout_reminder', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr_sym11 = visual.TextStim(win=win, name='instr_sym11',
    text='If you are ready to begin, please press the RIGHT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
sym_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "logo_trial"
logo_trialClock = core.Clock()
img_logo_trial = visual.ImageStim(
    win=win,
    name='img_logo_trial', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mask_logo_trial = visual.ImageStim(
    win=win,
    name='mask_logo_trial', units='height', 
    image='images/symbols/mask.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
key_reminder_logo_trial = visual.ImageStim(
    win=win,
    name='key_reminder_logo_trial', units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -7), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
sym_resp_trial = keyboard.Keyboard()

# Initialize components for Routine "instr_AMP"
instr_AMPClock = core.Clock()
instr_AMP1_1 = visual.TextStim(win=win, name='instr_AMP1_1',
    text='In this task, you will see the same symbols you just rated.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_AMP1_2 = visual.TextStim(win=win, name='instr_AMP1_2',
    text='Before you see each symbol, you will see a string of letters.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_AMP1_3 = visual.TextStim(win=win, name='instr_AMP1_3',
    text='This string of letters is a cue that the symbol is about to appear, helping you respond faster.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_AMP1_4 = visual.TextStim(win=win, name='instr_AMP1_4',
    text='You will be asked to rate whether each symbol makes you feel pleasant or unpleasant.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_AMP1_5 = visual.TextStim(win=win, name='instr_AMP1_5',
    text='If the symbol made you feel pleasant, press the RIGHT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_AMP1_6 = visual.TextStim(win=win, name='instr_AMP1_6',
    text='If the symbol made you feel unpleasant, press the LEFT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
instr_AMP1_7 = visual.TextStim(win=win, name='instr_AMP1_7',
    text='Remember to press RIGHT for pleasant and LEFT for unpleasant',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
instr_AMP1_8 = visual.TextStim(win=win, name='instr_AMP1_8',
    text='The symbol will quickly disappear and will be replaced with white noise, so be sure to make your responses as quickly as possible.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_AMP1_9 = visual.TextStim(win=win, name='instr_AMP1_9',
    text="Let's do a practice round.",
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
instr_AMP1_10 = visual.TextStim(win=win, name='instr_AMP1_10',
    text='When you are ready to begin press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
resp_AMP_ready1 = keyboard.Keyboard()

# Initialize components for Routine "AMP_prime"
AMP_primeClock = core.Clock()
AMP_wordstim_2 = visual.TextStim(win=win, name='AMP_wordstim_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AMP_key_reminder_1 = visual.ImageStim(
    win=win,
    name='AMP_key_reminder_1', units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prime_durs = [1, 3, 6]
prime_dur = np.random.choice(prime_durs)
mask_dur = 2 * prime_dur

# Initialize components for Routine "AMP_target_prac"
AMP_target_pracClock = core.Clock()
img_logo_AMP = visual.ImageStim(
    win=win,
    name='img_logo_AMP', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mask_AMP = visual.ImageStim(
    win=win,
    name='mask_AMP', units='height', 
    image='images/symbols/mask.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
AMP_key_reminder = visual.ImageStim(
    win=win,
    name='AMP_key_reminder', units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
resp_AMP = keyboard.Keyboard()

# Initialize components for Routine "instr_AMP_2"
instr_AMP_2Clock = core.Clock()
instr_AMP2_1 = visual.TextStim(win=win, name='instr_AMP2_1',
    text='Great job!',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_AMP2_2 = visual.TextStim(win=win, name='instr_AMP2_2',
    text='Remember that LEFT is unpleasant and RIGHT is pleasant.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr_AMP2_3 = visual.TextStim(win=win, name='instr_AMP2_3',
    text='If you are ready to begin, please press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
resp_AMP_ready = keyboard.Keyboard()

# Initialize components for Routine "instr_AMP_3"
instr_AMP_3Clock = core.Clock()
instr_AMP3_1 = visual.TextStim(win=win, name='instr_AMP3_1',
    text="Let's go!",
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AMP_prime"
AMP_primeClock = core.Clock()
AMP_wordstim_2 = visual.TextStim(win=win, name='AMP_wordstim_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
AMP_key_reminder_1 = visual.ImageStim(
    win=win,
    name='AMP_key_reminder_1', units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
prime_durs = [1, 3, 6]
prime_dur = np.random.choice(prime_durs)
mask_dur = 2 * prime_dur

# Initialize components for Routine "AMP_target_trials"
AMP_target_trialsClock = core.Clock()
img_logo_AMP_trials = visual.ImageStim(
    win=win,
    name='img_logo_AMP_trials', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
mask_AMP_2 = visual.ImageStim(
    win=win,
    name='mask_AMP_2', units='height', 
    image='images/symbols/mask.png', mask=None,
    ori=0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
AMP_key_reminder_2 = visual.ImageStim(
    win=win,
    name='AMP_key_reminder_2', units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
resp_AMP_trials = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_txt1 = visual.TextStim(win=win, name='rest_txt1',
    text='Take a quick break for as long as you need to rest your eyes. Press the RIGHT arrow key when you are ready for the next round.',
    font='verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rest_key_resp = keyboard.Keyboard()

# Initialize components for Routine "AMP_feedback"
AMP_feedbackClock = core.Clock()
AMP_nonword_rating = visual.RatingScale(win=win, name='AMP_nonword_rating', scale = "To what extent did you base your ratings of the symbols on the symbols themselves?",
choices=None, 
low=1, 
high=7, 
pos=[0,0],
precision=1, 
labels=["Not at all","Somewhat","Completely"], 
tickMarks=None, 
showValue=False,
showAccept=True,
acceptPreText='Click a value', 
acceptText='Accept?', 
acceptSize=1.0,
tickHeight=1.0, 
marker='slider',
markerStart=4, 
textSize=1.0,
stretch = 1.5, 
textColor='Black', 
textFont='Helvetica Bold',
disappear=True)
AMP_word_rating = visual.RatingScale(win=win, name='AMP_word_rating', scale = "To what extent did you base your ratings on the strings of letters that appeared before the symbols?",
choices=None, 
low=1, 
high=7, 
pos=[0,0],
precision=1, 
labels=["Not at all","Somewhat","Completely"], 
tickMarks=None, 
showValue=False,
showAccept=True,
acceptPreText='Click a value', 
acceptText='Accept?', 
acceptSize=1.0,
tickHeight=1.0, 
marker='slider',
markerStart=4, 
textSize=1.0,
stretch = 1.5, 
textColor='Black', 
textFont='Helvetica Bold',
disappear=True)
AMP_random_rating = visual.RatingScale(win=win, name='AMP_random_rating', scale = "To what extent did you respond randomly in this task?",
choices=None, 
low=1, 
high=7, 
pos=[0,0],
precision=1, 
labels=["Not at all","Somewhat","Completely"], 
tickMarks=None, 
showValue=False,
showAccept=True,
acceptPreText='Click a value', 
acceptText='Accept?', 
acceptSize=1.0,
tickHeight=1.0, 
marker='slider',
markerStart=4, 
textSize=1.0,
stretch = 1.5, 
textColor='Black', 
textFont='Helvetica Bold',
disappear=True)
AMP_feedback_instr = visual.TextStim(win=win, name='AMP_feedback_instr',
    text='You will now respond to a few questions. Please note that your responses to these questions are completely anonymous and will not affect your SONA credit in any way.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "instr_memtask"
instr_memtaskClock = core.Clock()
instr_memtask1 = visual.TextStim(win=win, name='instr_memtask1',
    text='In this task, you will see a selection of words you saw in this experiment, along with words you did NOT see.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_memtask2 = visual.TextStim(win=win, name='instr_memtask2',
    text='You will be asked to respond as to whether you think you saw the word during the experiment or not.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_memtask3 = visual.TextStim(win=win, name='instr_memtask3',
    text='If you think you saw the word during the experiment, press the RIGHT arrow key.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_memtask4 = visual.TextStim(win=win, name='instr_memtask4',
    text='If you think you did NOT see the word in the experiment, press the LEFT arrow key.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
layout_reminder_memtask = visual.ImageStim(
    win=win,
    name='layout_reminder_memtask', 
    image='images/layout_reminder_memtask.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
instr_memtask5 = visual.TextStim(win=win, name='instr_memtask5',
    text='If you are ready to begin, press the RIGHT arrow key.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_instr_memtask = keyboard.Keyboard()

# Initialize components for Routine "memtask"
memtaskClock = core.Clock()
memtask_word = visual.TextStim(win=win, name='memtask_word',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
resp_memtask = keyboard.Keyboard()
memtask_layout_reminder = visual.ImageStim(
    win=win,
    name='memtask_layout_reminder', units='deg', 
    image='images/layout_reminder_memtask.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "instr_LDT"
instr_LDTClock = core.Clock()
instr_LDT1 = visual.TextStim(win=win, name='instr_LDT1',
    text='In this task, you will see a selection of real words and nonsense words.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_LDT2 = visual.TextStim(win=win, name='instr_LDT2',
    text='You will see a real word or a nonsense word quickly followed by a string of "&" symbols\n',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_LDT3 = visual.TextStim(win=win, name='instr_LDT3',
    text='Upon seeing the "&" symbols, you should decide as quickly as possible whether you saw a real word or nonsense word',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_LDT4 = visual.TextStim(win=win, name='instr_LDT4',
    text='If you think you saw a real word, press the RIGHT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_LDT5 = visual.TextStim(win=win, name='instr_LDT5',
    text='If you think you saw a nonsense word, press the LEFT arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_LDT6 = visual.TextStim(win=win, name='instr_LDT6',
    text='Please make sure your fingers are in the correct place',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='images/keyboard_diagram.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
keyboard_reminder_LDT = visual.ImageStim(
    win=win,
    name='keyboard_reminder_LDT', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
instr_LDT7 = visual.TextStim(win=win, name='instr_LDT7',
    text='The words may be difficult to see, but please do the best you can',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_LT8 = visual.TextStim(win=win, name='instr_LT8',
    text="Let's do a practice round",
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
instr_LDT9_ = visual.TextStim(win=win, name='instr_LDT9_',
    text='When you are ready to begin, press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
key_resp_LDT_instr = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
LDT_fix_cross = visual.ImageStim(
    win=win,
    name='LDT_fix_cross', 
    image='images/crosshair.png', mask=None,
    ori=0, pos=(0, 0), size=[.05,.05],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "LDT_prac"
LDT_pracClock = core.Clock()
LDT_word_prac = visual.TextStim(win=win, name='LDT_word_prac',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
LDT_mask_prac = visual.TextStim(win=win, name='LDT_mask_prac',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_LDT_prac = keyboard.Keyboard()
key_reminder_3 = visual.ImageStim(
    win=win,
    name='key_reminder_3', units='deg', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "instr_LDT_2"
instr_LDT_2Clock = core.Clock()
instr_LDT9 = visual.TextStim(win=win, name='instr_LDT9',
    text='Great job!',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_LDT10 = visual.TextStim(win=win, name='instr_LDT10',
    text='Remember that LEFT is nonsense word and RIGHT is real word.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr_LDT11 = visual.TextStim(win=win, name='instr_LDT11',
    text='If you are ready to begin, please press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
resp_LDT_ready = keyboard.Keyboard()

# Initialize components for Routine "fix"
fixClock = core.Clock()
LDT_fix_cross = visual.ImageStim(
    win=win,
    name='LDT_fix_cross', 
    image='images/crosshair.png', mask=None,
    ori=0, pos=(0, 0), size=[.05,.05],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "LDT_trial"
LDT_trialClock = core.Clock()
LDT_word_trial = visual.TextStim(win=win, name='LDT_word_trial',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
LDT_mask_trial = visual.TextStim(win=win, name='LDT_mask_trial',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
resp_LDT_trial = keyboard.Keyboard()
key_reminder = visual.ImageStim(
    win=win,
    name='key_reminder', units='deg', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "LDT_feedback"
LDT_feedbackClock = core.Clock()
LDT_rating = visual.RatingScale(win=win, name='LDT_rating', scale = "To what extent did you respond randomly in this task?",
choices=None, 
low=1, 
high=7, 
pos=[0,0],
precision=1, 
labels=["Not at all","Somewhat","Completely"], 
tickMarks=None, 
showValue=False,
showAccept=True,
acceptPreText='Click a value', 
acceptText='Accept?', 
acceptSize=1.0,
tickHeight=1.0, 
marker='slider',
markerStart=4, 
textSize=1.0,
stretch = 1.5, 
textColor='Black', 
textFont='Helvetica Bold',
disappear=True)
LDT_feedback_inst = visual.TextStim(win=win, name='LDT_feedback_inst',
    text='You will now respond to a question. Please note that your response to this question is completely anonymous and will not affect your SONA credit in any way.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
instr_end = visual.TextStim(win=win, name='instr_end',
    text='Thank you for participating. You will now respond to a short survey.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "hold"-------
# update component parameters for each repeat
begin_key.keys = []
begin_key.rt = []
# keep track of which components have finished
holdComponents = [text, begin_key]
for thisComponent in holdComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
holdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "hold"-------
while continueRoutine:
    # get current time
    t = holdClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=holdClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *begin_key* updates
    waitOnFlip = False
    if begin_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin_key.frameNStart = frameN  # exact frame index
        begin_key.tStart = t  # local t and not account for scr refresh
        begin_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin_key, 'tStartRefresh')  # time at next scr refresh
        begin_key.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin_key.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin_key.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin_key.status == STARTED and not waitOnFlip:
        theseKeys = begin_key.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            begin_key.keys = theseKeys.name  # just the last key pressed
            begin_key.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in holdComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hold"-------
for thisComponent in holdComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if begin_key.keys in ['', [], None]:  # No response was made
    begin_key.keys = None
thisExp.addData('begin_key.keys',begin_key.keys)
if begin_key.keys != None:  # we had a response
    thisExp.addData('begin_key.rt', begin_key.rt)
thisExp.addData('begin_key.started', begin_key.tStartRefresh)
thisExp.addData('begin_key.stopped', begin_key.tStopRefresh)
thisExp.nextEntry()
# the Routine "hold" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_main"-------
# update component parameters for each repeat
key_resp_instr.keys = []
key_resp_instr.rt = []
# keep track of which components have finished
instr_mainComponents = [instr_2, instr_3, instr_4, instr_5, instr_6, position_reminder, instr_7, key_resp_instr]
for thisComponent in instr_mainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_main"-------
while continueRoutine:
    # get current time
    t = instr_mainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_mainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_2* updates
    if instr_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.tStart = t  # local t and not account for scr refresh
        instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_2, 'tStartRefresh')  # time at next scr refresh
        instr_2.setAutoDraw(True)
    if instr_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_2.tStop = t  # not accounting for scr refresh
            instr_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_2, 'tStopRefresh')  # time at next scr refresh
            instr_2.setAutoDraw(False)
    
    # *instr_3* updates
    if instr_3.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.tStart = t  # local t and not account for scr refresh
        instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_3, 'tStartRefresh')  # time at next scr refresh
        instr_3.setAutoDraw(True)
    if instr_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_3.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_3.tStop = t  # not accounting for scr refresh
            instr_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_3, 'tStopRefresh')  # time at next scr refresh
            instr_3.setAutoDraw(False)
    
    # *instr_4* updates
    if instr_4.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        instr_4.frameNStart = frameN  # exact frame index
        instr_4.tStart = t  # local t and not account for scr refresh
        instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_4, 'tStartRefresh')  # time at next scr refresh
        instr_4.setAutoDraw(True)
    if instr_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_4.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_4.tStop = t  # not accounting for scr refresh
            instr_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_4, 'tStopRefresh')  # time at next scr refresh
            instr_4.setAutoDraw(False)
    
    # *instr_5* updates
    if instr_5.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
        # keep track of start time/frame for later
        instr_5.frameNStart = frameN  # exact frame index
        instr_5.tStart = t  # local t and not account for scr refresh
        instr_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_5, 'tStartRefresh')  # time at next scr refresh
        instr_5.setAutoDraw(True)
    if instr_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_5.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_5.tStop = t  # not accounting for scr refresh
            instr_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_5, 'tStopRefresh')  # time at next scr refresh
            instr_5.setAutoDraw(False)
    
    # *instr_6* updates
    if instr_6.status == NOT_STARTED and tThisFlip >= 24-frameTolerance:
        # keep track of start time/frame for later
        instr_6.frameNStart = frameN  # exact frame index
        instr_6.tStart = t  # local t and not account for scr refresh
        instr_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_6, 'tStartRefresh')  # time at next scr refresh
        instr_6.setAutoDraw(True)
    if instr_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_6.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            instr_6.tStop = t  # not accounting for scr refresh
            instr_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_6, 'tStopRefresh')  # time at next scr refresh
            instr_6.setAutoDraw(False)
    
    # *position_reminder* updates
    if position_reminder.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
        # keep track of start time/frame for later
        position_reminder.frameNStart = frameN  # exact frame index
        position_reminder.tStart = t  # local t and not account for scr refresh
        position_reminder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(position_reminder, 'tStartRefresh')  # time at next scr refresh
        position_reminder.setAutoDraw(True)
    if position_reminder.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > position_reminder.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            position_reminder.tStop = t  # not accounting for scr refresh
            position_reminder.frameNStop = frameN  # exact frame index
            win.timeOnFlip(position_reminder, 'tStopRefresh')  # time at next scr refresh
            position_reminder.setAutoDraw(False)
    
    # *instr_7* updates
    if instr_7.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
        # keep track of start time/frame for later
        instr_7.frameNStart = frameN  # exact frame index
        instr_7.tStart = t  # local t and not account for scr refresh
        instr_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_7, 'tStartRefresh')  # time at next scr refresh
        instr_7.setAutoDraw(True)
    
    # *key_resp_instr* updates
    waitOnFlip = False
    if key_resp_instr.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr.frameNStart = frameN  # exact frame index
        key_resp_instr.tStart = t  # local t and not account for scr refresh
        key_resp_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr.getKeys(keyList=['right', 'esc'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr.keys = theseKeys.name  # just the last key pressed
            key_resp_instr.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:         continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_mainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_main"-------
for thisComponent in instr_mainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_2.started', instr_2.tStartRefresh)
thisExp.addData('instr_2.stopped', instr_2.tStopRefresh)
thisExp.addData('instr_3.started', instr_3.tStartRefresh)
thisExp.addData('instr_3.stopped', instr_3.tStopRefresh)
thisExp.addData('instr_4.started', instr_4.tStartRefresh)
thisExp.addData('instr_4.stopped', instr_4.tStopRefresh)
thisExp.addData('instr_5.started', instr_5.tStartRefresh)
thisExp.addData('instr_5.stopped', instr_5.tStopRefresh)
thisExp.addData('instr_6.started', instr_6.tStartRefresh)
thisExp.addData('instr_6.stopped', instr_6.tStopRefresh)
thisExp.addData('position_reminder.started', position_reminder.tStartRefresh)
thisExp.addData('position_reminder.stopped', position_reminder.tStopRefresh)
thisExp.addData('instr_7.started', instr_7.tStartRefresh)
thisExp.addData('instr_7.stopped', instr_7.tStopRefresh)
# check responses
if key_resp_instr.keys in ['', [], None]:  # No response was made
    key_resp_instr.keys = None
thisExp.addData('key_resp_instr.keys',key_resp_instr.keys)
if key_resp_instr.keys != None:  # we had a response
    thisExp.addData('key_resp_instr.rt', key_resp_instr.rt)
thisExp.addData('key_resp_instr.started', key_resp_instr.tStartRefresh)
thisExp.addData('key_resp_instr.stopped', key_resp_instr.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('exp_time', globalClock.getTime())
# the Routine "instr_main" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LDT_trials_cond2 = data.TrialHandler(nReps=int(expInfo['participant ID']) % 2 == 1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LDT_trials_cond2')
thisExp.addLoop(LDT_trials_cond2)  # add the loop to the experiment
thisLDT_trials_cond2 = LDT_trials_cond2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLDT_trials_cond2.rgb)
if thisLDT_trials_cond2 != None:
    for paramName in thisLDT_trials_cond2:
        exec('{} = thisLDT_trials_cond2[paramName]'.format(paramName))

for thisLDT_trials_cond2 in LDT_trials_cond2:
    currentLoop = LDT_trials_cond2
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_trials_cond2.rgb)
    if thisLDT_trials_cond2 != None:
        for paramName in thisLDT_trials_cond2:
            exec('{} = thisLDT_trials_cond2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr_LDT"-------
    # update component parameters for each repeat
    key_resp_LDT_instr.keys = []
    key_resp_LDT_instr.rt = []
    # keep track of which components have finished
    instr_LDTComponents = [instr_LDT1, instr_LDT2, instr_LDT3, instr_LDT4, instr_LDT5, instr_LDT6, image_3, keyboard_reminder_LDT, instr_LDT7, instr_LT8, instr_LDT9_, key_resp_LDT_instr]
    for thisComponent in instr_LDTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr_LDTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instr_LDT"-------
    while continueRoutine:
        # get current time
        t = instr_LDTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr_LDTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_LDT1* updates
        if instr_LDT1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT1.frameNStart = frameN  # exact frame index
            instr_LDT1.tStart = t  # local t and not account for scr refresh
            instr_LDT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT1, 'tStartRefresh')  # time at next scr refresh
            instr_LDT1.setAutoDraw(True)
        if instr_LDT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT1.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT1.tStop = t  # not accounting for scr refresh
                instr_LDT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT1, 'tStopRefresh')  # time at next scr refresh
                instr_LDT1.setAutoDraw(False)
        
        # *instr_LDT2* updates
        if instr_LDT2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT2.frameNStart = frameN  # exact frame index
            instr_LDT2.tStart = t  # local t and not account for scr refresh
            instr_LDT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT2, 'tStartRefresh')  # time at next scr refresh
            instr_LDT2.setAutoDraw(True)
        if instr_LDT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT2.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT2.tStop = t  # not accounting for scr refresh
                instr_LDT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT2, 'tStopRefresh')  # time at next scr refresh
                instr_LDT2.setAutoDraw(False)
        
        # *instr_LDT3* updates
        if instr_LDT3.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT3.frameNStart = frameN  # exact frame index
            instr_LDT3.tStart = t  # local t and not account for scr refresh
            instr_LDT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT3, 'tStartRefresh')  # time at next scr refresh
            instr_LDT3.setAutoDraw(True)
        if instr_LDT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT3.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT3.tStop = t  # not accounting for scr refresh
                instr_LDT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT3, 'tStopRefresh')  # time at next scr refresh
                instr_LDT3.setAutoDraw(False)
        
        # *instr_LDT4* updates
        if instr_LDT4.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT4.frameNStart = frameN  # exact frame index
            instr_LDT4.tStart = t  # local t and not account for scr refresh
            instr_LDT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT4, 'tStartRefresh')  # time at next scr refresh
            instr_LDT4.setAutoDraw(True)
        if instr_LDT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT4.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT4.tStop = t  # not accounting for scr refresh
                instr_LDT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT4, 'tStopRefresh')  # time at next scr refresh
                instr_LDT4.setAutoDraw(False)
        
        # *instr_LDT5* updates
        if instr_LDT5.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT5.frameNStart = frameN  # exact frame index
            instr_LDT5.tStart = t  # local t and not account for scr refresh
            instr_LDT5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT5, 'tStartRefresh')  # time at next scr refresh
            instr_LDT5.setAutoDraw(True)
        if instr_LDT5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT5.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT5.tStop = t  # not accounting for scr refresh
                instr_LDT5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT5, 'tStopRefresh')  # time at next scr refresh
                instr_LDT5.setAutoDraw(False)
        
        # *instr_LDT6* updates
        if instr_LDT6.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT6.frameNStart = frameN  # exact frame index
            instr_LDT6.tStart = t  # local t and not account for scr refresh
            instr_LDT6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT6, 'tStartRefresh')  # time at next scr refresh
            instr_LDT6.setAutoDraw(True)
        if instr_LDT6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT6.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT6.tStop = t  # not accounting for scr refresh
                instr_LDT6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT6, 'tStopRefresh')  # time at next scr refresh
                instr_LDT6.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *keyboard_reminder_LDT* updates
        if keyboard_reminder_LDT.status == NOT_STARTED and tThisFlip >= 42-frameTolerance:
            # keep track of start time/frame for later
            keyboard_reminder_LDT.frameNStart = frameN  # exact frame index
            keyboard_reminder_LDT.tStart = t  # local t and not account for scr refresh
            keyboard_reminder_LDT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboard_reminder_LDT, 'tStartRefresh')  # time at next scr refresh
            keyboard_reminder_LDT.setAutoDraw(True)
        if keyboard_reminder_LDT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyboard_reminder_LDT.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                keyboard_reminder_LDT.tStop = t  # not accounting for scr refresh
                keyboard_reminder_LDT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyboard_reminder_LDT, 'tStopRefresh')  # time at next scr refresh
                keyboard_reminder_LDT.setAutoDraw(False)
        
        # *instr_LDT7* updates
        if instr_LDT7.status == NOT_STARTED and tThisFlip >= 46-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT7.frameNStart = frameN  # exact frame index
            instr_LDT7.tStart = t  # local t and not account for scr refresh
            instr_LDT7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT7, 'tStartRefresh')  # time at next scr refresh
            instr_LDT7.setAutoDraw(True)
        if instr_LDT7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT7.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT7.tStop = t  # not accounting for scr refresh
                instr_LDT7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT7, 'tStopRefresh')  # time at next scr refresh
                instr_LDT7.setAutoDraw(False)
        
        # *instr_LT8* updates
        if instr_LT8.status == NOT_STARTED and tThisFlip >= 52-frameTolerance:
            # keep track of start time/frame for later
            instr_LT8.frameNStart = frameN  # exact frame index
            instr_LT8.tStart = t  # local t and not account for scr refresh
            instr_LT8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LT8, 'tStartRefresh')  # time at next scr refresh
            instr_LT8.setAutoDraw(True)
        if instr_LT8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LT8.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                instr_LT8.tStop = t  # not accounting for scr refresh
                instr_LT8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LT8, 'tStopRefresh')  # time at next scr refresh
                instr_LT8.setAutoDraw(False)
        
        # *instr_LDT9_* updates
        if instr_LDT9_.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT9_.frameNStart = frameN  # exact frame index
            instr_LDT9_.tStart = t  # local t and not account for scr refresh
            instr_LDT9_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT9_, 'tStartRefresh')  # time at next scr refresh
            instr_LDT9_.setAutoDraw(True)
        
        # *key_resp_LDT_instr* updates
        waitOnFlip = False
        if key_resp_LDT_instr.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            key_resp_LDT_instr.frameNStart = frameN  # exact frame index
            key_resp_LDT_instr.tStart = t  # local t and not account for scr refresh
            key_resp_LDT_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_LDT_instr, 'tStartRefresh')  # time at next scr refresh
            key_resp_LDT_instr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_LDT_instr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_LDT_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_LDT_instr.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_LDT_instr.getKeys(keyList=['right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_LDT_instr.keys = theseKeys.name  # just the last key pressed
                key_resp_LDT_instr.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_LDTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_LDT"-------
    for thisComponent in instr_LDTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LDT_trials_cond2.addData('instr_LDT1.started', instr_LDT1.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT1.stopped', instr_LDT1.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT2.started', instr_LDT2.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT2.stopped', instr_LDT2.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT3.started', instr_LDT3.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT3.stopped', instr_LDT3.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT4.started', instr_LDT4.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT4.stopped', instr_LDT4.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT5.started', instr_LDT5.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT5.stopped', instr_LDT5.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT6.started', instr_LDT6.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT6.stopped', instr_LDT6.tStopRefresh)
    LDT_trials_cond2.addData('image_3.started', image_3.tStartRefresh)
    LDT_trials_cond2.addData('image_3.stopped', image_3.tStopRefresh)
    LDT_trials_cond2.addData('keyboard_reminder_LDT.started', keyboard_reminder_LDT.tStartRefresh)
    LDT_trials_cond2.addData('keyboard_reminder_LDT.stopped', keyboard_reminder_LDT.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT7.started', instr_LDT7.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT7.stopped', instr_LDT7.tStopRefresh)
    LDT_trials_cond2.addData('instr_LT8.started', instr_LT8.tStartRefresh)
    LDT_trials_cond2.addData('instr_LT8.stopped', instr_LT8.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT9_.started', instr_LDT9_.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT9_.stopped', instr_LDT9_.tStopRefresh)
    # check responses
    if key_resp_LDT_instr.keys in ['', [], None]:  # No response was made
        key_resp_LDT_instr.keys = None
    LDT_trials_cond2.addData('key_resp_LDT_instr.keys',key_resp_LDT_instr.keys)
    if key_resp_LDT_instr.keys != None:  # we had a response
        LDT_trials_cond2.addData('key_resp_LDT_instr.rt', key_resp_LDT_instr.rt)
    LDT_trials_cond2.addData('key_resp_LDT_instr.started', key_resp_LDT_instr.tStartRefresh)
    LDT_trials_cond2.addData('key_resp_LDT_instr.stopped', key_resp_LDT_instr.tStopRefresh)
    # the Routine "instr_LDT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LDT_pracs_1 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condition_files/ldt_testrun.csv'),
        seed=None, name='LDT_pracs_1')
    thisExp.addLoop(LDT_pracs_1)  # add the loop to the experiment
    thisLDT_prac_1 = LDT_pracs_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_prac_1.rgb)
    if thisLDT_prac_1 != None:
        for paramName in thisLDT_prac_1:
            exec('{} = thisLDT_prac_1[paramName]'.format(paramName))
    
    for thisLDT_prac_1 in LDT_pracs_1:
        currentLoop = LDT_pracs_1
        # abbreviate parameter names if possible (e.g. rgb = thisLDT_prac_1.rgb)
        if thisLDT_prac_1 != None:
            for paramName in thisLDT_prac_1:
                exec('{} = thisLDT_prac_1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix"-------
        # update component parameters for each repeat
        rand_duration = random.randint(6, 18)
        # keep track of which components have finished
        fixComponents = [LDT_fix_cross]
        for thisComponent in fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "fix"-------
        while continueRoutine:
            # get current time
            t = fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_fix_cross* updates
            if LDT_fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDT_fix_cross.frameNStart = frameN  # exact frame index
                LDT_fix_cross.tStart = t  # local t and not account for scr refresh
                LDT_fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_fix_cross, 'tStartRefresh')  # time at next scr refresh
                LDT_fix_cross.setAutoDraw(True)
            if LDT_fix_cross.status == STARTED:
                if frameN >= (LDT_fix_cross.frameNStart + rand_duration):
                    # keep track of stop time/frame for later
                    LDT_fix_cross.tStop = t  # not accounting for scr refresh
                    LDT_fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_fix_cross, 'tStopRefresh')  # time at next scr refresh
                    LDT_fix_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix"-------
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_pracs_1.addData('LDT_fix_cross.started', LDT_fix_cross.tStartRefresh)
        LDT_pracs_1.addData('LDT_fix_cross.stopped', LDT_fix_cross.tStopRefresh)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "LDT_prac"-------
        # update component parameters for each repeat
        LDT_word_prac.setText(words)
        LDT_mask_prac.setText(mask)
        resp_LDT_prac.keys = []
        resp_LDT_prac.rt = []
        keys = []
        ldt_dur = random.randint(1, 6)
        ldt_mask_dur = 2 * ldt_dur
        # keep track of which components have finished
        LDT_pracComponents = [LDT_word_prac, LDT_mask_prac, resp_LDT_prac, key_reminder_3]
        for thisComponent in LDT_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LDT_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "LDT_prac"-------
        while continueRoutine:
            # get current time
            t = LDT_pracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LDT_pracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_word_prac* updates
            if LDT_word_prac.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                LDT_word_prac.frameNStart = frameN  # exact frame index
                LDT_word_prac.tStart = t  # local t and not account for scr refresh
                LDT_word_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_word_prac, 'tStartRefresh')  # time at next scr refresh
                LDT_word_prac.setAutoDraw(True)
            if LDT_word_prac.status == STARTED:
                if frameN >= (LDT_word_prac.frameNStart + ldt_dur):
                    # keep track of stop time/frame for later
                    LDT_word_prac.tStop = t  # not accounting for scr refresh
                    LDT_word_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_word_prac, 'tStopRefresh')  # time at next scr refresh
                    LDT_word_prac.setAutoDraw(False)
            
            # *LDT_mask_prac* updates
            if LDT_mask_prac.status == NOT_STARTED and LDT_word_prac.status==FINISHED:
                # keep track of start time/frame for later
                LDT_mask_prac.frameNStart = frameN  # exact frame index
                LDT_mask_prac.tStart = t  # local t and not account for scr refresh
                LDT_mask_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_mask_prac, 'tStartRefresh')  # time at next scr refresh
                LDT_mask_prac.setAutoDraw(True)
            if LDT_mask_prac.status == STARTED:
                if frameN >= (LDT_mask_prac.frameNStart + ldt_mask_dur):
                    # keep track of stop time/frame for later
                    LDT_mask_prac.tStop = t  # not accounting for scr refresh
                    LDT_mask_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_mask_prac, 'tStopRefresh')  # time at next scr refresh
                    LDT_mask_prac.setAutoDraw(False)
            
            # *resp_LDT_prac* updates
            waitOnFlip = False
            if resp_LDT_prac.status == NOT_STARTED and frameN >= ldt_dur:
                # keep track of start time/frame for later
                resp_LDT_prac.frameNStart = frameN  # exact frame index
                resp_LDT_prac.tStart = t  # local t and not account for scr refresh
                resp_LDT_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_LDT_prac, 'tStartRefresh')  # time at next scr refresh
                resp_LDT_prac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_LDT_prac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_LDT_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_LDT_prac.status == STARTED and not waitOnFlip:
                theseKeys = resp_LDT_prac.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    resp_LDT_prac.keys = theseKeys.name  # just the last key pressed
                    resp_LDT_prac.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            keys = event.getKeys()
            if 'j' in keys:
                    continueRoutine = False
                    try:
                        LDT_pracs_1.finished = True
                    except:
                        LDT_pracs.finished = True
            
            # *key_reminder_3* updates
            if key_reminder_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_reminder_3.frameNStart = frameN  # exact frame index
                key_reminder_3.tStart = t  # local t and not account for scr refresh
                key_reminder_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_reminder_3, 'tStartRefresh')  # time at next scr refresh
                key_reminder_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDT_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "LDT_prac"-------
        for thisComponent in LDT_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_pracs_1.addData('LDT_word_prac.started', LDT_word_prac.tStartRefresh)
        LDT_pracs_1.addData('LDT_word_prac.stopped', LDT_word_prac.tStopRefresh)
        LDT_pracs_1.addData('LDT_mask_prac.started', LDT_mask_prac.tStartRefresh)
        LDT_pracs_1.addData('LDT_mask_prac.stopped', LDT_mask_prac.tStopRefresh)
        # check responses
        if resp_LDT_prac.keys in ['', [], None]:  # No response was made
            resp_LDT_prac.keys = None
        LDT_pracs_1.addData('resp_LDT_prac.keys',resp_LDT_prac.keys)
        if resp_LDT_prac.keys != None:  # we had a response
            LDT_pracs_1.addData('resp_LDT_prac.rt', resp_LDT_prac.rt)
        LDT_pracs_1.addData('resp_LDT_prac.started', resp_LDT_prac.tStartRefresh)
        LDT_pracs_1.addData('resp_LDT_prac.stopped', resp_LDT_prac.tStopRefresh)
        thisExp.addData('task', "LDT_prac")
        thisExp.addData('keypress', resp_LDT_prac.keys)
        thisExp.addData('LDT_dur', ldt_dur)
        thisExp.addData('RT', resp_LDT_prac.rt)
        thisExp.addData('corr', resp_LDT_prac.corr)
        thisExp.addData('exp_time', globalClock.getTime())
        
        LDT_pracs_1.addData('key_reminder_3.started', key_reminder_3.tStartRefresh)
        LDT_pracs_1.addData('key_reminder_3.stopped', key_reminder_3.tStopRefresh)
        # the Routine "LDT_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'LDT_pracs_1'
    
    
    # ------Prepare to start Routine "instr_LDT_2"-------
    # update component parameters for each repeat
    resp_LDT_ready.keys = []
    resp_LDT_ready.rt = []
    keys = []
    # keep track of which components have finished
    instr_LDT_2Components = [instr_LDT9, instr_LDT10, image_6, instr_LDT11, resp_LDT_ready]
    for thisComponent in instr_LDT_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr_LDT_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instr_LDT_2"-------
    while continueRoutine:
        # get current time
        t = instr_LDT_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr_LDT_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_LDT9* updates
        if instr_LDT9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT9.frameNStart = frameN  # exact frame index
            instr_LDT9.tStart = t  # local t and not account for scr refresh
            instr_LDT9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT9, 'tStartRefresh')  # time at next scr refresh
            instr_LDT9.setAutoDraw(True)
        if instr_LDT9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT9.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT9.tStop = t  # not accounting for scr refresh
                instr_LDT9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT9, 'tStopRefresh')  # time at next scr refresh
                instr_LDT9.setAutoDraw(False)
        
        # *instr_LDT10* updates
        if instr_LDT10.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT10.frameNStart = frameN  # exact frame index
            instr_LDT10.tStart = t  # local t and not account for scr refresh
            instr_LDT10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT10, 'tStartRefresh')  # time at next scr refresh
            instr_LDT10.setAutoDraw(True)
        if instr_LDT10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT10.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT10.tStop = t  # not accounting for scr refresh
                instr_LDT10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT10, 'tStopRefresh')  # time at next scr refresh
                instr_LDT10.setAutoDraw(False)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            image_6.setAutoDraw(True)
        if image_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_6.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                image_6.tStop = t  # not accounting for scr refresh
                image_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
                image_6.setAutoDraw(False)
        
        # *instr_LDT11* updates
        if instr_LDT11.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT11.frameNStart = frameN  # exact frame index
            instr_LDT11.tStart = t  # local t and not account for scr refresh
            instr_LDT11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT11, 'tStartRefresh')  # time at next scr refresh
            instr_LDT11.setAutoDraw(True)
        
        # *resp_LDT_ready* updates
        waitOnFlip = False
        if resp_LDT_ready.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
            # keep track of start time/frame for later
            resp_LDT_ready.frameNStart = frameN  # exact frame index
            resp_LDT_ready.tStart = t  # local t and not account for scr refresh
            resp_LDT_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_LDT_ready, 'tStartRefresh')  # time at next scr refresh
            resp_LDT_ready.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_LDT_ready.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_LDT_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_LDT_ready.status == STARTED and not waitOnFlip:
            theseKeys = resp_LDT_ready.getKeys(keyList=['right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp_LDT_ready.keys = theseKeys.name  # just the last key pressed
                resp_LDT_ready.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_LDT_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_LDT_2"-------
    for thisComponent in instr_LDT_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LDT_trials_cond2.addData('instr_LDT9.started', instr_LDT9.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT9.stopped', instr_LDT9.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT10.started', instr_LDT10.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT10.stopped', instr_LDT10.tStopRefresh)
    LDT_trials_cond2.addData('image_6.started', image_6.tStartRefresh)
    LDT_trials_cond2.addData('image_6.stopped', image_6.tStopRefresh)
    LDT_trials_cond2.addData('instr_LDT11.started', instr_LDT11.tStartRefresh)
    LDT_trials_cond2.addData('instr_LDT11.stopped', instr_LDT11.tStopRefresh)
    # check responses
    if resp_LDT_ready.keys in ['', [], None]:  # No response was made
        resp_LDT_ready.keys = None
    LDT_trials_cond2.addData('resp_LDT_ready.keys',resp_LDT_ready.keys)
    if resp_LDT_ready.keys != None:  # we had a response
        LDT_trials_cond2.addData('resp_LDT_ready.rt', resp_LDT_ready.rt)
    LDT_trials_cond2.addData('resp_LDT_ready.started', resp_LDT_ready.tStartRefresh)
    LDT_trials_cond2.addData('resp_LDT_ready.stopped', resp_LDT_ready.tStopRefresh)
    # the Routine "instr_LDT_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LDT_trials_1 = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condition_files/LDT_conditions.csv'),
        seed=None, name='LDT_trials_1')
    thisExp.addLoop(LDT_trials_1)  # add the loop to the experiment
    thisLDT_trial_1 = LDT_trials_1.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_trial_1.rgb)
    if thisLDT_trial_1 != None:
        for paramName in thisLDT_trial_1:
            exec('{} = thisLDT_trial_1[paramName]'.format(paramName))
    
    for thisLDT_trial_1 in LDT_trials_1:
        currentLoop = LDT_trials_1
        # abbreviate parameter names if possible (e.g. rgb = thisLDT_trial_1.rgb)
        if thisLDT_trial_1 != None:
            for paramName in thisLDT_trial_1:
                exec('{} = thisLDT_trial_1[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix"-------
        # update component parameters for each repeat
        rand_duration = random.randint(6, 18)
        # keep track of which components have finished
        fixComponents = [LDT_fix_cross]
        for thisComponent in fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "fix"-------
        while continueRoutine:
            # get current time
            t = fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_fix_cross* updates
            if LDT_fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDT_fix_cross.frameNStart = frameN  # exact frame index
                LDT_fix_cross.tStart = t  # local t and not account for scr refresh
                LDT_fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_fix_cross, 'tStartRefresh')  # time at next scr refresh
                LDT_fix_cross.setAutoDraw(True)
            if LDT_fix_cross.status == STARTED:
                if frameN >= (LDT_fix_cross.frameNStart + rand_duration):
                    # keep track of stop time/frame for later
                    LDT_fix_cross.tStop = t  # not accounting for scr refresh
                    LDT_fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_fix_cross, 'tStopRefresh')  # time at next scr refresh
                    LDT_fix_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix"-------
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_trials_1.addData('LDT_fix_cross.started', LDT_fix_cross.tStartRefresh)
        LDT_trials_1.addData('LDT_fix_cross.stopped', LDT_fix_cross.tStopRefresh)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "LDT_trial"-------
        # update component parameters for each repeat
        LDT_word_trial.setText(words)
        LDT_mask_trial.setText(mask)
        resp_LDT_trial.keys = []
        resp_LDT_trial.rt = []
        keys = []
        ldt_dur = random.randint(1, 6)
        # keep track of which components have finished
        LDT_trialComponents = [LDT_word_trial, LDT_mask_trial, resp_LDT_trial, key_reminder]
        for thisComponent in LDT_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LDT_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "LDT_trial"-------
        while continueRoutine:
            # get current time
            t = LDT_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LDT_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_word_trial* updates
            if LDT_word_trial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                LDT_word_trial.frameNStart = frameN  # exact frame index
                LDT_word_trial.tStart = t  # local t and not account for scr refresh
                LDT_word_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_word_trial, 'tStartRefresh')  # time at next scr refresh
                LDT_word_trial.setAutoDraw(True)
            if LDT_word_trial.status == STARTED:
                if frameN >= (LDT_word_trial.frameNStart + ldt_dur):
                    # keep track of stop time/frame for later
                    LDT_word_trial.tStop = t  # not accounting for scr refresh
                    LDT_word_trial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_word_trial, 'tStopRefresh')  # time at next scr refresh
                    LDT_word_trial.setAutoDraw(False)
            
            # *LDT_mask_trial* updates
            if LDT_mask_trial.status == NOT_STARTED and frameN >= LDT_word_trial.status==FINISHED:
                # keep track of start time/frame for later
                LDT_mask_trial.frameNStart = frameN  # exact frame index
                LDT_mask_trial.tStart = t  # local t and not account for scr refresh
                LDT_mask_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_mask_trial, 'tStartRefresh')  # time at next scr refresh
                LDT_mask_trial.setAutoDraw(True)
            
            # *resp_LDT_trial* updates
            waitOnFlip = False
            if resp_LDT_trial.status == NOT_STARTED and frameN >= ldt_dur:
                # keep track of start time/frame for later
                resp_LDT_trial.frameNStart = frameN  # exact frame index
                resp_LDT_trial.tStart = t  # local t and not account for scr refresh
                resp_LDT_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_LDT_trial, 'tStartRefresh')  # time at next scr refresh
                resp_LDT_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_LDT_trial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_LDT_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_LDT_trial.status == STARTED and not waitOnFlip:
                theseKeys = resp_LDT_trial.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    resp_LDT_trial.keys = theseKeys.name  # just the last key pressed
                    resp_LDT_trial.rt = theseKeys.rt
                    # was this 'correct'?
                    if (resp_LDT_trial.keys == str(corr_ans)) or (resp_LDT_trial.keys == corr_ans):
                        resp_LDT_trial.corr = 1
                    else:
                        resp_LDT_trial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            keys = event.getKeys()
            if 'j' in keys:
                    continueRoutine = False
                    try:
                        LDT_trials_1.finished = True
                    except: 
                        LDT_trials.finished = True 
            
            # *key_reminder* updates
            if key_reminder.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_reminder.frameNStart = frameN  # exact frame index
                key_reminder.tStart = t  # local t and not account for scr refresh
                key_reminder.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_reminder, 'tStartRefresh')  # time at next scr refresh
                key_reminder.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDT_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "LDT_trial"-------
        for thisComponent in LDT_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_trials_1.addData('LDT_word_trial.started', LDT_word_trial.tStartRefresh)
        LDT_trials_1.addData('LDT_word_trial.stopped', LDT_word_trial.tStopRefresh)
        LDT_trials_1.addData('LDT_mask_trial.started', LDT_mask_trial.tStartRefresh)
        LDT_trials_1.addData('LDT_mask_trial.stopped', LDT_mask_trial.tStopRefresh)
        # check responses
        if resp_LDT_trial.keys in ['', [], None]:  # No response was made
            resp_LDT_trial.keys = None
            # was no response the correct answer?!
            if str(corr_ans).lower() == 'none':
               resp_LDT_trial.corr = 1;  # correct non-response
            else:
               resp_LDT_trial.corr = 0;  # failed to respond (incorrectly)
        # store data for LDT_trials_1 (TrialHandler)
        LDT_trials_1.addData('resp_LDT_trial.keys',resp_LDT_trial.keys)
        LDT_trials_1.addData('resp_LDT_trial.corr', resp_LDT_trial.corr)
        if resp_LDT_trial.keys != None:  # we had a response
            LDT_trials_1.addData('resp_LDT_trial.rt', resp_LDT_trial.rt)
        LDT_trials_1.addData('resp_LDT_trial.started', resp_LDT_trial.tStartRefresh)
        LDT_trials_1.addData('resp_LDT_trial.stopped', resp_LDT_trial.tStopRefresh)
        thisExp.addData('task', "LDT")
        thisExp.addData('keypress', resp_LDT_trial.keys)
        thisExp.addData('LDT_dur', ldt_dur)
        thisExp.addData('RT', resp_LDT_trial.rt)
        thisExp.addData('corr', resp_LDT_trial.corr)
        thisExp.addData('exp_time', globalClock.getTime())
        LDT_trials_1.addData('key_reminder.started', key_reminder.tStartRefresh)
        LDT_trials_1.addData('key_reminder.stopped', key_reminder.tStopRefresh)
        # the Routine "LDT_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'LDT_trials_1'
    
    
    # ------Prepare to start Routine "LDT_feedback"-------
    # update component parameters for each repeat
    LDT_rating.reset()
    keys = []
    # keep track of which components have finished
    LDT_feedbackComponents = [LDT_rating, LDT_feedback_inst]
    for thisComponent in LDT_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    LDT_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "LDT_feedback"-------
    while continueRoutine:
        # get current time
        t = LDT_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=LDT_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *LDT_rating* updates
        if LDT_rating.status == NOT_STARTED and t >= 10-frameTolerance:
            # keep track of start time/frame for later
            LDT_rating.frameNStart = frameN  # exact frame index
            LDT_rating.tStart = t  # local t and not account for scr refresh
            LDT_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDT_rating, 'tStartRefresh')  # time at next scr refresh
            LDT_rating.setAutoDraw(True)
        
        # *LDT_feedback_inst* updates
        if LDT_feedback_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDT_feedback_inst.frameNStart = frameN  # exact frame index
            LDT_feedback_inst.tStart = t  # local t and not account for scr refresh
            LDT_feedback_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDT_feedback_inst, 'tStartRefresh')  # time at next scr refresh
            LDT_feedback_inst.setAutoDraw(True)
        if LDT_feedback_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LDT_feedback_inst.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                LDT_feedback_inst.tStop = t  # not accounting for scr refresh
                LDT_feedback_inst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LDT_feedback_inst, 'tStopRefresh')  # time at next scr refresh
                LDT_feedback_inst.setAutoDraw(False)
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDT_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "LDT_feedback"-------
    for thisComponent in LDT_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for LDT_trials_cond2 (TrialHandler)
    LDT_trials_cond2.addData('LDT_rating.response', LDT_rating.getRating())
    LDT_trials_cond2.addData('LDT_rating.rt', LDT_rating.getRT())
    LDT_trials_cond2.addData('LDT_rating.started', LDT_rating.tStart)
    LDT_trials_cond2.addData('LDT_rating.stopped', LDT_rating.tStop)
    LDT_trials_cond2.addData('LDT_feedback_inst.started', LDT_feedback_inst.tStartRefresh)
    LDT_trials_cond2.addData('LDT_feedback_inst.stopped', LDT_feedback_inst.tStopRefresh)
    thisExp.addData("task", "LDT_feedback")
    # the Routine "LDT_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed int(expInfo['participant ID']) % 2 == 1 repeats of 'LDT_trials_cond2'


# ------Prepare to start Routine "instr_symbol"-------
# update component parameters for each repeat
resp_sym_rate.keys = []
resp_sym_rate.rt = []
keys = []
# keep track of which components have finished
instr_symbolComponents = [instr_sym1, instr_sym2, instr_sym3, instr_sym4, instr_sym5, logo_example, instr_sym6, logo_prac_layout_reminder, instr_sym7, instr_sym8, resp_sym_rate]
for thisComponent in instr_symbolComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_symbolClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_symbol"-------
while continueRoutine:
    # get current time
    t = instr_symbolClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_symbolClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_sym1* updates
    if instr_sym1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_sym1.frameNStart = frameN  # exact frame index
        instr_sym1.tStart = t  # local t and not account for scr refresh
        instr_sym1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym1, 'tStartRefresh')  # time at next scr refresh
        instr_sym1.setAutoDraw(True)
    if instr_sym1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym1.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym1.tStop = t  # not accounting for scr refresh
            instr_sym1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym1, 'tStopRefresh')  # time at next scr refresh
            instr_sym1.setAutoDraw(False)
    
    # *instr_sym2* updates
    if instr_sym2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        instr_sym2.frameNStart = frameN  # exact frame index
        instr_sym2.tStart = t  # local t and not account for scr refresh
        instr_sym2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym2, 'tStartRefresh')  # time at next scr refresh
        instr_sym2.setAutoDraw(True)
    if instr_sym2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym2.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym2.tStop = t  # not accounting for scr refresh
            instr_sym2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym2, 'tStopRefresh')  # time at next scr refresh
            instr_sym2.setAutoDraw(False)
    
    # *instr_sym3* updates
    if instr_sym3.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        instr_sym3.frameNStart = frameN  # exact frame index
        instr_sym3.tStart = t  # local t and not account for scr refresh
        instr_sym3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym3, 'tStartRefresh')  # time at next scr refresh
        instr_sym3.setAutoDraw(True)
    if instr_sym3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym3.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym3.tStop = t  # not accounting for scr refresh
            instr_sym3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym3, 'tStopRefresh')  # time at next scr refresh
            instr_sym3.setAutoDraw(False)
    
    # *instr_sym4* updates
    if instr_sym4.status == NOT_STARTED and tThisFlip >= 22-frameTolerance:
        # keep track of start time/frame for later
        instr_sym4.frameNStart = frameN  # exact frame index
        instr_sym4.tStart = t  # local t and not account for scr refresh
        instr_sym4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym4, 'tStartRefresh')  # time at next scr refresh
        instr_sym4.setAutoDraw(True)
    if instr_sym4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym4.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym4.tStop = t  # not accounting for scr refresh
            instr_sym4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym4, 'tStopRefresh')  # time at next scr refresh
            instr_sym4.setAutoDraw(False)
    
    # *instr_sym5* updates
    if instr_sym5.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
        # keep track of start time/frame for later
        instr_sym5.frameNStart = frameN  # exact frame index
        instr_sym5.tStart = t  # local t and not account for scr refresh
        instr_sym5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym5, 'tStartRefresh')  # time at next scr refresh
        instr_sym5.setAutoDraw(True)
    if instr_sym5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym5.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym5.tStop = t  # not accounting for scr refresh
            instr_sym5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym5, 'tStopRefresh')  # time at next scr refresh
            instr_sym5.setAutoDraw(False)
    
    # *logo_example* updates
    if logo_example.status == NOT_STARTED and tThisFlip >= 34-frameTolerance:
        # keep track of start time/frame for later
        logo_example.frameNStart = frameN  # exact frame index
        logo_example.tStart = t  # local t and not account for scr refresh
        logo_example.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_example, 'tStartRefresh')  # time at next scr refresh
        logo_example.setAutoDraw(True)
    if logo_example.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > logo_example.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            logo_example.tStop = t  # not accounting for scr refresh
            logo_example.frameNStop = frameN  # exact frame index
            win.timeOnFlip(logo_example, 'tStopRefresh')  # time at next scr refresh
            logo_example.setAutoDraw(False)
    
    # *instr_sym6* updates
    if instr_sym6.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
        # keep track of start time/frame for later
        instr_sym6.frameNStart = frameN  # exact frame index
        instr_sym6.tStart = t  # local t and not account for scr refresh
        instr_sym6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym6, 'tStartRefresh')  # time at next scr refresh
        instr_sym6.setAutoDraw(True)
    if instr_sym6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym6.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym6.tStop = t  # not accounting for scr refresh
            instr_sym6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym6, 'tStopRefresh')  # time at next scr refresh
            instr_sym6.setAutoDraw(False)
    
    # *logo_prac_layout_reminder* updates
    if logo_prac_layout_reminder.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
        # keep track of start time/frame for later
        logo_prac_layout_reminder.frameNStart = frameN  # exact frame index
        logo_prac_layout_reminder.tStart = t  # local t and not account for scr refresh
        logo_prac_layout_reminder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(logo_prac_layout_reminder, 'tStartRefresh')  # time at next scr refresh
        logo_prac_layout_reminder.setAutoDraw(True)
    if logo_prac_layout_reminder.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > logo_prac_layout_reminder.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            logo_prac_layout_reminder.tStop = t  # not accounting for scr refresh
            logo_prac_layout_reminder.frameNStop = frameN  # exact frame index
            win.timeOnFlip(logo_prac_layout_reminder, 'tStopRefresh')  # time at next scr refresh
            logo_prac_layout_reminder.setAutoDraw(False)
    
    # *instr_sym7* updates
    if instr_sym7.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
        # keep track of start time/frame for later
        instr_sym7.frameNStart = frameN  # exact frame index
        instr_sym7.tStart = t  # local t and not account for scr refresh
        instr_sym7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym7, 'tStartRefresh')  # time at next scr refresh
        instr_sym7.setAutoDraw(True)
    if instr_sym7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym7.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym7.tStop = t  # not accounting for scr refresh
            instr_sym7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym7, 'tStopRefresh')  # time at next scr refresh
            instr_sym7.setAutoDraw(False)
    
    # *instr_sym8* updates
    if instr_sym8.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
        # keep track of start time/frame for later
        instr_sym8.frameNStart = frameN  # exact frame index
        instr_sym8.tStart = t  # local t and not account for scr refresh
        instr_sym8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym8, 'tStartRefresh')  # time at next scr refresh
        instr_sym8.setAutoDraw(True)
    
    # *resp_sym_rate* updates
    waitOnFlip = False
    if resp_sym_rate.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
        # keep track of start time/frame for later
        resp_sym_rate.frameNStart = frameN  # exact frame index
        resp_sym_rate.tStart = t  # local t and not account for scr refresh
        resp_sym_rate.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_sym_rate, 'tStartRefresh')  # time at next scr refresh
        resp_sym_rate.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_sym_rate.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_sym_rate.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_sym_rate.status == STARTED and not waitOnFlip:
        theseKeys = resp_sym_rate.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            resp_sym_rate.keys = theseKeys.name  # just the last key pressed
            resp_sym_rate.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_symbolComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_symbol"-------
for thisComponent in instr_symbolComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_sym1.started', instr_sym1.tStartRefresh)
thisExp.addData('instr_sym1.stopped', instr_sym1.tStopRefresh)
thisExp.addData('instr_sym2.started', instr_sym2.tStartRefresh)
thisExp.addData('instr_sym2.stopped', instr_sym2.tStopRefresh)
thisExp.addData('instr_sym3.started', instr_sym3.tStartRefresh)
thisExp.addData('instr_sym3.stopped', instr_sym3.tStopRefresh)
thisExp.addData('instr_sym4.started', instr_sym4.tStartRefresh)
thisExp.addData('instr_sym4.stopped', instr_sym4.tStopRefresh)
thisExp.addData('instr_sym5.started', instr_sym5.tStartRefresh)
thisExp.addData('instr_sym5.stopped', instr_sym5.tStopRefresh)
thisExp.addData('logo_example.started', logo_example.tStartRefresh)
thisExp.addData('logo_example.stopped', logo_example.tStopRefresh)
thisExp.addData('instr_sym6.started', instr_sym6.tStartRefresh)
thisExp.addData('instr_sym6.stopped', instr_sym6.tStopRefresh)
thisExp.addData('logo_prac_layout_reminder.started', logo_prac_layout_reminder.tStartRefresh)
thisExp.addData('logo_prac_layout_reminder.stopped', logo_prac_layout_reminder.tStopRefresh)
thisExp.addData('instr_sym7.started', instr_sym7.tStartRefresh)
thisExp.addData('instr_sym7.stopped', instr_sym7.tStopRefresh)
thisExp.addData('instr_sym8.started', instr_sym8.tStartRefresh)
thisExp.addData('instr_sym8.stopped', instr_sym8.tStopRefresh)
# check responses
if resp_sym_rate.keys in ['', [], None]:  # No response was made
    resp_sym_rate.keys = None
thisExp.addData('resp_sym_rate.keys',resp_sym_rate.keys)
if resp_sym_rate.keys != None:  # we had a response
    thisExp.addData('resp_sym_rate.rt', resp_sym_rate.rt)
thisExp.addData('resp_sym_rate.started', resp_sym_rate.tStartRefresh)
thisExp.addData('resp_sym_rate.stopped', resp_sym_rate.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('exp_time', globalClock.getTime())
# the Routine "instr_symbol" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "symbol_prac"-------
# update component parameters for each repeat
sym_resp_1.keys = []
sym_resp_1.rt = []
# keep track of which components have finished
symbol_pracComponents = [img_logo_prac, mask_logo_prac, key_reminder_logo_prac, sym_resp_1]
for thisComponent in symbol_pracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
symbol_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "symbol_prac"-------
while continueRoutine:
    # get current time
    t = symbol_pracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=symbol_pracClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *img_logo_prac* updates
    if img_logo_prac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_logo_prac.frameNStart = frameN  # exact frame index
        img_logo_prac.tStart = t  # local t and not account for scr refresh
        img_logo_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_logo_prac, 'tStartRefresh')  # time at next scr refresh
        img_logo_prac.setAutoDraw(True)
    if img_logo_prac.status == STARTED:
        if frameN >= (img_logo_prac.frameNStart + 30):
            # keep track of stop time/frame for later
            img_logo_prac.tStop = t  # not accounting for scr refresh
            img_logo_prac.frameNStop = frameN  # exact frame index
            win.timeOnFlip(img_logo_prac, 'tStopRefresh')  # time at next scr refresh
            img_logo_prac.setAutoDraw(False)
    
    # *mask_logo_prac* updates
    if mask_logo_prac.status == NOT_STARTED and frameN >= 31:
        # keep track of start time/frame for later
        mask_logo_prac.frameNStart = frameN  # exact frame index
        mask_logo_prac.tStart = t  # local t and not account for scr refresh
        mask_logo_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mask_logo_prac, 'tStartRefresh')  # time at next scr refresh
        mask_logo_prac.setAutoDraw(True)
    
    # *key_reminder_logo_prac* updates
    if key_reminder_logo_prac.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_reminder_logo_prac.frameNStart = frameN  # exact frame index
        key_reminder_logo_prac.tStart = t  # local t and not account for scr refresh
        key_reminder_logo_prac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_reminder_logo_prac, 'tStartRefresh')  # time at next scr refresh
        key_reminder_logo_prac.setAutoDraw(True)
    
    # *sym_resp_1* updates
    waitOnFlip = False
    if sym_resp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        sym_resp_1.frameNStart = frameN  # exact frame index
        sym_resp_1.tStart = t  # local t and not account for scr refresh
        sym_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sym_resp_1, 'tStartRefresh')  # time at next scr refresh
        sym_resp_1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sym_resp_1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sym_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sym_resp_1.status == STARTED and not waitOnFlip:
        theseKeys = sym_resp_1.getKeys(keyList=['left', 'right', 'escape', 'n'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            if sym_resp_1.keys == []:  # then this was the first keypress
                sym_resp_1.keys = theseKeys.name  # just the first key pressed
                sym_resp_1.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in symbol_pracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "symbol_prac"-------
for thisComponent in symbol_pracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('img_logo_prac.started', img_logo_prac.tStartRefresh)
thisExp.addData('img_logo_prac.stopped', img_logo_prac.tStopRefresh)
thisExp.addData('mask_logo_prac.started', mask_logo_prac.tStartRefresh)
thisExp.addData('mask_logo_prac.stopped', mask_logo_prac.tStopRefresh)
thisExp.addData('key_reminder_logo_prac.started', key_reminder_logo_prac.tStartRefresh)
thisExp.addData('key_reminder_logo_prac.stopped', key_reminder_logo_prac.tStopRefresh)
# check responses
if sym_resp_1.keys in ['', [], None]:  # No response was made
    sym_resp_1.keys = None
thisExp.addData('sym_resp_1.keys',sym_resp_1.keys)
if sym_resp_1.keys != None:  # we had a response
    thisExp.addData('sym_resp_1.rt', sym_resp_1.rt)
thisExp.addData('sym_resp_1.started', sym_resp_1.tStartRefresh)
thisExp.addData('sym_resp_1.stopped', sym_resp_1.tStopRefresh)
thisExp.nextEntry()
# the Routine "symbol_prac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_symbol2"-------
# update component parameters for each repeat
sym_resp_2.keys = []
sym_resp_2.rt = []
# keep track of which components have finished
instr_symbol2Components = [instr_sym9, instr_sym10, sym_layout_reminder, instr_sym11, sym_resp_2]
for thisComponent in instr_symbol2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_symbol2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_symbol2"-------
while continueRoutine:
    # get current time
    t = instr_symbol2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_symbol2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_sym9* updates
    if instr_sym9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_sym9.frameNStart = frameN  # exact frame index
        instr_sym9.tStart = t  # local t and not account for scr refresh
        instr_sym9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym9, 'tStartRefresh')  # time at next scr refresh
        instr_sym9.setAutoDraw(True)
    if instr_sym9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym9.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym9.tStop = t  # not accounting for scr refresh
            instr_sym9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym9, 'tStopRefresh')  # time at next scr refresh
            instr_sym9.setAutoDraw(False)
    
    # *instr_sym10* updates
    if instr_sym10.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        instr_sym10.frameNStart = frameN  # exact frame index
        instr_sym10.tStart = t  # local t and not account for scr refresh
        instr_sym10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym10, 'tStartRefresh')  # time at next scr refresh
        instr_sym10.setAutoDraw(True)
    if instr_sym10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_sym10.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_sym10.tStop = t  # not accounting for scr refresh
            instr_sym10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_sym10, 'tStopRefresh')  # time at next scr refresh
            instr_sym10.setAutoDraw(False)
    
    # *sym_layout_reminder* updates
    if sym_layout_reminder.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        sym_layout_reminder.frameNStart = frameN  # exact frame index
        sym_layout_reminder.tStart = t  # local t and not account for scr refresh
        sym_layout_reminder.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sym_layout_reminder, 'tStartRefresh')  # time at next scr refresh
        sym_layout_reminder.setAutoDraw(True)
    if sym_layout_reminder.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > sym_layout_reminder.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            sym_layout_reminder.tStop = t  # not accounting for scr refresh
            sym_layout_reminder.frameNStop = frameN  # exact frame index
            win.timeOnFlip(sym_layout_reminder, 'tStopRefresh')  # time at next scr refresh
            sym_layout_reminder.setAutoDraw(False)
    
    # *instr_sym11* updates
    if instr_sym11.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        instr_sym11.frameNStart = frameN  # exact frame index
        instr_sym11.tStart = t  # local t and not account for scr refresh
        instr_sym11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_sym11, 'tStartRefresh')  # time at next scr refresh
        instr_sym11.setAutoDraw(True)
    
    # *sym_resp_2* updates
    waitOnFlip = False
    if sym_resp_2.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        sym_resp_2.frameNStart = frameN  # exact frame index
        sym_resp_2.tStart = t  # local t and not account for scr refresh
        sym_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(sym_resp_2, 'tStartRefresh')  # time at next scr refresh
        sym_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(sym_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(sym_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if sym_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = sym_resp_2.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            sym_resp_2.keys = theseKeys.name  # just the last key pressed
            sym_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False  
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_symbol2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_symbol2"-------
for thisComponent in instr_symbol2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_sym9.started', instr_sym9.tStartRefresh)
thisExp.addData('instr_sym9.stopped', instr_sym9.tStopRefresh)
thisExp.addData('instr_sym10.started', instr_sym10.tStartRefresh)
thisExp.addData('instr_sym10.stopped', instr_sym10.tStopRefresh)
thisExp.addData('sym_layout_reminder.started', sym_layout_reminder.tStartRefresh)
thisExp.addData('sym_layout_reminder.stopped', sym_layout_reminder.tStopRefresh)
thisExp.addData('instr_sym11.started', instr_sym11.tStartRefresh)
thisExp.addData('instr_sym11.stopped', instr_sym11.tStopRefresh)
# check responses
if sym_resp_2.keys in ['', [], None]:  # No response was made
    sym_resp_2.keys = None
thisExp.addData('sym_resp_2.keys',sym_resp_2.keys)
if sym_resp_2.keys != None:  # we had a response
    thisExp.addData('sym_resp_2.rt', sym_resp_2.rt)
thisExp.addData('sym_resp_2.started', sym_resp_2.tStartRefresh)
thisExp.addData('sym_resp_2.stopped', sym_resp_2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('exp_time', globalClock.getTime())
# the Routine "instr_symbol2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
logo_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/symbols.csv'),
    seed=None, name='logo_trials')
thisExp.addLoop(logo_trials)  # add the loop to the experiment
thisLogo_trial = logo_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLogo_trial.rgb)
if thisLogo_trial != None:
    for paramName in thisLogo_trial:
        exec('{} = thisLogo_trial[paramName]'.format(paramName))

for thisLogo_trial in logo_trials:
    currentLoop = logo_trials
    # abbreviate parameter names if possible (e.g. rgb = thisLogo_trial.rgb)
    if thisLogo_trial != None:
        for paramName in thisLogo_trial:
            exec('{} = thisLogo_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "logo_trial"-------
    # update component parameters for each repeat
    img_logo_trial.setImage(symbol)
    sym_resp_trial.keys = []
    sym_resp_trial.rt = []
    keys = []
    sym_id = symbol.split("_")[1].split(".")[0]
    # keep track of which components have finished
    logo_trialComponents = [img_logo_trial, mask_logo_trial, key_reminder_logo_trial, sym_resp_trial]
    for thisComponent in logo_trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    logo_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "logo_trial"-------
    while continueRoutine:
        # get current time
        t = logo_trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=logo_trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_logo_trial* updates
        if img_logo_trial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_logo_trial.frameNStart = frameN  # exact frame index
            img_logo_trial.tStart = t  # local t and not account for scr refresh
            img_logo_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_logo_trial, 'tStartRefresh')  # time at next scr refresh
            img_logo_trial.setAutoDraw(True)
        if img_logo_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_logo_trial.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                img_logo_trial.tStop = t  # not accounting for scr refresh
                img_logo_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_logo_trial, 'tStopRefresh')  # time at next scr refresh
                img_logo_trial.setAutoDraw(False)
        
        # *mask_logo_trial* updates
        if mask_logo_trial.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            mask_logo_trial.frameNStart = frameN  # exact frame index
            mask_logo_trial.tStart = t  # local t and not account for scr refresh
            mask_logo_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask_logo_trial, 'tStartRefresh')  # time at next scr refresh
            mask_logo_trial.setAutoDraw(True)
        
        # *key_reminder_logo_trial* updates
        if key_reminder_logo_trial.status == NOT_STARTED and tThisFlip >= .0-frameTolerance:
            # keep track of start time/frame for later
            key_reminder_logo_trial.frameNStart = frameN  # exact frame index
            key_reminder_logo_trial.tStart = t  # local t and not account for scr refresh
            key_reminder_logo_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_reminder_logo_trial, 'tStartRefresh')  # time at next scr refresh
            key_reminder_logo_trial.setAutoDraw(True)
        
        # *sym_resp_trial* updates
        waitOnFlip = False
        if sym_resp_trial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            sym_resp_trial.frameNStart = frameN  # exact frame index
            sym_resp_trial.tStart = t  # local t and not account for scr refresh
            sym_resp_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sym_resp_trial, 'tStartRefresh')  # time at next scr refresh
            sym_resp_trial.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(sym_resp_trial.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(sym_resp_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if sym_resp_trial.status == STARTED and not waitOnFlip:
            theseKeys = sym_resp_trial.getKeys(keyList=['left', 'right', 'escape', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if sym_resp_trial.keys == []:  # then this was the first keypress
                    sym_resp_trial.keys = theseKeys.name  # just the first key pressed
                    sym_resp_trial.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False
                logo_trials.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in logo_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "logo_trial"-------
    for thisComponent in logo_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    logo_trials.addData('img_logo_trial.started', img_logo_trial.tStartRefresh)
    logo_trials.addData('img_logo_trial.stopped', img_logo_trial.tStopRefresh)
    logo_trials.addData('mask_logo_trial.started', mask_logo_trial.tStartRefresh)
    logo_trials.addData('mask_logo_trial.stopped', mask_logo_trial.tStopRefresh)
    logo_trials.addData('key_reminder_logo_trial.started', key_reminder_logo_trial.tStartRefresh)
    logo_trials.addData('key_reminder_logo_trial.stopped', key_reminder_logo_trial.tStopRefresh)
    # check responses
    if sym_resp_trial.keys in ['', [], None]:  # No response was made
        sym_resp_trial.keys = None
    logo_trials.addData('sym_resp_trial.keys',sym_resp_trial.keys)
    if sym_resp_trial.keys != None:  # we had a response
        logo_trials.addData('sym_resp_trial.rt', sym_resp_trial.rt)
    logo_trials.addData('sym_resp_trial.started', sym_resp_trial.tStartRefresh)
    logo_trials.addData('sym_resp_trial.stopped', sym_resp_trial.tStopRefresh)
    thisExp.addData('symbol_id', sym_id)
    thisExp.addData('keypress', sym_resp_trial.keys)
    thisExp.addData('RT', sym_resp_trial.rt)
    thisExp.addData('task', "symbols")
    # the Routine "logo_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'logo_trials'


# ------Prepare to start Routine "instr_AMP"-------
# update component parameters for each repeat
resp_AMP_ready1.keys = []
resp_AMP_ready1.rt = []
keys = []
# keep track of which components have finished
instr_AMPComponents = [instr_AMP1_1, instr_AMP1_2, instr_AMP1_3, instr_AMP1_4, instr_AMP1_5, instr_AMP1_6, image_4, instr_AMP1_7, instr_AMP1_8, instr_AMP1_9, instr_AMP1_10, resp_AMP_ready1]
for thisComponent in instr_AMPComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_AMPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_AMP"-------
while continueRoutine:
    # get current time
    t = instr_AMPClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_AMPClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_AMP1_1* updates
    if instr_AMP1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_1.frameNStart = frameN  # exact frame index
        instr_AMP1_1.tStart = t  # local t and not account for scr refresh
        instr_AMP1_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_1, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_1.setAutoDraw(True)
    if instr_AMP1_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_1.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_1.tStop = t  # not accounting for scr refresh
            instr_AMP1_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_1, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_1.setAutoDraw(False)
    
    # *instr_AMP1_2* updates
    if instr_AMP1_2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_2.frameNStart = frameN  # exact frame index
        instr_AMP1_2.tStart = t  # local t and not account for scr refresh
        instr_AMP1_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_2, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_2.setAutoDraw(True)
    if instr_AMP1_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_2.tStop = t  # not accounting for scr refresh
            instr_AMP1_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_2, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_2.setAutoDraw(False)
    
    # *instr_AMP1_3* updates
    if instr_AMP1_3.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_3.frameNStart = frameN  # exact frame index
        instr_AMP1_3.tStart = t  # local t and not account for scr refresh
        instr_AMP1_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_3, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_3.setAutoDraw(True)
    if instr_AMP1_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_3.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_3.tStop = t  # not accounting for scr refresh
            instr_AMP1_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_3, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_3.setAutoDraw(False)
    
    # *instr_AMP1_4* updates
    if instr_AMP1_4.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_4.frameNStart = frameN  # exact frame index
        instr_AMP1_4.tStart = t  # local t and not account for scr refresh
        instr_AMP1_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_4, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_4.setAutoDraw(True)
    if instr_AMP1_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_4.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_4.tStop = t  # not accounting for scr refresh
            instr_AMP1_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_4, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_4.setAutoDraw(False)
    
    # *instr_AMP1_5* updates
    if instr_AMP1_5.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_5.frameNStart = frameN  # exact frame index
        instr_AMP1_5.tStart = t  # local t and not account for scr refresh
        instr_AMP1_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_5, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_5.setAutoDraw(True)
    if instr_AMP1_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_5.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_5.tStop = t  # not accounting for scr refresh
            instr_AMP1_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_5, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_5.setAutoDraw(False)
    
    # *instr_AMP1_6* updates
    if instr_AMP1_6.status == NOT_STARTED and tThisFlip >= 34-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_6.frameNStart = frameN  # exact frame index
        instr_AMP1_6.tStart = t  # local t and not account for scr refresh
        instr_AMP1_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_6, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_6.setAutoDraw(True)
    if instr_AMP1_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_6.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_6.tStop = t  # not accounting for scr refresh
            instr_AMP1_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_6, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_6.setAutoDraw(False)
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 40-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    if image_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_4.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            image_4.tStop = t  # not accounting for scr refresh
            image_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
            image_4.setAutoDraw(False)
    
    # *instr_AMP1_7* updates
    if instr_AMP1_7.status == NOT_STARTED and tThisFlip >= 46-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_7.frameNStart = frameN  # exact frame index
        instr_AMP1_7.tStart = t  # local t and not account for scr refresh
        instr_AMP1_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_7, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_7.setAutoDraw(True)
    if instr_AMP1_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_7.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_7.tStop = t  # not accounting for scr refresh
            instr_AMP1_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_7, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_7.setAutoDraw(False)
    
    # *instr_AMP1_8* updates
    if instr_AMP1_8.status == NOT_STARTED and tThisFlip >= 52-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_8.frameNStart = frameN  # exact frame index
        instr_AMP1_8.tStart = t  # local t and not account for scr refresh
        instr_AMP1_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_8, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_8.setAutoDraw(True)
    if instr_AMP1_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_8.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_8.tStop = t  # not accounting for scr refresh
            instr_AMP1_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_8, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_8.setAutoDraw(False)
    
    # *instr_AMP1_9* updates
    if instr_AMP1_9.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_9.frameNStart = frameN  # exact frame index
        instr_AMP1_9.tStart = t  # local t and not account for scr refresh
        instr_AMP1_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_9, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_9.setAutoDraw(True)
    if instr_AMP1_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP1_9.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP1_9.tStop = t  # not accounting for scr refresh
            instr_AMP1_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP1_9, 'tStopRefresh')  # time at next scr refresh
            instr_AMP1_9.setAutoDraw(False)
    
    # *instr_AMP1_10* updates
    if instr_AMP1_10.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP1_10.frameNStart = frameN  # exact frame index
        instr_AMP1_10.tStart = t  # local t and not account for scr refresh
        instr_AMP1_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP1_10, 'tStartRefresh')  # time at next scr refresh
        instr_AMP1_10.setAutoDraw(True)
    
    # *resp_AMP_ready1* updates
    waitOnFlip = False
    if resp_AMP_ready1.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
        # keep track of start time/frame for later
        resp_AMP_ready1.frameNStart = frameN  # exact frame index
        resp_AMP_ready1.tStart = t  # local t and not account for scr refresh
        resp_AMP_ready1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_AMP_ready1, 'tStartRefresh')  # time at next scr refresh
        resp_AMP_ready1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_AMP_ready1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_AMP_ready1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_AMP_ready1.status == STARTED and not waitOnFlip:
        theseKeys = resp_AMP_ready1.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            resp_AMP_ready1.keys = theseKeys.name  # just the last key pressed
            resp_AMP_ready1.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_AMPComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_AMP"-------
for thisComponent in instr_AMPComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_AMP1_1.started', instr_AMP1_1.tStartRefresh)
thisExp.addData('instr_AMP1_1.stopped', instr_AMP1_1.tStopRefresh)
thisExp.addData('instr_AMP1_2.started', instr_AMP1_2.tStartRefresh)
thisExp.addData('instr_AMP1_2.stopped', instr_AMP1_2.tStopRefresh)
thisExp.addData('instr_AMP1_3.started', instr_AMP1_3.tStartRefresh)
thisExp.addData('instr_AMP1_3.stopped', instr_AMP1_3.tStopRefresh)
thisExp.addData('instr_AMP1_4.started', instr_AMP1_4.tStartRefresh)
thisExp.addData('instr_AMP1_4.stopped', instr_AMP1_4.tStopRefresh)
thisExp.addData('instr_AMP1_5.started', instr_AMP1_5.tStartRefresh)
thisExp.addData('instr_AMP1_5.stopped', instr_AMP1_5.tStopRefresh)
thisExp.addData('instr_AMP1_6.started', instr_AMP1_6.tStartRefresh)
thisExp.addData('instr_AMP1_6.stopped', instr_AMP1_6.tStopRefresh)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
thisExp.addData('instr_AMP1_7.started', instr_AMP1_7.tStartRefresh)
thisExp.addData('instr_AMP1_7.stopped', instr_AMP1_7.tStopRefresh)
thisExp.addData('instr_AMP1_8.started', instr_AMP1_8.tStartRefresh)
thisExp.addData('instr_AMP1_8.stopped', instr_AMP1_8.tStopRefresh)
thisExp.addData('instr_AMP1_9.started', instr_AMP1_9.tStartRefresh)
thisExp.addData('instr_AMP1_9.stopped', instr_AMP1_9.tStopRefresh)
thisExp.addData('instr_AMP1_10.started', instr_AMP1_10.tStartRefresh)
thisExp.addData('instr_AMP1_10.stopped', instr_AMP1_10.tStopRefresh)
# check responses
if resp_AMP_ready1.keys in ['', [], None]:  # No response was made
    resp_AMP_ready1.keys = None
thisExp.addData('resp_AMP_ready1.keys',resp_AMP_ready1.keys)
if resp_AMP_ready1.keys != None:  # we had a response
    thisExp.addData('resp_AMP_ready1.rt', resp_AMP_ready1.rt)
thisExp.addData('resp_AMP_ready1.started', resp_AMP_ready1.tStartRefresh)
thisExp.addData('resp_AMP_ready1.stopped', resp_AMP_ready1.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('exp_time', globalClock.getTime())
# the Routine "instr_AMP" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AMP_pracs = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/amp_testrun.csv'),
    seed=None, name='AMP_pracs')
thisExp.addLoop(AMP_pracs)  # add the loop to the experiment
thisAMP_prac = AMP_pracs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAMP_prac.rgb)
if thisAMP_prac != None:
    for paramName in thisAMP_prac:
        exec('{} = thisAMP_prac[paramName]'.format(paramName))

for thisAMP_prac in AMP_pracs:
    currentLoop = AMP_pracs
    # abbreviate parameter names if possible (e.g. rgb = thisAMP_prac.rgb)
    if thisAMP_prac != None:
        for paramName in thisAMP_prac:
            exec('{} = thisAMP_prac[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AMP_prime"-------
    # update component parameters for each repeat
    AMP_wordstim_2.setText(words)
    # keep track of which components have finished
    AMP_primeComponents = [AMP_wordstim_2, AMP_key_reminder_1]
    for thisComponent in AMP_primeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AMP_primeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "AMP_prime"-------
    while continueRoutine:
        # get current time
        t = AMP_primeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AMP_primeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AMP_wordstim_2* updates
        if AMP_wordstim_2.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            AMP_wordstim_2.frameNStart = frameN  # exact frame index
            AMP_wordstim_2.tStart = t  # local t and not account for scr refresh
            AMP_wordstim_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AMP_wordstim_2, 'tStartRefresh')  # time at next scr refresh
            AMP_wordstim_2.setAutoDraw(True)
        if AMP_wordstim_2.status == STARTED:
            if frameN >= (AMP_wordstim_2.frameNStart + prime_dur):
                # keep track of stop time/frame for later
                AMP_wordstim_2.tStop = t  # not accounting for scr refresh
                AMP_wordstim_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AMP_wordstim_2, 'tStopRefresh')  # time at next scr refresh
                AMP_wordstim_2.setAutoDraw(False)
        
        # *AMP_key_reminder_1* updates
        if AMP_key_reminder_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AMP_key_reminder_1.frameNStart = frameN  # exact frame index
            AMP_key_reminder_1.tStart = t  # local t and not account for scr refresh
            AMP_key_reminder_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AMP_key_reminder_1, 'tStartRefresh')  # time at next scr refresh
            AMP_key_reminder_1.setAutoDraw(True)
        if AMP_key_reminder_1.status == STARTED:
            if frameN >= (AMP_key_reminder_1.frameNStart + 12):
                # keep track of stop time/frame for later
                AMP_key_reminder_1.tStop = t  # not accounting for scr refresh
                AMP_key_reminder_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(AMP_key_reminder_1, 'tStopRefresh')  # time at next scr refresh
                AMP_key_reminder_1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AMP_primeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AMP_prime"-------
    for thisComponent in AMP_primeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AMP_pracs.addData('AMP_wordstim_2.started', AMP_wordstim_2.tStartRefresh)
    AMP_pracs.addData('AMP_wordstim_2.stopped', AMP_wordstim_2.tStopRefresh)
    AMP_pracs.addData('AMP_key_reminder_1.started', AMP_key_reminder_1.tStartRefresh)
    AMP_pracs.addData('AMP_key_reminder_1.stopped', AMP_key_reminder_1.tStopRefresh)
    # the Routine "AMP_prime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "AMP_target_prac"-------
    # update component parameters for each repeat
    img_logo_AMP.setImage(symbols)
    resp_AMP.keys = []
    resp_AMP.rt = []
    keys = []
    # keep track of which components have finished
    AMP_target_pracComponents = [img_logo_AMP, mask_AMP, AMP_key_reminder, resp_AMP]
    for thisComponent in AMP_target_pracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AMP_target_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "AMP_target_prac"-------
    while continueRoutine:
        # get current time
        t = AMP_target_pracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AMP_target_pracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_logo_AMP* updates
        if img_logo_AMP.status == NOT_STARTED and frameN >= 1:
            # keep track of start time/frame for later
            img_logo_AMP.frameNStart = frameN  # exact frame index
            img_logo_AMP.tStart = t  # local t and not account for scr refresh
            img_logo_AMP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_logo_AMP, 'tStartRefresh')  # time at next scr refresh
            img_logo_AMP.setAutoDraw(True)
        if img_logo_AMP.status == STARTED:
            if frameN >= (img_logo_AMP.frameNStart + 30):
                # keep track of stop time/frame for later
                img_logo_AMP.tStop = t  # not accounting for scr refresh
                img_logo_AMP.frameNStop = frameN  # exact frame index
                win.timeOnFlip(img_logo_AMP, 'tStopRefresh')  # time at next scr refresh
                img_logo_AMP.setAutoDraw(False)
        
        # *mask_AMP* updates
        if mask_AMP.status == NOT_STARTED and frameN >= 31:
            # keep track of start time/frame for later
            mask_AMP.frameNStart = frameN  # exact frame index
            mask_AMP.tStart = t  # local t and not account for scr refresh
            mask_AMP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mask_AMP, 'tStartRefresh')  # time at next scr refresh
            mask_AMP.setAutoDraw(True)
        
        # *AMP_key_reminder* updates
        if AMP_key_reminder.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            AMP_key_reminder.frameNStart = frameN  # exact frame index
            AMP_key_reminder.tStart = t  # local t and not account for scr refresh
            AMP_key_reminder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AMP_key_reminder, 'tStartRefresh')  # time at next scr refresh
            AMP_key_reminder.setAutoDraw(True)
        
        # *resp_AMP* updates
        waitOnFlip = False
        if resp_AMP.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            resp_AMP.frameNStart = frameN  # exact frame index
            resp_AMP.tStart = t  # local t and not account for scr refresh
            resp_AMP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_AMP, 'tStartRefresh')  # time at next scr refresh
            resp_AMP.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_AMP.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_AMP.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_AMP.status == STARTED and not waitOnFlip:
            theseKeys = resp_AMP.getKeys(keyList=['left', 'right', 'escape', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if resp_AMP.keys == []:  # then this was the first keypress
                    resp_AMP.keys = theseKeys.name  # just the first key pressed
                    resp_AMP.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False
                AMP_pracs.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AMP_target_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AMP_target_prac"-------
    for thisComponent in AMP_target_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    AMP_pracs.addData('img_logo_AMP.started', img_logo_AMP.tStartRefresh)
    AMP_pracs.addData('img_logo_AMP.stopped', img_logo_AMP.tStopRefresh)
    AMP_pracs.addData('mask_AMP.started', mask_AMP.tStartRefresh)
    AMP_pracs.addData('mask_AMP.stopped', mask_AMP.tStopRefresh)
    AMP_pracs.addData('AMP_key_reminder.started', AMP_key_reminder.tStartRefresh)
    AMP_pracs.addData('AMP_key_reminder.stopped', AMP_key_reminder.tStopRefresh)
    # check responses
    if resp_AMP.keys in ['', [], None]:  # No response was made
        resp_AMP.keys = None
    AMP_pracs.addData('resp_AMP.keys',resp_AMP.keys)
    if resp_AMP.keys != None:  # we had a response
        AMP_pracs.addData('resp_AMP.rt', resp_AMP.rt)
    AMP_pracs.addData('resp_AMP.started', resp_AMP.tStartRefresh)
    AMP_pracs.addData('resp_AMP.stopped', resp_AMP.tStopRefresh)
    thisExp.addData('task', "AMP_prac")
    thisExp.addData('keypress', resp_AMP.keys)
    thisExp.addData('RT', resp_AMP.rt)
    thisExp.addData('exp_time', globalClock.getTime())
    thisExp.addData('prime_dur', prime_dur)
    # the Routine "AMP_target_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'AMP_pracs'


# ------Prepare to start Routine "instr_AMP_2"-------
# update component parameters for each repeat
resp_AMP_ready.keys = []
resp_AMP_ready.rt = []
# keep track of which components have finished
instr_AMP_2Components = [instr_AMP2_1, instr_AMP2_2, image_5, instr_AMP2_3, resp_AMP_ready]
for thisComponent in instr_AMP_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_AMP_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_AMP_2"-------
while continueRoutine:
    # get current time
    t = instr_AMP_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_AMP_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_AMP2_1* updates
    if instr_AMP2_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP2_1.frameNStart = frameN  # exact frame index
        instr_AMP2_1.tStart = t  # local t and not account for scr refresh
        instr_AMP2_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP2_1, 'tStartRefresh')  # time at next scr refresh
        instr_AMP2_1.setAutoDraw(True)
    if instr_AMP2_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP2_1.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP2_1.tStop = t  # not accounting for scr refresh
            instr_AMP2_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP2_1, 'tStopRefresh')  # time at next scr refresh
            instr_AMP2_1.setAutoDraw(False)
    
    # *instr_AMP2_2* updates
    if instr_AMP2_2.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP2_2.frameNStart = frameN  # exact frame index
        instr_AMP2_2.tStart = t  # local t and not account for scr refresh
        instr_AMP2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP2_2, 'tStartRefresh')  # time at next scr refresh
        instr_AMP2_2.setAutoDraw(True)
    if instr_AMP2_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP2_2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP2_2.tStop = t  # not accounting for scr refresh
            instr_AMP2_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP2_2, 'tStopRefresh')  # time at next scr refresh
            instr_AMP2_2.setAutoDraw(False)
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_5.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            image_5.tStop = t  # not accounting for scr refresh
            image_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
            image_5.setAutoDraw(False)
    
    # *instr_AMP2_3* updates
    if instr_AMP2_3.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP2_3.frameNStart = frameN  # exact frame index
        instr_AMP2_3.tStart = t  # local t and not account for scr refresh
        instr_AMP2_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP2_3, 'tStartRefresh')  # time at next scr refresh
        instr_AMP2_3.setAutoDraw(True)
    
    # *resp_AMP_ready* updates
    waitOnFlip = False
    if resp_AMP_ready.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        resp_AMP_ready.frameNStart = frameN  # exact frame index
        resp_AMP_ready.tStart = t  # local t and not account for scr refresh
        resp_AMP_ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_AMP_ready, 'tStartRefresh')  # time at next scr refresh
        resp_AMP_ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp_AMP_ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp_AMP_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp_AMP_ready.status == STARTED and not waitOnFlip:
        theseKeys = resp_AMP_ready.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            resp_AMP_ready.keys = theseKeys.name  # just the last key pressed
            resp_AMP_ready.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False  
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_AMP_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_AMP_2"-------
for thisComponent in instr_AMP_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_AMP2_1.started', instr_AMP2_1.tStartRefresh)
thisExp.addData('instr_AMP2_1.stopped', instr_AMP2_1.tStopRefresh)
thisExp.addData('instr_AMP2_2.started', instr_AMP2_2.tStartRefresh)
thisExp.addData('instr_AMP2_2.stopped', instr_AMP2_2.tStopRefresh)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)
thisExp.addData('instr_AMP2_3.started', instr_AMP2_3.tStartRefresh)
thisExp.addData('instr_AMP2_3.stopped', instr_AMP2_3.tStopRefresh)
# check responses
if resp_AMP_ready.keys in ['', [], None]:  # No response was made
    resp_AMP_ready.keys = None
thisExp.addData('resp_AMP_ready.keys',resp_AMP_ready.keys)
if resp_AMP_ready.keys != None:  # we had a response
    thisExp.addData('resp_AMP_ready.rt', resp_AMP_ready.rt)
thisExp.addData('resp_AMP_ready.started', resp_AMP_ready.tStartRefresh)
thisExp.addData('resp_AMP_ready.stopped', resp_AMP_ready.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('exp_time', globalClock.getTime())
# the Routine "instr_AMP_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_AMP_3"-------
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
instr_AMP_3Components = [instr_AMP3_1]
for thisComponent in instr_AMP_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_AMP_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_AMP_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr_AMP_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_AMP_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_AMP3_1* updates
    if instr_AMP3_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_AMP3_1.frameNStart = frameN  # exact frame index
        instr_AMP3_1.tStart = t  # local t and not account for scr refresh
        instr_AMP3_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_AMP3_1, 'tStartRefresh')  # time at next scr refresh
        instr_AMP3_1.setAutoDraw(True)
    if instr_AMP3_1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_AMP3_1.tStartRefresh + 4-frameTolerance:
            # keep track of stop time/frame for later
            instr_AMP3_1.tStop = t  # not accounting for scr refresh
            instr_AMP3_1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_AMP3_1, 'tStopRefresh')  # time at next scr refresh
            instr_AMP3_1.setAutoDraw(False)
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_AMP_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_AMP_3"-------
for thisComponent in instr_AMP_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_AMP3_1.started', instr_AMP3_1.tStartRefresh)
thisExp.addData('instr_AMP3_1.stopped', instr_AMP3_1.tStopRefresh)
thisExp.addData('exp_time', globalClock.getTime())

# set up handler to look after randomisation of conditions etc
trials_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/AMP_reps.xlsx'),
    seed=None, name='trials_loop')
thisExp.addLoop(trials_loop)  # add the loop to the experiment
thisTrials_loop = trials_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
if thisTrials_loop != None:
    for paramName in thisTrials_loop:
        exec('{} = thisTrials_loop[paramName]'.format(paramName))

for thisTrials_loop in trials_loop:
    currentLoop = trials_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_loop.rgb)
    if thisTrials_loop != None:
        for paramName in thisTrials_loop:
            exec('{} = thisTrials_loop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    AMP_trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(conditionfile),
        seed=None, name='AMP_trials')
    thisExp.addLoop(AMP_trials)  # add the loop to the experiment
    thisAMP_trial = AMP_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAMP_trial.rgb)
    if thisAMP_trial != None:
        for paramName in thisAMP_trial:
            exec('{} = thisAMP_trial[paramName]'.format(paramName))
    
    for thisAMP_trial in AMP_trials:
        currentLoop = AMP_trials
        # abbreviate parameter names if possible (e.g. rgb = thisAMP_trial.rgb)
        if thisAMP_trial != None:
            for paramName in thisAMP_trial:
                exec('{} = thisAMP_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "AMP_prime"-------
        # update component parameters for each repeat
        AMP_wordstim_2.setText(words)
        # keep track of which components have finished
        AMP_primeComponents = [AMP_wordstim_2, AMP_key_reminder_1]
        for thisComponent in AMP_primeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AMP_primeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AMP_prime"-------
        while continueRoutine:
            # get current time
            t = AMP_primeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AMP_primeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *AMP_wordstim_2* updates
            if AMP_wordstim_2.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                AMP_wordstim_2.frameNStart = frameN  # exact frame index
                AMP_wordstim_2.tStart = t  # local t and not account for scr refresh
                AMP_wordstim_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AMP_wordstim_2, 'tStartRefresh')  # time at next scr refresh
                AMP_wordstim_2.setAutoDraw(True)
            if AMP_wordstim_2.status == STARTED:
                if frameN >= (AMP_wordstim_2.frameNStart + prime_dur):
                    # keep track of stop time/frame for later
                    AMP_wordstim_2.tStop = t  # not accounting for scr refresh
                    AMP_wordstim_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AMP_wordstim_2, 'tStopRefresh')  # time at next scr refresh
                    AMP_wordstim_2.setAutoDraw(False)
            
            # *AMP_key_reminder_1* updates
            if AMP_key_reminder_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                AMP_key_reminder_1.frameNStart = frameN  # exact frame index
                AMP_key_reminder_1.tStart = t  # local t and not account for scr refresh
                AMP_key_reminder_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AMP_key_reminder_1, 'tStartRefresh')  # time at next scr refresh
                AMP_key_reminder_1.setAutoDraw(True)
            if AMP_key_reminder_1.status == STARTED:
                if frameN >= (AMP_key_reminder_1.frameNStart + 12):
                    # keep track of stop time/frame for later
                    AMP_key_reminder_1.tStop = t  # not accounting for scr refresh
                    AMP_key_reminder_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(AMP_key_reminder_1, 'tStopRefresh')  # time at next scr refresh
                    AMP_key_reminder_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AMP_primeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AMP_prime"-------
        for thisComponent in AMP_primeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AMP_trials.addData('AMP_wordstim_2.started', AMP_wordstim_2.tStartRefresh)
        AMP_trials.addData('AMP_wordstim_2.stopped', AMP_wordstim_2.tStopRefresh)
        AMP_trials.addData('AMP_key_reminder_1.started', AMP_key_reminder_1.tStartRefresh)
        AMP_trials.addData('AMP_key_reminder_1.stopped', AMP_key_reminder_1.tStopRefresh)
        # the Routine "AMP_prime" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AMP_target_trials"-------
        # update component parameters for each repeat
        img_logo_AMP_trials.setImage(symbols)
        resp_AMP_trials.keys = []
        resp_AMP_trials.rt = []
        keys = []
        sym_id = symbols.split("_")[1].split(".")[0]
        # keep track of which components have finished
        AMP_target_trialsComponents = [img_logo_AMP_trials, mask_AMP_2, AMP_key_reminder_2, resp_AMP_trials]
        for thisComponent in AMP_target_trialsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AMP_target_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "AMP_target_trials"-------
        while continueRoutine:
            # get current time
            t = AMP_target_trialsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AMP_target_trialsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *img_logo_AMP_trials* updates
            if img_logo_AMP_trials.status == NOT_STARTED and frameN >= 1:
                # keep track of start time/frame for later
                img_logo_AMP_trials.frameNStart = frameN  # exact frame index
                img_logo_AMP_trials.tStart = t  # local t and not account for scr refresh
                img_logo_AMP_trials.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_logo_AMP_trials, 'tStartRefresh')  # time at next scr refresh
                img_logo_AMP_trials.setAutoDraw(True)
            if img_logo_AMP_trials.status == STARTED:
                if frameN >= (img_logo_AMP_trials.frameNStart + 30):
                    # keep track of stop time/frame for later
                    img_logo_AMP_trials.tStop = t  # not accounting for scr refresh
                    img_logo_AMP_trials.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(img_logo_AMP_trials, 'tStopRefresh')  # time at next scr refresh
                    img_logo_AMP_trials.setAutoDraw(False)
            
            # *mask_AMP_2* updates
            if mask_AMP_2.status == NOT_STARTED and frameN >= 31:
                # keep track of start time/frame for later
                mask_AMP_2.frameNStart = frameN  # exact frame index
                mask_AMP_2.tStart = t  # local t and not account for scr refresh
                mask_AMP_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mask_AMP_2, 'tStartRefresh')  # time at next scr refresh
                mask_AMP_2.setAutoDraw(True)
            
            # *AMP_key_reminder_2* updates
            if AMP_key_reminder_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                AMP_key_reminder_2.frameNStart = frameN  # exact frame index
                AMP_key_reminder_2.tStart = t  # local t and not account for scr refresh
                AMP_key_reminder_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(AMP_key_reminder_2, 'tStartRefresh')  # time at next scr refresh
                AMP_key_reminder_2.setAutoDraw(True)
            
            # *resp_AMP_trials* updates
            waitOnFlip = False
            if resp_AMP_trials.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                resp_AMP_trials.frameNStart = frameN  # exact frame index
                resp_AMP_trials.tStart = t  # local t and not account for scr refresh
                resp_AMP_trials.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_AMP_trials, 'tStartRefresh')  # time at next scr refresh
                resp_AMP_trials.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_AMP_trials.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_AMP_trials.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_AMP_trials.status == STARTED and not waitOnFlip:
                theseKeys = resp_AMP_trials.getKeys(keyList=['left', 'right', 'escape', 'n'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    if resp_AMP_trials.keys == []:  # then this was the first keypress
                        resp_AMP_trials.keys = theseKeys.name  # just the first key pressed
                        resp_AMP_trials.rt = theseKeys.rt
                        # a response ends the routine
                        continueRoutine = False
            keys = event.getKeys()
            if 'j' in keys:
                    continueRoutine = False
                    AMP_trials.finished = True
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AMP_target_trialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AMP_target_trials"-------
        for thisComponent in AMP_target_trialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        AMP_trials.addData('img_logo_AMP_trials.started', img_logo_AMP_trials.tStartRefresh)
        AMP_trials.addData('img_logo_AMP_trials.stopped', img_logo_AMP_trials.tStopRefresh)
        AMP_trials.addData('mask_AMP_2.started', mask_AMP_2.tStartRefresh)
        AMP_trials.addData('mask_AMP_2.stopped', mask_AMP_2.tStopRefresh)
        AMP_trials.addData('AMP_key_reminder_2.started', AMP_key_reminder_2.tStartRefresh)
        AMP_trials.addData('AMP_key_reminder_2.stopped', AMP_key_reminder_2.tStopRefresh)
        # check responses
        if resp_AMP_trials.keys in ['', [], None]:  # No response was made
            resp_AMP_trials.keys = None
        AMP_trials.addData('resp_AMP_trials.keys',resp_AMP_trials.keys)
        if resp_AMP_trials.keys != None:  # we had a response
            AMP_trials.addData('resp_AMP_trials.rt', resp_AMP_trials.rt)
        AMP_trials.addData('resp_AMP_trials.started', resp_AMP_trials.tStartRefresh)
        AMP_trials.addData('resp_AMP_trials.stopped', resp_AMP_trials.tStopRefresh)
        thisExp.addData('task', "AMP")
        thisExp.addData('symbol_id', sym_id)
        thisExp.addData('keypress', resp_AMP_trials.keys)
        thisExp.addData('RT', resp_AMP_trials.rt)
        thisExp.addData('exp_time', globalClock.getTime())
        thisExp.addData('prime_dur', prime_dur)
        # the Routine "AMP_target_trials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'AMP_trials'
    
    
    # ------Prepare to start Routine "rest"-------
    # update component parameters for each repeat
    rest_key_resp.keys = []
    rest_key_resp.rt = []
    # keep track of which components have finished
    restComponents = [rest_txt1, rest_key_resp]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "rest"-------
    while continueRoutine:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_txt1* updates
        if rest_txt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_txt1.frameNStart = frameN  # exact frame index
            rest_txt1.tStart = t  # local t and not account for scr refresh
            rest_txt1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_txt1, 'tStartRefresh')  # time at next scr refresh
            rest_txt1.setAutoDraw(True)
        
        # *rest_key_resp* updates
        waitOnFlip = False
        if rest_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_key_resp.frameNStart = frameN  # exact frame index
            rest_key_resp.tStart = t  # local t and not account for scr refresh
            rest_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_key_resp, 'tStartRefresh')  # time at next scr refresh
            rest_key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(rest_key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(rest_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if rest_key_resp.status == STARTED and not waitOnFlip:
            theseKeys = rest_key_resp.getKeys(keyList=['right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                rest_key_resp.keys = theseKeys.name  # just the last key pressed
                rest_key_resp.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_loop.addData('rest_txt1.started', rest_txt1.tStartRefresh)
    trials_loop.addData('rest_txt1.stopped', rest_txt1.tStopRefresh)
    # check responses
    if rest_key_resp.keys in ['', [], None]:  # No response was made
        rest_key_resp.keys = None
    trials_loop.addData('rest_key_resp.keys',rest_key_resp.keys)
    if rest_key_resp.keys != None:  # we had a response
        trials_loop.addData('rest_key_resp.rt', rest_key_resp.rt)
    trials_loop.addData('rest_key_resp.started', rest_key_resp.tStartRefresh)
    trials_loop.addData('rest_key_resp.stopped', rest_key_resp.tStopRefresh)
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_loop'


# ------Prepare to start Routine "AMP_feedback"-------
# update component parameters for each repeat
AMP_nonword_rating.reset()
AMP_word_rating.reset()
AMP_random_rating.reset()
keys = []
# keep track of which components have finished
AMP_feedbackComponents = [AMP_nonword_rating, AMP_word_rating, AMP_random_rating, AMP_feedback_instr]
for thisComponent in AMP_feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
AMP_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "AMP_feedback"-------
while continueRoutine:
    # get current time
    t = AMP_feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=AMP_feedbackClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *AMP_nonword_rating* updates
    if AMP_nonword_rating.status == NOT_STARTED and AMP_feedback_instr.status==FINISHED:
        # keep track of start time/frame for later
        AMP_nonword_rating.frameNStart = frameN  # exact frame index
        AMP_nonword_rating.tStart = t  # local t and not account for scr refresh
        AMP_nonword_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AMP_nonword_rating, 'tStartRefresh')  # time at next scr refresh
        AMP_nonword_rating.setAutoDraw(True)
    # *AMP_word_rating* updates
    if AMP_word_rating.status == NOT_STARTED and AMP_nonword_rating.status==FINISHED:
        # keep track of start time/frame for later
        AMP_word_rating.frameNStart = frameN  # exact frame index
        AMP_word_rating.tStart = t  # local t and not account for scr refresh
        AMP_word_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AMP_word_rating, 'tStartRefresh')  # time at next scr refresh
        AMP_word_rating.setAutoDraw(True)
    # *AMP_random_rating* updates
    if AMP_random_rating.status == NOT_STARTED and AMP_word_rating.status==FINISHED:
        # keep track of start time/frame for later
        AMP_random_rating.frameNStart = frameN  # exact frame index
        AMP_random_rating.tStart = t  # local t and not account for scr refresh
        AMP_random_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AMP_random_rating, 'tStartRefresh')  # time at next scr refresh
        AMP_random_rating.setAutoDraw(True)
    
    # *AMP_feedback_instr* updates
    if AMP_feedback_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        AMP_feedback_instr.frameNStart = frameN  # exact frame index
        AMP_feedback_instr.tStart = t  # local t and not account for scr refresh
        AMP_feedback_instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AMP_feedback_instr, 'tStartRefresh')  # time at next scr refresh
        AMP_feedback_instr.setAutoDraw(True)
    if AMP_feedback_instr.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > AMP_feedback_instr.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            AMP_feedback_instr.tStop = t  # not accounting for scr refresh
            AMP_feedback_instr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(AMP_feedback_instr, 'tStopRefresh')  # time at next scr refresh
            AMP_feedback_instr.setAutoDraw(False)
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in AMP_feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "AMP_feedback"-------
for thisComponent in AMP_feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('AMP_nonword_rating.response', AMP_nonword_rating.getRating())
thisExp.addData('AMP_nonword_rating.rt', AMP_nonword_rating.getRT())
thisExp.nextEntry()
thisExp.addData('AMP_nonword_rating.started', AMP_nonword_rating.tStart)
thisExp.addData('AMP_nonword_rating.stopped', AMP_nonword_rating.tStop)
# store data for thisExp (ExperimentHandler)
thisExp.addData('AMP_word_rating.response', AMP_word_rating.getRating())
thisExp.addData('AMP_word_rating.rt', AMP_word_rating.getRT())
thisExp.nextEntry()
thisExp.addData('AMP_word_rating.started', AMP_word_rating.tStart)
thisExp.addData('AMP_word_rating.stopped', AMP_word_rating.tStop)
# store data for thisExp (ExperimentHandler)
thisExp.addData('AMP_random_rating.response', AMP_random_rating.getRating())
thisExp.addData('AMP_random_rating.rt', AMP_random_rating.getRT())
thisExp.nextEntry()
thisExp.addData('AMP_random_rating.started', AMP_random_rating.tStart)
thisExp.addData('AMP_random_rating.stopped', AMP_random_rating.tStop)
thisExp.addData('AMP_feedback_instr.started', AMP_feedback_instr.tStartRefresh)
thisExp.addData('AMP_feedback_instr.stopped', AMP_feedback_instr.tStopRefresh)
thisExp.addData('task', "AMP_feedback")


# the Routine "AMP_feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_memtask"-------
# update component parameters for each repeat
key_resp_instr_memtask.keys = []
key_resp_instr_memtask.rt = []
# keep track of which components have finished
instr_memtaskComponents = [instr_memtask1, instr_memtask2, instr_memtask3, instr_memtask4, layout_reminder_memtask, instr_memtask5, key_resp_instr_memtask]
for thisComponent in instr_memtaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_memtaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instr_memtask"-------
while continueRoutine:
    # get current time
    t = instr_memtaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_memtaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_memtask1* updates
    if instr_memtask1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_memtask1.frameNStart = frameN  # exact frame index
        instr_memtask1.tStart = t  # local t and not account for scr refresh
        instr_memtask1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_memtask1, 'tStartRefresh')  # time at next scr refresh
        instr_memtask1.setAutoDraw(True)
    if instr_memtask1.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_memtask1.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            instr_memtask1.tStop = t  # not accounting for scr refresh
            instr_memtask1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_memtask1, 'tStopRefresh')  # time at next scr refresh
            instr_memtask1.setAutoDraw(False)
    
    # *instr_memtask2* updates
    if instr_memtask2.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
        # keep track of start time/frame for later
        instr_memtask2.frameNStart = frameN  # exact frame index
        instr_memtask2.tStart = t  # local t and not account for scr refresh
        instr_memtask2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_memtask2, 'tStartRefresh')  # time at next scr refresh
        instr_memtask2.setAutoDraw(True)
    if instr_memtask2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_memtask2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_memtask2.tStop = t  # not accounting for scr refresh
            instr_memtask2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_memtask2, 'tStopRefresh')  # time at next scr refresh
            instr_memtask2.setAutoDraw(False)
    
    # *instr_memtask3* updates
    if instr_memtask3.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
        # keep track of start time/frame for later
        instr_memtask3.frameNStart = frameN  # exact frame index
        instr_memtask3.tStart = t  # local t and not account for scr refresh
        instr_memtask3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_memtask3, 'tStartRefresh')  # time at next scr refresh
        instr_memtask3.setAutoDraw(True)
    if instr_memtask3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_memtask3.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_memtask3.tStop = t  # not accounting for scr refresh
            instr_memtask3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_memtask3, 'tStopRefresh')  # time at next scr refresh
            instr_memtask3.setAutoDraw(False)
    
    # *instr_memtask4* updates
    if instr_memtask4.status == NOT_STARTED and tThisFlip >= 22-frameTolerance:
        # keep track of start time/frame for later
        instr_memtask4.frameNStart = frameN  # exact frame index
        instr_memtask4.tStart = t  # local t and not account for scr refresh
        instr_memtask4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_memtask4, 'tStartRefresh')  # time at next scr refresh
        instr_memtask4.setAutoDraw(True)
    if instr_memtask4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_memtask4.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_memtask4.tStop = t  # not accounting for scr refresh
            instr_memtask4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_memtask4, 'tStopRefresh')  # time at next scr refresh
            instr_memtask4.setAutoDraw(False)
    
    # *layout_reminder_memtask* updates
    if layout_reminder_memtask.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
        # keep track of start time/frame for later
        layout_reminder_memtask.frameNStart = frameN  # exact frame index
        layout_reminder_memtask.tStart = t  # local t and not account for scr refresh
        layout_reminder_memtask.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(layout_reminder_memtask, 'tStartRefresh')  # time at next scr refresh
        layout_reminder_memtask.setAutoDraw(True)
    if layout_reminder_memtask.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > layout_reminder_memtask.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            layout_reminder_memtask.tStop = t  # not accounting for scr refresh
            layout_reminder_memtask.frameNStop = frameN  # exact frame index
            win.timeOnFlip(layout_reminder_memtask, 'tStopRefresh')  # time at next scr refresh
            layout_reminder_memtask.setAutoDraw(False)
    
    # *instr_memtask5* updates
    if instr_memtask5.status == NOT_STARTED and tThisFlip >= 34-frameTolerance:
        # keep track of start time/frame for later
        instr_memtask5.frameNStart = frameN  # exact frame index
        instr_memtask5.tStart = t  # local t and not account for scr refresh
        instr_memtask5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_memtask5, 'tStartRefresh')  # time at next scr refresh
        instr_memtask5.setAutoDraw(True)
    
    # *key_resp_instr_memtask* updates
    waitOnFlip = False
    if key_resp_instr_memtask.status == NOT_STARTED and tThisFlip >= 34-frameTolerance:
        # keep track of start time/frame for later
        key_resp_instr_memtask.frameNStart = frameN  # exact frame index
        key_resp_instr_memtask.tStart = t  # local t and not account for scr refresh
        key_resp_instr_memtask.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_instr_memtask, 'tStartRefresh')  # time at next scr refresh
        key_resp_instr_memtask.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_instr_memtask.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_instr_memtask.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_instr_memtask.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_instr_memtask.getKeys(keyList=['right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_instr_memtask.keys = theseKeys.name  # just the last key pressed
            key_resp_instr_memtask.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_memtaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_memtask"-------
for thisComponent in instr_memtaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_memtask1.started', instr_memtask1.tStartRefresh)
thisExp.addData('instr_memtask1.stopped', instr_memtask1.tStopRefresh)
thisExp.addData('instr_memtask2.started', instr_memtask2.tStartRefresh)
thisExp.addData('instr_memtask2.stopped', instr_memtask2.tStopRefresh)
thisExp.addData('instr_memtask3.started', instr_memtask3.tStartRefresh)
thisExp.addData('instr_memtask3.stopped', instr_memtask3.tStopRefresh)
thisExp.addData('instr_memtask4.started', instr_memtask4.tStartRefresh)
thisExp.addData('instr_memtask4.stopped', instr_memtask4.tStopRefresh)
thisExp.addData('layout_reminder_memtask.started', layout_reminder_memtask.tStartRefresh)
thisExp.addData('layout_reminder_memtask.stopped', layout_reminder_memtask.tStopRefresh)
thisExp.addData('instr_memtask5.started', instr_memtask5.tStartRefresh)
thisExp.addData('instr_memtask5.stopped', instr_memtask5.tStopRefresh)
# check responses
if key_resp_instr_memtask.keys in ['', [], None]:  # No response was made
    key_resp_instr_memtask.keys = None
thisExp.addData('key_resp_instr_memtask.keys',key_resp_instr_memtask.keys)
if key_resp_instr_memtask.keys != None:  # we had a response
    thisExp.addData('key_resp_instr_memtask.rt', key_resp_instr_memtask.rt)
thisExp.addData('key_resp_instr_memtask.started', key_resp_instr_memtask.tStartRefresh)
thisExp.addData('key_resp_instr_memtask.stopped', key_resp_instr_memtask.tStopRefresh)
thisExp.nextEntry()
# the Routine "instr_memtask" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
memtask_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/memtask_conditions.csv'),
    seed=None, name='memtask_trials')
thisExp.addLoop(memtask_trials)  # add the loop to the experiment
thisMemtask_trial = memtask_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMemtask_trial.rgb)
if thisMemtask_trial != None:
    for paramName in thisMemtask_trial:
        exec('{} = thisMemtask_trial[paramName]'.format(paramName))

for thisMemtask_trial in memtask_trials:
    currentLoop = memtask_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMemtask_trial.rgb)
    if thisMemtask_trial != None:
        for paramName in thisMemtask_trial:
            exec('{} = thisMemtask_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "memtask"-------
    # update component parameters for each repeat
    memtask_word.setText(words)
    resp_memtask.keys = []
    resp_memtask.rt = []
    keys = []
    
    # keep track of which components have finished
    memtaskComponents = [memtask_word, resp_memtask, memtask_layout_reminder]
    for thisComponent in memtaskComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    memtaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "memtask"-------
    while continueRoutine:
        # get current time
        t = memtaskClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=memtaskClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *memtask_word* updates
        if memtask_word.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            memtask_word.frameNStart = frameN  # exact frame index
            memtask_word.tStart = t  # local t and not account for scr refresh
            memtask_word.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memtask_word, 'tStartRefresh')  # time at next scr refresh
            memtask_word.setAutoDraw(True)
        
        # *resp_memtask* updates
        waitOnFlip = False
        if resp_memtask.status == NOT_STARTED and tThisFlip >= .1-frameTolerance:
            # keep track of start time/frame for later
            resp_memtask.frameNStart = frameN  # exact frame index
            resp_memtask.tStart = t  # local t and not account for scr refresh
            resp_memtask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_memtask, 'tStartRefresh')  # time at next scr refresh
            resp_memtask.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_memtask.clock.reset)  # t=0 on next screen flip
        if resp_memtask.status == STARTED and not waitOnFlip:
            theseKeys = resp_memtask.getKeys(keyList=['left', 'right', 'escape'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp_memtask.keys = theseKeys.name  # just the last key pressed
                resp_memtask.rt = theseKeys.rt
                # was this 'correct'?
                if (resp_memtask.keys == str(corr_ans)) or (resp_memtask.keys == corr_ans):
                    resp_memtask.corr = 1
                else:
                    resp_memtask.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *memtask_layout_reminder* updates
        if memtask_layout_reminder.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            memtask_layout_reminder.frameNStart = frameN  # exact frame index
            memtask_layout_reminder.tStart = t  # local t and not account for scr refresh
            memtask_layout_reminder.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memtask_layout_reminder, 'tStartRefresh')  # time at next scr refresh
            memtask_layout_reminder.setAutoDraw(True)
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
                memtask_trials.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memtaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "memtask"-------
    for thisComponent in memtaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    memtask_trials.addData('memtask_word.started', memtask_word.tStartRefresh)
    memtask_trials.addData('memtask_word.stopped', memtask_word.tStopRefresh)
    # check responses
    if resp_memtask.keys in ['', [], None]:  # No response was made
        resp_memtask.keys = None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           resp_memtask.corr = 1;  # correct non-response
        else:
           resp_memtask.corr = 0;  # failed to respond (incorrectly)
    # store data for memtask_trials (TrialHandler)
    memtask_trials.addData('resp_memtask.keys',resp_memtask.keys)
    memtask_trials.addData('resp_memtask.corr', resp_memtask.corr)
    if resp_memtask.keys != None:  # we had a response
        memtask_trials.addData('resp_memtask.rt', resp_memtask.rt)
    memtask_trials.addData('resp_memtask.started', resp_memtask.tStartRefresh)
    memtask_trials.addData('resp_memtask.stopped', resp_memtask.tStopRefresh)
    memtask_trials.addData('memtask_layout_reminder.started', memtask_layout_reminder.tStartRefresh)
    memtask_trials.addData('memtask_layout_reminder.stopped', memtask_layout_reminder.tStopRefresh)
    thisExp.addData('task', "mem")
    thisExp.addData('keypress', resp_memtask.keys)
    thisExp.addData('RT', resp_memtask.rt)
    thisExp.addData('corr', resp_memtask.corr)
    # the Routine "memtask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'memtask_trials'


# set up handler to look after randomisation of conditions etc
LDT_cond1 = data.TrialHandler(nReps=int(expInfo['participant ID']) % 2 == 0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='LDT_cond1')
thisExp.addLoop(LDT_cond1)  # add the loop to the experiment
thisLDT_cond1 = LDT_cond1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLDT_cond1.rgb)
if thisLDT_cond1 != None:
    for paramName in thisLDT_cond1:
        exec('{} = thisLDT_cond1[paramName]'.format(paramName))

for thisLDT_cond1 in LDT_cond1:
    currentLoop = LDT_cond1
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_cond1.rgb)
    if thisLDT_cond1 != None:
        for paramName in thisLDT_cond1:
            exec('{} = thisLDT_cond1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instr_LDT"-------
    # update component parameters for each repeat
    key_resp_LDT_instr.keys = []
    key_resp_LDT_instr.rt = []
    # keep track of which components have finished
    instr_LDTComponents = [instr_LDT1, instr_LDT2, instr_LDT3, instr_LDT4, instr_LDT5, instr_LDT6, image_3, keyboard_reminder_LDT, instr_LDT7, instr_LT8, instr_LDT9_, key_resp_LDT_instr]
    for thisComponent in instr_LDTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr_LDTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instr_LDT"-------
    while continueRoutine:
        # get current time
        t = instr_LDTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr_LDTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_LDT1* updates
        if instr_LDT1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT1.frameNStart = frameN  # exact frame index
            instr_LDT1.tStart = t  # local t and not account for scr refresh
            instr_LDT1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT1, 'tStartRefresh')  # time at next scr refresh
            instr_LDT1.setAutoDraw(True)
        if instr_LDT1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT1.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT1.tStop = t  # not accounting for scr refresh
                instr_LDT1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT1, 'tStopRefresh')  # time at next scr refresh
                instr_LDT1.setAutoDraw(False)
        
        # *instr_LDT2* updates
        if instr_LDT2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT2.frameNStart = frameN  # exact frame index
            instr_LDT2.tStart = t  # local t and not account for scr refresh
            instr_LDT2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT2, 'tStartRefresh')  # time at next scr refresh
            instr_LDT2.setAutoDraw(True)
        if instr_LDT2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT2.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT2.tStop = t  # not accounting for scr refresh
                instr_LDT2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT2, 'tStopRefresh')  # time at next scr refresh
                instr_LDT2.setAutoDraw(False)
        
        # *instr_LDT3* updates
        if instr_LDT3.status == NOT_STARTED and tThisFlip >= 12-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT3.frameNStart = frameN  # exact frame index
            instr_LDT3.tStart = t  # local t and not account for scr refresh
            instr_LDT3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT3, 'tStartRefresh')  # time at next scr refresh
            instr_LDT3.setAutoDraw(True)
        if instr_LDT3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT3.tStartRefresh + 8-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT3.tStop = t  # not accounting for scr refresh
                instr_LDT3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT3, 'tStopRefresh')  # time at next scr refresh
                instr_LDT3.setAutoDraw(False)
        
        # *instr_LDT4* updates
        if instr_LDT4.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT4.frameNStart = frameN  # exact frame index
            instr_LDT4.tStart = t  # local t and not account for scr refresh
            instr_LDT4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT4, 'tStartRefresh')  # time at next scr refresh
            instr_LDT4.setAutoDraw(True)
        if instr_LDT4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT4.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT4.tStop = t  # not accounting for scr refresh
                instr_LDT4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT4, 'tStopRefresh')  # time at next scr refresh
                instr_LDT4.setAutoDraw(False)
        
        # *instr_LDT5* updates
        if instr_LDT5.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT5.frameNStart = frameN  # exact frame index
            instr_LDT5.tStart = t  # local t and not account for scr refresh
            instr_LDT5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT5, 'tStartRefresh')  # time at next scr refresh
            instr_LDT5.setAutoDraw(True)
        if instr_LDT5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT5.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT5.tStop = t  # not accounting for scr refresh
                instr_LDT5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT5, 'tStopRefresh')  # time at next scr refresh
                instr_LDT5.setAutoDraw(False)
        
        # *instr_LDT6* updates
        if instr_LDT6.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT6.frameNStart = frameN  # exact frame index
            instr_LDT6.tStart = t  # local t and not account for scr refresh
            instr_LDT6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT6, 'tStartRefresh')  # time at next scr refresh
            instr_LDT6.setAutoDraw(True)
        if instr_LDT6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT6.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT6.tStop = t  # not accounting for scr refresh
                instr_LDT6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT6, 'tStopRefresh')  # time at next scr refresh
                instr_LDT6.setAutoDraw(False)
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *keyboard_reminder_LDT* updates
        if keyboard_reminder_LDT.status == NOT_STARTED and tThisFlip >= 42-frameTolerance:
            # keep track of start time/frame for later
            keyboard_reminder_LDT.frameNStart = frameN  # exact frame index
            keyboard_reminder_LDT.tStart = t  # local t and not account for scr refresh
            keyboard_reminder_LDT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboard_reminder_LDT, 'tStartRefresh')  # time at next scr refresh
            keyboard_reminder_LDT.setAutoDraw(True)
        if keyboard_reminder_LDT.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyboard_reminder_LDT.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                keyboard_reminder_LDT.tStop = t  # not accounting for scr refresh
                keyboard_reminder_LDT.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyboard_reminder_LDT, 'tStopRefresh')  # time at next scr refresh
                keyboard_reminder_LDT.setAutoDraw(False)
        
        # *instr_LDT7* updates
        if instr_LDT7.status == NOT_STARTED and tThisFlip >= 46-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT7.frameNStart = frameN  # exact frame index
            instr_LDT7.tStart = t  # local t and not account for scr refresh
            instr_LDT7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT7, 'tStartRefresh')  # time at next scr refresh
            instr_LDT7.setAutoDraw(True)
        if instr_LDT7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT7.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT7.tStop = t  # not accounting for scr refresh
                instr_LDT7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT7, 'tStopRefresh')  # time at next scr refresh
                instr_LDT7.setAutoDraw(False)
        
        # *instr_LT8* updates
        if instr_LT8.status == NOT_STARTED and tThisFlip >= 52-frameTolerance:
            # keep track of start time/frame for later
            instr_LT8.frameNStart = frameN  # exact frame index
            instr_LT8.tStart = t  # local t and not account for scr refresh
            instr_LT8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LT8, 'tStartRefresh')  # time at next scr refresh
            instr_LT8.setAutoDraw(True)
        if instr_LT8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LT8.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                instr_LT8.tStop = t  # not accounting for scr refresh
                instr_LT8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LT8, 'tStopRefresh')  # time at next scr refresh
                instr_LT8.setAutoDraw(False)
        
        # *instr_LDT9_* updates
        if instr_LDT9_.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT9_.frameNStart = frameN  # exact frame index
            instr_LDT9_.tStart = t  # local t and not account for scr refresh
            instr_LDT9_.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT9_, 'tStartRefresh')  # time at next scr refresh
            instr_LDT9_.setAutoDraw(True)
        
        # *key_resp_LDT_instr* updates
        waitOnFlip = False
        if key_resp_LDT_instr.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            key_resp_LDT_instr.frameNStart = frameN  # exact frame index
            key_resp_LDT_instr.tStart = t  # local t and not account for scr refresh
            key_resp_LDT_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_LDT_instr, 'tStartRefresh')  # time at next scr refresh
            key_resp_LDT_instr.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_LDT_instr.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_LDT_instr.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_LDT_instr.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_LDT_instr.getKeys(keyList=['right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_LDT_instr.keys = theseKeys.name  # just the last key pressed
                key_resp_LDT_instr.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_LDTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_LDT"-------
    for thisComponent in instr_LDTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LDT_cond1.addData('instr_LDT1.started', instr_LDT1.tStartRefresh)
    LDT_cond1.addData('instr_LDT1.stopped', instr_LDT1.tStopRefresh)
    LDT_cond1.addData('instr_LDT2.started', instr_LDT2.tStartRefresh)
    LDT_cond1.addData('instr_LDT2.stopped', instr_LDT2.tStopRefresh)
    LDT_cond1.addData('instr_LDT3.started', instr_LDT3.tStartRefresh)
    LDT_cond1.addData('instr_LDT3.stopped', instr_LDT3.tStopRefresh)
    LDT_cond1.addData('instr_LDT4.started', instr_LDT4.tStartRefresh)
    LDT_cond1.addData('instr_LDT4.stopped', instr_LDT4.tStopRefresh)
    LDT_cond1.addData('instr_LDT5.started', instr_LDT5.tStartRefresh)
    LDT_cond1.addData('instr_LDT5.stopped', instr_LDT5.tStopRefresh)
    LDT_cond1.addData('instr_LDT6.started', instr_LDT6.tStartRefresh)
    LDT_cond1.addData('instr_LDT6.stopped', instr_LDT6.tStopRefresh)
    LDT_cond1.addData('image_3.started', image_3.tStartRefresh)
    LDT_cond1.addData('image_3.stopped', image_3.tStopRefresh)
    LDT_cond1.addData('keyboard_reminder_LDT.started', keyboard_reminder_LDT.tStartRefresh)
    LDT_cond1.addData('keyboard_reminder_LDT.stopped', keyboard_reminder_LDT.tStopRefresh)
    LDT_cond1.addData('instr_LDT7.started', instr_LDT7.tStartRefresh)
    LDT_cond1.addData('instr_LDT7.stopped', instr_LDT7.tStopRefresh)
    LDT_cond1.addData('instr_LT8.started', instr_LT8.tStartRefresh)
    LDT_cond1.addData('instr_LT8.stopped', instr_LT8.tStopRefresh)
    LDT_cond1.addData('instr_LDT9_.started', instr_LDT9_.tStartRefresh)
    LDT_cond1.addData('instr_LDT9_.stopped', instr_LDT9_.tStopRefresh)
    # check responses
    if key_resp_LDT_instr.keys in ['', [], None]:  # No response was made
        key_resp_LDT_instr.keys = None
    LDT_cond1.addData('key_resp_LDT_instr.keys',key_resp_LDT_instr.keys)
    if key_resp_LDT_instr.keys != None:  # we had a response
        LDT_cond1.addData('key_resp_LDT_instr.rt', key_resp_LDT_instr.rt)
    LDT_cond1.addData('key_resp_LDT_instr.started', key_resp_LDT_instr.tStartRefresh)
    LDT_cond1.addData('key_resp_LDT_instr.stopped', key_resp_LDT_instr.tStopRefresh)
    # the Routine "instr_LDT" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LDT_pracs = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condition_files/ldt_testrun.csv'),
        seed=None, name='LDT_pracs')
    thisExp.addLoop(LDT_pracs)  # add the loop to the experiment
    thisLDT_prac = LDT_pracs.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_prac.rgb)
    if thisLDT_prac != None:
        for paramName in thisLDT_prac:
            exec('{} = thisLDT_prac[paramName]'.format(paramName))
    
    for thisLDT_prac in LDT_pracs:
        currentLoop = LDT_pracs
        # abbreviate parameter names if possible (e.g. rgb = thisLDT_prac.rgb)
        if thisLDT_prac != None:
            for paramName in thisLDT_prac:
                exec('{} = thisLDT_prac[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix"-------
        # update component parameters for each repeat
        rand_duration = random.randint(6, 18)
        # keep track of which components have finished
        fixComponents = [LDT_fix_cross]
        for thisComponent in fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "fix"-------
        while continueRoutine:
            # get current time
            t = fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_fix_cross* updates
            if LDT_fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDT_fix_cross.frameNStart = frameN  # exact frame index
                LDT_fix_cross.tStart = t  # local t and not account for scr refresh
                LDT_fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_fix_cross, 'tStartRefresh')  # time at next scr refresh
                LDT_fix_cross.setAutoDraw(True)
            if LDT_fix_cross.status == STARTED:
                if frameN >= (LDT_fix_cross.frameNStart + rand_duration):
                    # keep track of stop time/frame for later
                    LDT_fix_cross.tStop = t  # not accounting for scr refresh
                    LDT_fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_fix_cross, 'tStopRefresh')  # time at next scr refresh
                    LDT_fix_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix"-------
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_pracs.addData('LDT_fix_cross.started', LDT_fix_cross.tStartRefresh)
        LDT_pracs.addData('LDT_fix_cross.stopped', LDT_fix_cross.tStopRefresh)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "LDT_prac"-------
        # update component parameters for each repeat
        LDT_word_prac.setText(words)
        LDT_mask_prac.setText(mask)
        resp_LDT_prac.keys = []
        resp_LDT_prac.rt = []
        keys = []
        ldt_dur = random.randint(1, 6)
        ldt_mask_dur = 2 * ldt_dur
        # keep track of which components have finished
        LDT_pracComponents = [LDT_word_prac, LDT_mask_prac, resp_LDT_prac, key_reminder_3]
        for thisComponent in LDT_pracComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LDT_pracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "LDT_prac"-------
        while continueRoutine:
            # get current time
            t = LDT_pracClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LDT_pracClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_word_prac* updates
            if LDT_word_prac.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                LDT_word_prac.frameNStart = frameN  # exact frame index
                LDT_word_prac.tStart = t  # local t and not account for scr refresh
                LDT_word_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_word_prac, 'tStartRefresh')  # time at next scr refresh
                LDT_word_prac.setAutoDraw(True)
            if LDT_word_prac.status == STARTED:
                if frameN >= (LDT_word_prac.frameNStart + ldt_dur):
                    # keep track of stop time/frame for later
                    LDT_word_prac.tStop = t  # not accounting for scr refresh
                    LDT_word_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_word_prac, 'tStopRefresh')  # time at next scr refresh
                    LDT_word_prac.setAutoDraw(False)
            
            # *LDT_mask_prac* updates
            if LDT_mask_prac.status == NOT_STARTED and LDT_word_prac.status==FINISHED:
                # keep track of start time/frame for later
                LDT_mask_prac.frameNStart = frameN  # exact frame index
                LDT_mask_prac.tStart = t  # local t and not account for scr refresh
                LDT_mask_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_mask_prac, 'tStartRefresh')  # time at next scr refresh
                LDT_mask_prac.setAutoDraw(True)
            if LDT_mask_prac.status == STARTED:
                if frameN >= (LDT_mask_prac.frameNStart + ldt_mask_dur):
                    # keep track of stop time/frame for later
                    LDT_mask_prac.tStop = t  # not accounting for scr refresh
                    LDT_mask_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_mask_prac, 'tStopRefresh')  # time at next scr refresh
                    LDT_mask_prac.setAutoDraw(False)
            
            # *resp_LDT_prac* updates
            waitOnFlip = False
            if resp_LDT_prac.status == NOT_STARTED and frameN >= ldt_dur:
                # keep track of start time/frame for later
                resp_LDT_prac.frameNStart = frameN  # exact frame index
                resp_LDT_prac.tStart = t  # local t and not account for scr refresh
                resp_LDT_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_LDT_prac, 'tStartRefresh')  # time at next scr refresh
                resp_LDT_prac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_LDT_prac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_LDT_prac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_LDT_prac.status == STARTED and not waitOnFlip:
                theseKeys = resp_LDT_prac.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    resp_LDT_prac.keys = theseKeys.name  # just the last key pressed
                    resp_LDT_prac.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            keys = event.getKeys()
            if 'j' in keys:
                    continueRoutine = False
                    try:
                        LDT_pracs_1.finished = True
                    except:
                        LDT_pracs.finished = True
            
            # *key_reminder_3* updates
            if key_reminder_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_reminder_3.frameNStart = frameN  # exact frame index
                key_reminder_3.tStart = t  # local t and not account for scr refresh
                key_reminder_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_reminder_3, 'tStartRefresh')  # time at next scr refresh
                key_reminder_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDT_pracComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "LDT_prac"-------
        for thisComponent in LDT_pracComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_pracs.addData('LDT_word_prac.started', LDT_word_prac.tStartRefresh)
        LDT_pracs.addData('LDT_word_prac.stopped', LDT_word_prac.tStopRefresh)
        LDT_pracs.addData('LDT_mask_prac.started', LDT_mask_prac.tStartRefresh)
        LDT_pracs.addData('LDT_mask_prac.stopped', LDT_mask_prac.tStopRefresh)
        # check responses
        if resp_LDT_prac.keys in ['', [], None]:  # No response was made
            resp_LDT_prac.keys = None
        LDT_pracs.addData('resp_LDT_prac.keys',resp_LDT_prac.keys)
        if resp_LDT_prac.keys != None:  # we had a response
            LDT_pracs.addData('resp_LDT_prac.rt', resp_LDT_prac.rt)
        LDT_pracs.addData('resp_LDT_prac.started', resp_LDT_prac.tStartRefresh)
        LDT_pracs.addData('resp_LDT_prac.stopped', resp_LDT_prac.tStopRefresh)
        thisExp.addData('task', "LDT_prac")
        thisExp.addData('keypress', resp_LDT_prac.keys)
        thisExp.addData('LDT_dur', ldt_dur)
        thisExp.addData('RT', resp_LDT_prac.rt)
        thisExp.addData('corr', resp_LDT_prac.corr)
        thisExp.addData('exp_time', globalClock.getTime())
        
        LDT_pracs.addData('key_reminder_3.started', key_reminder_3.tStartRefresh)
        LDT_pracs.addData('key_reminder_3.stopped', key_reminder_3.tStopRefresh)
        # the Routine "LDT_prac" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'LDT_pracs'
    
    
    # ------Prepare to start Routine "instr_LDT_2"-------
    # update component parameters for each repeat
    resp_LDT_ready.keys = []
    resp_LDT_ready.rt = []
    keys = []
    # keep track of which components have finished
    instr_LDT_2Components = [instr_LDT9, instr_LDT10, image_6, instr_LDT11, resp_LDT_ready]
    for thisComponent in instr_LDT_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instr_LDT_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instr_LDT_2"-------
    while continueRoutine:
        # get current time
        t = instr_LDT_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instr_LDT_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_LDT9* updates
        if instr_LDT9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT9.frameNStart = frameN  # exact frame index
            instr_LDT9.tStart = t  # local t and not account for scr refresh
            instr_LDT9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT9, 'tStartRefresh')  # time at next scr refresh
            instr_LDT9.setAutoDraw(True)
        if instr_LDT9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT9.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT9.tStop = t  # not accounting for scr refresh
                instr_LDT9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT9, 'tStopRefresh')  # time at next scr refresh
                instr_LDT9.setAutoDraw(False)
        
        # *instr_LDT10* updates
        if instr_LDT10.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT10.frameNStart = frameN  # exact frame index
            instr_LDT10.tStart = t  # local t and not account for scr refresh
            instr_LDT10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT10, 'tStartRefresh')  # time at next scr refresh
            instr_LDT10.setAutoDraw(True)
        if instr_LDT10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instr_LDT10.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                instr_LDT10.tStop = t  # not accounting for scr refresh
                instr_LDT10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(instr_LDT10, 'tStopRefresh')  # time at next scr refresh
                instr_LDT10.setAutoDraw(False)
        
        # *image_6* updates
        if image_6.status == NOT_STARTED and tThisFlip >= 10-frameTolerance:
            # keep track of start time/frame for later
            image_6.frameNStart = frameN  # exact frame index
            image_6.tStart = t  # local t and not account for scr refresh
            image_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
            image_6.setAutoDraw(True)
        if image_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_6.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                image_6.tStop = t  # not accounting for scr refresh
                image_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
                image_6.setAutoDraw(False)
        
        # *instr_LDT11* updates
        if instr_LDT11.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
            # keep track of start time/frame for later
            instr_LDT11.frameNStart = frameN  # exact frame index
            instr_LDT11.tStart = t  # local t and not account for scr refresh
            instr_LDT11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_LDT11, 'tStartRefresh')  # time at next scr refresh
            instr_LDT11.setAutoDraw(True)
        
        # *resp_LDT_ready* updates
        waitOnFlip = False
        if resp_LDT_ready.status == NOT_STARTED and tThisFlip >= 16-frameTolerance:
            # keep track of start time/frame for later
            resp_LDT_ready.frameNStart = frameN  # exact frame index
            resp_LDT_ready.tStart = t  # local t and not account for scr refresh
            resp_LDT_ready.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp_LDT_ready, 'tStartRefresh')  # time at next scr refresh
            resp_LDT_ready.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp_LDT_ready.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp_LDT_ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp_LDT_ready.status == STARTED and not waitOnFlip:
            theseKeys = resp_LDT_ready.getKeys(keyList=['right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp_LDT_ready.keys = theseKeys.name  # just the last key pressed
                resp_LDT_ready.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instr_LDT_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instr_LDT_2"-------
    for thisComponent in instr_LDT_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    LDT_cond1.addData('instr_LDT9.started', instr_LDT9.tStartRefresh)
    LDT_cond1.addData('instr_LDT9.stopped', instr_LDT9.tStopRefresh)
    LDT_cond1.addData('instr_LDT10.started', instr_LDT10.tStartRefresh)
    LDT_cond1.addData('instr_LDT10.stopped', instr_LDT10.tStopRefresh)
    LDT_cond1.addData('image_6.started', image_6.tStartRefresh)
    LDT_cond1.addData('image_6.stopped', image_6.tStopRefresh)
    LDT_cond1.addData('instr_LDT11.started', instr_LDT11.tStartRefresh)
    LDT_cond1.addData('instr_LDT11.stopped', instr_LDT11.tStopRefresh)
    # check responses
    if resp_LDT_ready.keys in ['', [], None]:  # No response was made
        resp_LDT_ready.keys = None
    LDT_cond1.addData('resp_LDT_ready.keys',resp_LDT_ready.keys)
    if resp_LDT_ready.keys != None:  # we had a response
        LDT_cond1.addData('resp_LDT_ready.rt', resp_LDT_ready.rt)
    LDT_cond1.addData('resp_LDT_ready.started', resp_LDT_ready.tStartRefresh)
    LDT_cond1.addData('resp_LDT_ready.stopped', resp_LDT_ready.tStopRefresh)
    # the Routine "instr_LDT_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    LDT_trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('condition_files/LDT_conditions.csv'),
        seed=None, name='LDT_trials')
    thisExp.addLoop(LDT_trials)  # add the loop to the experiment
    thisLDT_trial = LDT_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_trial.rgb)
    if thisLDT_trial != None:
        for paramName in thisLDT_trial:
            exec('{} = thisLDT_trial[paramName]'.format(paramName))
    
    for thisLDT_trial in LDT_trials:
        currentLoop = LDT_trials
        # abbreviate parameter names if possible (e.g. rgb = thisLDT_trial.rgb)
        if thisLDT_trial != None:
            for paramName in thisLDT_trial:
                exec('{} = thisLDT_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "fix"-------
        # update component parameters for each repeat
        rand_duration = random.randint(6, 18)
        # keep track of which components have finished
        fixComponents = [LDT_fix_cross]
        for thisComponent in fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "fix"-------
        while continueRoutine:
            # get current time
            t = fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_fix_cross* updates
            if LDT_fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LDT_fix_cross.frameNStart = frameN  # exact frame index
                LDT_fix_cross.tStart = t  # local t and not account for scr refresh
                LDT_fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_fix_cross, 'tStartRefresh')  # time at next scr refresh
                LDT_fix_cross.setAutoDraw(True)
            if LDT_fix_cross.status == STARTED:
                if frameN >= (LDT_fix_cross.frameNStart + rand_duration):
                    # keep track of stop time/frame for later
                    LDT_fix_cross.tStop = t  # not accounting for scr refresh
                    LDT_fix_cross.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_fix_cross, 'tStopRefresh')  # time at next scr refresh
                    LDT_fix_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix"-------
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_trials.addData('LDT_fix_cross.started', LDT_fix_cross.tStartRefresh)
        LDT_trials.addData('LDT_fix_cross.stopped', LDT_fix_cross.tStopRefresh)
        # the Routine "fix" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "LDT_trial"-------
        # update component parameters for each repeat
        LDT_word_trial.setText(words)
        LDT_mask_trial.setText(mask)
        resp_LDT_trial.keys = []
        resp_LDT_trial.rt = []
        keys = []
        ldt_dur = random.randint(1, 6)
        # keep track of which components have finished
        LDT_trialComponents = [LDT_word_trial, LDT_mask_trial, resp_LDT_trial, key_reminder]
        for thisComponent in LDT_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        LDT_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "LDT_trial"-------
        while continueRoutine:
            # get current time
            t = LDT_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=LDT_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LDT_word_trial* updates
            if LDT_word_trial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                LDT_word_trial.frameNStart = frameN  # exact frame index
                LDT_word_trial.tStart = t  # local t and not account for scr refresh
                LDT_word_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_word_trial, 'tStartRefresh')  # time at next scr refresh
                LDT_word_trial.setAutoDraw(True)
            if LDT_word_trial.status == STARTED:
                if frameN >= (LDT_word_trial.frameNStart + ldt_dur):
                    # keep track of stop time/frame for later
                    LDT_word_trial.tStop = t  # not accounting for scr refresh
                    LDT_word_trial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(LDT_word_trial, 'tStopRefresh')  # time at next scr refresh
                    LDT_word_trial.setAutoDraw(False)
            
            # *LDT_mask_trial* updates
            if LDT_mask_trial.status == NOT_STARTED and frameN >= LDT_word_trial.status==FINISHED:
                # keep track of start time/frame for later
                LDT_mask_trial.frameNStart = frameN  # exact frame index
                LDT_mask_trial.tStart = t  # local t and not account for scr refresh
                LDT_mask_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LDT_mask_trial, 'tStartRefresh')  # time at next scr refresh
                LDT_mask_trial.setAutoDraw(True)
            
            # *resp_LDT_trial* updates
            waitOnFlip = False
            if resp_LDT_trial.status == NOT_STARTED and frameN >= ldt_dur:
                # keep track of start time/frame for later
                resp_LDT_trial.frameNStart = frameN  # exact frame index
                resp_LDT_trial.tStart = t  # local t and not account for scr refresh
                resp_LDT_trial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_LDT_trial, 'tStartRefresh')  # time at next scr refresh
                resp_LDT_trial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_LDT_trial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_LDT_trial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_LDT_trial.status == STARTED and not waitOnFlip:
                theseKeys = resp_LDT_trial.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    resp_LDT_trial.keys = theseKeys.name  # just the last key pressed
                    resp_LDT_trial.rt = theseKeys.rt
                    # was this 'correct'?
                    if (resp_LDT_trial.keys == str(corr_ans)) or (resp_LDT_trial.keys == corr_ans):
                        resp_LDT_trial.corr = 1
                    else:
                        resp_LDT_trial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            keys = event.getKeys()
            if 'j' in keys:
                    continueRoutine = False
                    try:
                        LDT_trials_1.finished = True
                    except: 
                        LDT_trials.finished = True 
            
            # *key_reminder* updates
            if key_reminder.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_reminder.frameNStart = frameN  # exact frame index
                key_reminder.tStart = t  # local t and not account for scr refresh
                key_reminder.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_reminder, 'tStartRefresh')  # time at next scr refresh
                key_reminder.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in LDT_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "LDT_trial"-------
        for thisComponent in LDT_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        LDT_trials.addData('LDT_word_trial.started', LDT_word_trial.tStartRefresh)
        LDT_trials.addData('LDT_word_trial.stopped', LDT_word_trial.tStopRefresh)
        LDT_trials.addData('LDT_mask_trial.started', LDT_mask_trial.tStartRefresh)
        LDT_trials.addData('LDT_mask_trial.stopped', LDT_mask_trial.tStopRefresh)
        # check responses
        if resp_LDT_trial.keys in ['', [], None]:  # No response was made
            resp_LDT_trial.keys = None
            # was no response the correct answer?!
            if str(corr_ans).lower() == 'none':
               resp_LDT_trial.corr = 1;  # correct non-response
            else:
               resp_LDT_trial.corr = 0;  # failed to respond (incorrectly)
        # store data for LDT_trials (TrialHandler)
        LDT_trials.addData('resp_LDT_trial.keys',resp_LDT_trial.keys)
        LDT_trials.addData('resp_LDT_trial.corr', resp_LDT_trial.corr)
        if resp_LDT_trial.keys != None:  # we had a response
            LDT_trials.addData('resp_LDT_trial.rt', resp_LDT_trial.rt)
        LDT_trials.addData('resp_LDT_trial.started', resp_LDT_trial.tStartRefresh)
        LDT_trials.addData('resp_LDT_trial.stopped', resp_LDT_trial.tStopRefresh)
        thisExp.addData('task', "LDT")
        thisExp.addData('keypress', resp_LDT_trial.keys)
        thisExp.addData('LDT_dur', ldt_dur)
        thisExp.addData('RT', resp_LDT_trial.rt)
        thisExp.addData('corr', resp_LDT_trial.corr)
        thisExp.addData('exp_time', globalClock.getTime())
        LDT_trials.addData('key_reminder.started', key_reminder.tStartRefresh)
        LDT_trials.addData('key_reminder.stopped', key_reminder.tStopRefresh)
        # the Routine "LDT_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'LDT_trials'
    
    
    # ------Prepare to start Routine "LDT_feedback"-------
    # update component parameters for each repeat
    LDT_rating.reset()
    keys = []
    # keep track of which components have finished
    LDT_feedbackComponents = [LDT_rating, LDT_feedback_inst]
    for thisComponent in LDT_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    LDT_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "LDT_feedback"-------
    while continueRoutine:
        # get current time
        t = LDT_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=LDT_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *LDT_rating* updates
        if LDT_rating.status == NOT_STARTED and t >= 10-frameTolerance:
            # keep track of start time/frame for later
            LDT_rating.frameNStart = frameN  # exact frame index
            LDT_rating.tStart = t  # local t and not account for scr refresh
            LDT_rating.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDT_rating, 'tStartRefresh')  # time at next scr refresh
            LDT_rating.setAutoDraw(True)
        
        # *LDT_feedback_inst* updates
        if LDT_feedback_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LDT_feedback_inst.frameNStart = frameN  # exact frame index
            LDT_feedback_inst.tStart = t  # local t and not account for scr refresh
            LDT_feedback_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LDT_feedback_inst, 'tStartRefresh')  # time at next scr refresh
            LDT_feedback_inst.setAutoDraw(True)
        if LDT_feedback_inst.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > LDT_feedback_inst.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                LDT_feedback_inst.tStop = t  # not accounting for scr refresh
                LDT_feedback_inst.frameNStop = frameN  # exact frame index
                win.timeOnFlip(LDT_feedback_inst, 'tStopRefresh')  # time at next scr refresh
                LDT_feedback_inst.setAutoDraw(False)
        keys = event.getKeys()
        if 'j' in keys:
                continueRoutine = False 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDT_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "LDT_feedback"-------
    for thisComponent in LDT_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for LDT_cond1 (TrialHandler)
    LDT_cond1.addData('LDT_rating.response', LDT_rating.getRating())
    LDT_cond1.addData('LDT_rating.rt', LDT_rating.getRT())
    LDT_cond1.addData('LDT_rating.started', LDT_rating.tStart)
    LDT_cond1.addData('LDT_rating.stopped', LDT_rating.tStop)
    LDT_cond1.addData('LDT_feedback_inst.started', LDT_feedback_inst.tStartRefresh)
    LDT_cond1.addData('LDT_feedback_inst.stopped', LDT_feedback_inst.tStopRefresh)
    thisExp.addData("task", "LDT_feedback")
    # the Routine "LDT_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed int(expInfo['participant ID']) % 2 == 0 repeats of 'LDT_cond1'


# ------Prepare to start Routine "end"-------
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [instr_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_end* updates
    if instr_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instr_end.frameNStart = frameN  # exact frame index
        instr_end.tStart = t  # local t and not account for scr refresh
        instr_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instr_end, 'tStartRefresh')  # time at next scr refresh
        instr_end.setAutoDraw(True)
    if instr_end.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instr_end.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            instr_end.tStop = t  # not accounting for scr refresh
            instr_end.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instr_end, 'tStopRefresh')  # time at next scr refresh
            instr_end.setAutoDraw(False)
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instr_end.started', instr_end.tStartRefresh)
thisExp.addData('instr_end.stopped', instr_end.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
