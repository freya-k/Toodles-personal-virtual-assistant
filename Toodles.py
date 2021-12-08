import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import requests
import time
import pyjokes
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk
import PyPDF2
import sys
import smtplib
import tkinter
from tkinter import messagebox
import winsound

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

def message_bx():
    top = Toplevel()
    top.title("Help")
    top.geometry("500x600")

    text1 = "INSTRUCTIONS FOR COMMAND:"
    text2 = "General:"
    text3 = "To make a Wikipedia search on any topic, please use the word 'Wikipedia' in your instruction."
    text4 = "To open YouTube, please say 'Open YouTube'."
    text5 = "To open the Google homepage, please say 'Open Google'."
    text6 = "To know the time, please include 'time' in your instruction."
    text7 = "To know the news headlines, please include 'News' in your instruction."
    text8 = "To conduct a general websearch or play anything from the web, please use 'search' or 'play' in your instruction."
    text9 = "For a joke, please use 'joke' in your instruction."
    text11 = "Notes:"
    text12 = "To write a note, please include 'Write a note' in your instruction."
    text13 = "To view your notes, please use 'Show note' in your instruction."
    text14 = "GMail related:"
    text15 = "To open GMail, please say 'Open Gmail'."
    text16 = "To send an Email to a particular person, please include 'Send email to' or 'Send an email' in your instruction. And then mention the reciever's email address."
    text17 = "NOTE: You can only avail these two features if you have changed the security settings in your GMail to 'allowed' for access to low-security apps."
    text18 = "Buttons:"
    text19 = "Speak something button allows you to give instructions to Toodles."
    text20 = "Help button leads you to the user manual."
    text21 = "Pomodoro Timer button starts a timer for twenty five minutes."
    text22 = "Stop button shuts down the program."
    
    page_title = Label(top, text=text1, background="white", foreground="black", font="NoveSquare 64")
    page_title.pack()

    L1 = Label(top, text=text2, bg="#0d0d0d", fg="#d4f5f1", font="NoveSquare 24")
    L1.pack()

    wiki_search = Label(top, text=text3, bg="white", fg="black", font="NoveSquare 10")
    wiki_search.pack()

    yt = Label(top, text=text4, bg="white", fg="black", font="NoveSquare 10")
    yt.pack()

    google_open = Label(top, text=text5, bg="white", fg="black", font="NoveSquare 10")
    google_open.pack()

    tell_time = Label(top, text=text6, bg="white", fg="black", font="NoveSquare 10")
    tell_time.pack()

    headlines = Label(top, text=text7, bg="white", fg="black", font="NoveSquare 10")
    headlines.pack()

    web_search = Label(top, text=text8, bg="white", fg="black", font="NoveSquare 10")
    web_search.pack()

    jokes = Label(top, text=text9, bg="white", fg="black", font="NoveSquare 10")
    jokes.pack()


    L2 = Label(top, text=text11, bg="#0d0d0d", fg="#d4f5f1", font="NoveSquare 24")
    L2.pack()

    note_write = Label(top, text=text12, bg="white", fg="black", font="NoveSquare 10")
    note_write.pack()

    note_show = Label(top, text=text13, bg="white", fg="black", font="NoveSquare 10")
    note_show.pack()

    L3 = Label(top, text=text14, bg="#0d0d0d", fg="#d4f5f1", font="NoveSquare 24")
    L3.pack()

    gmail_open = Label(top, text=text15, bg="white", fg="black", font="NoveSquare 10")
    gmail_open.pack()

    gmail_to = Label(top, text=text16, bg="white", fg="black", font="NoveSquare 10")
    gmail_to.pack()


    warn1 = Label(top, text=text17, bg="white", fg="red", font="NoveSquare 10")
    warn1.pack()

    L4 = Label(top, text=text18, bg="#0d0d0d", fg="#d4f5f1", font="NoveSquare 24")
    L4.pack()

    TE1 = Label(top, text=text19, bg="white", fg="black", font="NoveSquare 10")
    TE1.pack()

    TE2 = Label(top, text=text20, bg="white", fg="black", font="NoveSquare 10")
    TE2.pack()

    TE3 = Label(top, text=text21, bg="white", fg="black", font="NoveSquare 10")
    TE3.pack()

    TE4 = Label(top, text=text22, bg="white", fg="black", font="NoveSquare 10")
    TE4.pack()

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    
    server.login('enter your email address', 'enter your password')
    server.sendmail('enter your email address', to, content)
    server.close()

    
