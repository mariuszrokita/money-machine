import os
import sys
import urllib.request


def get_source_url(stock_symbol, start_date, end_date):
    """Returns URL address template for requested stock and time frame.

    Example:
        stock_symbol = KRU
        start_date   = 20120101
        end_date     = 20161104
        Returned Url: http://stooq.pl/q/d/l/?s=kru&d1=20120101&d2=20161104&i=d
    """
    url_template = "http://stooq.pl/q/d/l/?s={}&d1={}&d2={}&i=d"

    # make dates compliant with format
    start_date = start_date.replace("-", "")
    end_date = end_date.replace("-", "")
    return url_template.format(stock_symbol, start_date, end_date)


def get_csv(url):
    """Returns CSV content with stock rates"""
    with urllib.request.urlopen(url) as response:
        content = str(response.read(), errors='ignore')

    # remove unnecessary text from the file and leave only csv data
    content_lines = content.splitlines()
    return '\n'.join(content_lines)
    return content


def get_base_dir(folder="../data-archive"):
    current_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_file, folder)


def symbol_to_path(symbol, base_dir="../data-archive", subfolder="stocks"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, subfolder, "{}.csv".format(str(symbol)))


def save_data_as_file(symbol, csv_content):
    """Saves content as a file."""
    # determine file path where file should be saved
    base_dir = get_base_dir()
    path = symbol_to_path(symbol, base_dir)
    print(path)

    f = open(path, 'w')
    f.write(csv_content)
    f.close()


def download_data(stock_symbol="KRU", start_date="2012-01-01", end_date="2016-12-31"):
    """Gets currency data from web and saves in the file."""
    url = get_source_url(stock_symbol, start_date, end_date)
    print("Attempting to download stocks data from address: " + url)
    csv_content = get_csv(url)
    save_data_as_file(stock_symbol, csv_content)


if __name__ == "__main__":
    # print("0: ", sys.argv[0])
    # print("1: ", sys.argv[1])
    # print("2: ", sys.argv[2])
    # print("3: ", sys.argv[3])

    start = sys.argv[1]
    if not start:
        start = '2012-01-01'

    end = sys.argv[2]
    if not end:
        end = '2017-12-31'

    stock_symbols = sys.argv[3].split(";")
    if not stock_symbols:
        stock_symbols = ['WIG', 'KRU', 'JSW', 'ETFW20L.PL']

    for stock_symbol in stock_symbols:
        print("=== download_data('%s', '%s', '%s')" % (stock_symbol, start, end))
        download_data(stock_symbol, start, end)
        print("")

    # start = '2012-01-01'
    # end = '2016-12-31'
    #
    # stock_symbols = ['WIG', 'KRU', 'JSW', 'ETFW20L.PL']
    # for symbol in stock_symbols:
    #     download_data(symbol, start, end)