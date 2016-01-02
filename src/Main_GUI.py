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
		self.backColor="#00d8b6"#"red"
		self.frontColor="white"
		self.fontSize=25
		self.fontType="Helvetica"

		# window and size
		self.root = Tkinter.Tk()
		self.root.title(title)
		self.root.geometry("1111x750+300+300")
		self.root.configure(background=self.backColor)
		

		# create frames for packing widgets
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


		# create reset line button
		self.buttonCanvas = Canvas(self.frameLine3, width=100, height=100, borderwidth=0, highlightthickness=0, bg=self.backColor,cursor="hand1")
		self.buttonCanvas.create_oval(0, 0, 100, 100,fill=self.frontColor,width=0)
		self.buttonCanvas.pack(side=BOTTOM, pady=10)
		self.canvas_id = self.buttonCanvas.create_text(50, 50, fill=self.backColor,font=(self.fontType, 14),justify='center')
		self.buttonCanvas.itemconfig(self.canvas_id,text="Reset Line")
		self.buttonCanvas.bind('<Button-1>', self.onResetButtonClick)  

		# create Score Label
		self.score = StringVar()
		self.score.set("Your score: -----")
		self.scoreLabel = Label(self.frameLine3, textvariable=self.score, bg=self.backColor,fg=self.frontColor,font=(self.fontType, self.fontSize))
		self.scoreLabel.pack(side=BOTTOM, pady=5)

		# create image
		self.currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
		self.parentdir = os.path.dirname(self.currentdir)
		self.imgName = self.parentdir+"/img/bowling2_"+self.frontColor+".png"
		self.imgCan = Canvas(self.root, width=int(614/2), height=int(460/2), bg=self.backColor)
		self.picture = PhotoImage(file=self.imgName)
		self.imgCan.create_image(152,115,image=self.picture)
		self.imgCan.pack(side=BOTTOM,pady=10)	

		# create the FrameScoreWidgets	
		i=1	
		self.frameWidgetList = []
		for r in range(2,4):
    			for c in range(5):
				if i<6:
        				self.frameWidgetList.append(FrameInput(self.frameLine1, i))
					self.frameWidgetList[i-1].pack(side=LEFT,padx=6)
				else:
        				self.frameWidgetList.append(FrameInput(self.frameLine2, i))
					self.frameWidgetList[i-1].pack(side=LEFT,padx=6)
				i = i+1
		for k in range(1):
			self.frameWidgetList.append(FrameInput(self.frameLine3, i))
			self.frameWidgetList[i-1].pack(side=LEFT,padx=6)
			i= i+1
			

		# create calculScore object
		self.scoreCalculator = CalculScore()


	# this function is called each time the text is modified in a frameWidget	
	def checkScore(self,a,b,c):
		if self.frameWidgetList[9].isSpare():
			self.frameWidgetList[10].blockBonusRoll2() # if the last frame is a spare, the bonus roll allow [a,-] with a in range (0,10)
		elif not(self.frameWidgetList[9].isStrike()):# if the last frame is a not a spare or a strike, the bonus roll is disabled [-,-]
			self.frameWidgetList[10].reset()

		# for all frames, store values and fill logical matrix of the object scoreCalculator
		for l in range(0,11):
			isBonus = False
			if l==10:
				isBonus=True
			if self.frameWidgetList[l].testValidFrame(self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1),isBonus):					
				if l>1:
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), self.frameWidgetList[l-1].isStrike(), (self.frameWidgetList[l-1].isStrike() + self.frameWidgetList[l-2].isStrike()))
				elif l==1:
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), self.frameWidgetList[l-1].isStrike(), False)
				else:
					self.scoreCalculator.updateValues(l,self.frameWidgetList[l].get(0), self.frameWidgetList[l].get(1), False, False)	
				
		self.score.set("Your score: "+ str(self.scoreCalculator.caluclateScore()))

	# track the changes of the textvariable in frameScoreWidgets	
	def trackChanges(self):
		for l in range(0,11):
			self.frameWidgetList[l].scoreEntry1.trace('w', self.checkScore)
			self.frameWidgetList[l].scoreEntry2.trace('w', self.checkScore)
		
		
	# binded function when click event is detected on the canva/button "reset line"	
	def onResetButtonClick(self, event):
    		for i in range(0,11):
			self.frameWidgetList[i].reset()
		self.score.set("Your score: -----")

	def applicationExit(self):
		self.root.destroy()
