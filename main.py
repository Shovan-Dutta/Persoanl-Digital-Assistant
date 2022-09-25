# 1 including all the library
# including the prebuild libraries
import pyttsx3 #pyttxs3 is a text to speech conversion
import speech_recognition as sr 
#including the user build libraries
import search
import restart_logout
import dt
import dictation
import toss_roll
import open_close
import weather_location
import system
import web_news
import brightness
#TKINTER
from tkinter import *
import tkinter
import PIL.Image, PIL.ImageTk
from PIL import Image


# IT IS USE FOR TKINTER
window = Tk()
window.title('ASSISTANT')

global var
global var1
bcolor = "black"

window.configure(bg=bcolor)
var = StringVar()
var1 = StringVar()
onImg = PhotoImage(file=r"stoggle-on.png")
offImg = PhotoImage(file=r"stoggle-off.png")

# 2 setting up the speechvoice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #DAVID & ZIRA 
engine.setProperty('rate', 168)

def update(ind):
    frame = frames[(ind)%20]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

# setting the dark and light mode with the switchs(function)
btnState = False
def switch():
    global btnState
    if btnState:
        btn.config(image=offImg, bg="black", activebackground="black")
        window.config(bg="black")
        chat1frame.config(bg = "black")
        bframe.config(bg = "black")
        dark.config(bg = "black",fg="white")
        light.config(bg = "black",fg="white")
        label.config(bg = "black")
        tframe.config(bg = "black")
        creditsframe.config(bg ="black")
        engine.setProperty('voice', voices[0].id)
        btnState = False
        return("Activating Dark Mode")
    else:
        btn.config(image=onImg, bg="white", activebackground="white")
        window.config(bg="white")
        chat1frame.config(bg = "white")
        bframe.config(bg = "white")
        dark.config(bg="white",fg="black")
        light.config(bg="white",fg="black")
        label.config(bg = "white")
        tframe.config(bg = "white")
        creditsframe.config(bg="white")
        engine.setProperty('voice', voices[1].id)
        btnState = True
        return("Activating Light Mode")
        

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# 3 for introduction
def intro():
    hour = dt.hour() 
    if hour>=0 and hour<12:
        var.set("A Very Good Morning!") # IT IS DISPLAY IN TKINTER
        window.update()
        speak("A very Good Morning!")

    elif hour>=12 and hour<18:
        var.set("Good Afternoon")
        window.update()
        speak("Good Afternoon!")   

    else:
        var.set("Good Evening!")
        window.update()
        speak("Good Evening!")  

    speak("Hello there, let me first introduce my creators! First there is SOUGATA PATRA, then there is Ritushree Dey, Shuvranshu Som, Rohita Kundu and last but not the least Shovan Dutta! ")
    speak("And I am your personal digital assistant. My job is to automate your small tasks with the help of voice commands. It would be my pleasure to do so. You can tell me what to do just by clicking the green play button.")


# 4 to wish every time it starts
def wishMe():
    hour = dt.hour() 
    if hour>=0 and hour<12:
        var.set("A Very Good Morning!") # IT IS DISPLAY IN TKINTER
        window.update()
        speak("A very Good Morning!")

    elif hour>=12 and hour<18:
        var.set("Good Afternoon")
        window.update()
        speak("Good Afternoon!")   

    else:
        var.set("Good Evening!")
        window.update()
        speak("Good Evening!")  

    d1 = dt.tellday()
    d2 = dt.dat()
    strTime = dt.tim()
    speak("Today is " + d1+ " " + d2 +", the time is " + strTime + " and I am your personal digital assistant, very excited and ready to help you! ")

# 5 for speech recognition
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source, duration = 6)

    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")    
        query = r.recognize_google(audio, language='eng-in')  #recognize_google function uses google audio to recognize speech
        #if "brother" in query or 'sister' in query:
        print(f"You said: {query}\n")
    

    except Exception as e:
        #print(e)    
        print("...")  
        return "None"
    var1.set(query)
    window.update()
    return query

#The Main function:
#6 The main function starts from here,the commands given by user is stored in the variable statement
#if __name__ == "__main__":
#tkinter buttom
def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg = 'orange')
    wishMe()
    while True:
        btn1.configure(bg = 'orange')
        query = takeCommand().lower()
        if 'stop' in query or'exit' in query or 'leave' in query or "go now" in query:
            var.set("Bye,Thanks for giving me your time")
            btn1.configure(bg = '#9efd38')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Thanks for giving me your time")
            break

