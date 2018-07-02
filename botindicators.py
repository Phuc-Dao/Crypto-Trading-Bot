import numpy

class BotIndicators(object):
	def __init__(self):
		 pass

	def movingAverage(self, dataPoints, period):
		if (len(dataPoints) > 1):
			return sum(dataPoints[-period:]) / float(len(dataPoints[-period:]))
