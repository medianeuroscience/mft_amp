#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.3),
    on Sat Feb 16 23:02:31 2019
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
expName = 'mf_amp'  # from the Builder filename that created this script
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
    originPath='/Users/jacobfisher/projects/inprogress/mf_amp/exp_files/mf_amp_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[.8,.8,.8], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "AMP_word"
AMP_wordClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
import random
import pandas as pd

words = pd.read_csv("words4exp.csv")

full_list = list(range(0,341))
care_virtue = list(range(0,12))
care_vice = list(range(12,24))
fair_virtue = list(range(24,36))
fair_vice = list(range(36,48))
loyal_virtue = list(range(48,60))
loyal_vice = list(range(60,72))
auth_virtue = list(range(72,84))
auth_vice = list(range(84,96))
sanc_virtue = list(range(96,108))
sanc_vice = list(range(108,120))
neutral = list(range(120,170))
nonword = list(range(170,340))
control = [340,341]

care_virtue_amp = random.sample(care_virtue, 7) 
care_vice_amp = random.sample(care_vice, 7)
fair_virtue_amp = random.sample(fair_virtue, 7) 
fair_vice_amp = random.sample(fair_vice, 7)
loyal_virtue_amp = random.sample(loyal_virtue, 7) 
loyal_vice_amp = random.sample(loyal_vice, 7)
auth_virtue_amp = random.sample(auth_virtue, 7) 
auth_vice_amp = random.sample(auth_vice, 7)
sanc_virtue_amp = random.sample(sanc_virtue, 7) 
sanc_vice_amp = random.sample(sanc_vice, 7)
nonword_amp = random.sample(nonword, 72)
control_amp = control

AMP_words = care_virtue_amp + care_vice_amp + fair_virtue_amp + fair_vice_amp + loyal_virtue_amp + loyal_vice_amp + auth_virtue_amp + auth_vice_amp + sanc_virtue_amp + sanc_vice_amp + control_amp

AMP_wordlist = words.loc[AMP_words].word.values
AMP_masklist = words.loc[nonword_amp].masks.values
AMP_nonwordlist = words.loc[nonword_amp].word.values
AMP_corr_ans = words.loc[AMP_words].correct_amp.values

df1 = pd.DataFrame(
    {'words': AMP_wordlist.tolist(),
     'corr_ans': AMP_corr_ans.tolist()
    })

df2 = pd.DataFrame(
     {'nonwords': AMP_nonwordlist.tolist(),
     'masks': AMP_masklist.tolist(),
    })


df1 = df1.sample(frac=1).reset_index(drop=True)
df2 = df2.sample(frac=1).reset_index(drop=True)

df_full = pd.concat([df1,df2], axis = 1)

df_full.to_csv("AMP_conditions.csv")

# Initialize components for Routine "AMP_nonword"
AMP_nonwordClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

text_6 = visual.TextStim(win=win, name='text_6',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('AMP_conditions.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "AMP_word"-------
    t = 0
    AMP_wordClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.875000)
    # update component parameters for each repeat
    text_4.setText(words)
    
    # keep track of which components have finished
    AMP_wordComponents = [text_4, text_5]
    for thisComponent in AMP_wordComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AMP_word"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AMP_wordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        frameRemains = 0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_4.status == STARTED and t >= frameRemains:
            text_4.setAutoDraw(False)
        
        # *text_5* updates
        if t >= 0.75 and text_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_5.tStart = t
            text_5.frameNStart = frameN  # exact frame index
            text_5.setAutoDraw(True)
        frameRemains = 0.75 + .125- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_5.status == STARTED and t >= frameRemains:
            text_5.setAutoDraw(False)
        
        
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
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    text.setText(nonwords)
    resp_1 = event.BuilderKeyResponse()
    
    text_6.setText(masks)
    # keep track of which components have finished
    AMP_nonwordComponents = [text, resp_1, text_6]
    for thisComponent in AMP_nonwordComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "AMP_nonword"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = AMP_nonwordClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + .75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
        # *resp_1* updates
        if t >= 0.0 and resp_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp_1.tStart = t
            resp_1.frameNStart = frameN  # exact frame index
            resp_1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp_1.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if resp_1.status == STARTED and t >= frameRemains:
            resp_1.status = FINISHED
        if resp_1.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right', 'escape', 'n'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if resp_1.keys == []:  # then this was the first keypress
                    resp_1.keys = theseKeys[0]  # just the first key pressed
                    resp_1.rt = resp_1.clock.getTime()
                    # was this 'correct'?
                    if (resp_1.keys == str(corr_ans)) or (resp_1.keys == corr_ans):
                        resp_1.corr = 1
                    else:
                        resp_1.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        
        
        # *text_6* updates
        if t >= 0.75 and text_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_6.tStart = t
            text_6.frameNStart = frameN  # exact frame index
            text_6.setAutoDraw(True)
        frameRemains = 0.75 + 3.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_6.status == STARTED and t >= frameRemains:
            text_6.setAutoDraw(False)
        
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
    if resp_1.keys in ['', [], None]:  # No response was made
        resp_1.keys=None
        # was no response the correct answer?!
        if str(corr_ans).lower() == 'none':
           resp_1.corr = 1;  # correct non-response
        else:
           resp_1.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp_1.keys',resp_1.keys)
    trials.addData('resp_1.corr', resp_1.corr)
    if resp_1.keys != None:  # we had a response
        trials.addData('resp_1.rt', resp_1.rt)
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

os.remove("AMP_conditions.csv")

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
