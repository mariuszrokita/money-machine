import urllib.request
import sys
import os


def get_source_url(currency_symbol, start_date, end_date):
    """Returns URL address for requested currency and time frame."""
    url_template = ("http://www.bankier.pl/narzedzia/archiwum-kursow-walutowych/get_answer?"
                    "op=4&cur_symbol={}&start_dt={}&end_dt={}&customs=0"
                    "&table_name=0&fromDay=0&monthDay=1&avg=0&avg_type=1&idTable=gemiusHitSection16")
    return url_template.format(currency_symbol, start_date, end_date)


def get_csv(url):
    """Returns CSV content with exchange rates"""
    with urllib.request.urlopen(url) as response:
        content = str(response.read(), errors='ignore')

    # remove unnecessary text from the file and leave only csv data
    content_lines = content.splitlines()[2:-4]
    return '\n'.join(content_lines)


def get_base_dir(folder="..\\data-archive"):
    current_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_file, folder)


def symbol_to_path(symbol, base_dir="..\\data-archive"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def save_data_as_file(symbol, csv_content):
    """Saves content as a file."""
    # determine file path where file should be saved
    base_dir = get_base_dir()
    path = symbol_to_path(symbol, base_dir)
    print(path)

    f = open(path, 'w')
    f.write(csv_content)
    f.close()


def download_data(currency_symbol="EUR", start_date="2013-01-01", end_date="2016-10-26"):
    """Gets currency data from web and saves in the file."""
    url = get_source_url(currency_symbol, start_date, end_date)
    csv_content = get_csv(url)
    save_data_as_file(currency_symbol, csv_content)


if __name__ == "__main__":
    download_data(sys.argv[0], sys.argv[1], sys.argv[2])


