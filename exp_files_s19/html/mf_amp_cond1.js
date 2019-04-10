/********************* 
 * Mf_Amp_Cond1 Test *
 *********************/

import { PsychoJS } from './lib/core-3.0.3.js';
import * as core from './lib/core-3.0.3.js';
import { TrialHandler } from './lib/data-3.0.3.js';
import { Scheduler } from './lib/util-3.0.3.js';
import * as util from './lib/util-3.0.3.js';
import * as visual from './lib/visual-3.0.3.js';
import { Sound } from './lib/sound-3.0.3.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.765, 0.765, 0.765]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'mf_amp_cond1';  // from the Builder filename that created this script
let expInfo = {'participant': ''};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(holdRoutineBegin);
flowScheduler.add(holdRoutineEachFrame);
flowScheduler.add(holdRoutineEnd);
flowScheduler.add(instr1RoutineBegin);
flowScheduler.add(instr1RoutineEachFrame);
flowScheduler.add(instr1RoutineEnd);
flowScheduler.add(instr_logoRoutineBegin);
flowScheduler.add(instr_logoRoutineEachFrame);
flowScheduler.add(instr_logoRoutineEnd);
flowScheduler.add(fixRoutineBegin);
flowScheduler.add(fixRoutineEachFrame);
flowScheduler.add(fixRoutineEnd);
flowScheduler.add(logo_pracRoutineBegin);
flowScheduler.add(logo_pracRoutineEachFrame);
flowScheduler.add(logo_pracRoutineEnd);
flowScheduler.add(instr_logo_2RoutineBegin);
flowScheduler.add(instr_logo_2RoutineEachFrame);
flowScheduler.add(instr_logo_2RoutineEnd);
const logo_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(logo_trialsLoopBegin, logo_trialsLoopScheduler);
flowScheduler.add(logo_trialsLoopScheduler);
flowScheduler.add(logo_trialsLoopEnd);
flowScheduler.add(instr_AMPRoutineBegin);
flowScheduler.add(instr_AMPRoutineEachFrame);
flowScheduler.add(instr_AMPRoutineEnd);
const AMP_pracsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AMP_pracsLoopBegin, AMP_pracsLoopScheduler);
flowScheduler.add(AMP_pracsLoopScheduler);
flowScheduler.add(AMP_pracsLoopEnd);
flowScheduler.add(instr_AMP_2RoutineBegin);
flowScheduler.add(instr_AMP_2RoutineEachFrame);
flowScheduler.add(instr_AMP_2RoutineEnd);
flowScheduler.add(instr_AMP_3RoutineBegin);
flowScheduler.add(instr_AMP_3RoutineEachFrame);
flowScheduler.add(instr_AMP_3RoutineEnd);
const AMP_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(AMP_trialsLoopBegin, AMP_trialsLoopScheduler);
flowScheduler.add(AMP_trialsLoopScheduler);
flowScheduler.add(AMP_trialsLoopEnd);
flowScheduler.add(AMP_feedbackRoutineBegin);
flowScheduler.add(AMP_feedbackRoutineEachFrame);
flowScheduler.add(AMP_feedbackRoutineEnd);
flowScheduler.add(instr_LDTRoutineBegin);
flowScheduler.add(instr_LDTRoutineEachFrame);
flowScheduler.add(instr_LDTRoutineEnd);
const LDT_pracsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LDT_pracsLoopBegin, LDT_pracsLoopScheduler);
flowScheduler.add(LDT_pracsLoopScheduler);
flowScheduler.add(LDT_pracsLoopEnd);
flowScheduler.add(instr_LDT_2RoutineBegin);
flowScheduler.add(instr_LDT_2RoutineEachFrame);
flowScheduler.add(instr_LDT_2RoutineEnd);
const LDT_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(LDT_trialsLoopBegin, LDT_trialsLoopScheduler);
flowScheduler.add(LDT_trialsLoopScheduler);
flowScheduler.add(LDT_trialsLoopEnd);
flowScheduler.add(LDT_feedbackRoutineBegin);
flowScheduler.add(LDT_feedbackRoutineEachFrame);
flowScheduler.add(LDT_feedbackRoutineEnd);
flowScheduler.add(endRoutineBegin);
flowScheduler.add(endRoutineEachFrame);
flowScheduler.add(endRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.0.3';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var holdClock;
var text;
var instr1Clock;
var instr_2;
var instr_3;
var instr_4;
var instr_5;
var instr_6;
var image;
var instr_7;
var instr_logoClock;
var instr_logo1;
var instr_logo2;
var instr_logo3;
var instr_logo4;
var instr_logo5;
var logo_example;
var instr_logo6;
var logo_prac_layout_reminder;
var instr_logo7;
var instr_logo8;
var fixClock;
var LDT_fix_cross;
var logo_pracClock;
var img_logo_prac;
var mask_logo_prac;
var key_reminder_logo_prac;
var instr_logo_2Clock;
var instr_logo9;
var instr_logo10;
var image_7;
var instr_logo11;
var logo_trialClock;
var img_logo_prac_2;
var mask_logo_prac_2;
var key_reminder_logo_prac_2;
var instr_AMPClock;
var instr_AMP1_1;
var instr_AMP1_2;
var instr_AMP1_3;
var instr_AMP1_4;
var instr_AMP1_5;
var instr_AMP1_6;
var image_4;
var instr_AMP1_7;
var instr_AMP1_8;
var instr_AMP1_9;
var instr_AMP1_10;
var AMP_prac_wordClock;
var AMP_wordstim_2;
var gap;
var AMP_nonwordstim_3;
var AMP_prac_maskClock;
var AMP_maskstim_2;
var key_reminder;
var instr_AMP_2Clock;
var instr_AMP2_1;
var instr_AMP2_2;
var image_5;
var instr_AMP2_3;
var instr_AMP_3Clock;
var instr_AMP3_1;
var AMP_trial_wordClock;
var AMP_wordstim;
var gap_1;
var AMP_nonwordstim_2;
var AMP_trial_maskClock;
var AMP_maskstim;
var key_reminder_2;
var AMP_feedbackClock;
var AMP_feedback_instr;
var instr_LDTClock;
var instr_LDT1;
var instr_LDT2;
var instr_LDT3;
var instr_LDT4;
var instr_LDT5;
var instr_LDT6;
var image_3;
var keyboard_reminder_LDT;
var instr_LDT7;
var instr_LT8;
var instr_LDT9_;
var LDT_pracClock;
var LDT_word_prac;
var LDT_mask_prac;
var key_reminder_3;
var instr_LDT_2Clock;
var instr_LDT9;
var instr_LDT10;
var image_6;
var instr_LDT11;
var LDT_trialClock;
var LDT_word_2;
var LDT_mask_2;
var key_reminder_4;
var LDT_feedbackClock;
var LDT_feedback_inst;
var endClock;
var instr_end;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "hold"
  holdClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the Language, Symbols, and Emotion study! Please wait until a researcher says you may begin.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  
  // Initialize components for Routine "instr1"
  instr1Clock = new util.Clock();
  instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_2',
    text: 'The goal of this experiment is to better understand how people react to symbols and understand language',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_3',
    text: 'You will be asked to complete three different tasks, followed by a short survey.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_4',
    text: 'Before we begin, please make sure your fingers are on the correct keys.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  instr_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_5',
    text: 'Your right index finger should be on the left arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  instr_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_6',
    text: 'Your right ring finger should be on the right arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -4.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', 
    image : 'images/keyboard_diagram.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  instr_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_7',
    text: 'If you are ready to begin please press the right arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -6.0 
  });
  
  
  // Initialize components for Routine "instr_logo"
  instr_logoClock = new util.Clock();
  instr_logo1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo1',
    text: 'Welcome to the first task! In this task, you will see a selection of symbols.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_logo2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo2',
    text: 'You will be asked to rate whether each symbol you see makes you feel pleasant or unpleasant.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_logo3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo3',
    text: 'If the symbol made you feel pleasant, press the RIGHT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  instr_logo4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo4',
    text: 'If the symbol made you feel unpleasant, press the LEFT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  instr_logo5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo5',
    text: 'The symbol will look something like this.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -4.0 
  });
  
  logo_example = new visual.ImageStim({
    win : psychoJS.window,
    name : 'logo_example', 
    image : 'images/symbols/symbol_1.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  instr_logo6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo6',
    text: 'Remember that you will press RIGHT if the symbol made you feel pleasant and LEFT if the symbol made you feel unpleasant.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -6.0 
  });
  
  logo_prac_layout_reminder = new visual.ImageStim({
    win : psychoJS.window,
    name : 'logo_prac_layout_reminder', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  instr_logo7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo7',
    text: 'First, we will do a brief practice round.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -8.0 
  });
  
  instr_logo8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo8',
    text: 'When you are ready to begin, press the RIGHT arrow key.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -9.0 
  });
  
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  LDT_fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDT_fix_cross', 
    image : 'images/crosshair.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  
  // Initialize components for Routine "logo_prac"
  logo_pracClock = new util.Clock();
  img_logo_prac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_logo_prac', 
    image : 'images/symbols/symbol_2.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  mask_logo_prac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_logo_prac', units : 'height', 
    image : 'images/symbols/mask.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_reminder_logo_prac = new visual.ImageStim({
    win : psychoJS.window,
    name : 'key_reminder_logo_prac', units : 'deg', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, (- 6)], size : [20, 10],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "instr_logo_2"
  instr_logo_2Clock = new util.Clock();
  instr_logo9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo9',
    text: 'Great job!',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_logo10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo10',
    text: 'Remember that LEFT is unpleasant and RIGHT is pleasant.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  instr_logo11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_logo11',
    text: 'If you are ready to begin, please press the RIGHT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  LDT_fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDT_fix_cross', 
    image : 'images/crosshair.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  
  // Initialize components for Routine "logo_trial"
  logo_trialClock = new util.Clock();
  img_logo_prac_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'img_logo_prac_2', 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  mask_logo_prac_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_logo_prac_2', units : 'height', 
    image : 'images/symbols/mask.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.1, 0.1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  key_reminder_logo_prac_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'key_reminder_logo_prac_2', units : 'deg', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, (- 6)], size : [20, 10],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "instr_AMP"
  instr_AMPClock = new util.Clock();
  instr_AMP1_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_1',
    text: 'Welcome to the second task! In this task, you will see a selection of symbols.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_AMP1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_2',
    text: 'Before you see each symbol, you will see a string of letters.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_AMP1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_3',
    text: 'This string of letters is a cue that the symbol is about to appear',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  instr_AMP1_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_4',
    text: 'You will be asked to rate whether each symbol makes you feel pleasant or unpleasant.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  instr_AMP1_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_5',
    text: 'If the symbol made you feel pleasant, press the RIGHT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -4.0 
  });
  
  instr_AMP1_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_6',
    text: 'If the symbol made you feel unpleasant, press the LEFT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -5.0 
  });
  
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  instr_AMP1_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_7',
    text: 'Remember to press RIGHT for pleasant and LEFT for unpleasant',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -7.0 
  });
  
  instr_AMP1_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_8',
    text: 'The symbol will quickly disappear and will be replaced with white noise, so be sure to make your responses as quickly as possible.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -8.0 
  });
  
  instr_AMP1_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_9',
    text: "Let's do a practice round.",
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -9.0 
  });
  
  instr_AMP1_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP1_10',
    text: 'When you are ready to begin press the right arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -10.0 
  });
  
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  LDT_fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDT_fix_cross', 
    image : 'images/crosshair.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  
  // Initialize components for Routine "AMP_prac_word"
  AMP_prac_wordClock = new util.Clock();
  AMP_wordstim_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_wordstim_2',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  gap = new visual.TextStim({
    win: psychoJS.window,
    name: 'gap',
    text: '',
    font: 'Verdana',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  AMP_nonwordstim_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_nonwordstim_3',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "AMP_prac_mask"
  AMP_prac_maskClock = new util.Clock();
  
  AMP_maskstim_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_maskstim_2',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  key_reminder = new visual.ImageStim({
    win : psychoJS.window,
    name : 'key_reminder', units : 'deg', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, (- 6)], size : [20, 10],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "instr_AMP_2"
  instr_AMP_2Clock = new util.Clock();
  instr_AMP2_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP2_1',
    text: 'Great job!',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_AMP2_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP2_2',
    text: 'Remember that LEFT is unpleasant and RIGHT is pleasant.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  instr_AMP2_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP2_3',
    text: 'If you are ready to begin, please press the right arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  
  // Initialize components for Routine "instr_AMP_3"
  instr_AMP_3Clock = new util.Clock();
  instr_AMP3_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_AMP3_1',
    text: "Let's go!",
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  LDT_fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDT_fix_cross', 
    image : 'images/crosshair.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  
  // Initialize components for Routine "AMP_trial_word"
  AMP_trial_wordClock = new util.Clock();
  AMP_wordstim = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_wordstim',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  gap_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'gap_1',
    text: '',
    font: 'Verdana',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  
  AMP_nonwordstim_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_nonwordstim_2',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "AMP_trial_mask"
  AMP_trial_maskClock = new util.Clock();
  
  AMP_maskstim = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_maskstim',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  key_reminder_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'key_reminder_2', units : 'deg', 
    image : 'images/layout_reminder_AMP.png', mask : undefined,
    ori : 0, pos : [0, (- 6)], size : [20, 10],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  // Initialize components for Routine "AMP_feedback"
  AMP_feedbackClock = new util.Clock();
  AMP_feedback_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'AMP_feedback_instr',
    text: 'You will now respond to a few questions. Please note that your responses to these questions are completely anonymous and will not affect your SONA credit in any way.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  
  // Initialize components for Routine "instr_LDT"
  instr_LDTClock = new util.Clock();
  instr_LDT1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT1',
    text: 'Welcome to the third task! In this task, you will see a selection of real words and nonsense words.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_LDT2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT2',
    text: 'You will see a real word or a nonsense word quickly followed by a string of "&" symbols\n',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  instr_LDT3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT3',
    text: 'Upon seeing the "&" symbols, you should decide as quickly as possible whether you saw a real word or nonsense word',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -2.0 
  });
  
  instr_LDT4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT4',
    text: 'If you think you saw a real word, press the RIGHT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  instr_LDT5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT5',
    text: 'If you think you saw a nonsense word, press the LEFT arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -4.0 
  });
  
  instr_LDT6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT6',
    text: 'Please make sure your fingers are in the correct place',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -5.0 
  });
  
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', 
    image : 'images/keyboard_diagram.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -6.0 
  });
  keyboard_reminder_LDT = new visual.ImageStim({
    win : psychoJS.window,
    name : 'keyboard_reminder_LDT', 
    image : 'images/layout_reminder_LDT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -7.0 
  });
  instr_LDT7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT7',
    text: 'The words may be difficult to see, but please do the best you can',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -8.0 
  });
  
  instr_LT8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LT8',
    text: "Let's do a practice round",
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -9.0 
  });
  
  instr_LDT9_ = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT9_',
    text: 'When you are ready to begin, press the right arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -10.0 
  });
  
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  LDT_fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDT_fix_cross', 
    image : 'images/crosshair.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  
  // Initialize components for Routine "LDT_prac"
  LDT_pracClock = new util.Clock();
  LDT_word_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDT_word_prac',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  LDT_mask_prac = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDT_mask_prac',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  
  key_reminder_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'key_reminder_3', units : 'deg', 
    image : 'images/layout_reminder_LDT.png', mask : undefined,
    ori : 0, pos : [0, (- 6)], size : [20, 10],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "instr_LDT_2"
  instr_LDT_2Clock = new util.Clock();
  instr_LDT9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT9',
    text: 'Great job!',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  instr_LDT10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT10',
    text: 'Remember that LEFT is nonsense word and RIGHT is real word.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', 
    image : 'images/layout_reminder_LDT.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.9, 0.5],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -2.0 
  });
  instr_LDT11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_LDT11',
    text: 'If you are ready to begin, please press the right arrow key',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -3.0 
  });
  
  
  // Initialize components for Routine "fix"
  fixClock = new util.Clock();
  LDT_fix_cross = new visual.ImageStim({
    win : psychoJS.window,
    name : 'LDT_fix_cross', 
    image : 'images/crosshair.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.05, 0.05],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  
  // Initialize components for Routine "LDT_trial"
  LDT_trialClock = new util.Clock();
  LDT_word_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDT_word_2',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  LDT_mask_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDT_mask_2',
    text: 'default text',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  
  key_reminder_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'key_reminder_4', units : 'deg', 
    image : 'images/layout_reminder_LDT.png', mask : undefined,
    ori : 0, pos : [0, (- 6)], size : [20, 10],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "LDT_feedback"
  LDT_feedbackClock = new util.Clock();
  LDT_feedback_inst = new visual.TextStim({
    win: psychoJS.window,
    name: 'LDT_feedback_inst',
    text: 'You will now respond to a question. Please note that your response to this question is completely anonymous and will not affect your SONA credit in any way.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: -1.0 
  });
  
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  instr_end = new visual.TextStim({
    win: psychoJS.window,
    name: 'instr_end',
    text: 'Thank you for participating. You will now respond to a short survey.',
    font: 'Verdana',
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('#212121'),  opacity: 1,
    depth: 0.0 
  });
  
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var begin_key;
var holdComponents;
function holdRoutineBegin() {
  //------Prepare to start Routine 'hold'-------
  t = 0;
  holdClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  begin_key = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  holdComponents = [];
  holdComponents.push(text);
  holdComponents.push(begin_key);
  
  for (const thisComponent of holdComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function holdRoutineEachFrame() {
  //------Loop for each frame of Routine 'hold'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = holdClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  
  // *begin_key* updates
  if (t >= 0.0 && begin_key.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    begin_key.tStart = t;  // (not accounting for frame time here)
    begin_key.frameNStart = frameN;  // exact frame index
    begin_key.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { begin_key.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (begin_key.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      begin_key.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      begin_key.rt = begin_key.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of holdComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function holdRoutineEnd() {
  //------Ending Routine 'hold'-------
  for (const thisComponent of holdComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (begin_key.keys === undefined || begin_key.keys.length === 0) {    // No response was made
      begin_key.keys = undefined;
  }
  
  psychoJS.experiment.addData('begin_key.keys', begin_key.keys);
  if (typeof begin_key.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('begin_key.rt', begin_key.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "hold" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_AMP_instr1;
var instr1Components;
function instr1RoutineBegin() {
  //------Prepare to start Routine 'instr1'-------
  t = 0;
  instr1Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_AMP_instr1 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr1Components = [];
  instr1Components.push(instr_2);
  instr1Components.push(instr_3);
  instr1Components.push(instr_4);
  instr1Components.push(instr_5);
  instr1Components.push(instr_6);
  instr1Components.push(image);
  instr1Components.push(instr_7);
  instr1Components.push(key_resp_AMP_instr1);
  
  for (const thisComponent of instr1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function instr1RoutineEachFrame() {
  //------Loop for each frame of Routine 'instr1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_2* updates
  if (t >= 0 && instr_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_2.tStart = t;  // (not accounting for frame time here)
    instr_2.frameNStart = frameN;  // exact frame index
    instr_2.setAutoDraw(true);
  }

  frameRemains = 0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_2.setAutoDraw(false);
  }
  
  // *instr_3* updates
  if (t >= 6 && instr_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_3.tStart = t;  // (not accounting for frame time here)
    instr_3.frameNStart = frameN;  // exact frame index
    instr_3.setAutoDraw(true);
  }

  frameRemains = 6 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_3.setAutoDraw(false);
  }
  
  // *instr_4* updates
  if (t >= 12 && instr_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_4.tStart = t;  // (not accounting for frame time here)
    instr_4.frameNStart = frameN;  // exact frame index
    instr_4.setAutoDraw(true);
  }

  frameRemains = 12 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_4.setAutoDraw(false);
  }
  
  // *instr_5* updates
  if (t >= 18 && instr_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_5.tStart = t;  // (not accounting for frame time here)
    instr_5.frameNStart = frameN;  // exact frame index
    instr_5.setAutoDraw(true);
  }

  frameRemains = 18 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_5.setAutoDraw(false);
  }
  
  // *instr_6* updates
  if (t >= 24 && instr_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_6.tStart = t;  // (not accounting for frame time here)
    instr_6.frameNStart = frameN;  // exact frame index
    instr_6.setAutoDraw(true);
  }

  frameRemains = 24 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_6.setAutoDraw(false);
  }
  
  // *image* updates
  if (t >= 28 && image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image.tStart = t;  // (not accounting for frame time here)
    image.frameNStart = frameN;  // exact frame index
    image.setAutoDraw(true);
  }

  frameRemains = 28 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image.setAutoDraw(false);
  }
  
  // *instr_7* updates
  if (t >= 32 && instr_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_7.tStart = t;  // (not accounting for frame time here)
    instr_7.frameNStart = frameN;  // exact frame index
    instr_7.setAutoDraw(true);
  }

  
  // *key_resp_AMP_instr1* updates
  if (t >= 38 && key_resp_AMP_instr1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_AMP_instr1.tStart = t;  // (not accounting for frame time here)
    key_resp_AMP_instr1.frameNStart = frameN;  // exact frame index
    key_resp_AMP_instr1.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_AMP_instr1.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_AMP_instr1.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right', 'esc']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_AMP_instr1.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_AMP_instr1.rt = key_resp_AMP_instr1.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr1Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr1RoutineEnd() {
  //------Ending Routine 'instr1'-------
  for (const thisComponent of instr1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_AMP_instr1.keys === undefined || key_resp_AMP_instr1.keys.length === 0) {    // No response was made
      key_resp_AMP_instr1.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_AMP_instr1.keys', key_resp_AMP_instr1.keys);
  if (typeof key_resp_AMP_instr1.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_AMP_instr1.rt', key_resp_AMP_instr1.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr1" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_logo_rate;
var instr_logoComponents;
function instr_logoRoutineBegin() {
  //------Prepare to start Routine 'instr_logo'-------
  t = 0;
  instr_logoClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_logo_rate = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr_logoComponents = [];
  instr_logoComponents.push(instr_logo1);
  instr_logoComponents.push(instr_logo2);
  instr_logoComponents.push(instr_logo3);
  instr_logoComponents.push(instr_logo4);
  instr_logoComponents.push(instr_logo5);
  instr_logoComponents.push(logo_example);
  instr_logoComponents.push(instr_logo6);
  instr_logoComponents.push(logo_prac_layout_reminder);
  instr_logoComponents.push(instr_logo7);
  instr_logoComponents.push(instr_logo8);
  instr_logoComponents.push(resp_logo_rate);
  
  for (const thisComponent of instr_logoComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_logoRoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_logo'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_logoClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_logo1* updates
  if (t >= 0.0 && instr_logo1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo1.tStart = t;  // (not accounting for frame time here)
    instr_logo1.frameNStart = frameN;  // exact frame index
    instr_logo1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo1.setAutoDraw(false);
  }
  
  // *instr_logo2* updates
  if (t >= 6 && instr_logo2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo2.tStart = t;  // (not accounting for frame time here)
    instr_logo2.frameNStart = frameN;  // exact frame index
    instr_logo2.setAutoDraw(true);
  }

  frameRemains = 6 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo2.setAutoDraw(false);
  }
  
  // *instr_logo3* updates
  if (t >= 16 && instr_logo3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo3.tStart = t;  // (not accounting for frame time here)
    instr_logo3.frameNStart = frameN;  // exact frame index
    instr_logo3.setAutoDraw(true);
  }

  frameRemains = 16 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo3.setAutoDraw(false);
  }
  
  // *instr_logo4* updates
  if (t >= 22 && instr_logo4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo4.tStart = t;  // (not accounting for frame time here)
    instr_logo4.frameNStart = frameN;  // exact frame index
    instr_logo4.setAutoDraw(true);
  }

  frameRemains = 22 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo4.setAutoDraw(false);
  }
  
  // *instr_logo5* updates
  if (t >= 34 && instr_logo5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo5.tStart = t;  // (not accounting for frame time here)
    instr_logo5.frameNStart = frameN;  // exact frame index
    instr_logo5.setAutoDraw(true);
  }

  frameRemains = 34 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo5.setAutoDraw(false);
  }
  
  // *logo_example* updates
  if (t >= 40 && logo_example.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    logo_example.tStart = t;  // (not accounting for frame time here)
    logo_example.frameNStart = frameN;  // exact frame index
    logo_example.setAutoDraw(true);
  }

  frameRemains = 40 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (logo_example.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    logo_example.setAutoDraw(false);
  }
  
  // *instr_logo6* updates
  if (t >= 46 && instr_logo6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo6.tStart = t;  // (not accounting for frame time here)
    instr_logo6.frameNStart = frameN;  // exact frame index
    instr_logo6.setAutoDraw(true);
  }

  frameRemains = 46 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo6.setAutoDraw(false);
  }
  
  // *logo_prac_layout_reminder* updates
  if (t >= 56 && logo_prac_layout_reminder.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    logo_prac_layout_reminder.tStart = t;  // (not accounting for frame time here)
    logo_prac_layout_reminder.frameNStart = frameN;  // exact frame index
    logo_prac_layout_reminder.setAutoDraw(true);
  }

  frameRemains = 56 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (logo_prac_layout_reminder.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    logo_prac_layout_reminder.setAutoDraw(false);
  }
  
  // *instr_logo7* updates
  if (t >= 62 && instr_logo7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo7.tStart = t;  // (not accounting for frame time here)
    instr_logo7.frameNStart = frameN;  // exact frame index
    instr_logo7.setAutoDraw(true);
  }

  frameRemains = 62 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo7.setAutoDraw(false);
  }
  
  // *instr_logo8* updates
  if (t >= 68 && instr_logo8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo8.tStart = t;  // (not accounting for frame time here)
    instr_logo8.frameNStart = frameN;  // exact frame index
    instr_logo8.setAutoDraw(true);
  }

  
  // *resp_logo_rate* updates
  if (t >= 68 && resp_logo_rate.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_logo_rate.tStart = t;  // (not accounting for frame time here)
    resp_logo_rate.frameNStart = frameN;  // exact frame index
    resp_logo_rate.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_logo_rate.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_logo_rate.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_logo_rate.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_logo_rate.rt = resp_logo_rate.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_logoComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_logoRoutineEnd() {
  //------Ending Routine 'instr_logo'-------
  for (const thisComponent of instr_logoComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_logo_rate.keys === undefined || resp_logo_rate.keys.length === 0) {    // No response was made
      resp_logo_rate.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_logo_rate.keys', resp_logo_rate.keys);
  if (typeof resp_logo_rate.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_logo_rate.rt', resp_logo_rate.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr_logo" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var fixComponents;
function fixRoutineBegin() {
  //------Prepare to start Routine 'fix'-------
  t = 0;
  fixClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  
  // keep track of which components have finished
  fixComponents = [];
  fixComponents.push(LDT_fix_cross);
  
  for (const thisComponent of fixComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function fixRoutineEachFrame() {
  //------Loop for each frame of Routine 'fix'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = fixClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *LDT_fix_cross* updates
  if (t >= 0.0 && LDT_fix_cross.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LDT_fix_cross.tStart = t;  // (not accounting for frame time here)
    LDT_fix_cross.frameNStart = frameN;  // exact frame index
    LDT_fix_cross.setAutoDraw(true);
  }

  frameRemains = 0.0 + rand_duration - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (LDT_fix_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    LDT_fix_cross.setAutoDraw(false);
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of fixComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function fixRoutineEnd() {
  //------Ending Routine 'fix'-------
  for (const thisComponent of fixComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // the Routine "fix" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var keypress_logo_prac;
var logo_pracComponents;
function logo_pracRoutineBegin() {
  //------Prepare to start Routine 'logo_prac'-------
  t = 0;
  logo_pracClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keypress_logo_prac = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  logo_pracComponents = [];
  logo_pracComponents.push(img_logo_prac);
  logo_pracComponents.push(mask_logo_prac);
  logo_pracComponents.push(key_reminder_logo_prac);
  logo_pracComponents.push(keypress_logo_prac);
  
  for (const thisComponent of logo_pracComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function logo_pracRoutineEachFrame() {
  //------Loop for each frame of Routine 'logo_prac'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = logo_pracClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *img_logo_prac* updates
  if (t >= 0.0 && img_logo_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    img_logo_prac.tStart = t;  // (not accounting for frame time here)
    img_logo_prac.frameNStart = frameN;  // exact frame index
    img_logo_prac.setAutoDraw(true);
  }

  frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (img_logo_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    img_logo_prac.setAutoDraw(false);
  }
  
  // *mask_logo_prac* updates
  if (t >= 0.3 && mask_logo_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mask_logo_prac.tStart = t;  // (not accounting for frame time here)
    mask_logo_prac.frameNStart = frameN;  // exact frame index
    mask_logo_prac.setAutoDraw(true);
  }

  
  // *key_reminder_logo_prac* updates
  if (t >= 0.3 && key_reminder_logo_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reminder_logo_prac.tStart = t;  // (not accounting for frame time here)
    key_reminder_logo_prac.frameNStart = frameN;  // exact frame index
    key_reminder_logo_prac.setAutoDraw(true);
  }

  
  // *keypress_logo_prac* updates
  if (t >= 0.3 && keypress_logo_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keypress_logo_prac.tStart = t;  // (not accounting for frame time here)
    keypress_logo_prac.frameNStart = frameN;  // exact frame index
    keypress_logo_prac.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keypress_logo_prac.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keypress_logo_prac.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right', 'escape', 'n']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (keypress_logo_prac.keys.length === 0) {  // then this was the first keypress
        keypress_logo_prac.keys = theseKeys[0];  // just the first key pressed
        keypress_logo_prac.rt = keypress_logo_prac.clock.getTime();
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of logo_pracComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function logo_pracRoutineEnd() {
  //------Ending Routine 'logo_prac'-------
  for (const thisComponent of logo_pracComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (keypress_logo_prac.keys === undefined || keypress_logo_prac.keys.length === 0) {    // No response was made
      keypress_logo_prac.keys = undefined;
  }
  
  psychoJS.experiment.addData('keypress_logo_prac.keys', keypress_logo_prac.keys);
  if (typeof keypress_logo_prac.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('keypress_logo_prac.rt', keypress_logo_prac.rt);
      routineTimer.reset();
      }
  
  // the Routine "logo_prac" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_logo_ready_2;
var instr_logo_2Components;
function instr_logo_2RoutineBegin() {
  //------Prepare to start Routine 'instr_logo_2'-------
  t = 0;
  instr_logo_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_logo_ready_2 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr_logo_2Components = [];
  instr_logo_2Components.push(instr_logo9);
  instr_logo_2Components.push(instr_logo10);
  instr_logo_2Components.push(image_7);
  instr_logo_2Components.push(instr_logo11);
  instr_logo_2Components.push(resp_logo_ready_2);
  
  for (const thisComponent of instr_logo_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_logo_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_logo_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_logo_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_logo9* updates
  if (t >= 0.0 && instr_logo9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo9.tStart = t;  // (not accounting for frame time here)
    instr_logo9.frameNStart = frameN;  // exact frame index
    instr_logo9.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo9.setAutoDraw(false);
  }
  
  // *instr_logo10* updates
  if (t >= 4 && instr_logo10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo10.tStart = t;  // (not accounting for frame time here)
    instr_logo10.frameNStart = frameN;  // exact frame index
    instr_logo10.setAutoDraw(true);
  }

  frameRemains = 4 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_logo10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_logo10.setAutoDraw(false);
  }
  
  // *image_7* updates
  if (t >= 10 && image_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_7.tStart = t;  // (not accounting for frame time here)
    image_7.frameNStart = frameN;  // exact frame index
    image_7.setAutoDraw(true);
  }

  frameRemains = 10 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_7.setAutoDraw(false);
  }
  
  // *instr_logo11* updates
  if (t >= 16 && instr_logo11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_logo11.tStart = t;  // (not accounting for frame time here)
    instr_logo11.frameNStart = frameN;  // exact frame index
    instr_logo11.setAutoDraw(true);
  }

  
  // *resp_logo_ready_2* updates
  if (t >= 16 && resp_logo_ready_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_logo_ready_2.tStart = t;  // (not accounting for frame time here)
    resp_logo_ready_2.frameNStart = frameN;  // exact frame index
    resp_logo_ready_2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_logo_ready_2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_logo_ready_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_logo_ready_2.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_logo_ready_2.rt = resp_logo_ready_2.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_logo_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_logo_2RoutineEnd() {
  //------Ending Routine 'instr_logo_2'-------
  for (const thisComponent of instr_logo_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_logo_ready_2.keys === undefined || resp_logo_ready_2.keys.length === 0) {    // No response was made
      resp_logo_ready_2.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_logo_ready_2.keys', resp_logo_ready_2.keys);
  if (typeof resp_logo_ready_2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_logo_ready_2.rt', resp_logo_ready_2.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr_logo_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var logo_trials;
function logo_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  logo_trials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_files/symbols.csv',
    seed: undefined, name: 'logo_trials'});
  psychoJS.experiment.addLoop(logo_trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisLogo_trial of logo_trials) {
    thisScheduler.add(importConditions(logo_trials));
    thisScheduler.add(fixRoutineBegin);
    thisScheduler.add(fixRoutineEachFrame);
    thisScheduler.add(fixRoutineEnd);
    thisScheduler.add(logo_trialRoutineBegin);
    thisScheduler.add(logo_trialRoutineEachFrame);
    thisScheduler.add(logo_trialRoutineEnd);
  }

  return Scheduler.Event.NEXT;
}


function logo_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(logo_trials);

  return Scheduler.Event.NEXT;
}

var AMP_pracs;
function AMP_pracsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  AMP_pracs = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_files/amp_testrun.csv',
    seed: undefined, name: 'AMP_pracs'});
  psychoJS.experiment.addLoop(AMP_pracs); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisAMP_prac of AMP_pracs) {
    thisScheduler.add(importConditions(AMP_pracs));
    thisScheduler.add(fixRoutineBegin);
    thisScheduler.add(fixRoutineEachFrame);
    thisScheduler.add(fixRoutineEnd);
    thisScheduler.add(AMP_prac_wordRoutineBegin);
    thisScheduler.add(AMP_prac_wordRoutineEachFrame);
    thisScheduler.add(AMP_prac_wordRoutineEnd);
    thisScheduler.add(AMP_prac_maskRoutineBegin);
    thisScheduler.add(AMP_prac_maskRoutineEachFrame);
    thisScheduler.add(AMP_prac_maskRoutineEnd);
    thisScheduler.add(endLoopIteration(thisAMP_prac));
  }

  return Scheduler.Event.NEXT;
}


function AMP_pracsLoopEnd() {
  psychoJS.experiment.removeLoop(AMP_pracs);

  return Scheduler.Event.NEXT;
}

var AMP_trials;
function AMP_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  AMP_trials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_files/AMP_conditions.csv',
    seed: undefined, name: 'AMP_trials'});
  psychoJS.experiment.addLoop(AMP_trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisAMP_trial of AMP_trials) {
    thisScheduler.add(importConditions(AMP_trials));
    thisScheduler.add(fixRoutineBegin);
    thisScheduler.add(fixRoutineEachFrame);
    thisScheduler.add(fixRoutineEnd);
    thisScheduler.add(AMP_trial_wordRoutineBegin);
    thisScheduler.add(AMP_trial_wordRoutineEachFrame);
    thisScheduler.add(AMP_trial_wordRoutineEnd);
    thisScheduler.add(AMP_trial_maskRoutineBegin);
    thisScheduler.add(AMP_trial_maskRoutineEachFrame);
    thisScheduler.add(AMP_trial_maskRoutineEnd);
    thisScheduler.add(endLoopIteration(thisAMP_trial));
  }

  return Scheduler.Event.NEXT;
}


function AMP_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(AMP_trials);

  return Scheduler.Event.NEXT;
}

var LDT_pracs;
function LDT_pracsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  LDT_pracs = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_files\\ldt_testrun.csv',
    seed: undefined, name: 'LDT_pracs'});
  psychoJS.experiment.addLoop(LDT_pracs); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisLDT_prac of LDT_pracs) {
    thisScheduler.add(importConditions(LDT_pracs));
    thisScheduler.add(fixRoutineBegin);
    thisScheduler.add(fixRoutineEachFrame);
    thisScheduler.add(fixRoutineEnd);
    thisScheduler.add(LDT_pracRoutineBegin);
    thisScheduler.add(LDT_pracRoutineEachFrame);
    thisScheduler.add(LDT_pracRoutineEnd);
    thisScheduler.add(endLoopIteration(thisLDT_prac));
  }

  return Scheduler.Event.NEXT;
}


function LDT_pracsLoopEnd() {
  psychoJS.experiment.removeLoop(LDT_pracs);

  return Scheduler.Event.NEXT;
}

var LDT_trials;
function LDT_trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  LDT_trials = new TrialHandler({
    psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'condition_files\\LDT_conditions.csv',
    seed: undefined, name: 'LDT_trials'});
  psychoJS.experiment.addLoop(LDT_trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisLDT_trial of LDT_trials) {
    thisScheduler.add(importConditions(LDT_trials));
    thisScheduler.add(fixRoutineBegin);
    thisScheduler.add(fixRoutineEachFrame);
    thisScheduler.add(fixRoutineEnd);
    thisScheduler.add(LDT_trialRoutineBegin);
    thisScheduler.add(LDT_trialRoutineEachFrame);
    thisScheduler.add(LDT_trialRoutineEnd);
    thisScheduler.add(endLoopIteration(thisLDT_trial));
  }

  return Scheduler.Event.NEXT;
}


function LDT_trialsLoopEnd() {
  psychoJS.experiment.removeLoop(LDT_trials);

  return Scheduler.Event.NEXT;
}

var keypress_logo_prac_2;
var logo_trialComponents;
function logo_trialRoutineBegin() {
  //------Prepare to start Routine 'logo_trial'-------
  t = 0;
  logo_trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  img_logo_prac_2.setImage(symbol);
  keypress_logo_prac_2 = new core.BuilderKeyResponse(psychoJS);
  // keep track of which components have finished
  logo_trialComponents = [];
  logo_trialComponents.push(img_logo_prac_2);
  logo_trialComponents.push(mask_logo_prac_2);
  logo_trialComponents.push(key_reminder_logo_prac_2);
  logo_trialComponents.push(keypress_logo_prac_2);
  
  for (const thisComponent of logo_trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function logo_trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'logo_trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = logo_trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *img_logo_prac_2* updates
  if (t >= 0.0 && img_logo_prac_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    img_logo_prac_2.tStart = t;  // (not accounting for frame time here)
    img_logo_prac_2.frameNStart = frameN;  // exact frame index
    img_logo_prac_2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (img_logo_prac_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    img_logo_prac_2.setAutoDraw(false);
  }
  
  // *mask_logo_prac_2* updates
  if (t >= 0.3 && mask_logo_prac_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    mask_logo_prac_2.tStart = t;  // (not accounting for frame time here)
    mask_logo_prac_2.frameNStart = frameN;  // exact frame index
    mask_logo_prac_2.setAutoDraw(true);
  }

  
  // *key_reminder_logo_prac_2* updates
  if (t >= 0.3 && key_reminder_logo_prac_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reminder_logo_prac_2.tStart = t;  // (not accounting for frame time here)
    key_reminder_logo_prac_2.frameNStart = frameN;  // exact frame index
    key_reminder_logo_prac_2.setAutoDraw(true);
  }

  
  // *keypress_logo_prac_2* updates
  if (t >= 0.3 && keypress_logo_prac_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keypress_logo_prac_2.tStart = t;  // (not accounting for frame time here)
    keypress_logo_prac_2.frameNStart = frameN;  // exact frame index
    keypress_logo_prac_2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keypress_logo_prac_2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keypress_logo_prac_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right', 'escape', 'n']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (keypress_logo_prac_2.keys.length === 0) {  // then this was the first keypress
        keypress_logo_prac_2.keys = theseKeys[0];  // just the first key pressed
        keypress_logo_prac_2.rt = keypress_logo_prac_2.clock.getTime();
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of logo_trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function logo_trialRoutineEnd() {
  //------Ending Routine 'logo_trial'-------
  for (const thisComponent of logo_trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (keypress_logo_prac_2.keys === undefined || keypress_logo_prac_2.keys.length === 0) {    // No response was made
      keypress_logo_prac_2.keys = undefined;
  }
  
  psychoJS.experiment.addData('keypress_logo_prac_2.keys', keypress_logo_prac_2.keys);
  if (typeof keypress_logo_prac_2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('keypress_logo_prac_2.rt', keypress_logo_prac_2.rt);
      routineTimer.reset();
      }
  
  // the Routine "logo_trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_AMP_ready1;
var instr_AMPComponents;
function instr_AMPRoutineBegin() {
  //------Prepare to start Routine 'instr_AMP'-------
  t = 0;
  instr_AMPClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_AMP_ready1 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr_AMPComponents = [];
  instr_AMPComponents.push(instr_AMP1_1);
  instr_AMPComponents.push(instr_AMP1_2);
  instr_AMPComponents.push(instr_AMP1_3);
  instr_AMPComponents.push(instr_AMP1_4);
  instr_AMPComponents.push(instr_AMP1_5);
  instr_AMPComponents.push(instr_AMP1_6);
  instr_AMPComponents.push(image_4);
  instr_AMPComponents.push(instr_AMP1_7);
  instr_AMPComponents.push(instr_AMP1_8);
  instr_AMPComponents.push(instr_AMP1_9);
  instr_AMPComponents.push(instr_AMP1_10);
  instr_AMPComponents.push(resp_AMP_ready1);
  
  for (const thisComponent of instr_AMPComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_AMPRoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_AMP'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_AMPClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_AMP1_1* updates
  if (t >= 0.0 && instr_AMP1_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_1.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_1.frameNStart = frameN;  // exact frame index
    instr_AMP1_1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_1.setAutoDraw(false);
  }
  
  // *instr_AMP1_2* updates
  if (t >= 6 && instr_AMP1_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_2.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_2.frameNStart = frameN;  // exact frame index
    instr_AMP1_2.setAutoDraw(true);
  }

  frameRemains = 6 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_2.setAutoDraw(false);
  }
  
  // *instr_AMP1_3* updates
  if (t >= 12 && instr_AMP1_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_3.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_3.frameNStart = frameN;  // exact frame index
    instr_AMP1_3.setAutoDraw(true);
  }

  frameRemains = 12 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_3.setAutoDraw(false);
  }
  
  // *instr_AMP1_4* updates
  if (t >= 18 && instr_AMP1_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_4.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_4.frameNStart = frameN;  // exact frame index
    instr_AMP1_4.setAutoDraw(true);
  }

  frameRemains = 18 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_4.setAutoDraw(false);
  }
  
  // *instr_AMP1_5* updates
  if (t >= 28 && instr_AMP1_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_5.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_5.frameNStart = frameN;  // exact frame index
    instr_AMP1_5.setAutoDraw(true);
  }

  frameRemains = 28 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_5.setAutoDraw(false);
  }
  
  // *instr_AMP1_6* updates
  if (t >= 34 && instr_AMP1_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_6.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_6.frameNStart = frameN;  // exact frame index
    instr_AMP1_6.setAutoDraw(true);
  }

  frameRemains = 34 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_6.setAutoDraw(false);
  }
  
  // *image_4* updates
  if (t >= 40 && image_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_4.tStart = t;  // (not accounting for frame time here)
    image_4.frameNStart = frameN;  // exact frame index
    image_4.setAutoDraw(true);
  }

  frameRemains = 40 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_4.setAutoDraw(false);
  }
  
  // *instr_AMP1_7* updates
  if (t >= 46 && instr_AMP1_7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_7.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_7.frameNStart = frameN;  // exact frame index
    instr_AMP1_7.setAutoDraw(true);
  }

  frameRemains = 46 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_7.setAutoDraw(false);
  }
  
  // *instr_AMP1_8* updates
  if (t >= 52 && instr_AMP1_8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_8.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_8.frameNStart = frameN;  // exact frame index
    instr_AMP1_8.setAutoDraw(true);
  }

  frameRemains = 52 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_8.setAutoDraw(false);
  }
  
  // *instr_AMP1_9* updates
  if (t >= 62 && instr_AMP1_9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_9.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_9.frameNStart = frameN;  // exact frame index
    instr_AMP1_9.setAutoDraw(true);
  }

  frameRemains = 62 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP1_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP1_9.setAutoDraw(false);
  }
  
  // *instr_AMP1_10* updates
  if (t >= 68 && instr_AMP1_10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP1_10.tStart = t;  // (not accounting for frame time here)
    instr_AMP1_10.frameNStart = frameN;  // exact frame index
    instr_AMP1_10.setAutoDraw(true);
  }

  
  // *resp_AMP_ready1* updates
  if (t >= 68 && resp_AMP_ready1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_AMP_ready1.tStart = t;  // (not accounting for frame time here)
    resp_AMP_ready1.frameNStart = frameN;  // exact frame index
    resp_AMP_ready1.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_AMP_ready1.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_AMP_ready1.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_AMP_ready1.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_AMP_ready1.rt = resp_AMP_ready1.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_AMPComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_AMPRoutineEnd() {
  //------Ending Routine 'instr_AMP'-------
  for (const thisComponent of instr_AMPComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_AMP_ready1.keys === undefined || resp_AMP_ready1.keys.length === 0) {    // No response was made
      resp_AMP_ready1.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_AMP_ready1.keys', resp_AMP_ready1.keys);
  if (typeof resp_AMP_ready1.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_AMP_ready1.rt', resp_AMP_ready1.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr_AMP" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var AMP_prac_wordComponents;
function AMP_prac_wordRoutineBegin() {
  //------Prepare to start Routine 'AMP_prac_word'-------
  t = 0;
  AMP_prac_wordClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  AMP_wordstim_2.setText(words);
  AMP_nonwordstim_3.setText(nonwords);
  // keep track of which components have finished
  AMP_prac_wordComponents = [];
  AMP_prac_wordComponents.push(AMP_wordstim_2);
  AMP_prac_wordComponents.push(gap);
  AMP_prac_wordComponents.push(AMP_nonwordstim_3);
  
  for (const thisComponent of AMP_prac_wordComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function AMP_prac_wordRoutineEachFrame() {
  //------Loop for each frame of Routine 'AMP_prac_word'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = AMP_prac_wordClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *AMP_wordstim_2* updates
  if (t >= 0 && AMP_wordstim_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_wordstim_2.tStart = t;  // (not accounting for frame time here)
    AMP_wordstim_2.frameNStart = frameN;  // exact frame index
    AMP_wordstim_2.setAutoDraw(true);
  }

  frameRemains = 0 + prime_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (AMP_wordstim_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    AMP_wordstim_2.setAutoDraw(false);
  }
  
  // *gap* updates
  if (t >= 0.1 && gap.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    gap.tStart = t;  // (not accounting for frame time here)
    gap.frameNStart = frameN;  // exact frame index
    gap.setAutoDraw(true);
  }

  frameRemains = 0.1 + 0.125 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (gap.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    gap.setAutoDraw(false);
  }
  
  // *AMP_nonwordstim_3* updates
  if (t >= 0.225 && AMP_nonwordstim_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_nonwordstim_3.tStart = t;  // (not accounting for frame time here)
    AMP_nonwordstim_3.frameNStart = frameN;  // exact frame index
    AMP_nonwordstim_3.setAutoDraw(true);
  }

  frameRemains = 0.225 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (AMP_nonwordstim_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    AMP_nonwordstim_3.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of AMP_prac_wordComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function AMP_prac_wordRoutineEnd() {
  //------Ending Routine 'AMP_prac_word'-------
  for (const thisComponent of AMP_prac_wordComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "AMP_prac_word" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_AMP_prac;
var AMP_prac_maskComponents;
function AMP_prac_maskRoutineBegin() {
  //------Prepare to start Routine 'AMP_prac_mask'-------
  t = 0;
  AMP_prac_maskClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_AMP_prac = new core.BuilderKeyResponse(psychoJS);
  
  AMP_maskstim_2.setText(mask);
  // keep track of which components have finished
  AMP_prac_maskComponents = [];
  AMP_prac_maskComponents.push(resp_AMP_prac);
  AMP_prac_maskComponents.push(AMP_maskstim_2);
  AMP_prac_maskComponents.push(key_reminder);
  
  for (const thisComponent of AMP_prac_maskComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function AMP_prac_maskRoutineEachFrame() {
  //------Loop for each frame of Routine 'AMP_prac_mask'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = AMP_prac_maskClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *resp_AMP_prac* updates
  if (t >= 0 && resp_AMP_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_AMP_prac.tStart = t;  // (not accounting for frame time here)
    resp_AMP_prac.frameNStart = frameN;  // exact frame index
    resp_AMP_prac.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_AMP_prac.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_AMP_prac.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right', 'escape', 'n']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (resp_AMP_prac.keys.length === 0) {  // then this was the first keypress
        resp_AMP_prac.keys = theseKeys[0];  // just the first key pressed
        resp_AMP_prac.rt = resp_AMP_prac.clock.getTime();
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *AMP_maskstim_2* updates
  if (t >= 0 && AMP_maskstim_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_maskstim_2.tStart = t;  // (not accounting for frame time here)
    AMP_maskstim_2.frameNStart = frameN;  // exact frame index
    AMP_maskstim_2.setAutoDraw(true);
  }

  
  // *key_reminder* updates
  if (t >= 0 && key_reminder.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reminder.tStart = t;  // (not accounting for frame time here)
    key_reminder.frameNStart = frameN;  // exact frame index
    key_reminder.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of AMP_prac_maskComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function AMP_prac_maskRoutineEnd() {
  //------Ending Routine 'AMP_prac_mask'-------
  for (const thisComponent of AMP_prac_maskComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_AMP_prac.keys === undefined || resp_AMP_prac.keys.length === 0) {    // No response was made
      resp_AMP_prac.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_AMP_prac.keys', resp_AMP_prac.keys);
  if (typeof resp_AMP_prac.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_AMP_prac.rt', resp_AMP_prac.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "AMP_prac_mask" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_AMP_ready;
var instr_AMP_2Components;
function instr_AMP_2RoutineBegin() {
  //------Prepare to start Routine 'instr_AMP_2'-------
  t = 0;
  instr_AMP_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_AMP_ready = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr_AMP_2Components = [];
  instr_AMP_2Components.push(instr_AMP2_1);
  instr_AMP_2Components.push(instr_AMP2_2);
  instr_AMP_2Components.push(image_5);
  instr_AMP_2Components.push(instr_AMP2_3);
  instr_AMP_2Components.push(resp_AMP_ready);
  
  for (const thisComponent of instr_AMP_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_AMP_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_AMP_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_AMP_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_AMP2_1* updates
  if (t >= 0.0 && instr_AMP2_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP2_1.tStart = t;  // (not accounting for frame time here)
    instr_AMP2_1.frameNStart = frameN;  // exact frame index
    instr_AMP2_1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP2_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP2_1.setAutoDraw(false);
  }
  
  // *instr_AMP2_2* updates
  if (t >= 4 && instr_AMP2_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP2_2.tStart = t;  // (not accounting for frame time here)
    instr_AMP2_2.frameNStart = frameN;  // exact frame index
    instr_AMP2_2.setAutoDraw(true);
  }

  frameRemains = 4 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP2_2.setAutoDraw(false);
  }
  
  // *image_5* updates
  if (t >= 10 && image_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_5.tStart = t;  // (not accounting for frame time here)
    image_5.frameNStart = frameN;  // exact frame index
    image_5.setAutoDraw(true);
  }

  frameRemains = 10 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_5.setAutoDraw(false);
  }
  
  // *instr_AMP2_3* updates
  if (t >= 16 && instr_AMP2_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP2_3.tStart = t;  // (not accounting for frame time here)
    instr_AMP2_3.frameNStart = frameN;  // exact frame index
    instr_AMP2_3.setAutoDraw(true);
  }

  
  // *resp_AMP_ready* updates
  if (t >= 16 && resp_AMP_ready.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_AMP_ready.tStart = t;  // (not accounting for frame time here)
    resp_AMP_ready.frameNStart = frameN;  // exact frame index
    resp_AMP_ready.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_AMP_ready.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_AMP_ready.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_AMP_ready.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_AMP_ready.rt = resp_AMP_ready.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_AMP_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_AMP_2RoutineEnd() {
  //------Ending Routine 'instr_AMP_2'-------
  for (const thisComponent of instr_AMP_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_AMP_ready.keys === undefined || resp_AMP_ready.keys.length === 0) {    // No response was made
      resp_AMP_ready.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_AMP_ready.keys', resp_AMP_ready.keys);
  if (typeof resp_AMP_ready.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_AMP_ready.rt', resp_AMP_ready.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr_AMP_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var instr_AMP_3Components;
function instr_AMP_3RoutineBegin() {
  //------Prepare to start Routine 'instr_AMP_3'-------
  t = 0;
  instr_AMP_3Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(4.000000);
  // update component parameters for each repeat
  
  // keep track of which components have finished
  instr_AMP_3Components = [];
  instr_AMP_3Components.push(instr_AMP3_1);
  
  for (const thisComponent of instr_AMP_3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_AMP_3RoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_AMP_3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_AMP_3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_AMP3_1* updates
  if (t >= 0.0 && instr_AMP3_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_AMP3_1.tStart = t;  // (not accounting for frame time here)
    instr_AMP3_1.frameNStart = frameN;  // exact frame index
    instr_AMP3_1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_AMP3_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_AMP3_1.setAutoDraw(false);
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_AMP_3Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_AMP_3RoutineEnd() {
  //------Ending Routine 'instr_AMP_3'-------
  for (const thisComponent of instr_AMP_3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  return Scheduler.Event.NEXT;
}

var AMP_trial_wordComponents;
function AMP_trial_wordRoutineBegin() {
  //------Prepare to start Routine 'AMP_trial_word'-------
  t = 0;
  AMP_trial_wordClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  AMP_wordstim.setText(words);
  
  AMP_nonwordstim_2.setText(nonwords);
  // keep track of which components have finished
  AMP_trial_wordComponents = [];
  AMP_trial_wordComponents.push(AMP_wordstim);
  AMP_trial_wordComponents.push(gap_1);
  AMP_trial_wordComponents.push(AMP_nonwordstim_2);
  
  for (const thisComponent of AMP_trial_wordComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function AMP_trial_wordRoutineEachFrame() {
  //------Loop for each frame of Routine 'AMP_trial_word'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = AMP_trial_wordClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *AMP_wordstim* updates
  if (t >= 0 && AMP_wordstim.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_wordstim.tStart = t;  // (not accounting for frame time here)
    AMP_wordstim.frameNStart = frameN;  // exact frame index
    AMP_wordstim.setAutoDraw(true);
  }

  frameRemains = 0 + prime_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (AMP_wordstim.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    AMP_wordstim.setAutoDraw(false);
  }
  
  // *gap_1* updates
  if (t >= 0.1 && gap_1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    gap_1.tStart = t;  // (not accounting for frame time here)
    gap_1.frameNStart = frameN;  // exact frame index
    gap_1.setAutoDraw(true);
  }

  frameRemains = 0.1 + 0.125 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (gap_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    gap_1.setAutoDraw(false);
  }
  
  
  // *AMP_nonwordstim_2* updates
  if (t >= 0.225 && AMP_nonwordstim_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_nonwordstim_2.tStart = t;  // (not accounting for frame time here)
    AMP_nonwordstim_2.frameNStart = frameN;  // exact frame index
    AMP_nonwordstim_2.setAutoDraw(true);
  }

  frameRemains = 0.225 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (AMP_nonwordstim_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    AMP_nonwordstim_2.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of AMP_trial_wordComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function AMP_trial_wordRoutineEnd() {
  //------Ending Routine 'AMP_trial_word'-------
  for (const thisComponent of AMP_trial_wordComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // the Routine "AMP_trial_word" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_AMP;
var AMP_trial_maskComponents;
function AMP_trial_maskRoutineBegin() {
  //------Prepare to start Routine 'AMP_trial_mask'-------
  t = 0;
  AMP_trial_maskClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_AMP = new core.BuilderKeyResponse(psychoJS);
  
  AMP_maskstim.setText(mask);
  // keep track of which components have finished
  AMP_trial_maskComponents = [];
  AMP_trial_maskComponents.push(resp_AMP);
  AMP_trial_maskComponents.push(AMP_maskstim);
  AMP_trial_maskComponents.push(key_reminder_2);
  
  for (const thisComponent of AMP_trial_maskComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function AMP_trial_maskRoutineEachFrame() {
  //------Loop for each frame of Routine 'AMP_trial_mask'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = AMP_trial_maskClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *resp_AMP* updates
  if (t >= 0.0 && resp_AMP.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_AMP.tStart = t;  // (not accounting for frame time here)
    resp_AMP.frameNStart = frameN;  // exact frame index
    resp_AMP.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_AMP.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_AMP.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (resp_AMP.keys.length === 0) {  // then this was the first keypress
        resp_AMP.keys = theseKeys[0];  // just the first key pressed
        resp_AMP.rt = resp_AMP.clock.getTime();
        // was this 'correct'?
        if (resp_AMP.keys == corr_ans) {
            resp_AMP.corr = 1;
        } else {
            resp_AMP.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
  }
  
  
  // *AMP_maskstim* updates
  if (t >= 0 && AMP_maskstim.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_maskstim.tStart = t;  // (not accounting for frame time here)
    AMP_maskstim.frameNStart = frameN;  // exact frame index
    AMP_maskstim.setAutoDraw(true);
  }

  
  // *key_reminder_2* updates
  if (t >= 0 && key_reminder_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reminder_2.tStart = t;  // (not accounting for frame time here)
    key_reminder_2.frameNStart = frameN;  // exact frame index
    key_reminder_2.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of AMP_trial_maskComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function AMP_trial_maskRoutineEnd() {
  //------Ending Routine 'AMP_trial_mask'-------
  for (const thisComponent of AMP_trial_maskComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_AMP.keys === undefined || resp_AMP.keys.length === 0) {    // No response was made
      resp_AMP.keys = undefined;
  }
  
  // was no response the correct answer?!
  if (resp_AMP.keys === undefined) {
    if (['None','none',undefined].includes(corr_ans)) {
       resp_AMP.corr = 1  // correct non-response
    } else {
       resp_AMP.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('resp_AMP.keys', resp_AMP.keys);
  psychoJS.experiment.addData('resp_AMP.corr', resp_AMP.corr);
  if (typeof resp_AMP.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_AMP.rt', resp_AMP.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "AMP_trial_mask" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var AMP_feedbackComponents;
function AMP_feedbackRoutineBegin() {
  //------Prepare to start Routine 'AMP_feedback'-------
  t = 0;
  AMP_feedbackClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  
  // keep track of which components have finished
  AMP_feedbackComponents = [];
  AMP_feedbackComponents.push(AMP_feedback_instr);
  
  for (const thisComponent of AMP_feedbackComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function AMP_feedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'AMP_feedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = AMP_feedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *AMP_feedback_instr* updates
  if (t >= 0.0 && AMP_feedback_instr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    AMP_feedback_instr.tStart = t;  // (not accounting for frame time here)
    AMP_feedback_instr.frameNStart = frameN;  // exact frame index
    AMP_feedback_instr.setAutoDraw(true);
  }

  frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (AMP_feedback_instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    AMP_feedback_instr.setAutoDraw(false);
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of AMP_feedbackComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function AMP_feedbackRoutineEnd() {
  //------Ending Routine 'AMP_feedback'-------
  for (const thisComponent of AMP_feedbackComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // the Routine "AMP_feedback" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var key_resp_LDT_instr;
var instr_LDTComponents;
function instr_LDTRoutineBegin() {
  //------Prepare to start Routine 'instr_LDT'-------
  t = 0;
  instr_LDTClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  key_resp_LDT_instr = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr_LDTComponents = [];
  instr_LDTComponents.push(instr_LDT1);
  instr_LDTComponents.push(instr_LDT2);
  instr_LDTComponents.push(instr_LDT3);
  instr_LDTComponents.push(instr_LDT4);
  instr_LDTComponents.push(instr_LDT5);
  instr_LDTComponents.push(instr_LDT6);
  instr_LDTComponents.push(image_3);
  instr_LDTComponents.push(keyboard_reminder_LDT);
  instr_LDTComponents.push(instr_LDT7);
  instr_LDTComponents.push(instr_LT8);
  instr_LDTComponents.push(instr_LDT9_);
  instr_LDTComponents.push(key_resp_LDT_instr);
  
  for (const thisComponent of instr_LDTComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_LDTRoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_LDT'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_LDTClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_LDT1* updates
  if (t >= 0.0 && instr_LDT1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT1.tStart = t;  // (not accounting for frame time here)
    instr_LDT1.frameNStart = frameN;  // exact frame index
    instr_LDT1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT1.setAutoDraw(false);
  }
  
  // *instr_LDT2* updates
  if (t >= 6 && instr_LDT2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT2.tStart = t;  // (not accounting for frame time here)
    instr_LDT2.frameNStart = frameN;  // exact frame index
    instr_LDT2.setAutoDraw(true);
  }

  frameRemains = 6 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT2.setAutoDraw(false);
  }
  
  // *instr_LDT3* updates
  if (t >= 12 && instr_LDT3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT3.tStart = t;  // (not accounting for frame time here)
    instr_LDT3.frameNStart = frameN;  // exact frame index
    instr_LDT3.setAutoDraw(true);
  }

  frameRemains = 12 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT3.setAutoDraw(false);
  }
  
  // *instr_LDT4* updates
  if (t >= 20 && instr_LDT4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT4.tStart = t;  // (not accounting for frame time here)
    instr_LDT4.frameNStart = frameN;  // exact frame index
    instr_LDT4.setAutoDraw(true);
  }

  frameRemains = 20 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT4.setAutoDraw(false);
  }
  
  // *instr_LDT5* updates
  if (t >= 26 && instr_LDT5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT5.tStart = t;  // (not accounting for frame time here)
    instr_LDT5.frameNStart = frameN;  // exact frame index
    instr_LDT5.setAutoDraw(true);
  }

  frameRemains = 26 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT5.setAutoDraw(false);
  }
  
  // *instr_LDT6* updates
  if (t >= 32 && instr_LDT6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT6.tStart = t;  // (not accounting for frame time here)
    instr_LDT6.frameNStart = frameN;  // exact frame index
    instr_LDT6.setAutoDraw(true);
  }

  frameRemains = 32 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT6.setAutoDraw(false);
  }
  
  // *image_3* updates
  if (t >= 38 && image_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_3.tStart = t;  // (not accounting for frame time here)
    image_3.frameNStart = frameN;  // exact frame index
    image_3.setAutoDraw(true);
  }

  frameRemains = 38 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_3.setAutoDraw(false);
  }
  
  // *keyboard_reminder_LDT* updates
  if (t >= 42 && keyboard_reminder_LDT.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyboard_reminder_LDT.tStart = t;  // (not accounting for frame time here)
    keyboard_reminder_LDT.frameNStart = frameN;  // exact frame index
    keyboard_reminder_LDT.setAutoDraw(true);
  }

  frameRemains = 42 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (keyboard_reminder_LDT.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    keyboard_reminder_LDT.setAutoDraw(false);
  }
  
  // *instr_LDT7* updates
  if (t >= 46 && instr_LDT7.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT7.tStart = t;  // (not accounting for frame time here)
    instr_LDT7.frameNStart = frameN;  // exact frame index
    instr_LDT7.setAutoDraw(true);
  }

  frameRemains = 46 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT7.setAutoDraw(false);
  }
  
  // *instr_LT8* updates
  if (t >= 52 && instr_LT8.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LT8.tStart = t;  // (not accounting for frame time here)
    instr_LT8.frameNStart = frameN;  // exact frame index
    instr_LT8.setAutoDraw(true);
  }

  frameRemains = 52 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LT8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LT8.setAutoDraw(false);
  }
  
  // *instr_LDT9_* updates
  if (t >= 56 && instr_LDT9_.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT9_.tStart = t;  // (not accounting for frame time here)
    instr_LDT9_.frameNStart = frameN;  // exact frame index
    instr_LDT9_.setAutoDraw(true);
  }

  
  // *key_resp_LDT_instr* updates
  if (t >= 56 && key_resp_LDT_instr.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_LDT_instr.tStart = t;  // (not accounting for frame time here)
    key_resp_LDT_instr.frameNStart = frameN;  // exact frame index
    key_resp_LDT_instr.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_LDT_instr.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (key_resp_LDT_instr.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      key_resp_LDT_instr.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      key_resp_LDT_instr.rt = key_resp_LDT_instr.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_LDTComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_LDTRoutineEnd() {
  //------Ending Routine 'instr_LDT'-------
  for (const thisComponent of instr_LDTComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_LDT_instr.keys === undefined || key_resp_LDT_instr.keys.length === 0) {    // No response was made
      key_resp_LDT_instr.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_LDT_instr.keys', key_resp_LDT_instr.keys);
  if (typeof key_resp_LDT_instr.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_LDT_instr.rt', key_resp_LDT_instr.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr_LDT" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_LDT_prac;
var LDT_pracComponents;
function LDT_pracRoutineBegin() {
  //------Prepare to start Routine 'LDT_prac'-------
  t = 0;
  LDT_pracClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  LDT_word_prac.setText(words);
  LDT_mask_prac.setText(mask);
  resp_LDT_prac = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  LDT_pracComponents = [];
  LDT_pracComponents.push(LDT_word_prac);
  LDT_pracComponents.push(LDT_mask_prac);
  LDT_pracComponents.push(resp_LDT_prac);
  LDT_pracComponents.push(key_reminder_3);
  
  for (const thisComponent of LDT_pracComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function LDT_pracRoutineEachFrame() {
  //------Loop for each frame of Routine 'LDT_prac'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = LDT_pracClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *LDT_word_prac* updates
  if (t >= 0 && LDT_word_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LDT_word_prac.tStart = t;  // (not accounting for frame time here)
    LDT_word_prac.frameNStart = frameN;  // exact frame index
    LDT_word_prac.setAutoDraw(true);
  }

  frameRemains = 0 + ldt_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (LDT_word_prac.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    LDT_word_prac.setAutoDraw(false);
  }
  
  // *LDT_mask_prac* updates
  if (t >= 0.06 && LDT_mask_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LDT_mask_prac.tStart = t;  // (not accounting for frame time here)
    LDT_mask_prac.frameNStart = frameN;  // exact frame index
    LDT_mask_prac.setAutoDraw(true);
  }

  
  // *resp_LDT_prac* updates
  if (t >= 0.06 && resp_LDT_prac.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_LDT_prac.tStart = t;  // (not accounting for frame time here)
    resp_LDT_prac.frameNStart = frameN;  // exact frame index
    resp_LDT_prac.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_LDT_prac.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_LDT_prac.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_LDT_prac.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_LDT_prac.rt = resp_LDT_prac.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *key_reminder_3* updates
  if (t >= 0.06 && key_reminder_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reminder_3.tStart = t;  // (not accounting for frame time here)
    key_reminder_3.frameNStart = frameN;  // exact frame index
    key_reminder_3.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of LDT_pracComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function LDT_pracRoutineEnd() {
  //------Ending Routine 'LDT_prac'-------
  for (const thisComponent of LDT_pracComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_LDT_prac.keys === undefined || resp_LDT_prac.keys.length === 0) {    // No response was made
      resp_LDT_prac.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_LDT_prac.keys', resp_LDT_prac.keys);
  if (typeof resp_LDT_prac.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_LDT_prac.rt', resp_LDT_prac.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "LDT_prac" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_LDT_ready;
var instr_LDT_2Components;
function instr_LDT_2RoutineBegin() {
  //------Prepare to start Routine 'instr_LDT_2'-------
  t = 0;
  instr_LDT_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  resp_LDT_ready = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instr_LDT_2Components = [];
  instr_LDT_2Components.push(instr_LDT9);
  instr_LDT_2Components.push(instr_LDT10);
  instr_LDT_2Components.push(image_6);
  instr_LDT_2Components.push(instr_LDT11);
  instr_LDT_2Components.push(resp_LDT_ready);
  
  for (const thisComponent of instr_LDT_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function instr_LDT_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'instr_LDT_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instr_LDT_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_LDT9* updates
  if (t >= 0.0 && instr_LDT9.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT9.tStart = t;  // (not accounting for frame time here)
    instr_LDT9.frameNStart = frameN;  // exact frame index
    instr_LDT9.setAutoDraw(true);
  }

  frameRemains = 0.0 + 4 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT9.setAutoDraw(false);
  }
  
  // *instr_LDT10* updates
  if (t >= 4 && instr_LDT10.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT10.tStart = t;  // (not accounting for frame time here)
    instr_LDT10.frameNStart = frameN;  // exact frame index
    instr_LDT10.setAutoDraw(true);
  }

  frameRemains = 4 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_LDT10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_LDT10.setAutoDraw(false);
  }
  
  // *image_6* updates
  if (t >= 10 && image_6.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    image_6.tStart = t;  // (not accounting for frame time here)
    image_6.frameNStart = frameN;  // exact frame index
    image_6.setAutoDraw(true);
  }

  frameRemains = 10 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (image_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    image_6.setAutoDraw(false);
  }
  
  // *instr_LDT11* updates
  if (t >= 16 && instr_LDT11.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_LDT11.tStart = t;  // (not accounting for frame time here)
    instr_LDT11.frameNStart = frameN;  // exact frame index
    instr_LDT11.setAutoDraw(true);
  }

  
  // *resp_LDT_ready* updates
  if (t >= 16 && resp_LDT_ready.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_LDT_ready.tStart = t;  // (not accounting for frame time here)
    resp_LDT_ready.frameNStart = frameN;  // exact frame index
    resp_LDT_ready.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_LDT_ready.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_LDT_ready.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['right']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_LDT_ready.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_LDT_ready.rt = resp_LDT_ready.clock.getTime();
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instr_LDT_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instr_LDT_2RoutineEnd() {
  //------Ending Routine 'instr_LDT_2'-------
  for (const thisComponent of instr_LDT_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_LDT_ready.keys === undefined || resp_LDT_ready.keys.length === 0) {    // No response was made
      resp_LDT_ready.keys = undefined;
  }
  
  psychoJS.experiment.addData('resp_LDT_ready.keys', resp_LDT_ready.keys);
  if (typeof resp_LDT_ready.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_LDT_ready.rt', resp_LDT_ready.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "instr_LDT_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var resp_LDT;
var LDT_trialComponents;
function LDT_trialRoutineBegin() {
  //------Prepare to start Routine 'LDT_trial'-------
  t = 0;
  LDT_trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  LDT_word_2.setText(words);
  LDT_mask_2.setText(mask);
  resp_LDT = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  LDT_trialComponents = [];
  LDT_trialComponents.push(LDT_word_2);
  LDT_trialComponents.push(LDT_mask_2);
  LDT_trialComponents.push(resp_LDT);
  LDT_trialComponents.push(key_reminder_4);
  
  for (const thisComponent of LDT_trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function LDT_trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'LDT_trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = LDT_trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *LDT_word_2* updates
  if (t >= 0 && LDT_word_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LDT_word_2.tStart = t;  // (not accounting for frame time here)
    LDT_word_2.frameNStart = frameN;  // exact frame index
    LDT_word_2.setAutoDraw(true);
  }

  frameRemains = 0 + ldt_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (LDT_word_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    LDT_word_2.setAutoDraw(false);
  }
  
  // *LDT_mask_2* updates
  if (t >= 0.06 && LDT_mask_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LDT_mask_2.tStart = t;  // (not accounting for frame time here)
    LDT_mask_2.frameNStart = frameN;  // exact frame index
    LDT_mask_2.setAutoDraw(true);
  }

  
  // *resp_LDT* updates
  if (t >= 0.06 && resp_LDT.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    resp_LDT.tStart = t;  // (not accounting for frame time here)
    resp_LDT.frameNStart = frameN;  // exact frame index
    resp_LDT.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { resp_LDT.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (resp_LDT.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['left', 'right', 'escape']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
        psychoJS.experiment.experimentEnded = true;
    }
    if (theseKeys.length > 0) {  // at least one key was pressed
      resp_LDT.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      resp_LDT.rt = resp_LDT.clock.getTime();
      // was this 'correct'?
      if (resp_LDT.keys == corr_ans) {
          resp_LDT.corr = 1;
      } else {
          resp_LDT.corr = 0;
      }
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  
  // *key_reminder_4* updates
  if (t >= 0.06 && key_reminder_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_reminder_4.tStart = t;  // (not accounting for frame time here)
    key_reminder_4.frameNStart = frameN;  // exact frame index
    key_reminder_4.setAutoDraw(true);
  }

  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of LDT_trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function LDT_trialRoutineEnd() {
  //------Ending Routine 'LDT_trial'-------
  for (const thisComponent of LDT_trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (resp_LDT.keys === undefined || resp_LDT.keys.length === 0) {    // No response was made
      resp_LDT.keys = undefined;
  }
  
  // was no response the correct answer?!
  if (resp_LDT.keys === undefined) {
    if (['None','none',undefined].includes(corr_ans)) {
       resp_LDT.corr = 1  // correct non-response
    } else {
       resp_LDT.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('resp_LDT.keys', resp_LDT.keys);
  psychoJS.experiment.addData('resp_LDT.corr', resp_LDT.corr);
  if (typeof resp_LDT.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('resp_LDT.rt', resp_LDT.rt);
      routineTimer.reset();
      }
  
  
  // the Routine "LDT_trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var LDT_feedbackComponents;
function LDT_feedbackRoutineBegin() {
  //------Prepare to start Routine 'LDT_feedback'-------
  t = 0;
  LDT_feedbackClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  
  // keep track of which components have finished
  LDT_feedbackComponents = [];
  LDT_feedbackComponents.push(LDT_feedback_inst);
  
  for (const thisComponent of LDT_feedbackComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function LDT_feedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'LDT_feedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = LDT_feedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *LDT_feedback_inst* updates
  if (t >= 0.0 && LDT_feedback_inst.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    LDT_feedback_inst.tStart = t;  // (not accounting for frame time here)
    LDT_feedback_inst.frameNStart = frameN;  // exact frame index
    LDT_feedback_inst.setAutoDraw(true);
  }

  frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (LDT_feedback_inst.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    LDT_feedback_inst.setAutoDraw(false);
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of LDT_feedbackComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function LDT_feedbackRoutineEnd() {
  //------Ending Routine 'LDT_feedback'-------
  for (const thisComponent of LDT_feedbackComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // the Routine "LDT_feedback" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endComponents;
function endRoutineBegin() {
  //------Prepare to start Routine 'end'-------
  t = 0;
  endClock.reset(); // clock
  frameN = -1;
  routineTimer.add(6.000000);
  // update component parameters for each repeat
  
  // keep track of which components have finished
  endComponents = [];
  endComponents.push(instr_end);
  
  for (const thisComponent of endComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function endRoutineEachFrame() {
  //------Loop for each frame of Routine 'end'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = endClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instr_end* updates
  if (t >= 0.0 && instr_end.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instr_end.tStart = t;  // (not accounting for frame time here)
    instr_end.frameNStart = frameN;  // exact frame index
    instr_end.setAutoDraw(true);
  }

  frameRemains = 0.0 + 6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (instr_end.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    instr_end.setAutoDraw(false);
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of endComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // check for quit (the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEnd() {
  //------Ending Routine 'end'-------
  for (const thisComponent of endComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({message, isCompleted});

  return Scheduler.Event.QUIT;
}