def pomodoroTimer():
    t_now = datetime.datetime.now()
    t_pom = 25*60
    t_delta = datetime.timedelta(0, t_pom)
    t_fut = t_now + t_delta
    delta_sec = 5*60
    t_fin = t_now + datetime.timedelta(0, t_pom+delta_sec)
    total_pomodoros = 0
    breaks = 0


    messagebox.showinfo("Pomodoro started!", "\nIt is now "+t_now.strftime("%H:%M") + " hours. \nTimer set for 25 minutes.")
    total_pomodoros = 0
    breaks = 0


    while True:
        if t_now < t_fut:
            print("Pomodoro time!")
            speak("Pomodoro time!")

        elif t_fut <= t_now <= t_fin:
            print("Break.")
            if breaks == 0:
                print("If break")
                for i in range(5):
                    winsound.Beep((i+100), 700)
                print("Break Time!")
                speak("Break Time!")
                breaks += 1
        else:
            print("Finished")
            speak("Finished")
            breaks += 0

            for i in range(10):
                winsound.Beep((i+100), 500)

                usr_ans = messagebox.askyesno("Pomodoro finished!","Would you like to start another pomodoro?")
                total_pomodoros += 1
                if usr_ans == True:
                    t_now = datetime.datetime.now()
                    t_fut = t_now + dt.timedelta(0, t_pom)
                    t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)
                    continue
                elif usr_ans == False:
                    messagebox.showinfo("Pomodoro finished!", "\nYou completed" + str(total_pomodoros) + " Pomodoros today!")

        print("Sleeping...")
        time.sleep(20)
        t_now = datetime.datetime.now()
        timenow = t_now.strftime("%H:%M")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            print("Recognizing....")
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement

print("Loading your AI personal assistant Toodles")
speak("Loading your AI personal assistant Toodles")



def btn_clicked():
    if __name__=='__main__':

        while True:
            
            speak("Tell me how can I help you now?")
            statement = takeCommand().lower()
            if statement==0:
                continue

            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak('your personal assistant Toodles is shutting down,Good bye')
                print('your personal assistant Toodles is shutting down,Good bye')
                window.destroy

            elif 'wikipedia' in statement:
                speak('Searching Wikipedia...')
                statement =statement.replace("wikipedia", "")
                results = wikipedia.summary(statement, sentences=3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in statement:
                speak('Opening Youtube')
                webbrowser.open("http://www.youtube.com/results?search_query=")
                time.sleep(5)

            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.co.in/")
                speak("Google chrome is open now")
                time.sleep(5)

            elif 'open gmail' in statement:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif 'time' in statement:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif 'news' in statement:
                news = webbrowser.open_new_tab('https://timesofindia.indiatimes.com/home/headlines')
                speak('Here are some headlines from the Times of India,Happy reading')
                time.sleep(6)

                 
            elif 'search' in statement or 'play' in statement:
             
                statement = statement.replace("search", "")
                result = statement
                speak(statement)
                statement = statement.replace("play", "")         
                webbrowser.open_new_tab(statement)
                
                time.sleep(5)


 
            elif 'send a mail' in statement or 'send an email' in statement:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    speak("whom should i send this to?")
                    to = input()   
                    sendEmail(to, content)
                    speak("Email has been sent !")
                except Exception as e:
                    print("I am not able to send this email")
                    speak("I am not able to send this email")

            elif 'joke' in statement:
                My_joke = pyjokes.get_joke(language="en", category="all")
                speak(My_joke)
                print(My_joke)

            elif "write a note" in statement:
                speak("What should i write")
                note = takeCommand()
                file = open('jarvis.txt', 'w')
                file.write(note)
         
            elif "show note" in statement:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                top = Toplevel()
                top.title("Help")
                top.geometry("500x600")
                print(file.read())
                speak(file.read(6))


            elif 'who are you' in statement or 'what can you do' in statement:
                speak('I am Toodles version 1 point O your personal assistant. I am programmed to minor tasks like'
                          'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                          'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


            elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
                speak("I was built by Freya")
                print("I was built by Freya")

            elif "what can you do" in statement or "what functions can you perform" in statement:
                speak("Kindly refer to the list created to help you. You can access this list by clicking on the 'Help' button")


window = Tk()

window.geometry = ("1440x1024")
bg = PhotoImage( file = 'C:\\Users\\admin\\Desktop\\Toodlebg.png')
canvas1 = Canvas(window, width = 1640, height = 1224)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image(0, 0, image = bg, anchor = NW)

frame1_myButton = Button(canvas1, borderwidth = 0, text="Speak something!",bg="#d4f5f1", fg="Black", command=btn_clicked)
frame1_myButton.pack()
frame1_myButton.place(x=670, y=290)

frame1_helpbtn = Button(canvas1, borderwidth = 0, text="Help", bg="#d4f5f1", fg="Black", command= message_bx)
frame1_helpbtn.pack()
frame1_helpbtn.place(x=470, y=490)

stop_btn = Button(canvas1,borderwidth = 0, text="Stop", bg="red", fg="Black", command= window.destroy)
stop_btn.pack()
stop_btn.place(x=920, y=490)

Pomodorobtn = Button(canvas1, borderwidth =0, text = 'Pomodoro Time', command = pomodoroTimer)
Pomodorobtn.pack()
Pomodorobtn.place(x=670, y=490)






window.resizable(True, True)
window.mainloop()
