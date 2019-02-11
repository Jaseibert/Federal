# Federal

This is a simple package built on top of pandas datareader to pull in Federal Reserve Data from the Federal Reserve in St. Louis (FRED). 

## Basic Usage:

```python

# Import the FRED Module
from Federal.Econ import FRED

#Instatiate a FRED Object
f = FRED()

#Set your Start & End Dates
f.start_date(1900,1,1)
f.end_date(2018,1,1)

# Make the Call
df = fred.metroGDP(name='Houston')
df.head()

```

## Setting Start & End Dates 

Once imported, you delare the start date and end date via the `FRED.start_date()` and `FRED.end_date()` functions. These functions define the range of dates for the data that you are for. Once declared these values will be applied to each query unless explicitly changed. 

There are several different datetime format variants that the `FRED.start_date()` and `FRED.end_date()` functions accept: 

1. DateTime format: (Year, Month, Day): **Integer**
```python
f = FRED()
f.start_date(1900,1,1)
f.end_date(2018,1,1)
```

2. DateTime format: (Day/Month/Year): **String**
```python
f = FRED()
f.start_date('1/1/1900')
f.end_date('1/1/2018')
```

3. DateTime format: (Day-Month-Year): **String**
```python
f = FRED()
f.start_date('1-1-1900')
f.end_date('1-1-2018')
```

4. DateTime format: (Day.Month.Year): **String**
```python
f = FRED()
f.start_date('1.1.1900')
f.end_date('1.1.2018')
```

5. DateTime format: (Month/Day/Year): **String**
```python
f = FRED()
f.start_date('14/1/1900')
f.end_date('16/1/2018')
```

### National Gross Domestic Product (GDP) 

After instantiating a FRED object, and defining the start and end dates using the `FRED.start_date()` and `FRED.end_date()` functions you can use the function `FRED.GDP()` depending on its parameters to return either nominal GDP or real GDP. 

```python

f = FRED()
f.start_date('1/1/1900')
f.end_date('1/1/2018')

# real GDP
df = f.GDP()
df.head()

# Nominal GDP
df = f.GDP(nominal=True)
df.head()
```

### State Gross Domestic Product (GSP)

Similar to the `FRED.GDP()` afer making the necessary calls you can pull in information around State-Level GDP using the `FRED.stateGDP()` function. It requires one arguement, which is the two-character string representing the state of interest. In the case below we pull the state GDP for Indiana. 

```python
f = FRED()
f.start_date('1/1/1900')
f.end_date('1/1/2018')

# State GDP
df = f.stateGDP('IN')
df.head()
```

### Metropolitan Gross Domestic Product (GMP)

The final variation of GDP that the FRED module pulls in is Metropolitan-Level GDP. The Federal Reserve uses Census Bureau Statistical Area (CBSA) Codes to define each metro within their API. Here using the `FRED.metroGDP()` function you can either pass the cbsa code or a name of a metro area as arguements within the funtion. Beyond this, similar to national GDP, by passing `FRED.metroGDP(name='<Any Metro Name>',nominal=True)` with nominal equal to True, the function will return the nominal metro GDP. 


```python

f = FRED()
f.start_date('1/1/1900')
f.end_date('1/1/2018')

# Metropolitian GDP - Declaring the City Name
df = f.metroGDP(name='Houston')
df.head()

# Metropolitian GDP - Declaring the CBSA code
df = f.metroGDP(cbsa=26420)
df.head()

# Metropolitian GDP - nominal
df = f.metroGDP(cbsa=26420, nominal=True)
df.head()

# Metropolitian GDP - nominal
df = f.metroGDP(name='Houston', nominal=True)
df.head()
```
