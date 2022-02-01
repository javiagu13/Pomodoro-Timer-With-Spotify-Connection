# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 12:26:01 2022

@author: Javi
"""

#from playsound import playsound
#playsound('')
import time
import pygame
import os
import Tkinter as tk
import ttk
from PIL import ImageTk, Image
import multiprocessing


#POMODORO_TIME=25
#REST_TIME=5
#SPOTIFY_FILE_PATH="C:/Users/Javi/AppData/Roaming/Spotify/Spotify.exe"
#SPOTIFY_FILE_PATH="C:/Program Files/WindowsApps/SpotifyAB.SpotifyMusic_1.177.645.0_x86__zpdnekdrzrea0/Spotify.exe"
#PROGRAM_TO_KILL="Spotify.exe"

file1 = open('settings.txt', 'r')
Lines = file1.readlines()


POMODORO_TIME=int(Lines[0].split("\n")[0])
REST_TIME=int(Lines[1].split("\n")[0])
SPOTIFY_FILE_PATH=Lines[2].split("\n")[0]
PROGRAM=Lines[3].split("\n")[0]
file1.close()

PROGRAM_TO_KILL="taskkill /im "+PROGRAM

def start_two_process_pomotime(windowToClose):
    if __name__ == '__main__':   
        multiprocessing.freeze_support()
        if windowToClose != None:
            windowToClose.destroy()
        print("Two Process Pomo Time")
        p2 =  multiprocessing.Process(target= TimerPomodoro)
        p1 =  multiprocessing.Process(target= start_pomodoro)
        p1.start()
        p2.start()
       
        p2.join()
        p1.join()

def start_two_process_resttime():
    if __name__ == '__main__':   
        multiprocessing.freeze_support()
        p2 =  multiprocessing.Process(target= TimerRest)
        p1 =  multiprocessing.Process(target= start_rest)
        p1.start()
        p2.start()
       
        p2.join()
        p1.join()
        
        imReady()
    
    
    
def start_pomodoro():
        file1 = open('settings.txt', 'r')
        Lines = file1.readlines()
        POMODORO_TIME=int(Lines[0].split("\n")[0])
        REST_TIME=int(Lines[1].split("\n")[0])
        SPOTIFY_FILE_PATH=Lines[2].split("\n")[0]
        PROGRAM=Lines[3].split("\n")[0]
        file1.close()
        
        #POMODORO BEGIN
        pygame.mixer.init()
        pygame.mixer.music.load('pomodoroBegin.mp3')
        pygame.mixer.music.play()
        time.sleep((60*POMODORO_TIME)-30)
        
        #30 SECOND TO REST
        pygame.mixer.init()
        pygame.mixer.music.load('30second.mp3')
        pygame.mixer.music.play()
        print("This prints once a minute.")
        time.sleep(15) 
        
        #15 SECOND TO REST
        pygame.mixer.init()
        pygame.mixer.music.load('15second.mp3')
        pygame.mixer.music.play()
        time.sleep(15) 
        start_two_process_resttime()
        
        
        
def start_rest():
        #REST TIME
        os.system(PROGRAM_TO_KILL)
        time.sleep((60*REST_TIME)-15)
        
        
        #15 SECOND TO GO BACK
        pygame.mixer.init()
        pygame.mixer.music.load('rest15second.mp3')
        pygame.mixer.music.play()
        time.sleep(15)
        os.startfile(SPOTIFY_FILE_PATH)
        start_two_process_pomotime(None)
        

def imReady():
    if __name__ == '__main__':  
        multiprocessing.freeze_support()
        newWindow = tk.Tk()
        newWindow.configure(background='black')
        newWindow.title("New Window")
        newWindow.geometry("400x200")
        my_label = tk.Label(newWindow, background="black", fg="white",text="Prepare your music!", font=("Helvetica",28))
        my_label.place(x=40,y=43)
        button2 = ttk.Button(newWindow, text="I'm Ready!",width=25,command=lambda:start_two_process_pomotime(newWindow))
        button2.place(x=125,y=150)
        os.startfile(SPOTIFY_FILE_PATH)
        #root.destroy()
        
def TimerPomodoro():
    newWindow = tk.Tk()
    newWindow.configure(background='black')
    newWindow.title("Timer")
    my_label = tk.Label(newWindow, background="black", fg="white",text="WORK TIME!", font=("Helvetica",38))
    my_label.place(x=40,y=30)
    newWindow.geometry("400x200")
    my_label = tk.Label(newWindow, background="black", fg="white",text="TIMER!", font=("Helvetica",48))
    my_label.place(x=80,y=100)
    mins=str(POMODORO_TIME)
    submit(newWindow,my_label,"00",mins,"00")
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)

def TimerRest():
    newWindow = tk.Tk()
    newWindow.configure(background='black')
    newWindow.title("Timer")
    my_label = tk.Label(newWindow, background="black", fg="white",text="REST TIME!", font=("Helvetica",38))
    my_label.place(x=40,y=30)
    newWindow.geometry("400x200")
    my_label = tk.Label(newWindow, background="black", fg="white",text="TIMER!", font=("Helvetica",48))
    my_label.place(x=80,y=100)
    mins=str(REST_TIME)
    submit(newWindow,my_label,"00",mins,"00")
    newWindow.protocol("WM_DELETE_WINDOW", on_closing)

def submit(newWindow,my_label,hour,minute,second):
    try:
        temp = int(hour)*3600 + int(minute)*60 + int(second)
    except:
        print("Please input the right value")
    while temp >-1:
        mins,secs = divmod(temp,60)
        hours=0
        if mins >60:
            hours, mins = divmod(mins, 60)
        my_label.config(text="{0:2d}".format(hours) + ":" + "{0:2d}".format(mins) + ":" + "{0:2d}".format(secs))
        newWindow.update()
        time.sleep(1)
        if (temp == 0):
            print("Time Countdown", "Time's up ")
        temp -= 1
    newWindow.destroy()
    
    
def setTimer():
    file1 = open('settings.txt', 'r')
    Lines = file1.readlines()    
    POMODORO_TIME=int(Lines[0].split("\n")[0])
    REST_TIME=int(Lines[1].split("\n")[0])
    file1.close()
    
    newWindow = tk.Tk()
    newWindow.geometry("400x200")
    newWindow.configure(background='black')
    newWindow.title("Settings")
    my_label = tk.Label(newWindow, background="black", fg="white",text="Pomodoro Time: ", font=("Helvetica",14))
    my_label.place(x=50,y=25)
    pomoTime = ttk.Entry(newWindow)
    pomoTime.insert(0, POMODORO_TIME)
    pomoTime.place(x=210,y=28)
    
    my_label = tk.Label(newWindow, background="black", fg="white",text="Rest Time: ", font=("Helvetica",14))
    my_label.place(x=50,y=75)
    restTime = ttk.Entry(newWindow)
    restTime.insert(0, REST_TIME)
    restTime.place(x=210,y=78)
    
    button2 = ttk.Button(newWindow, text="Set Pomodoro Settings!",width=25,command=lambda:setTimerValues(newWindow,pomoTime.get(), restTime.get()))
    button2.place(x=125,y=135)

def setTimerValues(newWindow, pomoTime, restTime):
    newWindow.destroy()
    a_file = open("settings.txt", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[0] = pomoTime+"\n"
    list_of_lines[1] = restTime+"\n"
    
    a_file = open("settings.txt", "w")
    a_file.writelines(list_of_lines)
    a_file.close()
    
    
def setSpotiPath():
    file1 = open('settings.txt', 'r')
    Lines = file1.readlines()
    SPOTIFY_FILE_PATH=Lines[2].split("\n")[0]
    PROGRAM=Lines[3].split("\n")[0]
    file1.close()
    newWindow = tk.Tk()
    newWindow.geometry("400x200")
    newWindow.configure(background='black')
    newWindow.title("Settings")
    my_label = tk.Label(newWindow, background="black", fg="white",text="Spotify Path: ", font=("Helvetica",14))
    my_label.place(x=40,y=25)
    spotiPath = ttk.Entry(newWindow)
    spotiPath.insert(0, SPOTIFY_FILE_PATH)
    spotiPath.place(x=210,y=28)
    
    my_label = tk.Label(newWindow, background="black", fg="white",text="Spotify executable: ", font=("Helvetica",14))
    my_label.place(x=40,y=75)
    executableName = ttk.Entry(newWindow)
    executableName.insert(0, PROGRAM)
    executableName.place(x=210,y=78)
    
    button2 = ttk.Button(newWindow, text="Set Spotify Path!",width=25,command=lambda:setSpotiValues(newWindow, spotiPath.get(),executableName.get()))
    button2.place(x=125,y=135)

def setSpotiValues(newWindow, pomoTime, restTime):
    newWindow.destroy()
    a_file = open("settings.txt", "r")
    list_of_lines = a_file.readlines()
    list_of_lines[2] = pomoTime+"\n"
    list_of_lines[3] = restTime+"\n"
    
    a_file = open("settings.txt", "w")
    a_file.writelines(list_of_lines)
    a_file.close()

def on_closing():
    pygame.quit()
    window.destroy()
    exit()
    os.system("taskkill /im "+"pomodoro.exe")
    os.system("taskkill /im "+"pomodoro.exe")
    
if __name__ == '__main__':  
    multiprocessing.freeze_support()
    window = tk.Tk()
    
    
    #dropmenu
    menubar = tk.Menu(window)
    window.config(menu=menubar)  # Lo asignamos a la base
    
    filemenu = tk.Menu(menubar)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Timer", command=setTimer)
    filemenu.add_command(label="Spotify Path", command=setSpotiPath)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)

    menubar.add_cascade(label="Archivo", menu=filemenu)
    
    style = ttk.Style()
    window.title("Pomodoro - Javier Aguirre")
    window.geometry("500x600")
    window.configure(background='black')
    print(style.theme_names())
    #style.theme_use("winnative")
    style.theme_use("clam")
    
    #style.theme_use("alt")
    #style.theme_use("default")
    #style.theme_use("classic")
    #style.theme_use("vista")
    #pomoPhoto=tk.PhotoImage(file="./pomodoro.png")
    
    
    
    #pomoPhoto = ImageTk.PhotoImage(file="C:/Users/Javi/Documents/giphy.gif")
    #ttk.Label(window, image=pomoPhoto) 
    button = ttk.Button(window, text="Start Pomodoro!",width=25,command=imReady)
    button.place(x="170",y="450")
    
    img=Image.open('pomodoro.png')
    img=ImageTk.PhotoImage(img)
    panel = ttk.Label(window, image = img, background="black")
    panel.place(x="-40",y="0")
    
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.mainloop()






