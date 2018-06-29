from botlog import BotLog

#bot that performs trade methods
class BotTrade(object):
	def __init__(self,currentPrice,stopLoss=0):
		self.output = BotLog()
		self.status = "OPEN"
		self.entryPrice = currentPrice
		self.exitPrice = ""
		self.output.log("Trade opened")
		if (stopLoss):
			self.stopLoss = currentPrice - stopLoss
	#shows closing price
	def close(self,currentPrice):
		self.status = "CLOSED"
		self.exitPrice = currentPrice
		self.output.log("Trade closed")
    #shows previous ticks
	def tick(self, currentPrice):
		if (self.stopLoss):
			if (currentPrice < self.stopLoss):
				self.close(currentPrice)
    #show trades
    def showTrade(self):
		tradeStatus = "Entry Price: "+str(self.entryPrice)+" Status: "+str(self.status)+" Exit Price: "+str(self.exitPrice)

		if (self.status == "CLOSED"):
			tradeStatus = tradeStatus + " Profit: "
			if (self.exitPrice > self.entryPrice):
				tradeStatus = tradeStatus + "\033[92m"
			else:
				tradeStatus = tradeStatus + "\033[91m"

			tradeStatus = tradeStatus+str(self.exitPrice - self.entryPrice)+"\033[0m"

		self.output.log(tradeStatus)