import datetime as dt
import re

class Formatter(object):

    def __init__(self):
        return

    def date_formatter(self,dates,delim):
        d = r"[{}]".format(delim)
        if re.search(d, dates) is not None:
            try:
                val = dt.datetime.strptime(str(dates),'%m'+delim+'%d'+delim+'%Y')
                return val
            except ValueError:
                try:
                    val = dt.datetime.strptime(str(dates),'%d'+delim+'%m'+delim+'%Y')
                    return val
                except ValueError:
                    val = dt.datetime.strptime(str(dates),'%Y'+delim+'%m'+delim+'%d')
                    return val
