import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import re
from .CBSA import *
from .DateFormatter import *

class FRED(object):

    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end
        return

############################################################################################
#DateTime Formatting
############################################################################################

    def start_date(self, date=None, year=None, month=None, day=None, full=False):
        """ This function defines the start date for the query"""
        try:
            F = Formatter()
            if date is not None:
                #Logic For other Formats
                if F.date_formatter(date,'/') is not None:
                    self.start = F.date_formatter(date,'/')
                    return self.start
                elif F.date_formatter(date,'-') is not None:
                    self.start = F.date_formatter(date,'-')
                    return self.start
                elif F.date_formatter(date,'.') is not None:
                    self.start = F.date_formatter(date,'.')
                    return self.start
                else:
                    raise ValueError('Not a Valid Date. It must be (m/d/y), (d/m/y), or (y/m/d)..')
            elif full is not False:
                self.start = dt.datetime.strptime('1800-01-01','%Y-%m-%d')
                return self.start
            else:
                self.start = dt.datetime(year, month, day)
                return self.start
        except ValueError:
            print("Check the date that you submitted. It must be (m/d/y), (d/m/y), or (y/m/d)..")

    def end_date(self, date=None, year=None, month=None, day=None, full=False):
        """ This function defines the end date for the query

        date:
        """
        try:
            F = Formatter()
            if date is not None:
                #Logic For other Formats
                if F.date_formatter(date,'/') is not None:
                    self.end = F.date_formatter(date,'/')
                    return self.end
                elif F.date_formatter(date,'-') is not None:
                    self.end = F.date_formatter(date,'-')
                    return self.end
                elif F.date_formatter(date,'.') is not None:
                    self.end = F.date_formatter(date,'.')
                    return self.end
                else:
                    raise ValueError('Not a Valid Date. It must be (m/d/y), (d/m/y), or (y/m/d)..')
            elif full is not False:
                self.end = dt.datetime.now()
                return self.end
            else:
                self.end = dt.datetime(year, month, day)
                return self.end
        except ValueError:
            print("Check the date that you submitted. It must be (m/d/y), (d/m/y), or (y/m/d)..")

    def GDP(self,nominal=False):
        """ This function reads in Real or Nominal GDP in Billions of Dollars.

        nominal (Bool): Defines either Real GDP or Nominal GDP
        """
        code = 'GDP'
        try:
            if nominal is True:
                #2012-Chained Dollars
                df = web.DataReader(code+ 'C1', 'fred', self.start, self.end)
                df.rename(columns = {f'{code}C1':'nGDP_2012Chained_Billions$'}, inplace = True)
                return df
            else:
                df = web.DataReader(code, 'fred', self.start, self.end)
                df.rename(columns = {f'{code}':'rGDP_2012Chained_Billions$'}, inplace = True)
                return df
        except ValueError:
            print('The arguement nominal is a Boolean Value. Please pass True or False.')


############################################################################################
#State: GDP
############################################################################################

    def stateGDP(self, state):
        """ This function creates the correct query to call for a State's rGDP.

        State (String): The 2-Character State ID.
        """
        code = 'NGSP'
        try:
            df = web.DataReader(state + code, 'fred', self.start, self.end)
            df.rename(columns = {f'{state}{code}':f'{state}_GDP_Millions$'}, inplace = True)
            return df
        except ValueError:
             print("Invalid State Abbreviation. The state abbreviation should be a string of length 2")

############################################################################################
#Metropolitian: GDP
############################################################################################

    def metroGDP(self,name=None,cbsa=None,nominal=False):
            """ This function creates the correct query to call for a Metro areas nGDP
            in Million of Chained 2009 Dollars Not Seasonally Adjusted.

            name (String): The metro name that you are searching for.
            cbsa (int):    The CBSA code for a metro.
            nominal (Bool): nominal GDP or Real GDP
            """
            if nominal is True:
                code = 'NGMP'
            else:
                code = 'RGMP'

            if name is not None:
                hyphen = r"[-]"
                try:
                    for k,v in CBSA_Codes.items():
                        split_metro_list = re.split(hyphen, v)
                        for metro in split_metro_list:
                            match = re.search(str(name),metro)
                            if match is not None:
                                df = web.DataReader(code+str(k), 'fred', self.start, self.end)
                                df.rename(columns = {f'{code}{k}':f'{v}_GDP_Millions$'}, inplace = True)
                                return df
                            else:
                                pass
                except ValueError:
                    print('Not a valid census bureau statistical area (cbsa) name.')
            elif cbsa is not None:
                try:
                    for k,v in CBSA_Codes.items():
                        match = re.search(str(cbsa),str(k))
                        if match is not None:
                            df = web.DataReader(code+str(cbsa), 'fred', self.start, self.end)
                            df.rename(columns = {f'{code}{k}':f'{v}_GDP_Millions$'}, inplace = True)
                            return df
                except ValueError:
                    print('This doesnt look like a valid cbsa code, try again.')
            else:
                raise ValueError('Not a valid census bureau statistical area (cbsa) code or name.')

############################################################################################
#Federal: Unemployment Rate
############################################################################################

    def unemployment(self, sa=True):
        """ This function returns the civilian unemployment rate.

        sa: True if you want sesonally adjusted values, False if not. """

        code = 'UNRATE'
        try:
            if sa == True:
                df = web.DataReader(code, 'fred', self.start, self.end)
            else:
                df = web.DataReader(code + 'NSA', 'fred', self.start, self.end)
        except:
            pass
        return df
