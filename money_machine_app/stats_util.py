"""Set of utilities used for plotting."""

import pandas as pd
import matplotlib.pyplot as plt


def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return pd.rolling_mean(values, window=window)


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    return pd.rolling_std(values, window=window)


def get_bollinger_bands(rolling_mean, rolling_std):
    """Return upper and lower Bollinger Bands."""
    upper_band = rolling_mean + 2 * rolling_std
    lower_band = rolling_mean - 2 * rolling_std
    return upper_band, lower_band


def plot_data(df, title="Exchange rates", ylabel="Price"):
    """Plot provided data frame."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)
    plt.show()
