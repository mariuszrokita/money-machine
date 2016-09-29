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


def plot_data(df, title="Stock prices"):
    """Plot stock prices"""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    return pd.rolling_std(values, window=window)


def get_bollinger_bands(rm, rstd):
    """Return upper and lower Bollinger Bands."""
    upper_band = rm + 2*rstd
    lower_band = rm - 2*rstd
    return upper_band, lower_band


def test_run():
    # Read data
    dates = pd.date_range('2012-01-01', '2012-12-31')
    symbols = ['SPY']
    df = get_data(symbols, dates)

    # Compute Bollinger Bands
    # 1. Compute rolling mean using a 20-day window
    rm_SPY = get_rolling_mean(df['SPY'], window=20)

    # 2. Compute rolling standard deviation
    rstd_SPY = get_rolling_std(df['SPY'], window=20)

    # 3. Compute upper and lower bands
    upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)

    # Plot SPY data, rolling meand and Bollinger Bands
    ax = df['SPY'].plot(title="Bollinger Bands", label="SPY")
    rm_SPY.plot(title="Rolling mean", ax=ax)
    upper_band.plot(label="Upper Bollinger band", ax=ax)
    lower_band.plot(label="Lower Bollinger band", ax=ax)

    # Add axis labels and legend
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc="upper left")
    plt.show()


if __name__ == "__main__":
    test_run()

