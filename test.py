from Econ.Fred import *
from Econ.CBSA import *
import datetime as dt
import unittest
import pandas_datareader.data as web

class setup_tests(object):

    def __init__(self):
        return

    def setup_test_dates(self,date=False,date1=False,year=False,month=False,day=False,full=False):
        f = FRED()
        if date is not False:
            start = f.start_date(date='1/1/1900')
            end = f.end_date(date='1/1/2018')
            return start,end
        elif date1 is not False:
            start = f.start_date(date='1-1-1900')
            end = f.end_date(date='1-1-2018')
            return start,end
        elif full is not False:
            start = f.start_date(full=True)
            end = f.end_date(full=True)
            return start,end
        else:
            start = f.start_date(year=1900,month=1,day=1)
            end = f.end_date(year=1900,month=1,day=1)
            return start,end

    def setup_test_gdp(self,nominal=True):
        f = FRED()
        f.start_date(date='1/1/1900')
        f.end_date(date='1/1/2018')
        if nominal is True:
            df = f.GDP(nominal=True)
            return df
        else:
            df = f.GDP(nominal=False)
            return df

    def setup_test_state_gdp(self):
        f = FRED()
        f.start_date(date='1/1/1900')
        f.end_date(date='1/1/2018')
        df = f.stateGDP('TX')
        return df

    def setup_test_metro_gdp(name=False,cbsa=False,nominal=False):
        f = FRED()
        f.start_date(date='1/1/1900')
        f.end_date(date='1/1/2018')
        if name is not False:
            df = f.metroGDP(name='Houston')
            return df
        elif cbsa is not False:
            df = f.metroGDP(cbsa=26420)
            return df
        elif cbsa is not False and nominal is not False:
            df = f.metroGDP(cbsa=26420,nominal=True)
            return df
        elif name is not False and nominal is not False:
            df = f.metroGDP(name='Houston', nominal=True)
            return df
        else:
            pass

class TestFRED(unittest.TestCase):

    def test_dates_date_0(self):
        s = setup_tests()
        start,end = s.setup_test_dates(date=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(2018,1,1))

    def test_dates_date_1(self):
        s = setup_tests()
        start,end = s.setup_test_dates(date1=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(2018,1,1))

    def test_dates_date_error(self):
        f = FRED()
        with self.assertRaises(ValueError):
            start = f.start_date(date='Jeremy')
            end = f.end_date(date='Jeremy')

    def test_dates_ymd(self):
        s=setup_tests()
        start,end = s.setup_test_dates(year=True,month=True,day=True)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(1900,1,1))

    def test_dates_ymd_error(self):
        f=FRED()
        with self.assertRaises(TypeError):
            start = f.start_date(year='1900',month='1',day='1')
            end = f.end_date(year='1900',month='1',day='1')

    def test_nominal_gdp(self):
        s=setup_tests()
        df = s.setup_test_gdp(nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('GDPC1', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_real_gdp(self):
        s=setup_tests()
        df = s.setup_test_gdp(nominal=False)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('GDP', 'fred', start, end)
        self.assertEqual(df[0],test_df[0])

    def test_state_gdp(self):
        s=setup_tests()
        df = s.setup_test_state_gdp()
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('TXNGSP', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_state_gdp_error(self):
        s=setup_tests()
        state = 'Texas'
        with self.assertRaises(TypeError):
            df = s.setup_test_state_gdp(state)

    def test_metro_gdp_name(self):
        s=setup_tests()
        df = s.setup_test_metro_gdp(name=True,nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('RGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_metro_gdp_cbsa(self):
        s=setup_tests()
        df = s.setup_test_metro_gdp(cbsa=True, nominal=False)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('RGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_metro_gdp_cbsa_nominal(self):
        s=setup_tests()
        df = s.setup_test_metro_gdp(cbsa=True, nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('NGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_metro_gdp_name_nominal(self):
        s=setup_tests()
        df = s.setup_test_metro_gdp(name=True,nominal=True)
        start,end = s.setup_test_dates(date=True)
        test_df = web.DataReader('NGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
