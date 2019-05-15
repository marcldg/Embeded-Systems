from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

convert = {"a":".-", "b":"-...", "c":"-.-.", "d":"	-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}

## hardware
whiteled = LED(27)

## GUI DEFINITIONS ##
win = Tk()
morsecode = StringVar()
win.title("MORSE CODE GENERATOR")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTIONS ###
def encrypt():
    cipher = ' '
    for letter in morsecode.get().lower():
        if letter != ' ':
            cipher += convert[letter] + ' '
        else:
            cipher += ' '
    for letter in cipher:
        if letter == '.':
            dot()
        elif letter == '-':
            dash()

def dot():
	whiteled.on()
	time.sleep(0.5)
	whiteled.off()
	time.sleep(0.5)
	        
def dash():
	whiteled.on()
	time.sleep(2)
	whiteled.off()
	time.sleep(2)

		  
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        

### WIDGETS ###

Label = Label(win, text='Enter your personalised text', font = myFont)
Label.pack()

Entry = Entry(win, textvariable = morsecode)
Entry.pack()

Submit = Button(win, text='OK', command = encrypt, bg = 'blue')
Submit.pack()

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red')
exitButton.pack()

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly