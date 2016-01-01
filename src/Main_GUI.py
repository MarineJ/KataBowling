#!/usr/bin/python

import Tkinter
from Tkinter import *
import FrameScoreWidget
from FrameScoreWidget import FrameInput
from ScoreCalculus import CalculScore
import os,sys,inspect


class GUI():
	def __init__(self, title):
	
		# style colors
		self.backColor="red"
		self.frontColor="white"
		self.fontSize=25
		self.fontType="Helvetica"


		self.root = Tkinter.Tk()
		#self.root.protocol("WM_DELETE_WINDOW", self.applicationExit)
		self.root.title(title)
		self.root.geometry("1111x750+300+300")
		self.root.configure(background=self.backColor)
		


		# create frames
		self.frameLine1 = Frame(self.root,bg=self.backColor)
		self.frameLine1.pack(padx=self.root.winfo_width()/2, side=TOP)
		self.frameLine2 = Frame(self.root,bg=self.backColor)
		self.frameLine2.pack(padx=self.root.winfo_width()/2, side=TOP)
		self.frameLine3 = Frame(self.root,bg=self.backColor)
		self.frameLine3.pack(padx=self.root.winfo_width()/2, side=TOP)
		self.frameLine3.visible = False
		
		# create title Label
		self.title1 = Label(self.frameLine1, text="American Ten-riin Bowling", bg=self.backColor, fg=self.frontColor,font=(self.fontType, self.fontSize))
		self.title1.pack(side=TOP,pady=30)


		# reset line button
		self.buttonCanvas = Canvas(self.frameLine3, width=100, height=100, borderwidth=0, highlightthickness=0, bg=self.backColor)
		self.buttonCanvas.create_oval(0, 0, 100, 100,fill=self.frontColor,width=0)
		self.buttonCanvas.pack(side=BOTTOM, pady=10)
		self.canvas_id = self.buttonCanvas.create_text(40, 40, fill=self.backColor)
		self.buttonCanvas.itemconfig(self.canvas_id, text="reset line")
		self.buttonCanvas.bind('<Button-1>', self.onResetButtonClick)  


		# create Score Label
		self.score = StringVar()
		self.score.set("Your score: -----")
		self.scoreLabel = Label(self.frameLine3, textvariable=self.score, bg=self.backColor,fg=self.frontColor,font=(self.fontType, self.fontSize))
		self.scoreLabel.pack(side=BOTTOM, pady=5)

		# image
		self.currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		self.parentdir = os.path.dirname(self.currentdir)
		self.imgName = self.parentdir+"/img/bowling2_"+self.frontColor+".png"
		self.imgCan = Canvas(self.root, width=int(614/2), height=int(460/2), bg=self.backColor)
		self.picture = PhotoImage(file=self.imgName)
		self.imgCan.create_image(152,115,image=self.picture)
		self.imgCan.pack(side=BOTTOM,pady=10)	


		# create frame 
		# create the 10 FrameScoreWidgets	
		i=1	
		self.frameWidgetList = []
		for r in range(2,4):
    			for c in range(5):
				if i<6:
        				self.frameWidgetList.append(FrameInput(self.frameLine1, i))
					self.frameWidgetList[i-1].pack(side=LEFT)
				else:
        				self.frameWidgetList.append(FrameInput(self.frameLine2, i))
					self.frameWidgetList[i-1].pack(side=LEFT)
				i = i+1
		for k in range(2):
			self.frameWidgetList.append(FrameInput(self.frameLine3, i))
			self.frameWidgetList[i-1].pack(side=LEFT)
			i= i+1
			

		self.scoreCalculator = CalculScore()


	def checkScore(self,a,b,c):
		updateScore=True
		for l in range(0,10):
			if self.frameWidgetList[l].testValidFrame(self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1)):
				if l>1 and int(self.frameWidgetList[l-1].get(0))==10 and int(self.frameWidgetList[l-2].get(0))==10:
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), True, True)
				elif l>1 and int(self.frameWidgetList[l-1].get(0))==10 and int(self.frameWidgetList[l-2].get(0))!=10:
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), True, False)
				elif l==1 and self.frameWidgetList[l-1].get(0)=="10":
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), True, False)	
				else:
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), False, False)
			else:
				updateScore = False
		if updateScore:
			self.score.set("Your score: "+ str(self.scoreCalculator.caluclateScore()))
		else:
			"non update score Label"
			self.score.set("Your score: ---")
	
	def trackChanges(self):
		for l in range(0,10):
			self.frameWidgetList[l].scoreEntry1.trace('w', self.frameWidgetList[l].store)
			self.frameWidgetList[l].scoreEntry2.trace('w', self.frameWidgetList[l].store)
			self.frameWidgetList[l].scoreEntry1.trace('w', self.checkScore)
			self.frameWidgetList[l].scoreEntry2.trace('w', self.checkScore)
		
		
	def onResetButtonClick(self, event):
    		for i in range(0,10):
			print "reset"
			self.frameWidgetList[i].reset()

	def applicationExit(self):
		self.root.destroy()
