import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as web
import re
from Federal.CBSA import *

class Fred:

    def __init__(self):
        return

############################################################################################
#Dates
############################################################################################

    def start_date(self, year, month, day):
        """ This function defines the start date for the query"""
        self.start = dt.datetime(year, month, day)
        return self.start

    def end_date(self, year, month, day):
        """ This function defines the End Date for the query."""
        self.end = dt.datetime(year, month, day)
        return self.end

############################################################################################
#Federal: GDP
############################################################################################

    def GDP(self, nominal=False,sa=True):
        """ This function reads in Real or Nominal GDP in Billions of Dollars.

        nominal (Boolean):
        sa (Boolean):
        """
        code = 'GDP'
        try:
            if nominal == True:
                #2012-Chained Dollars
                df = web.DataReader(code, 'fred', self.start, self.end)
            else:
                df = web.DataReader(code + 'C1', 'fred', self.start, self.end)
        except:
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
        except:
            assert len(state) == 2, "State should be a string of length 2"
        return df

############################################################################################
#Metropolitian: GDP
############################################################################################

    def cbsa_decoder(name):
        """This function takes a string and searches for a match dictionary of CBSA codes

        name (String): The metro name that you are searching for.
        """
        hyphen = r"[-]"
        for k,v in CBSA_Codes.items():
            split = re.split(hyphen, v)
            for word in split:
                match = re.search(str(name),v)
                if match == None:
                    pass
                else:
                     return k

    def metroGDP(name,cbsa=None,nominal=False):
            """ This function creates the correct query to call for a Metro areas nGDP
            in Millions of Chained 2009 Dollars Not Seasonally Adjusted.

            name (String): The metro name that you are searching for.
            cbsa (int):    The CBSA code for a metro.
            nominal (Bool): nominal GDP or Real GDP
            """
            if nominal == True:
                code = 'NGMP'
            else:
                code = 'RGMP'

            if cbsa is None:
                k = cbsa_decoder(name)
                df = web.DataReader(code+str(k), 'fred', self.start, self.end)
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
