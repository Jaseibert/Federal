# Federal

This is a simple package built on top of pandas datareader to pull in Federal Reserve Data from the Federal Reserve in St. Louis (FRED). 

[Setting Start & End Dates](#setting-start-&-end-dates)

## Basic Usage:

We import the module FRED, which is used to interact with the Federal Reserve API, as follows:

```python

# Import the FRED Module
from Federal.Econ import FRED

#Instatiate a FRED Object
f = Econ.FRED()

#Set your Start & End Dates
f.start_date(1900,1,1)
f.end_date(2018,1,1)

# Make the Call
df = fred.metroGDP(name='Houston')
df.head()

```

## Setting Start & End Dates 

Once imported, you delare the start date and end date via the `FRED.start_date()` and `FRED.end_date()` functions. These functions define the range of dates for the data that you are for. Once declared these values will be applied to each query unless explicitly changed. 

There are several different datetime format variants that the `FRED.start_date()` and `FRED.end_date()` functions accept. 

1. DateTime format: (Year, Month, Day) *Integers*
```python
f = Econ.FRED()
f.start_date(1900,1,1)
f.end_date(2018,1,1)
```

2. DateTime format: (Day/Month/Year) *String*
```python
f = Econ.FRED()
f.start_date('1/1/1900')
f.end_date('1/1/2018')
```

3. DateTime format: (Day-Month-Year) *String*
```python
f = Econ.FRED()
f.start_date('1-1-1900')
f.end_date('1-1-2018')
```

4. DateTime format: (Day.Month.Year) *String*
```python
f = Econ.FRED()
f.start_date('1.1.1900')
f.end_date('1.1.2018')
```

5. DateTime format: (Month/Day/Year) *String*
```python
f = Econ.FRED()
f.start_date('14/1/1900')
f.end_date('16/1/2018')
```


### 2. Pulling National GDP (nomimalGDP or realGDP)



```python

# Nominal GDP
df = f.GDP(nominal=True)
df.head()

# real GDP - Default
df = f.GDP()
df.head()

# Seasonally-Adjusted nGDP
df = f.GDP(nominal=True, sa=True)
df.head()

# Seasonally-Adjusted rGDP
df = f.GDP(sa=True)
df.head()
```

### 3. Pulling State GDP (GSP)

```python

# State GDP
df = fred.stateGDP('IN')
df.head()
```

### 3. Pulling State GDP (GSP)

```python

# Metropolitian GDP - Declaring the City Name
df = fred.metroGDP(name='Houston')
df.head()

# Metropolitian GDP - Declaring the CBSA code
df = fred.metroGDP(cbsa=26420)
df.head()

# Metropolitian GDP - nominal
df = fred.metroGDP(cbsa=26420, nominal=True)
df.head()
```