# 7 to change volume
        elif 'volume' in query:
            dictation.vol(query)

# 8 Activate and deactivate light mode
        elif "light mode" in query or "dark mode" in query:
            s=switch()
            var.set(s)#IT US SHOWING IN TKINTER
            window.update()
            speak(s)

# 9 Increase & decrease brightness
        elif "brightness" in query:
            if "increase" in query:
                v = brightness.increase()
                var.set(v)#IT US SHOWING IN TKINTER
                window.update()
                speak(v)
            else:
                v = brightness.decrease()
                var.set(v)#IT US SHOWING IN TKINTER
                window.update()
                speak(v)

# 10 just opens youtube, whatsapp, e-carts, social media, google webpages (online feature)
        elif 'open youtube' in query:
            var.set('opening Youtube')#IT US SHOWING IN TKINTER
            window.update()
            speak('opening Youtube')
            web_news.youtube()
        elif 'open whatsapp' in query:
            var.set('opening WhatsApp')#IT US SHOWING IN TKINTER
            window.update()
            speak("opening WhatsApp")
            web_news.whatsapp()
        elif 'open google' in query:
            var.set('opening Google')#IT US SHOWING IN TKINTER
            window.update()
            speak("Opening Google")
            web_news.google()
        elif 'open gmail' in query:
            var.set('opening gmail')#IT US SHOWING IN TKINTER
            window.update()
            speak("opening Gmail")
            web_news.gmail()
        elif 'open wikipedia' in query:
            var.set('opening Wikipedia')#IT US SHOWING IN TKINTER
            window.update()
            speak("Opening Wikipedia")
            web_news.wikipedia()
        elif 'open amazon' in query:
            var.set('opening Amazon')#IT US SHOWING IN TKINTER
            window.update()
            speak('opening Amazon')
            web_news.amazon()
        elif 'open flipkart' in query:
            var.set('opening Flipkart')#IT US SHOWING IN TKINTER
            window.update()
            speak('Opening Flipkart' )
            web_news.amazon()
        elif 'open facebook' in query:
            var.set('opening Facebook')#IT US SHOWING IN TKINTER
            window.update()
            speak('Opening Facebook')
            web_news.facebook()
        elif 'open instagram' in query:
            var.set('opening Instagram')#IT US SHOWING IN TKINTER
            window.update()
            speak('opening Instagram')
            web_news.instagram()

# 11 fetches news.(supported languages for news English, Hindi, Bengali) (online feature)
        elif 'news' in query:
            var.set('I just pulled this live stream and some articles. \nHere you go!')#IT US SHOWING IN TKINTER
            window.update()
            speak("I just pulled this live stream and some articles. Here you go!")
            if "english" in query:
                web_news.eng_news()
            elif "hindi" in query:
                web_news.hin_news()
            elif "bengali" in query or "bangla" in query:
                web_news.beng_news()
            elif "read" in query or 'news' in query:
                web_news.read_news()

# 12 tells about the day, date, time, weather with one command.(online feature)
        elif 'brief me' in query or "what's up" in query or 'about today' in query:
            try:
                d1 = dt.tellday()
                d2 = dt.dat()
                w = weather_location.weather()
                strTime = dt.tim()
                var.set("Today is" + d1 + d2 +", the time is" + strTime + ", \nand it is " + str(w[0]) + "degrees outside")#IT US SHOWING IN TKINTER
                window.update()
                speak("Today is" + d1 + d2 +", the time is" + strTime + ", and it is " + str(w[0]) + "degrees outside" )
            except Exception:
                speak('something went wrong please try again')

# 13 tells my current location ('city', 'state', 'country') (online feature)
        elif 'current location' in query or 'present location' in query or 'where am i' in query:
            w = weather_location.locate()
            var.set("we are currently at " + str(w[0])+' in the state ' +str(w[1])+ ' in the country' + str(w[2]))#IT US SHOWING IN TKINTER
            window.update()
            speak("we are currently at " + str(w[0])+' in the state ' +str(w[1])+ ' in the country' + str(w[2]) )

# 14 tells the battery percentage (offline feature)
        elif 'battery information' in query or 'battery status' in query or 'battery' in query:
            s = system.battery_info()
            if bool(s[1]) == True :
                var.set("The battery is at " + str(s[0]) + " percent and \nis currently plugged in.")#IT US SHOWING IN TKINTER
                window.update()
                speak("The battery is at " + str(s[0]) + " percent and is currently plugged in.")
            else:
                var.set("The battery is at " + str(s[0]) + "percent and \nis not currently plugged in.")#IT US SHOWING IN TKINTER
                window.update()
                speak("The battery is at " + str(s[0]) + "percent and is not currently plugged in.")

