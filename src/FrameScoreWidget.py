import Tkinter
from Tkinter import *

# this class is used to create a customed double entry widget for frames and to controll the possibles score are input by the user
class FrameInput(Tkinter.Frame):
	def __init__(self, master, frameNum):

		# style colors
		self.backColor="#00d8b6"#"red"
		self.frontColor="white"
		self.fontSize=14
		self.fontType="Helvetica"

		Tkinter.Frame.__init__(self, master, width=master.winfo_width()*100/5,bg=self.backColor)
		# add label
		self.title = StringVar()
		self.title.set("Frame"+str(frameNum))
		self.frameTitle = Label(self,textvariable=self.title, bg=self.backColor, fg=self.frontColor,font=(self.fontType, self.fontSize))
		if frameNum>10:
			self.title.set("Bonus Rolls")
		self.frameTitle.pack(side=TOP)
		self.scoreEntry1 = StringVar()
		self.scoreEntry2 = StringVar()
		self.scoreEntry1.set("-")
		self.scoreEntry2.set("-")
		# create the first entry box
		self.Entry1 = Entry(self, textvariable=self.scoreEntry1, bd =0, width=7,font=(self.fontType, self.fontSize),justify='center')
		self.Entry1.pack(side = LEFT,padx=4)
		# create the second entry box
		self.Entry2 = Entry(self, textvariable=self.scoreEntry2, bd =0, width=7,font=(self.fontType, self.fontSize),justify='center')
		self.Entry2.pack(side = LEFT,padx=4)
		# add an argument for frame number
		self.frameNumber = frameNum
		
	def testValidFrame(self, Val1, Val2, isBonus):
		if not(isBonus) and Val1.isdigit() and Val2.isdigit() and (int(Val1)+int(Val2))>10:
			self.reset()
			return False
		if isBonus and Val1.isdigit() and Val2.isdigit() and (int(Val1)+int(Val2))>20:
			self.reset()
			return False
		elif (not(Val1.isdigit()) and Val1!="-") or (not(Val2.isdigit()) and Val2!="-"):
			self.reset()
			return False
		elif (Val1.isdigit() and int(Val1)>10) or (Val2.isdigit() and int(Val2)>10): 
			self.reset()
			return False 
		else:
			return True


	def blockBonusRoll2(self):
		self.scoreEntry2.set("-")
		
	def reset(self):
		self.scoreEntry1.set("-")
		self.scoreEntry2.set("-")

	def isStrike(self):
		if self.scoreEntry1.get()=="10":
			return True
		else:
			return False

	def isSpare(self):
		if self.scoreEntry1.get().isdigit() and  self.scoreEntry2.get().isdigit() and int(self.scoreEntry1.get())+int(self.scoreEntry2.get())==10:
			return True
		elif  self.scoreEntry2.get()=="10":
			return True
		else:
			return False

	def get(self,val):
		tab = [self.scoreEntry1.get(), self.scoreEntry2.get()]
		if tab[0]==10.0 and val==1:
			return "0"
		if tab[0]=="-" and val==0:
			return "0"
		if tab[1]=="-" and val==1:
			return "0"
		if tab[val]=='':
			return "0"					
		return tab[val]



										
	
			
			
