import pandas as pd
import pandas_datareader.data as web
import re
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
