# The Necessities
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web


# Extend the Range of Searchable Features
################################################################################
#GDP
################################################################################

class GDP:

	def __init__(self, adj=False):
		self.adj = adj
		return

	def Start_Date(self, Year, Month, Day):
		self.start = dt.datetime(Year, Month, Day)
		return self.start

	def End_Date(self, Year, Month, Day):
		self.end = dt.datetime(Year, Month, Day)
		return self.end

	def Seasonally_Adjusted(self, adj):
		#if self.adj == 'True':
		return
# Define a function to pull in d
	def GET(self, start, end):
		variable = Vars['GDP']
		df = web.DataReader(variable, 'fred', self.start, self.end)
		print(df.head(10))
		return

	def StateGDP(self, state):
		global df
		state = str(state)
		if len(state) == 0:
			return state
		elif len(state) == 2:
			df = web.DataReader(state + 'NGSP' , 'fred', self.start, self.end)
			return df
		else:
			state = state[:1]
			df = web.DataReader(state + 'NGSP' , 'fred', self.start, self.end)
			return df

GDP = GDP()
GDP.Start_Date(1900,1,1)
GDP.End_Date(2018,1,1)
GDP.StateGDP('IN')
df.head()
