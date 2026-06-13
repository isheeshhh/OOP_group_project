import os
from tkinter import *

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(SCRIPT_DIR, "assets")

root = Tk()
root.title("EduLearn")
try:
    root.iconbitmap(os.path.join(ASSET_DIR, "puplogo.ico"))
except TclError:
    pass

root.geometry("900x600")
root.configure(bg="white")

root.mainloop()