# 15 takes screenshot(offline feature)
        elif 'screenshot' in query:
            if dictation.screenshot() != 0:
                var.set('screenshot has been successfully taken and \nsaved in the public pictures folder in the c drive')#IT US SHOWING IN TKINTER
                window.update()
                speak('screenshot has been successfully taken and saved in the public pictures folder in the c drive')
            else:
                var.set("something went wrong please try again")#IT US SHOWING IN TKINTER
                window.update()
                speak("something went wrong please try again")

# 16 tells the current weather condition of the current location(online feature)
        elif 'weather report' in query or 'weather' in query:
            try:
                w = weather_location.weather()
                var.set('the current temperature is ' + str(w[0])+' degrees, \nbut feels like '+ str(w[2]) +' degrees, '+ 'and the currnet humidity is' + str(w[1]))#IT US SHOWING IN TKINTER
                window.update()
                speak ('the current temperature is ' + str(w[0])+' degree, but feels like '+ str(w[2]) +' degrees, '+ 'and the currnet humidity is' + str(w[1]))
            except Exception:
                var.set('something went wrong please try again later')#IT US SHOWING IN TKINTER
                window.update()
                speak('something went wrong please try again later')

# 17 set timer (offline feature)
        elif 'countdown' in query or 'timer' in query:
            speak ("for how long should I set the timer for ?")
            speak ("tell the duration in minutes")
            d = takeCommand()
            if "minute" in d or "minutes" in d:
                result = d.find('minute' or 'minutes')
                d =d.replace(d[result:], "")
            if dictation.countdown(d) != 0:
                speak(" Time Up! Time up! Time up!")

# 18 tells about the current cpu and ram usage(offline feature)
        elif 'system information' in query:
            s =system.current_sys()
            v = str(brightness.current())
            var.set('The current cpu usage is around ' + str(s[0])+ 'percent, ram at ' + str(s[1])+ " percent \nwith "+ v+" percent screen brightness")#IT US SHOWING IN TKINTER
            window.update()
            speak('The current cpu usage is around ' + str(s[0])+ 'percent, ram at ' + str(s[1])+ " percent with "+ v+" percent screen brightness")

# 19 carries out normal conversations (offline feature)
        elif 'thank you' in query:
            var.set("I am pleased, that i could help you")#IT US SHOWING IN TKINTER
            window.update()
            speak("I am pleased, that i could help you")
        elif 'how are you' in query:
            var.set("I am fine, Thank you")#IT US SHOWING IN TKINTER
            window.update()
            speak("I am fine, Thank you")
        elif 'am lonely' in query:
            var.set("I am always here for you")#IT US SHOWING IN TKINTER
            window.update()
            speak("I am always here for you")
        elif 'what are you' in query or 'who are you' in query:
            var.set("I am few lines of python code")#IT US SHOWING IN TKINTER
            window.update()
            speak("I am few lines of python code")
        elif 'help me' in query:
            var.set("Just let me know what to do !")#IT US SHOWING IN TKINTER
            window.update()
            speak("Just let me know what to do !")
        elif 'what can you do' in query:
            var.set('i can do many things just try me')#IT US SHOWING IN TKINTER
            window.update()
            speak('i can do many things just try me')
        elif "made you" in query or "created you" in query: 
            var.set("I have been created by you guys.")#IT US SHOWING IN TKINTER
            window.update()
            speak("I have been created by you guys.") 
        elif "who i am" in query:
            var.set("If you talk then definately your human.")#IT US SHOWING IN TKINTER
            window.update()
            speak("If you talk then definately your human.")
        elif "why you came to world" in query:
            var.set("You guys made me, so you know better")#IT US SHOWING IN TKINTER
            window.update()
            speak("You guys made me, so you know better")
        elif "What is the meaning of life ?" in query:
            var.set("42")#IT US SHOWING IN TKINTER
            window.update()
            speak("42")#1st easter egg

