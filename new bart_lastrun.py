#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.01), November 26, 2015, at 17:01
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'new bart'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\The E-R\\Desktop\\new bart\\new bart.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1366, 768), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Throughout the task, you will be presented with 90 balloons, one at a time. For each balloon you can press the Spacebar button to pump and increase the size of the balloon. You will accumulate 5 points in a temporary bank for each pump. You will not be shown the amount you have accumulated in your temporary bank. At any point, you can stop pumping up the balloon and press the Enter button. Pressing the Enter button will start you on the next balloon and will transfer the accumulated points from your temporary bank to your permanent bank labeled \u201cTotal Earned.\u201d The amount you earned on the previous balloon is shown in the box labeled \u201cLast Balloon.\u201d It is your choice to determine how much to pump up the balloon, but be aware that at some point the balloon will explode. The explosion point varies across balloons, ranging from the first pump to enough pumps to make the balloon fill the entire computer screen. If the balloon explodes before you press the Enter button to collect the accumulated points, then you move on to the next balloon and all points in your temporary bank are lost. Exploded balloons do not affect the points accumulated in your permanent bank.\n\nPress SPACEBAR to start.',    font=u'Arial',
    pos=[0, 0], height=0.065, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
#initialize maximum number of pumps
maxPumps = 999

#initialize scoring variables
#round score
rscore = 0
#last round score
lscore = 0
#total score
tscore = 0
BalloonImage = visual.ImageStim(win=win, name='BalloonImage',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
bankedEarnings=0.0
lastBalloonEarnings=0.0
thisBalloonEarnings=0.0
balloonSize=0.08
balloonMsgHeight=0.01
Banked = visual.TextStim(win=win, ori=0, name='Banked',
    text='default text',    font=u'Arial',
    pos=[0, 0.8], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0)

# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
from psychopy import sound
bang = sound.Sound("bang.wav")
cash = sound.Sound("cashregister.wav")
#when the balloon pops, it will play the bang.wav file
#when the user banks, the cash register sound file will play 

# Initialize components for Routine "FinalScore"
FinalScoreClock = core.Clock()
finalscore = visual.TextStim(win=win, ori=0, name='finalscore',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(text)
InstructionsComponents.append(key_resp_2)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialtypes.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    #set the maximum number of pumps to be a random number between 1 and the maximum pumsp for the balloon
    maxPumps = randint(1, balloonrisk)
    
    #reset round score to 0
    rscore = 0
    BalloonImage.setImage(balloonpic)
    
    BankButton = event.BuilderKeyResponse()  # create an object of type KeyResponse
    BankButton.status = NOT_STARTED
    balloonSize=0.08
    popped=False
    nPumps=0
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(BalloonImage)
    trialComponents.append(BankButton)
    trialComponents.append(Banked)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if event.getKeys(['space']):
            nPumps+=1
            rscore +=1
            if nPumps>maxPumps:
                popped=True
                continueRoutine=False
                rscore = 0
        
        # *BalloonImage* updates
        if t >= 0.0 and BalloonImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            BalloonImage.tStart = t  # underestimates by a little under one frame
            BalloonImage.frameNStart = frameN  # exact frame index
            BalloonImage.setAutoDraw(True)
        if BalloonImage.status == STARTED:  # only update if being drawn
            BalloonImage.setPos([0+balloonSize/2,0], log=False)
            BalloonImage.setSize(balloonSize, log=False)
        thisBalloonEarnings=nPumps*0.05
        
        # *BankButton* updates
        if t >= 0.0 and BankButton.status == NOT_STARTED:
            # keep track of start time/frame for later
            BankButton.tStart = t  # underestimates by a little under one frame
            BankButton.frameNStart = frameN  # exact frame index
            BankButton.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if BankButton.status == STARTED:
            theseKeys = event.getKeys(keyList=['return'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        balloonSize=0.1+nPumps*0.015
        
        # *Banked* updates
        if t >= 0.0 and Banked.status == NOT_STARTED:
            # keep track of start time/frame for later
            Banked.tStart = t  # underestimates by a little under one frame
            Banked.frameNStart = frameN  # exact frame index
            Banked.setAutoDraw(True)
        if Banked.status == STARTED:  # only update if being drawn
            Banked.setText(u"You have banked:\n%.2f points" %rscore, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #set last round score to current round score
    lscore = rscore
    #add current round score to total score
    tscore += rscore
    #calculate cash 'earned'
    if popped:
      thisBalloonEarnings=0.0
      lastBalloonEarnings=0.0
    else:   lastBalloonEarnings=thisBalloonEarnings
    bankedEarnings = bankedEarnings+lastBalloonEarnings
    #save data
    trials.addData('nPumps', nPumps)
    trials.addData('size', balloonSize)
    trials.addData('earnings', thisBalloonEarnings)
    trials.addData('popped', popped)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "Feedback"-------
    t = 0
    FeedbackClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if popped==True:
      bang.play()
    else:
      cash.play()
    # keep track of which components have finished
    FeedbackComponents = []
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Feedback"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "FinalScore"-------
t = 0
FinalScoreClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
finalscore.setText(u"You earned a total of\n%2.f points!" %tscore)
DoneKey = event.BuilderKeyResponse()  # create an object of type KeyResponse
DoneKey.status = NOT_STARTED
# keep track of which components have finished
FinalScoreComponents = []
FinalScoreComponents.append(finalscore)
FinalScoreComponents.append(DoneKey)
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "FinalScore"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = FinalScoreClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finalscore* updates
    if t >= 0.0 and finalscore.status == NOT_STARTED:
        # keep track of start time/frame for later
        finalscore.tStart = t  # underestimates by a little under one frame
        finalscore.frameNStart = frameN  # exact frame index
        finalscore.setAutoDraw(True)
    
    # *DoneKey* updates
    if t >= 0.0 and DoneKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        DoneKey.tStart = t  # underestimates by a little under one frame
        DoneKey.frameNStart = frameN  # exact frame index
        DoneKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if DoneKey.status == STARTED:
        theseKeys = event.getKeys(keyList=['q', 'return'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalScoreComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "FinalScore"-------
for thisComponent in FinalScoreComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "FinalScore" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()




win.close()
core.quit()
