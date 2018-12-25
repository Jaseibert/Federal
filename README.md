# Federal

This is a simple package built on top of pandas datareader to pull in Federal Reserve Data from the Federal Reserve in St. Louis (FRED)

Usage:

1. Instantiate an instance of GDP:
2. Use it to define the Start & End Dates
3. Declare the State ID that you are looking for.

Example:
1. FRED = FRED()
2. FRED.Start_Date(1900,1,1)
3. FRED.End_Date(2018,1,1)
4. FRED.StateGDP('IN')
5. df.head()
