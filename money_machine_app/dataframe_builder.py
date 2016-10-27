"""Build a dataframe in pandas."""
import pandas as pd
import money_machine_app.util as util


def test_run():
    # Define a date range
    dates = pd.date_range('2016-10-01', '2016-10-31')

    # Choose currency symbols to read
    symbols = ['EUR', 'USD', 'GBP']

    # Get stock data
    df = util.get_currency_data(symbols, dates)

    print(df)


if __name__ == "__main__":
    test_run()