# 20 meaning, synonyms, Antonyms(online feature)

        elif "meaning" in query or "meanings" in query:
            m = dictation.meaning(query)
            if m != 0:
                var.set("the meanings are")#IT US SHOWING IN TKINTER
                window.update()
                speak("the meanings are")
                speak(m)
            else:
                var.set("something went wrong please try again")#IT US SHOWING IN TKINTER
                window.update()
                speak("something went wrong please try again")
        elif "synonym" in query or "synonyms" in query:
            m = dictation.syno(query)
            if m != 0:
                var.set("the synonyms are")#IT US SHOWING IN TKINTER
                window.update()
                speak("the synonyms are")
                speak(m)
            else:
                var.set("something went wrong please try again")#IT US SHOWING IN TKINTER
                window.update()
                speak("something went wrong please try again")
        elif "antonym" in query or "antonyms" in query:
            m = dictation.anto(query)
            if m != 0:
                var.set("the antonyms are")#IT US SHOWING IN TKINTER
                window.update()
                speak("the antonyms are")
                speak(m)
            else:
                var.set("something went wrong please try again")#IT US SHOWING IN TKINTER
                window.update()
                speak("something went wrong please try again")

# 21 tells the current time or day or date only (offline feature)
        elif 'time' in query:
            strTime = dt.tim() 
            var.set("Sir the time is %s "% strTime )
            window.update()
            speak("Now, the time is "+strTime)
        elif "day" in query or 'date' in query: 
            day = dt.tellday()
            dat = dt.dat()
            var.set("Today is" + day +"and the date is "+dat)
            window.update()
            speak("Today is" + day +"and the date is "+dat)

# 22 search for summery or definition from wikipedia, search for videos and play songs and search normally in google. (online feature)
        elif 'search' in query or 'online' in query or "about" in query or "summary" in query or "play" in query or "describe" in query or "what" in query or "where" in query or "when" in query or "wikipedia" in query or 'google' in query or 'youtube' in query:
            var.set("searching")
            window.update()
            if 'google' in query or 'online' in query or "where" in query or 'when' in query:
                speak('searching')
                if search.gs(query) != 0:
                    speak("found this on google")
                else:
                    var.set("something went wrong please try again")
                    window.update()
                    speak("something went wrong please try again")
            elif "youtube" in query or "video" in query or "song" in query or "play" in query:
                speak('searching')
                if search.yt(query) != 0:
                    speak("this is the first thing i found on youtube")
                else:
                    var.set("something went wrong please try again")
                    window.update()
                    speak("something went wrong please try again")
            elif "wikipedia" in query:
                try:
                    speak('searching')
                    w = search.wikiopen(query)
                    speak("here you go!")
                    web_news.open(w[0])
                    speak("according to wikipedia")
                    speak(w[1])
                except Exception:
                    var.set("something went wrong please try again")
                    window.update()
                    speak("something went wrong please try again")    
            elif "about" in query or "summary" in query or "describe" in query or "what" in query :
                try:
                    speak('searching')
                    speak("just a moment please")
                    w = search.wiki(query)
                    speak(w)
                except Exception:
                    var.set("something went wrong please try again")
                    window.update()
                    speak("something went wrong please try again")

# 23 opens any application on the machine (offline feature)
        elif 'open' in query:
            var.set("just a second")
            window.update()
            speak("just a second")
            if open_close.open(query) != 1:
                var.set("Please repeat, i didn't get you!")
                window.update()
                speak("Please repeat, i didn't get you!")

# 24 closes any open application on the machine(offline feature)
        elif 'close' in query:
            if(open_close.close(query) == 1):
                var.set("Application closed successfully!")
                window.update()
                speak("Application closed successfully!")
            else:
                var.set("something went wrong please try again!")
                window.update()
                speak("something went wrong please try again!")

# 25 takes small notes .txt file  (live trans-script)(offline feature)
        elif 'write a note' in query or "note" in query or 'write' in query :
            var.set('pease tell what to note')
            window.update()
            speak('pease tell what to note')
            note = takeCommand()
            if dictation.dict(note) != 0:
                var.set("I have taken down the note and \nsaved it in the public documents folder in c drive! ")
                window.update()
                speak ("I have taken down the note and saved it in the public documents folder in c drive! ")
            else:
                var.set('I could not take down the note due to some error!')
                window.update()
                speak('I could not take down the note due to some error!')

# 26 shutdown, restart,logout the computer and cancel the shutdown of the computer (offline feature)
        elif 'cancel shutdown' in query:
            search.cancelsd()
            var.set("shutdown procedure has been terminated!")
            window.update()
            speak("shutdown procedure has been terminated!")
        elif 'shutdown' in query:
            search.sd()
            var.set('shutdown will initiate in exactly 60 seconds')
            window.update()
            speak('shutdown will initiate in exactly 60 seconds')
        elif 'restart' in query:
            restart_logout.restart()
            var.set('restart will initiate in 60 seconds')
            window.update()
            speak('restart will initiate in 60 seconds')
        elif 'log out' in query:
            restart_logout.logout()
            var.set('logout will initiate in 60 seconds')
            window.update()
            speak('logout will initiate in 60 seconds')

