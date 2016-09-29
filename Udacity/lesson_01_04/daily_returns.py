"""Some comment on the module."""

import os
import pandas as pd
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="..\\data"):
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


def plot_data(df, title="Stock prices", ylabel="Price"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
    plt.show()


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # way 1
    #daily_returns = df.copy()  # copy given DataFrame to match size and column names
    #daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    #daily_returns.ix[0, :] = 0  # set daily returns for row 0 to 0

    # way 2
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    #plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


if __name__ == "__main__":
    test_run()

