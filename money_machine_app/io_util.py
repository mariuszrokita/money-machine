"""Utilities module for reusable things across project."""

import os
import pandas as pd


def get_base_dir(folder="..\\data-archive"):
    current_file = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(current_file, folder)


def symbol_to_path(symbol, base_dir="..\\data-archive", sub_folder=""):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, sub_folder, "{}.csv".format(str(symbol)))


def get_currency_data(symbols, dates):
    """Read currency data (exchange rate) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, get_base_dir(), sub_folder="currencies"),
                              delimiter=";",
                              index_col="Data",  # by default integer is used as an index
                              parse_dates=True,
                              usecols=['Data', 'Kurs'],  # we're interested in only 2 columns
                              na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Kurs': symbol})
        df = df.join(df_temp)
        df = df.dropna()  # drop dates without exchange rates
    return df


def get_stock_data(symbols, dates):
    """Read stock data (exchange rate) for given symbols from CSV files."""
    # create an empty dataframe
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol, get_base_dir(), sub_folder="stocks"),
                              delimiter=",",
                              index_col="Data",  # by default integer is used as an index
                              parse_dates=True,
                              usecols=['Data', 'Zamkniecie'],  # we're interested in only 2 columns
                              na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Zamkniecie': symbol})
        df = df.join(df_temp)
        if symbol == 'WIG':  # drop dates when Giełda Papierów Wartościowych did not trade
            df = df.dropna(subset=["WIG"])
    return df
