import dt
import os
from PyDictionary import PyDictionary
from word2number import w2n
import sounddevice
from scipy.io.wavfile import write  
import numpy as np 
import cv2 
import string
import random
import time
import pyautogui
import subprocess

# funtion to create random names for saving files
def rando_name():
    res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = 4))
    return(str(res))

# function to take dictation and save that dictation as .txt file (live transcribe)
def dict(note):
    try:
        program_name = 'notepad.exe'
        d1 = dt.tellday()
        d2 = dt.dat()
        sp = 'C:\\Users\\Public\\Documents'
        n = os.path.join(sp,d2 +'_'+d1+'.txt')
        app = open(n,'a')
        subprocess.Popen([program_name,n])
        app.write('## '+note+'. \n')
        return(1)
    except:
        return (0)
# function to find meaning of a given word
def meaning(query):
    try:
        if 'for' in query:
            result = query.find('for')
            query =query.replace(query[0:result+3], "")
        elif 'word' in query:
            result = query.find('word')
            query =query.replace(query[0:result+4], "")
        elif 'of' in query:
            result = query.find('of')
            query =query.replace(query[0:result+2], "")
        m = PyDictionary.meaning(query)
        for state in m: 
            return(m[state])
    except Exception:
        return(0) 

# function to find synonym of a given word
def syno(query):
    try:    
        if 'for' in query:
            result = query.find('for')
            query =query.replace(query[0:result+3], "")
        elif 'word' in query:
            result = query.find('word')
            query =query.replace(query[0:result+4], "")
        elif 'of' in query:
            result = query.find('of')
            query =query.replace(query[0:result+2], "")
        m = PyDictionary.synonym(query)
        return (str(m))
    except Exception:
        return (0)

# function to find antonym of a given word
def anto(query):
    try:
        if 'for' in query:
            result = query.find('for')
            query =query.replace(query[0:result+3], "")
        elif 'word' in query:
            result = query.find('word')
            query =query.replace(query[0:result+4], "")
        elif 'of' in query:
            result = query.find('of')
            query =query.replace(query[0:result+2], "")
        m = PyDictionary.antonym(query)
        return (str(m))
    except Exception:
        return (0)

# function to record voice/audio for a given period of time(in seconds)
def voicerecord(d):
    try:    
        freq = 44100  # Sampling frequency
        sp = 'C:\\Users\\Public\\Music'
        d1 = dt.tellday()
        d2 = dt.dat()
        t  = str(rando_name())
        duration = w2n.word_to_num(d) # Recording duration 
        recording = sounddevice.rec(int(60*duration * freq), samplerate=freq, channels=2) # Start recorder with the given values of duration and sample frequency 
        sounddevice.wait()# Record audio for the given number of seconds 
        # This will convert the NumPy array to an audio 
        # file with the given sampling frequency
        n = os.path.join(sp, d2 +'_'+ d1+'_' +t +'.wav') 
        write(n, freq, recording) 
        return (1)
    except Exception:
        return(0)

# function to take screenshot
def screenshot():
    try:
        sp = 'C:\\Users\\Public\\Pictures'
        d1 = dt.tellday()
        d2 = dt.dat()
        t  = str(rando_name())
        # take screenshot using pyautogui 
        image = pyautogui.screenshot() 
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR) 
        # writing it to the disk using opencv
        n = os.path.join(sp, d2 +'_'+ d1+'_' +t +'.png')
        #n = os.path.join(sp, t +'.png')
        cv2.imwrite(n, image) 
        return(1)
    except Exception:
        return(0)

def sleep(d):
    try:
        duration = w2n.word_to_num(d)
        time.sleep(duration*60)
        return(1)
    except Exception:
        return(0)

#for timer
def countdown(t):
    try:
        duration = w2n.word_to_num(t)
        d = duration *60
        while d: 
            mins, secs = divmod(d, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            d -= 1
        return(1)
    except Exception:
        return(0)

#to control volume
def vol(d):
    if 'increase' in d or 'volumeup' in d:
        pyautogui.press("volumeup")
    elif 'decrease' in d or 'volumedown' in d:
        pyautogui.press("volumedown")
    elif 'mute' in d:
        pyautogui.press('volumemute')