# 27 to make voice recording (offline feature)
        elif 'voice recording' in query or 'record voice' in query or 'audio recording' in query or 'record audio' in query:
            speak ("for how long should I record?")
            speak ("tell the duration in minutes")
            d = takeCommand()
            if "minute" in d or "minutes" in d:
                result = d.find('minute' or 'minutes')
                d =d.replace(d[result:], "")
            if dictation.voicerecord(d) != 0:
                var.set('the voice recording has been saved in the public music folder \nin the c drive in your computer')
                window.update()
                speak ('the voice recording has been saved in the public music folder in the c drive in your computer')
            else:
                var.set("the voice recording either could not be \ncreated or could not be saved. ")
                window.update()
                speak("the voice recording either could not be created or could not be saved. ")

# 28 to toss a coin or roll a dice (offline feature)
        elif 'toss a coin' in query or 'toss again' in query:
            a= toss_roll.coin()
            var.set(a)
            window.update()
            speak(a)
        elif 'roll a dice' in query or 'roll again' in query:
            a=toss_roll.dice()
            var.set(a)
            window.update()
            speak(a)

# 29 to stop or close and prevent listening for a period of time & sleep mode (offline feature)
        elif "don't listen" in query or "stop listening" in query or "sleep mode" in query:
            var.set("For how many minutes you want me to \nstop listening")
            window.update() 
            speak("For how many minutes you want me to stop listening")
            d = takeCommand()
            if "minute" in d or "minutes" in d:
                result = d.find('minute' or 'minutes')
                d =d.replace(d[result:], "")
            if dictation.sleep(d) != 0:
                var.set('Sleep mode was Successful!')
                window.update()
                speak('Sleep mode was Successful!')
            else:
                var.set("Something went wrong please try again later!")
                window.update()
                speak("Something went wrong please try again later!")

# it is tkinter part 

# setting the top labels user and welcome
chat1frame = Frame(window,pady=10,background=bcolor)
chat1frame.pack()

label1 = Label(chat1frame, textvariable = var1,bg = '#f8de7e',padx=10,pady=5,font=("Times", 20))
var1.set('USER')
label1.grid(column = 0,row= 0,pady=2.5)

label2 = Label(chat1frame, textvariable = var, bg = '#87cefa',padx=10,pady=5,font=("Times", 20))
var.set('! WELCOME !')
label2.grid(column=0,row=1,pady=2.5)

#adding the gif robot image
frames = [PhotoImage(file='r1.gif',format = 'gif -index %i' %(i)) for i in range(20)]
label = Label(window, width = 550, height = 400, background=bcolor)
label.pack()
window.after(0, update, 0)


# For placing the switch / toggle button for the theme change
tframe = Frame(window,pady=10,background=bcolor, width=550)
tframe.pack()
dark = Label(tframe,text ="DARK",fg="white",font=("Times", 20), bg="black")
dark.grid(column =0,row  =0)
btn = tkinter.Button(tframe, text="OFF", borderwidth=0, command=switch, bg="black", activebackground="black")
btn.grid(column=1, row=0,padx=5)
btn.config(image=offImg)
light = Label(tframe,text ="LIGHT",fg="white",font=("Times", 20), bg="black")
light.grid(column =2,row  =0)


# For placing the buttons (wishme, play,exit)
bframe = Frame(window,background=bcolor,padx=10)
bframe.pack()
btn0 = Button(bframe,text = 'INTRO',width = 15,command= intro,bg = '#fff44f',bd=10,font=("Courier", 13))#command to be added later
btn0.grid(column=0,row=0,padx=2.5)
btn1 = Button(bframe,text = 'PLAY',width = 15,command=play, bg = '#9efd38',bd = 10,font=("Courier", 13))#command to be added later
btn1.grid(column=1,row=0)
btn2 = Button(bframe,text = 'EXIT',width = 15, command = window.destroy, bg = '#ff4040', bd = 10,font=("Courier", 13))
btn2.grid(column=2,row=0,padx=2.5)


# For showing the names involved in the project
creditsframe = Frame(window, background=bcolor)
creditsframe.pack()
label3 = Label(creditsframe,text="",font="Courier 10",pady=10,fg = "white",background=bcolor)
label3.grid(column=0, row = 0)



window.mainloop()