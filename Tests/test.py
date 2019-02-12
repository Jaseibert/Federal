from Econ.GDP import *
from Formatter.CBSAFormatter import *
from Formatter.DateFormatter import *
import datetime as dt
import unittest
import pandas_datareader.data as web

class setup_tests(object):

    def __init__(self):
        return

    def setup_test_dates(self,date=False,date1=False,date2=False,date3=False,year=False,month=False,day=False,full=False):
        '''Sets up a consistent enviornment for testing the start and end date functions.'''
        d = DateFormatter()
        if date is True:
            #Test for the deliminator "/"
            start = d.start_date(date='1/1/1900')
            end = d.end_date(date='1/1/2010')
            return start,end
        elif date1 is True:
            #Test for the deliminator "-"
            start = d.start_date(date='1-1-1900')
            end = d.end_date(date='1-1-2010')
            return start,end
        elif date2 is True:
            #Test for the deliminator "."
            start = d.start_date(date='1.1.1900')
            end = d.end_date(date='1.1.2010')
            return start,end
        elif date3 is True:
            #Test for the Non-North American formatting of DateTimes
            start = d.start_date(date='20.1.1900')
            end = d.end_date(date='20.1.2010')
            return start,end
        elif full is True:
            #Test for the full arguement
            start = d.start_date(full=True)
            end = d.end_date(full=True)
            return start,end
        else:
            #Test for the YMD arguement
            start = d.start_date(year=1900,month=1,day=1)
            end = d.end_date(year=1900,month=1,day=1)
            return start,end

    def setup_test_gdp(self,nominal=True):
        '''Sets up a consistent enviornment for testing the GDP function.'''

        d = DateFormatter()
        g = GDP()
        d.start_date(date='1/1/1900')
        d.end_date(date='1/1/2018')
        if nominal is True:
            df = g.GDP(nominal=True)
            return df
        else:
            df = g.GDP(nominal=False)
            return df

    def setup_test_state_gdp(self):
        '''Sets up a consistent enviornment for testing the stateGDP function.'''

        d = DateFormatter()
        g = GDP()
        d.start_date(date='1/1/1900')
        d.end_date(date='1/1/2018')
        df = g.stateGDP('TX')
        return df

    def setup_test_metro_gdp(self,name=False,cbsa=False,nominal=False):
        '''Sets up a consistent enviornment for testing the MetroGDP function.'''

        d = DateFormatter()
        g = GDP()
        d.start_date(date='1/1/1900')
        d.end_date(date='1/1/2018')
        if name is not False and nominal is False:
            df = g.metroGDP(name='Houston')
            return df
        elif cbsa is not False and nominal is False:
            df = g.metroGDP(cbsa=26420)
            return df
        elif cbsa is not False and nominal is not False:
            df = g.metroGDP(cbsa=26420,nominal=True)
            return df
        elif name is not False and nominal is not False:
            df = g.metroGDP(name='Houston', nominal=True)
            return df
        else:
            pass

class TestFRED(unittest.TestCase):

    def test_dates_date_0(self):
        '''Tests the that the dates can handle '\' as the deliminator.'''
        s = setup_tests()
        start,end = s.setup_test_dates(date=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(2010,1,1))

    def test_dates_date_1(self):
        ''''Tests the that the dates can handle '-' as the deliminator.'''
        s = setup_tests()
        start,end = s.setup_test_dates(date1=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(2010,1,1))

    def test_dates_date_2(self):
        '''Tests the that the dates can handle '.' as the deliminator.'''
        s = setup_tests()
        start,end = s.setup_test_dates(date2=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(2010,1,1))

    def test_dates_date_3(self):
        '''Tests the that the dates can handle the "Day/Month/Year format"'''
        s = setup_tests()
        start,end = s.setup_test_dates(date3=True)
        self.assertEqual(start, dt.datetime(1900,1,20))
        self.assertEqual(end, dt.datetime(2010,1,20))

    def test_dates_ymd(self):
        '''Tests the that the dates function parameters year, month and day work properly.'''
        s=setup_tests()
        start,end = s.setup_test_dates(year=True,month=True,day=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(1900,1,1))

    def test_dates_ymd_error(self):
        '''Tests that the dates function parameters year, month and day error properly.'''
        d = DateFormatter()
        with self.assertRaises(TypeError):
            start = d.start_date(year='1900',month='1',day='1')
            end = d.end_date(year='1900',month='1',day='1')

    def test_nominal_gdp(self):
        '''Tests that the GDP function with the nominal parameter set to pull Nominal GDP works properly.'''
        s=setup_tests()
        df = s.setup_test_gdp(nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('GDPC1', 'fred', start, end)
        self.assertEqual(df['GDPC1'][10],test_df['GDPC1'][10])

    def test_real_gdp(self):
        '''Tests that the GDP function with the nominal parameter set to pull Real GDP works properly.'''
        s=setup_tests()
        df = s.setup_test_gdp(nominal=False)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('GDP', 'fred', start, end)
        self.assertEqual(df['GDP'][2],test_df['GDP'][2])

    def test_state_gdp(self):
        '''Tests that the state GDP function works properly.'''
        s=setup_tests()
        df = s.setup_test_state_gdp()
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('TXNGSP', 'fred', start, end)
        self.assertEqual(df['TXNGSP'][5],test_df['TXNGSP'][5])

    def test_state_gdp_error(self):
        '''Tests that the state GDP function errors properly.'''
        s=setup_tests()
        state = 'Texas'
        with self.assertRaises(TypeError):
            df = s.setup_test_state_gdp(state)

    def test_metro_gdp_name(self):
        '''Tests that the metroGDP function with the name paramater selected parses a metro name properly.'''
        s=setup_tests()
        df = s.setup_test_metro_gdp(name=True,nominal=False)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('RGMP26420', 'fred', start, end)
        self.assertEqual(df['RGMP26420'][0],test_df['RGMP26420'][0])

    def test_metro_gdp_cbsa(self):
        '''Tests that the metroGDP function with the cbsa paramater selected parses the cbsa properly.'''
        s=setup_tests()
        df = s.setup_test_metro_gdp(cbsa=True, nominal=False)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('RGMP26420', 'fred', start, end)
        self.assertEqual(df['RGMP26420'][0],test_df['RGMP26420'][0])

    def test_metro_gdp_cbsa_nominal(self):
        '''Tests that the metroGDP function with the cbsa & nominal paramaters selected works properly.'''
        s=setup_tests()
        df = s.setup_test_metro_gdp(cbsa=True, nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('NGMP26420', 'fred', start, end)
        self.assertEqual(df['NGMP26420'][0],test_df['NGMP26420'][0])

    def test_metro_gdp_name_nominal(self):
        '''Tests that the metroGDP function with the name & nominal paramaters selected works properly.'''
        s=setup_tests()
        df = s.setup_test_metro_gdp(name=True,nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('NGMP26420', 'fred', start, end)
        self.assertEqual(df['NGMP26420'][2],test_df['NGMP26420'][2])

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
