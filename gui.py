import tkinter as tk
from tkinter import *
from tkinter import filedialog
import ntpath

# file paths for XMLS
GIAS_path, GIBO_path, GIMO_path, FIMO_path = [], [], [], []


# button commands
def GIAS_import():
    global GIAS_path
    GIAS_path = filedialog.askopenfilename()
    if ".xml" in GIAS_path:
        feedback_text_1.configure(text = ntpath.basename(GIAS_path), bg = "OliveDrab4")
    else:
        feedback_text_1.configure(text = "File is not an XML", bg = "red4")

def GIBO_import():
    global GIBO_path
    GIBO_path = filedialog.askopenfilename()
    if ".xml" in GIBO_path:
        feedback_text_2.configure(text = ntpath.basename(GIBO_path), bg = "OliveDrab4")
    else:
        feedback_text_2.configure(text = "File is not an XML", bg = "red4")

def GIMO_import():
    global GIMO_path
    GIMO_path = filedialog.askopenfilename()
    if ".xml" in GIMO_path:
        feedback_text_3.configure(text = ntpath.basename(GIMO_path), bg = "OliveDrab4")
    else:
        feedback_text_3.configure(text = "File is not an XML", bg = "red4")

def FIMO_import():
    global FIMO_path
    FIMO_path = filedialog.askopenfilename()
    if ".xml" in FIMO_path:
        feedback_text_4.configure(text = ntpath.basename(FIMO_path), bg = "OliveDrab4")
    else:
        feedback_text_4.configure(text = "File is not an XML", bg = "red4")


window = Tk()

window.title("ViR Reporting Tool")

window.geometry('450x250')

window.configure(bg = "grey25")



# Labels
GIAS_label = Label(window, text="Direct to 'Grow In As Surveyed' XML file:", fg = "ivory2")
GIAS_label.grid(column=0, row=0, pady=5)
GIAS_label.configure(bg = "grey25")

GIBO_label = Label(window, text="Direct to 'Grow In Blow Out' XML file:", fg = "ivory2")
GIBO_label.grid(column=0, row=2, pady=5)
GIBO_label.configure(bg = "grey25")

GIMO_label = Label(window, text="Direct to 'Grow In Max Op' XML file:", fg = "ivory2")
GIMO_label.grid(column=0, row=4, pady=5)
GIMO_label.configure(bg = "grey25")

FIMO_label = Label(window, text="Direct to 'Fall In Max Op' XML file:", fg = "ivory2")
FIMO_label.grid(column=0, row=6, pady=5)
FIMO_label.configure(bg = "grey25")

# Buttons
GIAS_button = tk.Button(window, text='Browse', command=GIAS_import, bg = "ivory4")
GIAS_button.grid(column=3, row=0, pady=5)

GIBO_button = tk.Button(window, text='Browse', command=GIBO_import, bg = "ivory4")
GIBO_button.grid(column=3, row=2, pady=5)

GIMO_button = tk.Button(window, text='Browse', command=GIMO_import, bg = "ivory4")
GIMO_button.grid(column=3, row=4, pady=5)

FIMO_button = tk.Button(window, text='Browse', command=FIMO_import, bg = "ivory4")
FIMO_button.grid(column=3, row=6, pady=5)

process_button = tk.Button(window, text='Process', height = 2, width = 10, bg = "ivory4")
process_button.grid(row=7, column=1, rowspan=2, sticky=S, pady=20)


# feedback labels

feedback_text_1 = Label(window, width = 20, bg = "white")
feedback_text_1.grid(column = 1, row = 0, padx=(10, 10))
feedback_text_1.configure(bg = "azure4")

feedback_text_2 = Label(window, width = 20, bg = "white")
feedback_text_2.grid(column = 1, row = 2, padx=(10, 10))
feedback_text_2.configure(bg = "azure4")

feedback_text_3 = Label(window, width = 20, bg = "white")
feedback_text_3.grid(column = 1, row = 4, padx=(10, 10))
feedback_text_3.configure(bg = "azure4")

feedback_text_4 = Label(window, width = 20, bg = "white")
feedback_text_4.grid(column = 1, row = 6, padx=(10, 10))
feedback_text_4.configure(bg = "azure4")

window.mainloop()


