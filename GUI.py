from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
redled = LED(17)
greenled = LED(18)
whiteled = LED(27)

## GUI DEFINITIONS ##
win = Tk()
win.title("LED MASTER-REMOTE")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### EVENT FUNCTIONS ###
def redledToggle():
    if redled.is_lit:
        redled.off()
        redLedButton["text"] = "Turn LED On"
    else:
        redled.on()
        redLedButton["text"] = "Turn LED Off"
        
def greenledToggle():
    if greenled.is_lit:
        greenled.off()
        greenLedButton["text"] = "Turn LED On"
    else:
        greenled.on()
        greenLedButton["text"] = "Turn LED Off"
        
def whiteledToggle():
    if whiteled.is_lit:
        whiteled.off()
        whiteLedButton["text"] = "Turn LED On"
    else:
        whiteled.on()
        whiteLedButton["text"] = "Turn LED Off"
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
        

### WIDGETS ###
redLedButton = Button(win, text = 'Turn LED On', font = myFont, command = redledToggle, bg = 'bisque2', height = 1, width = 24)
redLedButton.grid(row=0, column=1)

greenLedButton = Button(win, text = 'Turn LED On', font = myFont, command = greenledToggle, bg = 'green', height = 1, width = 24)
greenLedButton.grid(row=1, column=1)

whiteLedButton = Button(win, text = 'Turn LED On', font = myFont, command = whiteledToggle, bg = 'gold', height = 1, width = 24)
whiteLedButton.grid(row=2, column=1)


exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 10)
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly