from gtts import gTTS, lang

import os

from tkinter import *
root = Tk()

canvas = Canvas(root, width=400, height=500)
canvas.pack()


def texttospeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system("start output.mp3")


label = Label(text="TEXT TO SPEECH CONVERTER")
canvas.create_window(200, 100, window=label)

entry = Entry(root)
canvas.create_window(200, 180, window=entry)


button = Button(text="start", command=texttospeech)
canvas.create_window(200, 230, window=button)

root.mainloop()
