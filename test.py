from Econ.Fred import FRED
from Econ.CBSA import *
import datetime as dt
import unittest

class TestFRED(unittest.TestCase):

    f = FRED()

    def setup_test_dates(self,date=None,year=None,month=None,day=None,full=None):
        if date is not None:
            start = f.start_date(date=date)
            end = f.end_date(date=date)
            return start,end
        elif full is not None:
            start = f.start_date(full=True)
            end = f.end_date(full=True)
            return start,end
        else:
            start = f.start_date(year=year,month=month,day=day)
            end = f.end_date(year=year,month=month,day=day)
            return start,end

    def test_dates_date_0(self):
        #Test Dates
        start,end = setup_test_dates(date='1/1/1900')
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(1900,1,1))

    def test_dates_date_1(self):
        #Test Dates
        start,end = setup_test_dates(date='1-1-1900')
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(1900,1,1))

    def test_dates_date_error(self):
        date = 'Jeremy'
        with self.assertRaises(TypeError):
            start,end = setup_test_dates(date=date)

    def test_dates_full(self):
        start,end = setup_test_dates(full=True)
        self.assertEqual(start, dt.datetime.strptime('1800-01-01','%Y-%m-%d'))
        self.assertEqual(end, dt.datetime.now())

    def test_dates_ymd(self):
        start,end = setup_test_dates(year=1900,month=1,day=1)
        self.assertEqual(start, dt.datetime(1900,1,1))
        self.assertEqual(end, dt.datetime(1900,1,1))

    def test_dates_ymd_error(self):
        date = 'Jeremy'
        with self.assertRaises(TypeError):
            start,end = setup_test_dates(year='1900',month='1',day='1')

    def setup_test_gdp(self,nominal=None):
        f.start_date(full=True)
        f.end_date(full=True)
        if nominal is not None:
            df = f.GDP(nominal=nominal)
            return df
        else:
            pass

    def test_nominal_gdp(self):
        df = setup_test_gdp(nominal=True)
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('GDPC1', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_real_gdp(self):
        df = setup_test_gdp(nominal=False)
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('GDP', 'fred', start, end)
        self.assertEqual(df,test_df)

    def setup_test_state_gdp(self,state):
        f.start_date(full=True)
        f.end_date(full=True)
        df = f.stateGDP(state)
        return df

    def test_state_gdp(self):
        df = setup_test_state_gdp('TX')
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('TXNGSP', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_state_gdp_error(self):
        state = 'Texas'
        with self.assertRaises(TypeError):
            df = setup_test_state_gdp(state)

    def setup_test_metro_gdp(name=None,cbsa=None,nominal=None):
        f.start_date(full=True)
        f.end_date(full=True)
        if name is not None:
            df = f.metroGDP(name=name)
            return df
        elif cbsa is not None:
            df = f.metroGDP(cbsa=cbsa)
            return df
        elif cbsa is not None and nominal is not None:
            df = f.metroGDP(cbsa=cbsa,nominal=nominal)
            return df
        elif name is not None and nominal is not None:
            df = f.metroGDP(name=name, nominal=nominal)
            return df
        else:
            pass

    def test_metro_gdp_name(self):
        df = setup_test_metro_gdp(name='Houston',nominal=True)
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('RGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_metro_gdp_cbsa(self):
        df = setup_test_metro_gdp(cbsa=26420, nominal=False)
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('RGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_metro_gdp_cbsa_nominal(self):
        df = setup_test_metro_gdp(cbsa=26420, nominal=True)
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('NGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

    def test_metro_gdp_name_nominal(self):
        df = setup_test_metro_gdp(name='Houston',nominal=True)
        start = f.start_date(full=True)
        end = f.end_date(full=True)
        test_df = web.DataReader('NGMP26420', 'fred', start, end)
        self.assertEqual(df,test_df)

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")
