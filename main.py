#!/usr/bin/env python3
from tkinter import *
import subprocess

# Settings
import settings

class device(object):
	id = 0

	# The class "constructor" - It's actually an initializer 
	def __init__(self, id):
			self.id = id

def make_device(id):
		device_id = device(id)
		return device_id

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		devices = subprocess.check_output('xinput | awk -F= "/.*pointer/ {print \$2}" | cut -f1', shell=True).decode('ascii')
		# xinput | awk -F= "/$pointer1.*pointer/ {print \$2}" | cut -f1
		# xinput | awk -F= "/$pointer1.*pointer/ {print \$1}" | cut -f1
		# devices = ['mouse', 'mouse3']
		# for device in devices:
		print(devices.split('\n'))
		# devices = subprocess.check_output(xinput --list)
		# for device in devicesz:
		# 	t = make_device(device)
		
		# print(t.id)
		var = StringVar(master)
		var.set("Select Device")
		option = OptionMenu(frame, var, devices)
		option.pack()

		# Greeting
		self.label_welcome = Label(frame,
			text='LabRat v0.0.2',
			justify=LEFT)
		self.label_welcome.pack(side="top", fill="both", expand=True)
		
		# Speed Slider
		self.label_speed = Label(frame,
			text='Set Mouse Speed',
			justify=LEFT)
		self.label_speed.pack(side="top", fill="both", expand=True)
		self.scale_speed = Scale(frame,width=10, from_=0, to=10,orient=HORIZONTAL,resolution=0.1)
		self.scale_speed.pack(padx=settings.padding,pady=settings.padding)

		# Apply Button
		self.apply = Button(frame, 
			text="OK",
			command=self.set_speed)
		self.apply.pack(side="left")

		self.close = Button(frame, 
			text="Quit",
			command=quit)
		self.close.pack(side="right")



	def set_speed(self):
		n = str(self.scale_speed.get())
		subprocess.call(["echo",n]);
		subprocess.call(['xinput','--set-prop','15','Device Accel Constant Deceleration',n])
	

root = Tk()
root.title('LabRat')
root.geometry("300x200")

app = App(root)

root.mainloop()