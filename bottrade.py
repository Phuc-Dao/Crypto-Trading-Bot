rom botlog import BotLog

class BotTrade(object):
	def __init__(self,currentPrice,stopLoss=0):
		self.output = BotLog()
		self.status = "OPEN"
		self.entryPrice = currentPrice
		self.exitPrice = ""
		self.output.log("Trade opened")
		if (stopLoss):
			self.stopLoss = currentPrice - stopLoss
	
	def close(self,currentPrice):
		self.status = "CLOSED"
		self.exitPrice = currentPrice
		self.output.log("Trade closed")

	def tick(self, currentPrice):
		if (self.stopLoss):
			if (currentPrice < self.stopLoss):
				self.close(currentPrice)