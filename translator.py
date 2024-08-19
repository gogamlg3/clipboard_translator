import easyocr
from PIL import ImageGrab
from time import sleep
import numpy
import win32clipboard
from googletrans import Translator
from tkinter import *    

translator = Translator()
reader = easyocr.Reader(['en'])

root=Tk()
root.title("overlay")
root.geometry(f'1920x150+0+0')
root.overrideredirect(True)
root.attributes("-transparentcolor", "white")
root.config(bg="white")
root.wm_attributes("-topmost", 1)

while True:
    image = ImageGrab.grabclipboard()

    if image != None:
        try:
            image = numpy.array(image)
            ocr = reader.readtext(image, detail=0)
            text = ' '.join(ocr)
            print(f"[original]: {text}")

            translation = translator.translate(text, src='en', dest='ru')
            print(f"[translate]: {translation.text}")

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.CloseClipboard()

            main_label=Label(root,text=translation.text,fg="red",font=(72),bg="#2C2C2C")
            main_label.pack()
            root.update()
            sleep(5)
            main_label.destroy()
            root.update()

        except Exception as e:
            print(e)

    sleep(1)
