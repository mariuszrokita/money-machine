"""Some comment on the module."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Udacity.util import get_data, plot_data


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = (df / df.shift(1)) - 1
    daily_returns.ix[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)
    #plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind="scatter", x='SPY', y='XOM')

    ## fit linear regression
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    print("beta_XOM=", beta_XOM)
    print("alpha_XOM=", alpha_XOM)
    plt.plot(daily_returns['SPY'], beta_XOM*daily_returns['SPY'] + alpha_XOM, '-', color='r')
    plt.show()

    # Scatterplot SPY vs GLD
    daily_returns.plot(kind="scatter", x='SPY', y='GLD')

    ## fit linear regression
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    print("beta_GLD=", beta_GLD)
    print("alpha_GLD=", alpha_GLD)
    plt.plot(daily_returns['SPY'], beta_GLD * daily_returns['SPY'] + alpha_GLD, '-', color='r')
    plt.show()

    # Calculate correlation coefficient
    print(daily_returns.corr(method='pearson'))


if __name__ == "__main__":
    test_run()

