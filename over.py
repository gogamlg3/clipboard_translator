import easyocr
from PIL import ImageGrab
from time import sleep
import numpy
#import win32clipboard
from googletrans import Translator
from tkinter import *
import threading

translator = Translator()
reader = easyocr.Reader(['ru'])

def overlay(input_text):
    root=Tk()
    root.title("overlay")
    root.geometry(f'1920x150+0+0')
    root.overrideredirect(True)
    root.attributes("-transparentcolor", "white")
    root.config(bg="white")
    root.wm_attributes("-topmost", 1)
    main_label=Label(root,text=input_text,fg="red",font=(72),bg="#2C2C2C")
    main_label.pack()
    root.update()
    sleep(15)
    main_label.destroy()
    root.update()

prev_image = 0
while True:
    image = ImageGrab.grabclipboard()

    if image != None and image != prev_image:
        try:
            nimage = numpy.array(image)
            ocr = reader.readtext(nimage, detail=0)
            text = ' '.join(ocr)
            print(f"[original]: {text}")

            #translation = translator.translate(text, src='en', dest='ru')
            #print(f"[translate]: {translation.text}")

            prev_image = image
            #win32clipboard.OpenClipboard()
            #win32clipboard.EmptyClipboard()
            #win32clipboard.CloseClipboard()
            
            thread = threading.Thread(target=overlay, args=(translation.text,))
            thread.start()



        except Exception as e:
            print(e)

    sleep(1)
