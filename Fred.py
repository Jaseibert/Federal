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

class FRED:

	def __init__(self, adj=False):
		self.adj = adj
		return

	def Start_Date(self, Year, Month, Day):
		""" This function defines the start date for the query"""
		self.start = dt.datetime(Year, Month, Day)
		return self.start

	def End_Date(self, Year, Month, Day):
		""" This function defines the End Date for the query."""
		self.end = dt.datetime(Year, Month, Day)
		return self.end

	def Seasonally_Adjusted(self, adj):
		#if self.adj == 'True':
		return
# Define a function to pull in d
	def GET(self, start, end):
		""" This function is the wrapper on top of pandas datareader.
		start: Start Date
		end: End Date
		"""
		variable = Vars['GDP']
		df = web.DataReader(variable, 'fred', self.start, self.end)
		print(df.head(10))
		return

	def StateGDP(self, state):
		""" This function creates the correct query to call for a State's rGDP."""
		global df
		try:
			if len(state) == 0:
				return state
			elif len(state) == 2:
				df = web.DataReader(state + 'NGSP' , 'fred', self.start, self.end)
				return df
			else:
				assert len(state) == 2, "State should be a string of length 2"
		except:
			assert len(state) == 2, "State should be a string of length 2"
		return
