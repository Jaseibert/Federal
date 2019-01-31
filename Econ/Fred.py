import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import re
from .CBSA import *

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
        if date is not None:
            try:
                mat=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', date)
                if mat is not None:
                    match = dt.datetime(*(map(int, mat.groups()[-1::-1])))
                    self.start = dt.datetime.strptime(str(match),'%m %d %Y')
                else:
                    pass
            except ValueError:
                pass
            return self.start
        elif full is not False:
            self.start = dt.datetime.strptime('1800-01-01','%Y-%m-%d')
            return self.start
        else:
            self.start = dt.datetime(year, month, day)
            return self.start

    def end_date(self, date=None, year=None, month=None, day=None, full=False):
        """ This function defines the End Date for the query."""
        if date is not None:
            try:
                mat=re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', date)
                if mat is not None:
                    match = dt.datetime(*(map(int, mat.groups()[-1::-1])))
                    self.end = dt.datetime.strptime(str(match),'%m %d %Y')
                else:
                    pass
            except ValueError:
                pass
            return self.end
        elif full is not False:
            self.end = dt.datetime.now()
            return self.end
        else:
            self.end = dt.datetime(year, month, day)
            return self.end

############################################################################################
#Federal: GDP
############################################################################################

    def GDP(self,nominal=False):
        """ This function reads in Real or Nominal GDP in Billions of Dollars.

        nominal (Boolean):
        """
        code = 'GDP'
        try:
            if nominal == True:
                #2012-Chained Dollars
                df = web.DataReader(code, 'fred', self.start, self.end)
            else:
                df = web.DataReader(code + 'C1', 'fred', self.start, self.end)
        except ValueError:
            pass
        return df

############################################################################################
#State: GDP
############################################################################################

    def stateGDP(self, state):
        """ This function creates the correct query to call for a State's rGDP.

        State (String): The 2-Character State ID.
        """
        code = 'NGSP'
        try:
            if len(state) == 0:
                return state
            elif len(state) == 2:
                df = web.DataReader(state + code, 'fred', self.start, self.end)
                return df
            else:
                assert len(state) == 2, "State should be a string of length 2"
        except :
            assert len(state) == 2, "State should be a string of length 2"
        return df

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
            if nominal == True:
                code = 'NGMP'
            else:
                code = 'RGMP'
            if cbsa is None:
                hyphen = r"[-]"
                for k,v in CBSA_Codes.items():
                    split = re.split(hyphen, v)
                    for word in split:
                        match= re.search(str(name),v)
                        if match != None:
                            key = k
                        else:
                            pass
                df = web.DataReader(code+str(key), 'fred', self.start, self.end)
            elif cbsa is not None:
                df = web.DataReader(code+str(cbsa), 'fred', self.start, self.end)
            else:
                pass
            return df

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
