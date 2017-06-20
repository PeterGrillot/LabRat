#!/bin/env/python

# Import Modules
from tkinter import *
import subprocess
import shlex

# Styles
import settings

root = Tk()

# Instructions
root.title('MouseTrap')
Label(text='Set Mouse Speed \nUses GTK Setting, 0 = Faster <-> 10 = Slower',justify=LEFT).pack(side=TOP,padx=settings.padding,pady=settings.padding)

scale = Scale(root, from_=0, to=5,orient=HORIZONTAL,resolution=0.1)
scale.pack(side=TOP,padx=settings.padding,pady=settings.padding)

# Get Mouse Settings from GUI
def setMouse():
		n = str(scale.get())
		#subprocess.call(["echo",n]);
		subprocess.call(['xinput','--set-prop','15','Device Accel Constant Deceleration',n])
Button(root, text='Ok', command=setMouse).pack(side=LEFT,padx=settings.padding,pady=settings.padding)
Button(root, text="Close",command=root.destroy).pack(side=RIGHT,padx=settings.padding,pady=settings.padding)

root.mainloop()