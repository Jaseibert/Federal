import pandas as pd
import pandas_datareader.data as web
from Federal.Formatter.CBSAFormatter import *
from Federal.Formatter.DateFormatter import *

class Unemployment(object):

    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end
        return

############################################################################################
#Federal: Unemployment Rate
############################################################################################

    def national_unemp(self, sa=True):
        """ This function returns the civilian unemployment rate.

        sa: True if you want sesonally adjusted values, False if not. """

        code = 'UNRATE'
        if sa is True:
            df = web.DataReader(code, 'fred', self.start, self.end)
        else:
            df = web.DataReader(code + 'NSA', 'fred', self.start, self.end)
        return df

############################################################################################
#State: Unemployment Rate
############################################################################################

    def state_unemp(self, state):
        """ This function returns the civilian unemployment rate.

        State (String): The 2-Character State ID.
        """

        code = 'UR'
        try:
            df = web.DataReader(state + code, 'fred', self.start, self.end)
            df.rename(columns = {f'{state}{code}':f'{state}_UnempRate'}, inplace = True)
            return df
        except ValueError:
             print("Invalid State Abbreviation. The state abbreviation should be a string of length 2")
        return df

############################################################################################
#State: Unemployment Rate
############################################################################################

    def state_unemp(self, state):
        """ This function returns the civilian unemployment rate.

        State (String): The 2-Character State ID.
        """

        code = 'UR'
        try:
            df = web.DataReader(state + code, 'fred', self.start, self.end)
            df.rename(columns = {f'{state}{code}':f'{state}_UnempRate'}, inplace = True)
            return df
        except ValueError:
             print("Invalid State Abbreviation. The state abbreviation should be a string of length 2")
        return df
