import sys, getopt
import time
from botchart import BotChart
from botstrategy import BotStrategy
from botlog import BotLog
from botcandlestick import BotCandlestick

#Main container running the bot
def main(argv):
	#Trades using the btc to xmr currency
	chart = BotChart("poloniex","BTC_XMR",300,False)
	#Function from bot strategy, which is a class containeing various datas
	#such as opening price for the tick, closing price for the tick.
	strategy = BotStrategy()

	#Empty array holding the candlestick data
	candlesticks = []
	developingCandlestick = BotCandlestick()

	#Loop that continues indefinately
	while True:
		try:
			developingCandlestick.tick(chart.getCurrentPrice())
		except urllib2.URLError:
			time.sleep(int(30)) #Sleep function so that we dont overload the server with requests. Which
			#can result in the account or our ip getting banned.
			developingCandlestick.tick(chart.getCurrentPrice())

		#check if it is closing price, if it is the append to the array
		if (developingCandlestick.isClosed()):
			candlesticks.append(developingCandlestick)
			strategy.tick(developingCandlestick)
			developingCandlestick = BotCandlestick()
		
		time.sleep(int(30))

if __name__ == "__main__":
	main(sys.argv[1:])