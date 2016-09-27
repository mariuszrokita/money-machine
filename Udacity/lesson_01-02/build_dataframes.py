"""Build a dataframe in pandas."""
import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="../data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    if 'SPY' not in symbols:    # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        # Read SPY data into temporary dataframe
        df_temp = pd.read_csv(symbol_to_path(symbol),
                              index_col="Date",  # by default integer is used as an index
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],  # we're interested in only 2 columns
                              na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def normalize_data(df):
    """Normalize stock prices using the first row of the dataframe."""
    return df / df.ix[0, :]


def plot_data(df, title="Stock prices"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    plot_data(df.ix[start_index:end_index, columns], title="Selected data")


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']  # SPY will be added in get_data()

    # Get stock data
    df = get_data(symbols, dates)

    # Normalize data
    df = normalize_data(df)

    # Slice by row range (dates) using DataFrame.ix[] selector
    print(df.ix['2010-01-01':'2010-01-31'])

    # Slice by column (symbols)
    print(df['GOOG'])
    print(df[['GOOG', 'IBM']])

    # Slice by row range (dates) and columns using DataFrame.ix[] selector
    print(df.ix['2010-01-01':'2010-01-31', ['GOOG', 'IBM']])

    # Slice and plot
    plot_selected(df, ['SPY', 'IBM', 'GOOG', 'GLD'], '2010-01-01', '2010-12-31')


if __name__ == "__main__":
    test_run()

