import os
import requests
from dateutil.parser import parse


def download_data(symbol='SPY', start='1997-01-01', end='2016-01-01'):
    s = parse(start)
    e = parse(end)

    url = "http://chart.finance.yahoo.com/table.csv"
    payload = {'s' : str(symbol), 'a' : s.month-1, 'b' : s.day, 'c' : s.year,
               'd' : e.month-1, 'e' : e.day, 'f' : e.year, 'g' : 'd', 'ignore' : '.csv'}
    return requests.get(url, params=payload)


def get_csv(symbol='SPY', start='1997-01-01', end='2016-01-01'):
    r = download_data(symbol, start, end)

    if r.status_code != 200:
        return False

    path = os.path.join('../data/', str(symbol) + '.csv')
    print(path)

    f = open(path, 'wb')
    f.write(r.content)
    f.close()

    return True

get_csv(symbol='GOOG')
get_csv(symbol='GLD')
