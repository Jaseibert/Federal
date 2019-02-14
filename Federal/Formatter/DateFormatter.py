import datetime as dt
import re

class DateFormatter(object):

    def __init__(self,start=None,end=None):
        self.start = start
        self.end = end
        return

############################################################################################
#DateTime Formatting
############################################################################################
    def date_formatter(self,dates,delim):
        d = r"[{}]".format(delim)
        if re.search(d, dates) is not None:
            try:
                val = dt.datetime.strptime(str(dates),'%m'+delim+'%d'+delim+'%Y')
                if val is not None:
                    return val
            except ValueError:
                try:
                    val = dt.datetime.strptime(str(dates),'%d'+delim+'%m'+delim+'%Y')
                    if val is not None:
                        return val
                except ValueError:
                    val = dt.datetime.strptime(str(dates),'%Y'+delim+'%m'+delim+'%d')
                    if val is not None:
                        return val
                    else:
                        raise ValueError('Date cannot be formatted')

############################################################################################
#StartDate Formatting
############################################################################################

    def start_date(self, date=None, year=None, month=None, day=None, full=False):
        """ This function defines the start date for the query"""
        try:
            if date is not None:
                #Logic For other Formats
                if self.date_formatter(date,'/') is not None:
                    self.start = self.date_formatter(date,'/')
                    return self.start
                elif self.date_formatter(date,'-') is not None:
                    self.start = self.date_formatter(date,'-')
                    return self.start
                elif self.date_formatter(date,'.') is not None:
                    self.start = self.date_formatter(date,'.')
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
############################################################################################
#EndDate Formatting
############################################################################################

    def end_date(self, date=None, year=None, month=None, day=None, full=False):
        """ This function defines the end date for the query."""
        try:
            if date is not None:
                #Logic For other Formats
                if self.date_formatter(date,'/') is not None:
                    self.end = self.date_formatter(date,'/')
                    return self.end
                elif self.date_formatter(date,'-') is not None:
                    self.end = self.date_formatter(date,'-')
                    return self.end
                elif self.date_formatter(date,'.') is not None:
                    self.end = self.date_formatter(date,'.')
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
