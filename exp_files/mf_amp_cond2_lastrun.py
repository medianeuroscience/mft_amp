#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Wed Feb 20 20:43:23 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.3'
expName = 'mf_amp_cond2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/jacobfisher/projects/inprogress/mf_amp/exp_files/mf_amp_cond2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='#FAFAFA', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instr1"
instr1Clock = core.Clock()
instr_1 = visual.TextStim(win=win, name='instr_1',
    text='Welcome to the Language and Emotion study!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_2 = visual.TextStim(win=win, name='instr_2',
    text='The goal of this experiment is to better understand how people react to language',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_3 = visual.TextStim(win=win, name='instr_3',
    text='You will be asked to complete three different tasks, followed by a short survey.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_4 = visual.TextStim(win=win, name='instr_4',
    text='Before we begin, please make sure your fingers are on the correct keys.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_5 = visual.TextStim(win=win, name='instr_5',
    text='Your right index finger should be on the left arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_6 = visual.TextStim(win=win, name='instr_6',
    text='Your right ring finger should be on the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image = visual.ImageStim(
    win=win, name='image',
    image='images/keyboard_diagram.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
instr_7 = visual.TextStim(win=win, name='instr_7',
    text='If you are ready to begin please press the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);


# Initialize components for Routine "instr_LDT"
instr_LDTClock = core.Clock()
instr_LDT1 = visual.TextStim(win=win, name='instr_LDT1',
    text='Welcome to the first task!\n\nIn this task, you will see a selection of words and non-words',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_LDT2 = visual.TextStim(win=win, name='instr_LDT2',
    text='You will see a real word or a nonsense word quickly followed by a string of "&" symbols\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_LDT3 = visual.TextStim(win=win, name='instr_LDT3',
    text='Upon seeing the "&" symbols, you should decide as quickly as possible whether you saw a word or non-word',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_LDT4 = visual.TextStim(win=win, name='instr_LDT4',
    text='If you think you saw a real word, press the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_LDT5 = visual.TextStim(win=win, name='instr_LDT5',
    text='If you think you saw a nonsense word, press the left arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_LDT6 = visual.TextStim(win=win, name='instr_LDT6',
    text='Please make sure your fingers are in the correct place',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='images/keyboard_diagram.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
keyboard_reminder_LDT = visual.ImageStim(
    win=win, name='keyboard_reminder_LDT',
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
instr_LDT7 = visual.TextStim(win=win, name='instr_LDT7',
    text='The words may be difficult to see, but please do the best you can',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_LT8 = visual.TextStim(win=win, name='instr_LT8',
    text="Let's do a practice round",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_LDT9_ = visual.TextStim(win=win, name='instr_LDT9_',
    text='When you are ready to begin, press the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);


# Initialize components for Routine "LDT_fix_prac"
LDT_fix_pracClock = core.Clock()
LDT_fix_cross = visual.ImageStim(
    win=win, name='LDT_fix_cross',units='pix', 
    image='images/crosshair.png', mask=None,
    ori=0, pos=(0, 0), size=[50,50],
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

key_reminder_3 = visual.ImageStim(
    win=win, name='key_reminder_3',units='deg', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

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
    text='Remember that LEFT is nonsense word\nand RIGHT is real word.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_6 = visual.ImageStim(
    win=win, name='image_6',
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


# Initialize components for Routine "LDT_fix"
LDT_fixClock = core.Clock()
LDT_fix_cross_2 = visual.ImageStim(
    win=win, name='LDT_fix_cross_2',units='pix', 
    image='images/crosshair.png', mask=None,
    ori=0, pos=(0, 0), size=[50,50],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "LDT_trial"
LDT_trialClock = core.Clock()
LDT_word_2 = visual.TextStim(win=win, name='LDT_word_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
LDT_mask_2 = visual.TextStim(win=win, name='LDT_mask_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

key_reminder_4 = visual.ImageStim(
    win=win, name='key_reminder_4',units='deg', 
    image='images/layout_reminder_LDT.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_AMP"
instr_AMPClock = core.Clock()
instr_AMP1 = visual.TextStim(win=win, name='instr_AMP1',
    text='Welcome to the second task!\n\nIn this task, you will see a selection of words.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_AMP2 = visual.TextStim(win=win, name='instr_AMP2',
    text='After seeing each word, you will see a nonsense word.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_AMP3 = visual.TextStim(win=win, name='instr_AMP3',
    text='After this, you will see a string of "&" symbols',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_AMP4 = visual.TextStim(win=win, name='instr_AMP4',
    text='Upon seeing the "&" symbols, you will rate whether the nonsense word you just saw made you feel positive or negative',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
instr_AMP5 = visual.TextStim(win=win, name='instr_AMP5',
    text='If the nonsense word made you feel positive, press the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
instr_AMP6 = visual.TextStim(win=win, name='instr_AMP6',
    text='If the non-word made you feel negative, press the left arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
instr_AMP7 = visual.TextStim(win=win, name='instr_AMP7',
    text='Remember you are rating the nonsense word, NOT the word that came before it.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
instr_AMP8 = visual.TextStim(win=win, name='instr_AMP8',
    text="Let's do a practice round.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
instr_AMP13 = visual.TextStim(win=win, name='instr_AMP13',
    text='When you are ready to begin press the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);


# Initialize components for Routine "AMP_prac_word"
AMP_prac_wordClock = core.Clock()
AMP_wordstim_2 = visual.TextStim(win=win, name='AMP_wordstim_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
gap = visual.TextStim(win=win, name='gap',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
import random 
import pandas as pd
import numpy as np

# reading in the CSV so that I can generate the conditions file for the AMP
words = pd.read_csv("condition_files/words4exp.csv")

# Here are the row indices for all of the words in the full CSV.

unique_cats = {k:None for k in words.category.unique()}
for k,v in unique_cats.items():
    unique_cats[k] = list(words[words.category == k].index.values)

# Taking a sample from each category for the AMP and plugging the rest into the LDT

full_amp_words = {k:None for k in unique_cats.keys() if k != "neutral"}
full_ldt_words = {k:None for k in unique_cats.keys()}
for k,v in unique_cats.items():
    if "." in str(k): 
        full_amp_words[k] = random.sample(unique_cats[k],7)
        full_ldt_words[k] = [x for x in unique_cats[k] if x not in full_amp_words[k]]
    if k == "nonword":
        full_amp_words[k] = random.sample(unique_cats[k],92)
        full_ldt_words[k] = [x for x in unique_cats[k] if x not in full_amp_words[k]]
    if k =="control":
        full_amp_words[k] = unique_cats[k]
    if k == "neutral":
        full_ldt_words[k] = unique_cats[k]

# Generating the final list of AMP words

amp_moral_words = []
amp_nonwords = []
for k,v in full_amp_words.items():
    if k != "nonword":
        for i in v:
            amp_moral_words.append(i)
    if k == "nonword":
        for i in v:
            amp_nonwords.append(i)
            
# Taking a random sample of 10 of the nonwords to use as primes, and then adding them to the primes list
amp_nonword_primes = random.sample(amp_nonwords,10)
amp_primes_list = amp_moral_words + amp_nonword_primes

for x in amp_nonword_primes:
  amp_nonwords.remove(x)


amp_nonword_select = random.sample(amp_nonwords,10)
amp_full_list = amp_moral_words + amp_nonword_select

for x in amp_nonword_select:
  amp_nonwords.remove(x)

# Pulling the words, correct answers, and categories for all of the indices for our moral words plus our ten nonword controls
AMP_wordlist = words.loc[amp_primes_list].words.values
AMP_corr_ans = words.loc[amp_primes_list].correct_amp.values
AMP_category = words.loc[amp_primes_list].category.values

#pulling the nonwords and masks for our targets that weren't selected to be included in the prime
AMP_nonwordlist = words.loc[amp_nonwords].words.values
AMP_masklist = words.loc[amp_nonwords].masks.values

# df1 is the words that will be used as primes and their associated categories and correct answers

df1 = pd.DataFrame(
    {'words': AMP_wordlist.tolist(),
     'corr_ans': AMP_corr_ans.tolist(),
     'category': AMP_category.tolist()
    })

# df2 is the nonwords that will be used as targets and their associated masks

df2 = pd.DataFrame(
     {'nonwords': AMP_nonwordlist.tolist(),
     'mask': AMP_masklist.tolist(),
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

# Concatenating all of the primes and targets horizontally

rep1 = pd.concat([primes_rep1,targets_rep1], axis = 1)
rep2 = pd.concat([primes_rep2,targets_rep2], axis = 1)
rep3 = pd.concat([primes_rep3,targets_rep3], axis = 1)
rep4 = pd.concat([primes_rep4,targets_rep4], axis = 1)

# Concatenating all of the reps horizontally

df_full = pd.concat([rep1,rep2,rep3,rep4], axis = 0)

df_full.reset_index(inplace=True, drop=True)

df_full.to_csv("condition_files/AMP_conditions.csv")

# Getting the LDT words 

ldt_wordlist = []
for k,v in full_ldt_words.items():
    if k != "control":
        for i in v:
            ldt_wordlist.append(i)

# Pulling the words, correct answers, and categories for all of the indices for our words
LDT_words = words.loc[ldt_wordlist].words.values
LDT_corr = words.loc[ldt_wordlist].correct_ldt.values
LDT_category = words.loc[ldt_wordlist].category.values
LDT_masklist = words.loc[ldt_wordlist].masks.values

# Creating a dataframe and writing to CSV

df_ldt = pd.DataFrame(
    {'words': LDT_words.tolist(),
     'corr_ans': LDT_corr.tolist(),
     'category': LDT_category.tolist(),
     'mask': LDT_masklist.tolist()
    })

df_ldt.to_csv("condition_files/LDT_conditions.csv")
AMP_nonwordstim_3 = visual.TextStim(win=win, name='AMP_nonwordstim_3',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AMP_nonword_prac"
AMP_nonword_pracClock = core.Clock()

AMP_maskstim_2 = visual.TextStim(win=win, name='AMP_maskstim_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_reminder = visual.ImageStim(
    win=win, name='key_reminder',units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_AMP_2"
instr_AMP_2Clock = core.Clock()
instr_AMP9 = visual.TextStim(win=win, name='instr_AMP9',
    text='Great job!',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_AMP14 = visual.TextStim(win=win, name='instr_AMP14',
    text='Remember that LEFT is negative\nand RIGHT is positive.',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
instr_AMP11 = visual.TextStim(win=win, name='instr_AMP11',
    text='If you are ready to begin, please press the right arrow key',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);


# Initialize components for Routine "instr_AMP_3"
instr_AMP_3Clock = core.Clock()
instr_AMP12 = visual.TextStim(win=win, name='instr_AMP12',
    text="Let's go!",
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Initialize components for Routine "AMP_word"
AMP_wordClock = core.Clock()
AMP_wordstim = visual.TextStim(win=win, name='AMP_wordstim',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
gap_1 = visual.TextStim(win=win, name='gap_1',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

AMP_nonwordstim_2 = visual.TextStim(win=win, name='AMP_nonwordstim_2',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "AMP_nonword"
AMP_nonwordClock = core.Clock()

AMP_maskstim = visual.TextStim(win=win, name='AMP_maskstim',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_reminder_2 = visual.ImageStim(
    win=win, name='key_reminder_2',units='deg', 
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, -6), size=(20, 10),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instr_tweets"
instr_tweetsClock = core.Clock()
instr_LDT1_2 = visual.TextStim(win=win, name='instr_LDT1_2',
    text='Welcome to the third task!\n\nIn this task, you will see a selection of tweets',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instr_LDT2_2 = visual.TextStim(win=win, name='instr_LDT2_2',
    text='You will be asked to rate how the tweet made you feel.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
instr_LDT3_2 = visual.TextStim(win=win, name='instr_LDT3_2',
    text='If the tweet made you feel positive, press the RIGHT arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
instr_LDT4_2 = visual.TextStim(win=win, name='instr_LDT4_2',
    text='If the tweet made you feel negative, press the LEFT arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
keyboard_reminder_LDT_2 = visual.ImageStim(
    win=win, name='keyboard_reminder_LDT_2',
    image='images/layout_reminder_AMP.png', mask=None,
    ori=0, pos=(0, 0), size=(0.9, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
instr_LDT8_2 = visual.TextStim(win=win, name='instr_LDT8_2',
    text='When you are ready to begin, press the right arrow key',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);


# Initialize components for Routine "tweets"
tweetsClock = core.Clock()
tweet = visual.TextStim(win=win, name='tweet',
    text='default text',
    font='Verdana',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='#212121', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr1"-------
t = 0
instr1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_AMP_instr1 = event.BuilderKeyResponse()

# keep track of which components have finished
instr1Components = [instr_1, instr_2, instr_3, instr_4, instr_5, instr_6, image, instr_7, key_resp_AMP_instr1]
for thisComponent in instr1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr1"-------
while continueRoutine:
    # get current time
    t = instr1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_1* updates
    if t >= 0.0 and instr_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_1.tStart = t
        instr_1.frameNStart = frameN  # exact frame index
        instr_1.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_1.status == STARTED and t >= frameRemains:
        instr_1.setAutoDraw(False)
    
    # *instr_2* updates
    if t >= 6 and instr_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_2.tStart = t
        instr_2.frameNStart = frameN  # exact frame index
        instr_2.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_2.status == STARTED and t >= frameRemains:
        instr_2.setAutoDraw(False)
    
    # *instr_3* updates
    if t >= 12 and instr_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_3.tStart = t
        instr_3.frameNStart = frameN  # exact frame index
        instr_3.setAutoDraw(True)
    frameRemains = 12 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_3.status == STARTED and t >= frameRemains:
        instr_3.setAutoDraw(False)
    
    # *instr_4* updates
    if t >= 18 and instr_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_4.tStart = t
        instr_4.frameNStart = frameN  # exact frame index
        instr_4.setAutoDraw(True)
    frameRemains = 18 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_4.status == STARTED and t >= frameRemains:
        instr_4.setAutoDraw(False)
    
    # *instr_5* updates
    if t >= 24 and instr_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_5.tStart = t
        instr_5.frameNStart = frameN  # exact frame index
        instr_5.setAutoDraw(True)
    frameRemains = 24 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_5.status == STARTED and t >= frameRemains:
        instr_5.setAutoDraw(False)
    
    # *instr_6* updates
    if t >= 30 and instr_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_6.tStart = t
        instr_6.frameNStart = frameN  # exact frame index
        instr_6.setAutoDraw(True)
    frameRemains = 30 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_6.status == STARTED and t >= frameRemains:
        instr_6.setAutoDraw(False)
    
    # *image* updates
    if t >= 34 and image.status == NOT_STARTED:
        # keep track of start time/frame for later
        image.tStart = t
        image.frameNStart = frameN  # exact frame index
        image.setAutoDraw(True)
    frameRemains = 34 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image.status == STARTED and t >= frameRemains:
        image.setAutoDraw(False)
    
    # *instr_7* updates
    if t >= 38 and instr_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_7.tStart = t
        instr_7.frameNStart = frameN  # exact frame index
        instr_7.setAutoDraw(True)
    
    # *key_resp_AMP_instr1* updates
    if t >= 38 and key_resp_AMP_instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_AMP_instr1.tStart = t
        key_resp_AMP_instr1.frameNStart = frameN  # exact frame index
        key_resp_AMP_instr1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_AMP_instr1.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_AMP_instr1.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_AMP_instr1.keys = theseKeys[-1]  # just the last key pressed
            key_resp_AMP_instr1.rt = key_resp_AMP_instr1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:         continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr1"-------
for thisComponent in instr1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_AMP_instr1.keys in ['', [], None]:  # No response was made
    key_resp_AMP_instr1.keys=None
thisExp.addData('key_resp_AMP_instr1.keys',key_resp_AMP_instr1.keys)
if key_resp_AMP_instr1.keys != None:  # we had a response
    thisExp.addData('key_resp_AMP_instr1.rt', key_resp_AMP_instr1.rt)
thisExp.nextEntry()

# the Routine "instr1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_LDT"-------
t = 0
instr_LDTClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_LDT_instr = event.BuilderKeyResponse()

# keep track of which components have finished
instr_LDTComponents = [instr_LDT1, instr_LDT2, instr_LDT3, instr_LDT4, instr_LDT5, instr_LDT6, image_3, keyboard_reminder_LDT, instr_LDT7, instr_LT8, instr_LDT9_, key_resp_LDT_instr]
for thisComponent in instr_LDTComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_LDT"-------
while continueRoutine:
    # get current time
    t = instr_LDTClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_LDT1* updates
    if t >= 0.0 and instr_LDT1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT1.tStart = t
        instr_LDT1.frameNStart = frameN  # exact frame index
        instr_LDT1.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT1.status == STARTED and t >= frameRemains:
        instr_LDT1.setAutoDraw(False)
    
    # *instr_LDT2* updates
    if t >= 6 and instr_LDT2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT2.tStart = t
        instr_LDT2.frameNStart = frameN  # exact frame index
        instr_LDT2.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT2.status == STARTED and t >= frameRemains:
        instr_LDT2.setAutoDraw(False)
    
    # *instr_LDT3* updates
    if t >= 12 and instr_LDT3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT3.tStart = t
        instr_LDT3.frameNStart = frameN  # exact frame index
        instr_LDT3.setAutoDraw(True)
    frameRemains = 12 + 8- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT3.status == STARTED and t >= frameRemains:
        instr_LDT3.setAutoDraw(False)
    
    # *instr_LDT4* updates
    if t >= 20 and instr_LDT4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT4.tStart = t
        instr_LDT4.frameNStart = frameN  # exact frame index
        instr_LDT4.setAutoDraw(True)
    frameRemains = 20 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT4.status == STARTED and t >= frameRemains:
        instr_LDT4.setAutoDraw(False)
    
    # *instr_LDT5* updates
    if t >= 26 and instr_LDT5.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT5.tStart = t
        instr_LDT5.frameNStart = frameN  # exact frame index
        instr_LDT5.setAutoDraw(True)
    frameRemains = 26 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT5.status == STARTED and t >= frameRemains:
        instr_LDT5.setAutoDraw(False)
    
    # *instr_LDT6* updates
    if t >= 32 and instr_LDT6.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT6.tStart = t
        instr_LDT6.frameNStart = frameN  # exact frame index
        instr_LDT6.setAutoDraw(True)
    frameRemains = 32 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT6.status == STARTED and t >= frameRemains:
        instr_LDT6.setAutoDraw(False)
    
    # *image_3* updates
    if t >= 38 and image_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_3.tStart = t
        image_3.frameNStart = frameN  # exact frame index
        image_3.setAutoDraw(True)
    frameRemains = 38 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_3.status == STARTED and t >= frameRemains:
        image_3.setAutoDraw(False)
    
    # *keyboard_reminder_LDT* updates
    if t >= 42 and keyboard_reminder_LDT.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyboard_reminder_LDT.tStart = t
        keyboard_reminder_LDT.frameNStart = frameN  # exact frame index
        keyboard_reminder_LDT.setAutoDraw(True)
    frameRemains = 42 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if keyboard_reminder_LDT.status == STARTED and t >= frameRemains:
        keyboard_reminder_LDT.setAutoDraw(False)
    
    # *instr_LDT7* updates
    if t >= 46 and instr_LDT7.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT7.tStart = t
        instr_LDT7.frameNStart = frameN  # exact frame index
        instr_LDT7.setAutoDraw(True)
    frameRemains = 46 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT7.status == STARTED and t >= frameRemains:
        instr_LDT7.setAutoDraw(False)
    
    # *instr_LT8* updates
    if t >= 52 and instr_LT8.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LT8.tStart = t
        instr_LT8.frameNStart = frameN  # exact frame index
        instr_LT8.setAutoDraw(True)
    frameRemains = 52 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LT8.status == STARTED and t >= frameRemains:
        instr_LT8.setAutoDraw(False)
    
    # *instr_LDT9_* updates
    if t >= 56 and instr_LDT9_.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT9_.tStart = t
        instr_LDT9_.frameNStart = frameN  # exact frame index
        instr_LDT9_.setAutoDraw(True)
    
    # *key_resp_LDT_instr* updates
    if t >= 56 and key_resp_LDT_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_LDT_instr.tStart = t
        key_resp_LDT_instr.frameNStart = frameN  # exact frame index
        key_resp_LDT_instr.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_LDT_instr.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_LDT_instr.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_LDT_instr.keys = theseKeys[-1]  # just the last key pressed
            key_resp_LDT_instr.rt = key_resp_LDT_instr.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if key_resp_LDT_instr.keys in ['', [], None]:  # No response was made
    key_resp_LDT_instr.keys=None
thisExp.addData('key_resp_LDT_instr.keys',key_resp_LDT_instr.keys)
if key_resp_LDT_instr.keys != None:  # we had a response
    thisExp.addData('key_resp_LDT_instr.rt', key_resp_LDT_instr.rt)
thisExp.nextEntry()

# the Routine "instr_LDT" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LDT_prac_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/ldt_testrun.csv'),
    seed=None, name='LDT_prac_loop')
thisExp.addLoop(LDT_prac_loop)  # add the loop to the experiment
thisLDT_prac_loop = LDT_prac_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLDT_prac_loop.rgb)
if thisLDT_prac_loop != None:
    for paramName in thisLDT_prac_loop:
        exec('{} = thisLDT_prac_loop[paramName]'.format(paramName))

for thisLDT_prac_loop in LDT_prac_loop:
    currentLoop = LDT_prac_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_prac_loop.rgb)
    if thisLDT_prac_loop != None:
        for paramName in thisLDT_prac_loop:
            exec('{} = thisLDT_prac_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "LDT_fix_prac"-------
    t = 0
    LDT_fix_pracClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rand_duration = random.randint(100, 300)/1000
    # keep track of which components have finished
    LDT_fix_pracComponents = [LDT_fix_cross]
    for thisComponent in LDT_fix_pracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "LDT_fix_prac"-------
    while continueRoutine:
        # get current time
        t = LDT_fix_pracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDT_fix_cross* updates
        if t >= 0.0 and LDT_fix_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            LDT_fix_cross.tStart = t
            LDT_fix_cross.frameNStart = frameN  # exact frame index
            LDT_fix_cross.setAutoDraw(True)
        frameRemains = 0.0 + rand_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if LDT_fix_cross.status == STARTED and t >= frameRemains:
            LDT_fix_cross.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDT_fix_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "LDT_fix_prac"-------
    for thisComponent in LDT_fix_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "LDT_fix_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "LDT_prac"-------
    t = 0
    LDT_pracClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.060000)
    # update component parameters for each repeat
    LDT_word_prac.setText(words)
    LDT_mask_prac.setText(mask)
    resp_LDT_prac = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    LDT_pracComponents = [LDT_word_prac, LDT_mask_prac, resp_LDT_prac, key_reminder_3]
    for thisComponent in LDT_pracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "LDT_prac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = LDT_pracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDT_word_prac* updates
        if t >= 0 and LDT_word_prac.status == NOT_STARTED:
            # keep track of start time/frame for later
            LDT_word_prac.tStart = t
            LDT_word_prac.frameNStart = frameN  # exact frame index
            LDT_word_prac.setAutoDraw(True)
        frameRemains = 0 + .06- win.monitorFramePeriod * 0.75  # most of one frame period left
        if LDT_word_prac.status == STARTED and t >= frameRemains:
            LDT_word_prac.setAutoDraw(False)
        
        # *LDT_mask_prac* updates
        if t >= .06 and LDT_mask_prac.status == NOT_STARTED:
            # keep track of start time/frame for later
            LDT_mask_prac.tStart = t
            LDT_mask_prac.frameNStart = frameN  # exact frame index
            LDT_mask_prac.setAutoDraw(True)
        frameRemains = .06 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if LDT_mask_prac.status == STARTED and t >= frameRemains:
            LDT_mask_prac.setAutoDraw(False)
        
        # *resp_LDT_prac* updates
        if t >= .06 and resp_LDT_prac.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_LDT_prac.tStart = t
            resp_LDT_prac.frameNStart = frameN  # exact frame index
            resp_LDT_prac.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_LDT_prac.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = .06 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp_LDT_prac.status == STARTED and t >= frameRemains:
            resp_LDT_prac.status = FINISHED
        if resp_LDT_prac.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp_LDT_prac.keys = theseKeys[-1]  # just the last key pressed
                resp_LDT_prac.rt = resp_LDT_prac.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # *key_reminder_3* updates
        if t >= 0.06 and key_reminder_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_reminder_3.tStart = t
            key_reminder_3.frameNStart = frameN  # exact frame index
            key_reminder_3.setAutoDraw(True)
        frameRemains = 0.06 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_reminder_3.status == STARTED and t >= frameRemains:
            key_reminder_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # check responses
    if resp_LDT_prac.keys in ['', [], None]:  # No response was made
        resp_LDT_prac.keys=None
    LDT_prac_loop.addData('resp_LDT_prac.keys',resp_LDT_prac.keys)
    if resp_LDT_prac.keys != None:  # we had a response
        LDT_prac_loop.addData('resp_LDT_prac.rt', resp_LDT_prac.rt)
    thisExp.addData('task', "LDT_prac")
    thisExp.addData('keypress', resp_LDT_prac.keys)
    thisExp.addData('RT', resp_LDT_prac.rt)
    thisExp.addData('corr', resp_LDT_prac.corr)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LDT_prac_loop'


# ------Prepare to start Routine "instr_LDT_2"-------
t = 0
instr_LDT_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp_LDT_ready = event.BuilderKeyResponse()

# keep track of which components have finished
instr_LDT_2Components = [instr_LDT9, instr_LDT10, image_6, instr_LDT11, resp_LDT_ready]
for thisComponent in instr_LDT_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_LDT_2"-------
while continueRoutine:
    # get current time
    t = instr_LDT_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_LDT9* updates
    if t >= 0.0 and instr_LDT9.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT9.tStart = t
        instr_LDT9.frameNStart = frameN  # exact frame index
        instr_LDT9.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT9.status == STARTED and t >= frameRemains:
        instr_LDT9.setAutoDraw(False)
    
    # *instr_LDT10* updates
    if t >= 4 and instr_LDT10.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT10.tStart = t
        instr_LDT10.frameNStart = frameN  # exact frame index
        instr_LDT10.setAutoDraw(True)
    frameRemains = 4 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT10.status == STARTED and t >= frameRemains:
        instr_LDT10.setAutoDraw(False)
    
    # *image_6* updates
    if t >= 10 and image_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_6.tStart = t
        image_6.frameNStart = frameN  # exact frame index
        image_6.setAutoDraw(True)
    frameRemains = 10 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_6.status == STARTED and t >= frameRemains:
        image_6.setAutoDraw(False)
    
    # *instr_LDT11* updates
    if t >= 16 and instr_LDT11.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT11.tStart = t
        instr_LDT11.frameNStart = frameN  # exact frame index
        instr_LDT11.setAutoDraw(True)
    
    # *resp_LDT_ready* updates
    if t >= 16 and resp_LDT_ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_LDT_ready.tStart = t
        resp_LDT_ready.frameNStart = frameN  # exact frame index
        resp_LDT_ready.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp_LDT_ready.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if resp_LDT_ready.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp_LDT_ready.keys = theseKeys[-1]  # just the last key pressed
            resp_LDT_ready.rt = resp_LDT_ready.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if resp_LDT_ready.keys in ['', [], None]:  # No response was made
    resp_LDT_ready.keys=None
thisExp.addData('resp_LDT_ready.keys',resp_LDT_ready.keys)
if resp_LDT_ready.keys != None:  # we had a response
    thisExp.addData('resp_LDT_ready.rt', resp_LDT_ready.rt)
thisExp.nextEntry()

# the Routine "instr_LDT_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
LDT_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/LDT_conditions.csv'),
    seed=None, name='LDT_loop')
thisExp.addLoop(LDT_loop)  # add the loop to the experiment
thisLDT_loop = LDT_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLDT_loop.rgb)
if thisLDT_loop != None:
    for paramName in thisLDT_loop:
        exec('{} = thisLDT_loop[paramName]'.format(paramName))

for thisLDT_loop in LDT_loop:
    currentLoop = LDT_loop
    # abbreviate parameter names if possible (e.g. rgb = thisLDT_loop.rgb)
    if thisLDT_loop != None:
        for paramName in thisLDT_loop:
            exec('{} = thisLDT_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "LDT_fix"-------
    t = 0
    LDT_fixClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rand_duration = random.randint(100, 300)/1000
    # keep track of which components have finished
    LDT_fixComponents = [LDT_fix_cross_2]
    for thisComponent in LDT_fixComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "LDT_fix"-------
    while continueRoutine:
        # get current time
        t = LDT_fixClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDT_fix_cross_2* updates
        if t >= 0.0 and LDT_fix_cross_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            LDT_fix_cross_2.tStart = t
            LDT_fix_cross_2.frameNStart = frameN  # exact frame index
            LDT_fix_cross_2.setAutoDraw(True)
        frameRemains = 0.0 + rand_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if LDT_fix_cross_2.status == STARTED and t >= frameRemains:
            LDT_fix_cross_2.setAutoDraw(False)
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in LDT_fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "LDT_fix"-------
    for thisComponent in LDT_fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "LDT_fix" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "LDT_trial"-------
    t = 0
    LDT_trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.060000)
    # update component parameters for each repeat
    LDT_word_2.setText(words)
    LDT_mask_2.setText(mask)
    resp_LDT = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    LDT_trialComponents = [LDT_word_2, LDT_mask_2, resp_LDT, key_reminder_4]
    for thisComponent in LDT_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "LDT_trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = LDT_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *LDT_word_2* updates
        if t >= 0 and LDT_word_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            LDT_word_2.tStart = t
            LDT_word_2.frameNStart = frameN  # exact frame index
            LDT_word_2.setAutoDraw(True)
        frameRemains = 0 + .06- win.monitorFramePeriod * 0.75  # most of one frame period left
        if LDT_word_2.status == STARTED and t >= frameRemains:
            LDT_word_2.setAutoDraw(False)
        
        # *LDT_mask_2* updates
        if t >= .06 and LDT_mask_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            LDT_mask_2.tStart = t
            LDT_mask_2.frameNStart = frameN  # exact frame index
            LDT_mask_2.setAutoDraw(True)
        frameRemains = .06 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if LDT_mask_2.status == STARTED and t >= frameRemains:
            LDT_mask_2.setAutoDraw(False)
        
        # *resp_LDT* updates
        if t >= .06 and resp_LDT.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_LDT.tStart = t
            resp_LDT.frameNStart = frameN  # exact frame index
            resp_LDT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_LDT.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = .06 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp_LDT.status == STARTED and t >= frameRemains:
            resp_LDT.status = FINISHED
        if resp_LDT.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp_LDT.keys = theseKeys[-1]  # just the last key pressed
                resp_LDT.rt = resp_LDT.clock.getTime()
                # was this 'correct'?
                if (resp_LDT.keys == str(corr_ans)) or (resp_LDT.keys == corr_ans):
                    resp_LDT.corr = 1
                else:
                    resp_LDT.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        
        # *key_reminder_4* updates
        if t >= 0.06 and key_reminder_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_reminder_4.tStart = t
            key_reminder_4.frameNStart = frameN  # exact frame index
            key_reminder_4.setAutoDraw(True)
        frameRemains = 0.06 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_reminder_4.status == STARTED and t >= frameRemains:
            key_reminder_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    # check responses
    if resp_LDT.keys in ['', [], None]:  # No response was made
        resp_LDT.keys=None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           resp_LDT.corr = 1;  # correct non-response
        else:
           resp_LDT.corr = 0;  # failed to respond (incorrectly)
    # store data for LDT_loop (TrialHandler)
    LDT_loop.addData('resp_LDT.keys',resp_LDT.keys)
    LDT_loop.addData('resp_LDT.corr', resp_LDT.corr)
    if resp_LDT.keys != None:  # we had a response
        LDT_loop.addData('resp_LDT.rt', resp_LDT.rt)
    thisExp.addData('task', "LDT")
    thisExp.addData('keypress', resp_LDT.keys)
    thisExp.addData('RT', resp_LDT.rt)
    thisExp.addData('corr', resp_LDT.corr)
    thisExp.nextEntry()
    
# completed 1 repeats of 'LDT_loop'


# ------Prepare to start Routine "instr_AMP"-------
t = 0
instr_AMPClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp_AMP_ready1 = event.BuilderKeyResponse()

# keep track of which components have finished
instr_AMPComponents = [instr_AMP1, instr_AMP2, instr_AMP3, instr_AMP4, instr_AMP5, instr_AMP6, image_4, instr_AMP7, instr_AMP8, instr_AMP13, resp_AMP_ready1]
for thisComponent in instr_AMPComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_AMP"-------
while continueRoutine:
    # get current time
    t = instr_AMPClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_AMP1* updates
    if t >= 0.0 and instr_AMP1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP1.tStart = t
        instr_AMP1.frameNStart = frameN  # exact frame index
        instr_AMP1.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP1.status == STARTED and t >= frameRemains:
        instr_AMP1.setAutoDraw(False)
    
    # *instr_AMP2* updates
    if t >= 6 and instr_AMP2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP2.tStart = t
        instr_AMP2.frameNStart = frameN  # exact frame index
        instr_AMP2.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP2.status == STARTED and t >= frameRemains:
        instr_AMP2.setAutoDraw(False)
    
    # *instr_AMP3* updates
    if t >= 12 and instr_AMP3.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP3.tStart = t
        instr_AMP3.frameNStart = frameN  # exact frame index
        instr_AMP3.setAutoDraw(True)
    frameRemains = 12 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP3.status == STARTED and t >= frameRemains:
        instr_AMP3.setAutoDraw(False)
    
    # *instr_AMP4* updates
    if t >= 18 and instr_AMP4.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP4.tStart = t
        instr_AMP4.frameNStart = frameN  # exact frame index
        instr_AMP4.setAutoDraw(True)
    frameRemains = 18 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP4.status == STARTED and t >= frameRemains:
        instr_AMP4.setAutoDraw(False)
    
    # *instr_AMP5* updates
    if t >= 28 and instr_AMP5.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP5.tStart = t
        instr_AMP5.frameNStart = frameN  # exact frame index
        instr_AMP5.setAutoDraw(True)
    frameRemains = 28 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP5.status == STARTED and t >= frameRemains:
        instr_AMP5.setAutoDraw(False)
    
    # *instr_AMP6* updates
    if t >= 34 and instr_AMP6.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP6.tStart = t
        instr_AMP6.frameNStart = frameN  # exact frame index
        instr_AMP6.setAutoDraw(True)
    frameRemains = 34 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP6.status == STARTED and t >= frameRemains:
        instr_AMP6.setAutoDraw(False)
    
    # *image_4* updates
    if t >= 40 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t
        image_4.frameNStart = frameN  # exact frame index
        image_4.setAutoDraw(True)
    frameRemains = 40 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_4.status == STARTED and t >= frameRemains:
        image_4.setAutoDraw(False)
    
    # *instr_AMP7* updates
    if t >= 46 and instr_AMP7.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP7.tStart = t
        instr_AMP7.frameNStart = frameN  # exact frame index
        instr_AMP7.setAutoDraw(True)
    frameRemains = 46 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP7.status == STARTED and t >= frameRemains:
        instr_AMP7.setAutoDraw(False)
    
    # *instr_AMP8* updates
    if t >= 52 and instr_AMP8.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP8.tStart = t
        instr_AMP8.frameNStart = frameN  # exact frame index
        instr_AMP8.setAutoDraw(True)
    frameRemains = 52 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP8.status == STARTED and t >= frameRemains:
        instr_AMP8.setAutoDraw(False)
    
    # *instr_AMP13* updates
    if t >= 58 and instr_AMP13.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP13.tStart = t
        instr_AMP13.frameNStart = frameN  # exact frame index
        instr_AMP13.setAutoDraw(True)
    
    # *resp_AMP_ready1* updates
    if t >= 58 and resp_AMP_ready1.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_AMP_ready1.tStart = t
        resp_AMP_ready1.frameNStart = frameN  # exact frame index
        resp_AMP_ready1.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp_AMP_ready1.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if resp_AMP_ready1.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp_AMP_ready1.keys = theseKeys[-1]  # just the last key pressed
            resp_AMP_ready1.rt = resp_AMP_ready1.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if resp_AMP_ready1.keys in ['', [], None]:  # No response was made
    resp_AMP_ready1.keys=None
thisExp.addData('resp_AMP_ready1.keys',resp_AMP_ready1.keys)
if resp_AMP_ready1.keys != None:  # we had a response
    thisExp.addData('resp_AMP_ready1.rt', resp_AMP_ready1.rt)
thisExp.nextEntry()

# the Routine "instr_AMP" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
AMP_prac_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/amp_testrun.csv'),
    seed=None, name='AMP_prac_loop')
thisExp.addLoop(AMP_prac_loop)  # add the loop to the experiment
thisAMP_prac_loop = AMP_prac_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAMP_prac_loop.rgb)
if thisAMP_prac_loop != None:
    for paramName in thisAMP_prac_loop:
        exec('{} = thisAMP_prac_loop[paramName]'.format(paramName))

for thisAMP_prac_loop in AMP_prac_loop:
    currentLoop = AMP_prac_loop
    # abbreviate parameter names if possible (e.g. rgb = thisAMP_prac_loop.rgb)
    if thisAMP_prac_loop != None:
        for paramName in thisAMP_prac_loop:
            exec('{} = thisAMP_prac_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AMP_prac_word"-------
    t = 0
    AMP_prac_wordClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.525000)
    # update component parameters for each repeat
    AMP_wordstim_2.setText(words)
    
    AMP_nonwordstim_3.setText(nonwords)
    # keep track of which components have finished
    AMP_prac_wordComponents = [AMP_wordstim_2, gap, AMP_nonwordstim_3]
    for thisComponent in AMP_prac_wordComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AMP_prac_word"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AMP_prac_wordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AMP_wordstim_2* updates
        if t >= 0 and AMP_wordstim_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            AMP_wordstim_2.tStart = t
            AMP_wordstim_2.frameNStart = frameN  # exact frame index
            AMP_wordstim_2.setAutoDraw(True)
        frameRemains = 0 + .1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if AMP_wordstim_2.status == STARTED and t >= frameRemains:
            AMP_wordstim_2.setAutoDraw(False)
        
        # *gap* updates
        if t >= 0.1 and gap.status == NOT_STARTED:
            # keep track of start time/frame for later
            gap.tStart = t
            gap.frameNStart = frameN  # exact frame index
            gap.setAutoDraw(True)
        frameRemains = 0.1 + .125- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gap.status == STARTED and t >= frameRemains:
            gap.setAutoDraw(False)
        
        
        # *AMP_nonwordstim_3* updates
        if t >= .225 and AMP_nonwordstim_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            AMP_nonwordstim_3.tStart = t
            AMP_nonwordstim_3.frameNStart = frameN  # exact frame index
            AMP_nonwordstim_3.setAutoDraw(True)
        frameRemains = .225 + .300- win.monitorFramePeriod * 0.75  # most of one frame period left
        if AMP_nonwordstim_3.status == STARTED and t >= frameRemains:
            AMP_nonwordstim_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AMP_prac_wordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AMP_prac_word"-------
    for thisComponent in AMP_prac_wordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "AMP_nonword_prac"-------
    t = 0
    AMP_nonword_pracClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    resp_AMP_prac = event.BuilderKeyResponse()
    
    AMP_maskstim_2.setText(mask)
    # keep track of which components have finished
    AMP_nonword_pracComponents = [resp_AMP_prac, AMP_maskstim_2, key_reminder]
    for thisComponent in AMP_nonword_pracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AMP_nonword_prac"-------
    while continueRoutine:
        # get current time
        t = AMP_nonword_pracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_AMP_prac* updates
        if t >= 0 and resp_AMP_prac.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_AMP_prac.tStart = t
            resp_AMP_prac.frameNStart = frameN  # exact frame index
            resp_AMP_prac.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_AMP_prac.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp_AMP_prac.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'escape', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if resp_AMP_prac.keys == []:  # then this was the first keypress
                    resp_AMP_prac.keys = theseKeys[0]  # just the first key pressed
                    resp_AMP_prac.rt = resp_AMP_prac.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
        
        
        # *AMP_maskstim_2* updates
        if t >= 0 and AMP_maskstim_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            AMP_maskstim_2.tStart = t
            AMP_maskstim_2.frameNStart = frameN  # exact frame index
            AMP_maskstim_2.setAutoDraw(True)
        
        # *key_reminder* updates
        if t >= 0 and key_reminder.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_reminder.tStart = t
            key_reminder.frameNStart = frameN  # exact frame index
            key_reminder.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AMP_nonword_pracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AMP_nonword_prac"-------
    for thisComponent in AMP_nonword_pracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_AMP_prac.keys in ['', [], None]:  # No response was made
        resp_AMP_prac.keys=None
    AMP_prac_loop.addData('resp_AMP_prac.keys',resp_AMP_prac.keys)
    if resp_AMP_prac.keys != None:  # we had a response
        AMP_prac_loop.addData('resp_AMP_prac.rt', resp_AMP_prac.rt)
    thisExp.addData('task', "AMP_prac")
    thisExp.addData('keypress', resp_AMP_prac.keys)
    thisExp.addData('RT', resp_AMP_prac.rt)
    # the Routine "AMP_nonword_prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'AMP_prac_loop'


# ------Prepare to start Routine "instr_AMP_2"-------
t = 0
instr_AMP_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp_AMP_ready = event.BuilderKeyResponse()

# keep track of which components have finished
instr_AMP_2Components = [instr_AMP9, instr_AMP14, image_5, instr_AMP11, resp_AMP_ready]
for thisComponent in instr_AMP_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_AMP_2"-------
while continueRoutine:
    # get current time
    t = instr_AMP_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_AMP9* updates
    if t >= 0.0 and instr_AMP9.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP9.tStart = t
        instr_AMP9.frameNStart = frameN  # exact frame index
        instr_AMP9.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP9.status == STARTED and t >= frameRemains:
        instr_AMP9.setAutoDraw(False)
    
    # *instr_AMP14* updates
    if t >= 4 and instr_AMP14.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP14.tStart = t
        instr_AMP14.frameNStart = frameN  # exact frame index
        instr_AMP14.setAutoDraw(True)
    frameRemains = 4 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP14.status == STARTED and t >= frameRemains:
        instr_AMP14.setAutoDraw(False)
    
    # *image_5* updates
    if t >= 10 and image_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_5.tStart = t
        image_5.frameNStart = frameN  # exact frame index
        image_5.setAutoDraw(True)
    frameRemains = 10 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_5.status == STARTED and t >= frameRemains:
        image_5.setAutoDraw(False)
    
    # *instr_AMP11* updates
    if t >= 16 and instr_AMP11.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP11.tStart = t
        instr_AMP11.frameNStart = frameN  # exact frame index
        instr_AMP11.setAutoDraw(True)
    
    # *resp_AMP_ready* updates
    if t >= 16 and resp_AMP_ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_AMP_ready.tStart = t
        resp_AMP_ready.frameNStart = frameN  # exact frame index
        resp_AMP_ready.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp_AMP_ready.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if resp_AMP_ready.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp_AMP_ready.keys = theseKeys[-1]  # just the last key pressed
            resp_AMP_ready.rt = resp_AMP_ready.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False  
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# check responses
if resp_AMP_ready.keys in ['', [], None]:  # No response was made
    resp_AMP_ready.keys=None
thisExp.addData('resp_AMP_ready.keys',resp_AMP_ready.keys)
if resp_AMP_ready.keys != None:  # we had a response
    thisExp.addData('resp_AMP_ready.rt', resp_AMP_ready.rt)
thisExp.nextEntry()

# the Routine "instr_AMP_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_AMP_3"-------
t = 0
instr_AMP_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat

# keep track of which components have finished
instr_AMP_3Components = [instr_AMP12]
for thisComponent in instr_AMP_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_AMP_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instr_AMP_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_AMP12* updates
    if t >= 0.0 and instr_AMP12.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_AMP12.tStart = t
        instr_AMP12.frameNStart = frameN  # exact frame index
        instr_AMP12.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_AMP12.status == STARTED and t >= frameRemains:
        instr_AMP12.setAutoDraw(False)
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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


# set up handler to look after randomisation of conditions etc
AMP_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/AMP_conditions.csv', selection='0:30'),
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
    
    # ------Prepare to start Routine "AMP_word"-------
    t = 0
    AMP_wordClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.250000)
    # update component parameters for each repeat
    AMP_wordstim.setText(words)
    
    AMP_nonwordstim_2.setText(nonwords)
    # keep track of which components have finished
    AMP_wordComponents = [AMP_wordstim, gap_1, AMP_nonwordstim_2]
    for thisComponent in AMP_wordComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AMP_word"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AMP_wordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *AMP_wordstim* updates
        if t >= 0 and AMP_wordstim.status == NOT_STARTED:
            # keep track of start time/frame for later
            AMP_wordstim.tStart = t
            AMP_wordstim.frameNStart = frameN  # exact frame index
            AMP_wordstim.setAutoDraw(True)
        frameRemains = 0 + .075- win.monitorFramePeriod * 0.75  # most of one frame period left
        if AMP_wordstim.status == STARTED and t >= frameRemains:
            AMP_wordstim.setAutoDraw(False)
        
        # *gap_1* updates
        if t >= 0.075 and gap_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            gap_1.tStart = t
            gap_1.frameNStart = frameN  # exact frame index
            gap_1.setAutoDraw(True)
        frameRemains = 0.075 + .025- win.monitorFramePeriod * 0.75  # most of one frame period left
        if gap_1.status == STARTED and t >= frameRemains:
            gap_1.setAutoDraw(False)
        
        
        # *AMP_nonwordstim_2* updates
        if t >= 0.1 and AMP_nonwordstim_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            AMP_nonwordstim_2.tStart = t
            AMP_nonwordstim_2.frameNStart = frameN  # exact frame index
            AMP_nonwordstim_2.setAutoDraw(True)
        frameRemains = 0.1 + .15- win.monitorFramePeriod * 0.75  # most of one frame period left
        if AMP_nonwordstim_2.status == STARTED and t >= frameRemains:
            AMP_nonwordstim_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AMP_wordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AMP_word"-------
    for thisComponent in AMP_wordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "AMP_nonword"-------
    t = 0
    AMP_nonwordClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    resp_AMP = event.BuilderKeyResponse()
    
    AMP_maskstim.setText(mask)
    # keep track of which components have finished
    AMP_nonwordComponents = [resp_AMP, AMP_maskstim, key_reminder_2]
    for thisComponent in AMP_nonwordComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AMP_nonword"-------
    while continueRoutine:
        # get current time
        t = AMP_nonwordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *resp_AMP* updates
        if t >= 0.0 and resp_AMP.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_AMP.tStart = t
            resp_AMP.frameNStart = frameN  # exact frame index
            resp_AMP.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_AMP.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp_AMP.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'escape', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if resp_AMP.keys == []:  # then this was the first keypress
                    resp_AMP.keys = theseKeys[0]  # just the first key pressed
                    resp_AMP.rt = resp_AMP.clock.getTime()
                    # was this 'correct'?
                    if (resp_AMP.keys == str(corr_ans)) or (resp_AMP.keys == corr_ans):
                        resp_AMP.corr = 1
                    else:
                        resp_AMP.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        
        # *AMP_maskstim* updates
        if t >= 0 and AMP_maskstim.status == NOT_STARTED:
            # keep track of start time/frame for later
            AMP_maskstim.tStart = t
            AMP_maskstim.frameNStart = frameN  # exact frame index
            AMP_maskstim.setAutoDraw(True)
        
        # *key_reminder_2* updates
        if t >= 0 and key_reminder_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_reminder_2.tStart = t
            key_reminder_2.frameNStart = frameN  # exact frame index
            key_reminder_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AMP_nonwordComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AMP_nonword"-------
    for thisComponent in AMP_nonwordComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_AMP.keys in ['', [], None]:  # No response was made
        resp_AMP.keys=None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           resp_AMP.corr = 1;  # correct non-response
        else:
           resp_AMP.corr = 0;  # failed to respond (incorrectly)
    # store data for AMP_trials (TrialHandler)
    AMP_trials.addData('resp_AMP.keys',resp_AMP.keys)
    AMP_trials.addData('resp_AMP.corr', resp_AMP.corr)
    if resp_AMP.keys != None:  # we had a response
        AMP_trials.addData('resp_AMP.rt', resp_AMP.rt)
    thisExp.addData('task', "AMP")
    thisExp.addData('keypress', resp_AMP.keys)
    thisExp.addData('RT', resp_AMP.rt)
    thisExp.addData('corr', resp_AMP.corr)
    # the Routine "AMP_nonword" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'AMP_trials'


# ------Prepare to start Routine "instr_tweets"-------
t = 0
instr_tweetsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_LDT_instr_2 = event.BuilderKeyResponse()

# keep track of which components have finished
instr_tweetsComponents = [instr_LDT1_2, instr_LDT2_2, instr_LDT3_2, instr_LDT4_2, keyboard_reminder_LDT_2, instr_LDT8_2, key_resp_LDT_instr_2]
for thisComponent in instr_tweetsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instr_tweets"-------
while continueRoutine:
    # get current time
    t = instr_tweetsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr_LDT1_2* updates
    if t >= 0.0 and instr_LDT1_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT1_2.tStart = t
        instr_LDT1_2.frameNStart = frameN  # exact frame index
        instr_LDT1_2.setAutoDraw(True)
    frameRemains = 0.0 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT1_2.status == STARTED and t >= frameRemains:
        instr_LDT1_2.setAutoDraw(False)
    
    # *instr_LDT2_2* updates
    if t >= 6 and instr_LDT2_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT2_2.tStart = t
        instr_LDT2_2.frameNStart = frameN  # exact frame index
        instr_LDT2_2.setAutoDraw(True)
    frameRemains = 6 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT2_2.status == STARTED and t >= frameRemains:
        instr_LDT2_2.setAutoDraw(False)
    
    # *instr_LDT3_2* updates
    if t >= 12 and instr_LDT3_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT3_2.tStart = t
        instr_LDT3_2.frameNStart = frameN  # exact frame index
        instr_LDT3_2.setAutoDraw(True)
    frameRemains = 12 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT3_2.status == STARTED and t >= frameRemains:
        instr_LDT3_2.setAutoDraw(False)
    
    # *instr_LDT4_2* updates
    if t >= 18 and instr_LDT4_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT4_2.tStart = t
        instr_LDT4_2.frameNStart = frameN  # exact frame index
        instr_LDT4_2.setAutoDraw(True)
    frameRemains = 18 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if instr_LDT4_2.status == STARTED and t >= frameRemains:
        instr_LDT4_2.setAutoDraw(False)
    
    # *keyboard_reminder_LDT_2* updates
    if t >= 24 and keyboard_reminder_LDT_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyboard_reminder_LDT_2.tStart = t
        keyboard_reminder_LDT_2.frameNStart = frameN  # exact frame index
        keyboard_reminder_LDT_2.setAutoDraw(True)
    frameRemains = 24 + 6- win.monitorFramePeriod * 0.75  # most of one frame period left
    if keyboard_reminder_LDT_2.status == STARTED and t >= frameRemains:
        keyboard_reminder_LDT_2.setAutoDraw(False)
    
    # *instr_LDT8_2* updates
    if t >= 30 and instr_LDT8_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr_LDT8_2.tStart = t
        instr_LDT8_2.frameNStart = frameN  # exact frame index
        instr_LDT8_2.setAutoDraw(True)
    
    # *key_resp_LDT_instr_2* updates
    if t >= 30 and key_resp_LDT_instr_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_LDT_instr_2.tStart = t
        key_resp_LDT_instr_2.frameNStart = frameN  # exact frame index
        key_resp_LDT_instr_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_LDT_instr_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_LDT_instr_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['right'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_LDT_instr_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_LDT_instr_2.rt = key_resp_LDT_instr_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    keys = event.getKeys()
    if 'j' in keys:
            continueRoutine = False 
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_tweetsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_tweets"-------
for thisComponent in instr_tweetsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_LDT_instr_2.keys in ['', [], None]:  # No response was made
    key_resp_LDT_instr_2.keys=None
thisExp.addData('key_resp_LDT_instr_2.keys',key_resp_LDT_instr_2.keys)
if key_resp_LDT_instr_2.keys != None:  # we had a response
    thisExp.addData('key_resp_LDT_instr_2.rt', key_resp_LDT_instr_2.rt)
thisExp.nextEntry()

# the Routine "instr_tweets" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tweet_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('condition_files/tweets.xlsx'),
    seed=None, name='tweet_loop')
thisExp.addLoop(tweet_loop)  # add the loop to the experiment
thisTweet_loop = tweet_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTweet_loop.rgb)
if thisTweet_loop != None:
    for paramName in thisTweet_loop:
        exec('{} = thisTweet_loop[paramName]'.format(paramName))

for thisTweet_loop in tweet_loop:
    currentLoop = tweet_loop
    # abbreviate parameter names if possible (e.g. rgb = thisTweet_loop.rgb)
    if thisTweet_loop != None:
        for paramName in thisTweet_loop:
            exec('{} = thisTweet_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "tweets"-------
    t = 0
    tweetsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    tweet.setText(tweets)
    resp_tweets = event.BuilderKeyResponse()
    
    # keep track of which components have finished
    tweetsComponents = [tweet, resp_tweets]
    for thisComponent in tweetsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "tweets"-------
    while continueRoutine:
        # get current time
        t = tweetsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *tweet* updates
        if t >= 0 and tweet.status == NOT_STARTED:
            # keep track of start time/frame for later
            tweet.tStart = t
            tweet.frameNStart = frameN  # exact frame index
            tweet.setAutoDraw(True)
        
        # *resp_tweets* updates
        if t >= 1 and resp_tweets.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_tweets.tStart = t
            resp_tweets.frameNStart = frameN  # exact frame index
            resp_tweets.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_tweets.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 1 + 9- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp_tweets.status == STARTED and t >= frameRemains:
            resp_tweets.status = FINISHED
        if resp_tweets.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                resp_tweets.keys = theseKeys[-1]  # just the last key pressed
                resp_tweets.rt = resp_tweets.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tweetsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "tweets"-------
    for thisComponent in tweetsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp_tweets.keys in ['', [], None]:  # No response was made
        resp_tweets.keys=None
    tweet_loop.addData('resp_tweets.keys',resp_tweets.keys)
    if resp_tweets.keys != None:  # we had a response
        tweet_loop.addData('resp_tweets.rt', resp_tweets.rt)
    thisExp.addData('task', "tweets")
    thisExp.addData('keypress', resp_tweets.keys)
    thisExp.addData('RT', resp_tweets.rt)
    # the Routine "tweets" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'tweet_loop'









os.remove("AMP_conditions.csv")







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
