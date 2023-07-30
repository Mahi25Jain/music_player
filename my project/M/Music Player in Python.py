import tkinter as tk  
import fnmatch
import os
from pygame import mixer


canvas = tk.Tk()
canvas.title("My music player")
canvas.geometry("500x600")
canvas.config(bg ="blue")

rootpath = "F:\\my music player"
pattern ="*.mp3" 

mixer.init()

prev_img = tk.PhotoImage(file ="prev_img.png")
stop_img = tk.PhotoImage(file ="stop_img.png")
play_img = tk.PhotoImage(file ="play_img.png")
pause_img = tk.PhotoImage(file ="pause_img.png")
next_img = tk.PhotoImage(file ="next_img.png")

def select():
    label.config(text = listbox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listbox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listbox.select_clear('active') 


def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0]+1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)
    
def play_prev():
    next_song = listbox.curselection()
    next_song = next_song[0]-1
    next_song_name = listbox.get(next_song)
    label.config(text = next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)    
    
def pause_song():
    if pauseButton["text"] == "pause":
       mixer.music.pause()
       pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"
        
        
listbox = tk.Listbox(canvas, fg = "cyan", background="black" ,width = 200, font=15)
listbox.pack( padx = 15 , pady = 15)

label = tk.Label (canvas, text ='', background= 'blue', fg = 'yellow', font=('ds-digital',18))
label.pack(pady = 15)

top = tk.Frame(canvas ,bg= "black")
top.pack(padx =15 ,  pady = 10, anchor = 'center')

prevButton = tk.Button(canvas, text="prev" ,image=prev_img, bg = 'black',borderwidth=0 , command= play_prev)
prevButton.pack(pady = 15, in_=top, side ='left')

playButton = tk.Button(canvas, text="play",image=play_img, bg = 'black',borderwidth=0 , command=select)
playButton.pack(pady = 15, in_=top, side ='left')

pauseButton = tk.Button(canvas, text="play",image=pause_img, bg = 'black',borderwidth=0 , command=pause_song)
pauseButton.pack(pady = 15, in_=top, side ='left')

stopButton = tk.Button(canvas, text="stop",image=stop_img, bg = 'black',borderwidth=0 , command = stop)
stopButton.pack(pady = 15, in_=top, side ='left')

nextButton = tk.Button(canvas, text="next",image=next_img, bg = 'black',borderwidth=0 , command=play_next)
nextButton.pack(pady = 15, in_=top, side ='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert('end', filename)
        
canvas.mainloop()