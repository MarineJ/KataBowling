import Tkinter
from Tkinter import *

# this class is used to create a 
class FrameInput(Tkinter.Frame):
	def __init__(self, master, frameNum):

		# style colors
		self.backColor="red"
		self.frontColor="white"
		self.fontSize=14
		self.fontType="Helvetica"

		Tkinter.Frame.__init__(self, master, width=master.winfo_width()*100/5,bg=self.backColor)
		# add label
		self.title = StringVar()
		self.title.set("Frame"+str(frameNum))
		self.frameTitle = Label(self,textvariable=self.title, bg=self.backColor, fg=self.frontColor,font=(self.fontType, self.fontSize))
		if frameNum>10:
			self.title.set("Bonus Frame")
		self.frameTitle.pack(side=TOP)
		self.scoreEntry1 = StringVar()
		self.scoreEntry2 = StringVar()
		self.scoreEntry1.set('X')
		self.scoreEntry2.set('X')
		# create the first entry box
		self.Entry1 = Entry(self, textvariable=self.scoreEntry1, bd =0, width=10,font=(self.fontType, self.fontSize))
		self.Entry1.pack(side = LEFT)
		# create the second entry box
		self.Entry2 = Entry(self, textvariable=self.scoreEntry2, bd =0, width=10,font=(self.fontType, self.fontSize))
		self.Entry2.pack(side = LEFT)
		# add an argument for frame number
		self.frameNumber = frameNum
		
	def testValidFrame(self, Val1, Val2):
		if Val1.isdigit() and Val2=="X":
			return True
		elif (Val1.isdigit() and Val2.isdigit() and (int(Val1)+int(Val2))<11):
			return True
		else:
			return False
		
	def blockEntry2ifStrikeEntry1(self):
			self.scoreEntry1.set("10")
			self.scoreEntry2.set("X")
	
	def redisplayEntry1IfEntry2Strike():
			self.scoreEntry1.set("10")
			self.scoreEntry2.set("X")
		
	def reset(self):
		self.scoreEntry1.set("X")
		self.scoreEntry2.set("X")			
			
	def store(self,a,b,c):
		val1 = self.Entry1.get()
		val2 = self.Entry2.get()
		if self.testValidFrame(val1, val2):
			self.scoreEntry1.set(val1)
			self.scoreEntry2.set(val2)
		elif val1 == "10":
			self.blockEntry2ifStrikeEntry1()
		elif val2 == "10":
			self.redisplayEntry1IfEntry2Strike()
		elif val1!="" and val2!="":
			self.reset()

	def get(self,val):
		tab = [self.scoreEntry1.get(), self.scoreEntry2.get()]
		if tab[0]==10.0 and val==1:
			return "0"
		if tab[0]=="X" and val==0:
			return "0"
		if tab[1]=="X" and val==1:
			return "0"
					
		return tab[val]



										
	
			
			
