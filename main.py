#!/usr/bin/env python3
from tkinter import *
import subprocess

# Settings
import settings

# Main App
class App:
	default_id = None

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		# mouse_name = 'pointer:MOSART Semi. 2.4G Keyboard Mouse' 
		# mouse_id = subprocess.check_output("xinput list --id-only 'pointer:MOSART Semi. 2.4G Keyboard Mouse'",shell=True).decode()
		# print(mouse_id)
		# Create List of Devices
		#names = subprocess.check_output(['xinput','list','--name-only'])
		#ids = subprocess.check_output(['xinput','list','--id-only'])

		# names_list = names.decode().splitlines()

		# devices_array = []


		# for name in names_list:
		# 	arr = {}
		# 	arr['name'] = name
		# 	arr['id'] = subprocess.check_output(['xinput','list','--id-only',name]).decode().replace('\n','')
		# 	devices_array.append(arr)
		
		# print(devices_array)
		# var = StringVar(master)
		# var.set('Select Device')
		# option = OptionMenu(frame, var, *devices_array,command=self.getit)
		# option.pack()

		# Greeting
		self.label_welcome = Label(frame,
			text='LabRat v0.0.2',
			justify=LEFT)
		self.label_welcome.pack(side='top', fill='both', expand=True)
		
		# Speed Slider
		self.label_speed = Label(frame,
			text='Set Mouse Speed',
			justify=LEFT)
		self.label_speed.pack(side='top', fill='both', expand=True)
		self.scale_speed = Scale(frame,width=10, from_=0, length=290, to=10,orient=HORIZONTAL,resolution=0.1)
		self.scale_speed.pack(padx=settings.padding,pady=settings.padding)

		# Apply Button
		self.apply = Button(frame, 
			text='OK',
			command=self.set_speed)
		self.apply.pack(side='left')

		self.close = Button(frame, 
			text='Quit',
			command=quit)
		self.close.pack(side='right')

	# def getit(self,florp):
	# 	global default_id
	# 	default_id = florp['id']
		

	def set_speed(self):
		t_id = subprocess.check_output("xinput list --id-only 'pointer:MOSART Semi. 2.4G Keyboard Mouse'",shell=True)
		mouse_id = t_id.decode().replace('\n','')
		n = str(self.scale_speed.get())
		# subprocess.call(['echo',n]);
		subprocess.call(['xinput','--set-prop',str(mouse_id),'Device Accel Constant Deceleration',str(n)])
	

root = Tk()
root.title('LabRat')
root.geometry('300x200')

app = App(root)

root.mainloop()