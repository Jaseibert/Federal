import pandas as pd
import pandas_datareader.data as web
import re
import Federal.Formatter.CBSAFormatter as c
import Federal.Formatter.DateFormatter as d

class GDP(object):

    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end
        return

############################################################################################
#Federal: GDP
############################################################################################
    def federal_gdp(self,nominal=False):
        """ This function reads in Real or Nominal GDP in Billions of Dollars.

        nominal (Bool): Defines either Real GDP or Nominal GDP
        """

        code = 'GDP'
        try:
            if nominal is True:
                df = web.DataReader(code+ 'C1', 'fred', self.start, self.end)
                df.rename(columns = {f'{code}C1':'nGDP_2012Chained_Billions$'},inplace=True)
                return df
            else:
                df = web.DataReader(code, 'fred', self.start, self.end)
                df.rename(columns = {f'{code}':'rGDP_2012Chained_Billions$'},inplace=True)
                return df
        except ValueError:
            print('The arguement nominal is a Boolean Value. Please pass True or False.')

############################################################################################
#State: GDP
############################################################################################

    def state_gdp(self, state):
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


    def get_metro_name(self,metro_name):
        for k,v in c.CBSA_Codes.items():
            split_metro_list = re.split(r'[-]', v)
            for metro in split_metro_list:
                match = re.search(str(metro_name),metro)
                if match is not None:
                    return k,v
                else:
                    pass

    def get_metro_cbsa_num(self,cbsa_code):
        for k,v in c.CBSA_Codes.items():
            match = re.search(str(cbsa_code),str(k))
            if match is not None:
                return k,v
            else:
                pass

############################################################################################
#Metropolitian: GDP
############################################################################################

    def metro_gdp(self,name=None,cbsa=None,nominal=False):
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
                try:
                    k,v = self.get_metro_name(metro_name=name)
                    df = web.DataReader(code+str(k), 'fred', self.start, self.end)
                    df.rename(columns = {f'{code}{k}':f'{v}_{code}_Millions$'},inplace=True)
                    return df
                except ValueError:
                    print('Not a valid Core-Based Statistical Area (CBSA) city name.')
            elif cbsa is not None:
                try:
                    k,v = self.get_metro_cbsa_num(cbsa_code=cbsa)
                    df = web.DataReader(code+str(k), 'fred', self.start, self.end)
                    df.rename(columns = {f'{code}{k}':f'{v}_{code}_Millions$'},inplace=True)
                    return df
                except ValueError:
                    print('This doesnt look like a valid Core-Based Statistical Area (CBSA), try again.')
            else:
                raise ValueError('Not a valid Core-Based Statistical Area (CBSA) code or name.')
