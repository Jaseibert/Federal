# Federal

This is a simple package built on top of pandas datareader to pull in Federal Reserve Data from the Federal Reserve in St. Louis (FRED)

Usage:

1. Instantiate an instance of GDP:
2. Use it to define the Start & End Dates
3. Declare the State ID that you are looking for.

Example:
FRED = FRED()
FRED.Start_Date(1900,1,1)
FRED.End_Date(2018,1,1)
FRED.StateGDP('IN')
df.head()
