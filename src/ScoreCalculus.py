import numpy

# this class is used for score calculation
class CalculScore():
	def __init__(self):
		self.frameScoreTab = numpy.zeros((10,4))
		self.LogicalStrikeSpare = numpy.zeros((10,4))

	def updateValues(self, i, val1, val2, isOnePrevStrike, are2PrevStrikes):
		if are2PrevStrikes:
			self.LogicalStrikeSpare[i-1,range(0,4)]=[1,0,2,1]
		elif isOnePrevStrike:
			self.LogicalStrikeSpare[i-1,range(0,4)]=[1,0,1,1]
		if int(val1)==10:
			self.LogicalStrikeSpare[i,range(0,4)]=[1,0,1,1]
		elif int(val1)+int(val2)==10:
			self.LogicalStrikeSpare[i,range(0,4)]=[1,1,1,0]
		else:
			self.LogicalStrikeSpare[i,range(0,4)]=[1,1,0,0]
		if i==0:		
			self.frameScoreTab[i,range(0,2)]=[val1,val2]
		else:
			self.frameScoreTab[i-1,range(2,4)]=[val1,val2]
			self.frameScoreTab[i,range(0,2)]=[val1,val2]
	
			
		
		
	def caluclateScore(self):
		score = self.frameScoreTab*self.LogicalStrikeSpare
		score = numpy.sum(score)
		print score
		return score

	


