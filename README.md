# Federal Package

This is a simple module built on top of Pandas-Datareader to make it easer to pull in Federal Reserve Data from the Federal Reserve in St. Louis (FRED).

## Installation

`pip install Federal`

## Basic Usage:

```python

# Import the GDP and DateFormatter Modules
from Federal.Econ import GDP
from Federal.Formatter import DateFormatter

#Insatiate the GDP and DateFormatter Objects
g = GDP()
d = DateFormatter()

#Set your Start & End Dates
d.start_date(1900,1,1)
d.end_date(2018,1,1)

# Make the Call
df = g.metro_gdp(name='Houston')
df.head()
```

## Setting Start & End Dates

Once imported, you declare the start date and end date via the `DateFormatter.start_date()` and `DateFormatter.end_date()` functions. These functions define the range of dates for the data that you are for. Once declared these values will be applied to each query unless explicitly changed.

There are several different DateTime format variants that the `DateFormatter.start_date()` and `DateFormatter.end_date()` functions accept:

1. DateTime format: (Year, Month, Day): **Integer**
```python
# Import the DateFormatter Modules
from Federal.Formatter import DateFormatter

#Insatiate the DateFormatter Object
d = DateFormatter()

d.start_date(1900,1,1)
d.end_date(2018,1,1)
```

2. DateTime format: (Day/Month/Year): **String**
```python
# Import the DateFormatter Modules
from Federal.Formatter import DateFormatter

#Insatiate the DateFormatter Object
d = DateFormatter()

d.start_date('1/1/1900')
d.end_date('1/1/2018')
```

3. DateTime format: (Day-Month-Year): **String**
```python
# Import the DateFormatter Modules
from Federal.Formatter import DateFormatter

#Insatiate the DateFormatter Object
d = DateFormatter()

d.start_date('1-1-1900')
d.end_date('1-1-2018')
```

4. DateTime format: (Day.Month.Year): **String**
```python
# Import the DateFormatter Modules
from Federal.Formatter import DateFormatter

#Insatiate the DateFormatter Object
d = DateFormatter()

d.start_date('1.1.1900')
d.end_date('1.1.2018')
```

5. DateTime format: (Month/Day/Year): **String**
```python
# Import the DateFormatter Modules
from Federal.Formatter import DateFormatter

#Insatiate the DateFormatter Object
d = DateFormatter()

d.start_date('14/1/1900')
d.end_date('16/1/2018')
```

### National Gross Domestic Product (GDP)

After instantiating a FRED object, and defining the start and end dates using the `GDP.start_date()` and `GDP.end_date()` functions you can use the function `GDP.national_gdp()` depending on its parameters to return either nominal GDP or real GDP.

```python
# Import the GDP and DateFormatter Modules
from Federal.Econ import GDP
from Federal.Formatter import DateFormatter

#Insatiate the GDP and DateFormatter Objects
g = GDP()
d = DateFormatter()

#Set Dates
d.start_date('1/1/1900')
d.end_date('1/1/2018')

# Real GDP
df = g.national_gdp()
df.head()

# Nominal GDP
df = g.national_gdp(nominal=True)
df.head()
```

### State Gross Domestic Product (GSP)

Similar to the `GDP.national_gdp()` after making the necessary calls you can pull in information around State-Level GDP using the `GDP.state_gdp()` function. It requires one argument, which is the two-character string representing the state of interest. In the case below we pull the state GDP for Indiana.

```python
# Import the GDP and DateFormatter Modules
from Federal.Econ import GDP
from Federal.Formatter import DateFormatter

#Insatiate the GDP and DateFormatter Objects
g = GDP()
d = DateFormatter()

#Set the Dates
d.start_date('1/1/1900')
d.end_date('1/1/2018')

# State GDP
df = g.state_gdp('IN')
df.head()
```

### Metropolitan Gross Domestic Product (GMP)

The final variation of GDP that the FRED module pulls in is Metropolitan-Level GDP. The Federal Reserve uses Core-Based Statistical Area (CBSA) Codes to define each metro within their API. Here using the `GDP.metro_gdp()` function you can either pass the CBSA code or a name of a metro area as arguments within the function. Beyond this, similar to national GDP, by passing `GDP.metro_gdp(name='<Any Metro Name>',nominal=True)` with nominal equal to True, the function will return the nominal metro GDP.


```python
# Import the GDP and DateFormatter Modules
from Federal.Econ import GDP
from Federal.Formatter import DateFormatter

#Insatiate the GDP and DateFormatter Objects
g = GDP()
d = DateFormatter()

#Set the Dates
d.start_date('1/1/1900')
d.end_date('1/1/2018')

# Metropolitan GDP - Passing the City Name as an argument
df = g.metro_gdp(name='Houston')
df.head()

# Metropolitan GDP - Passing the CBSA code as an argument
df = g.metro_gdp(cbsa=26420)
df.head()

# Metropolitan GDP - nominal
df = g.metro_gdp(cbsa=26420, nominal=True)
df.head()

# Metropolitan GDP - nominal
df = g.metro_gdp(name='Houston', nominal=True)
df.head()
```
### National Unemployment

Unemployment is defined by the `Unemployment.national_unemp()` function. This function takes an argument `sa` which returns either seasonally-adjusted non seasonally-adjusted unemployment.

```python
# Import the GDP and DateFormatter Modules
from Federal.Econ import Unemployment
from Federal.Formatter import DateFormatter

#Insatiate the GDP and DateFormatter Objects
u = Unemployment()
d = DateFormatter()

#Set the Dates
d.start_date('1/1/1900')
d.end_date('1/1/2018')

# Seasonally-Adjusted National Unemployment
df = u.national_unemp(sa=True)
df.head()

# Non Seasonally-Adjusted National Unemployment
df = u.national_unemp(sa=False)
df.head()
