# Federal

This is a simple package built on top of pandas datareader to pull in Federal Reserve Data from the Federal Reserve in St. Louis (FRED)

## Basic Usage:

### 1. Setting Start & End Dates

```python

# Setting Dates
fred = FRED()
fred.start_date(1900,1,1)
fred.end_date(2018,1,1)
```
### 2. Pulling GDP (nGDP or rGDP)

```python

# Nominal GDP
df = fred.GDP(nominal=True)
df.head()

# real GDP - Default
df = fred.GDP()
df.head()

# Seasonally-Adjusted nGDP
df = fred.GDP(nominal=True, sa=True)
df.head()

# Seasonally-Adjusted rGDP
df = fred.GDP(sa=True)
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
