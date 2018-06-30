from botlog import BotLog
from botindicators import BotIndicators
from bottrade import BotTrade

class BotStrategy(object):
	def __init__(self):
		self.output = BotLog()
		self.prices = []
		self.closes = [] # Needed for Momentum Indicator
		self.trades = []
		self.currentPrice = ""
		self.currentClose = ""
		self.numSimulTrades = 1
		self.indicators = BotIndicators()

        