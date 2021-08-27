import tkinter as tk
from tkinter import *
from tkinter import filedialog


# file paths for XMLS
GIAS_path, GIBO_path, GIMO_path, FIMO_path = [], [], [], []

# button commands
def GIAS_import():
	GIAS_path = filedialog.askopenfilename()
	
def GIBO_import():
    GIAS_path = filedialog.askopenfilename()

def GIMO_import():
    GIAS_path = filedialog.askopenfilename()

def FIMO_import():
    GIAS_path = filedialog.askopenfilename()


window = Tk()

window.title("ViR Reporting Tool")

window.geometry('800x400')

# Labels
GIAS_label = Label(window, text="Direct to 'Grow In As Surveyed' XML file:", justify='left')
GIAS_label.grid(column=0, row=0)

GIBO_label = Label(window, text="Direct to 'Grow In Blow Out' XML file:", justify='left')
GIBO_label.grid(column=0, row=2)

GIMO_label = Label(window, text="Direct to 'Grow In Max Op' XML file:", justify='left')
GIMO_label.grid(column=0, row=4)

FIMO_label = Label(window, text="Direct to 'Fall In Max Op' XML file:", justify='left')
FIMO_label.grid(column=0, row=6)

# Text
GIAS_text = Entry(window, width=20, state='disabled' )
GIAS_text.grid(column=4, row=0)

GIBO_text = Entry(window,width=20, state='disabled')
GIBO_text.grid(column=4, row=2)

GIMO_text = Entry(window,width=20, state='disabled')
GIMO_text.grid(column=4, row=4)

FIMO_text = Entry(window,width=20, state='disabled')
FIMO_text.grid(column=4, row=6)


# Buttons
GIAS_button = tk.Button(window, text='Browse', command=GIAS_import)
GIAS_button.grid(column=5, row=0)

GIBO_button = tk.Button(window, text='Browse', command=GIBO_import)
GIBO_button.grid(column=5, row=2)

GIMO_button = tk.Button(window, text='Browse', command=GIMO_import)
GIMO_button.grid(column=5, row=4)

FIMO_button = tk.Button(window, text='Browse', command=FIMO_import)
FIMO_button.grid(column=5, row=6)

window.mainloop()