"""Some comment on the module."""

import pandas as pd
import matplotlib.pyplot as plt

from Udacity.util import get_data, plot_data


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM']
    df = get_data(symbols, dates)
    #plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Plot both histograms on the same chart
    daily_returns['SPY'].hist(bins=20, label="SPY")  # changing no. of bins to 20
    daily_returns['XOM'].hist(bins=20, label="XOM")
    plt.legend(loc="upper right")
    plt.show()


if __name__ == "__main__":
    test_run()

