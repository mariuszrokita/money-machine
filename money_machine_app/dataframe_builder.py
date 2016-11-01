"""Build a dataframe in pandas."""
import pandas as pd
import matplotlib.pyplot as plt
import money_machine_app.io_util as util
import money_machine_app.math_util as math_util
import money_machine_app.stats_util as stats_util


def build_dataframe(symbols, dates):
    df = util.get_currency_data(symbols, dates)
    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2016-06-01', '2016-10-31')

    # Choose currency symbols to read
    symbols = ['EUR', 'USD', 'GBP']

    # Get stock data
    df = build_dataframe(symbols, dates)

    ##################
    # EUR - statistics
    ##################

    sma5_eur = stats_util.get_rolling_mean(df['EUR'], window=5)
    sma20_eur = stats_util.get_rolling_mean(df['EUR'], window=20)
    rstd_eur = stats_util.get_rolling_std(df['EUR'], window=20)
    upper_band_eur, lower_band_eur = stats_util.get_bollinger_bands(sma20_eur, rstd_eur)

    # visualize data
    ax_eur = df['EUR'].plot(title="EUR - statistics", color='b', label="EUR exchange rates")
    sma5_eur.plot(label="SMA 5", color='c', linestyle='--', ax=ax_eur)
    sma20_eur.plot(label="SMA 20", color='m', linestyle=':', ax=ax_eur)
    upper_band_eur.plot(label="Upper Bollinger band", color='r', ax=ax_eur)
    lower_band_eur.plot(label="Lower Bollinger band", color='g', ax=ax_eur)
    ax_eur.set_xlabel("Date")
    ax_eur.set_ylabel("Price")
    ax_eur.legend(loc="upper right")

    # show intersection points between SMA-5 and SMA-20
    x_values = range(0, len(sma5_eur), 1)
    intersection_points = math_util.get_intersection_points(x_values, sma5_eur, sma20_eur)
    for intersect_point in intersection_points:
        plt.plot(intersect_point[0], intersect_point[1], 'co')

    plt.grid()
    plt.show()

    # ##################
    # # USD - statistics
    # ##################
    #
    # sma5_usd = stats_util.get_rolling_mean(df['USD'], window=5)
    # sma20_usd = stats_util.get_rolling_mean(df['USD'], window=20)
    # rstd_usd = stats_util.get_rolling_std(df['USD'], window=20)
    # upper_band_usd, lower_band_usd = stats_util.get_bollinger_bands(sma20_usd, rstd_usd)
    #
    # # visualize data
    # ax_usd = df['USD'].plot(title="USD - statistics", color='b', label="USD exchange rates")
    # sma5_usd.plot(label="SMA 5", color='c', linestyle='--', ax=ax_usd)
    # sma20_usd.plot(label="SMA 20", color='m', linestyle=':', ax=ax_usd)
    # upper_band_usd.plot(label="Upper Bollinger band", color='r', ax=ax_usd)
    # lower_band_usd.plot(label="Lower Bollinger band", color='g', ax=ax_usd)
    # ax_usd.set_xlabel("Date")
    # ax_usd.set_ylabel("Price")
    # ax_usd.legend(loc="upper right")
    # plt.show()
    #
    # ##################
    # # GBP - statistics
    # ##################
    #
    # sma5_gbp = stats_util.get_rolling_mean(df['GBP'], window=5)
    # sma20_gbp = stats_util.get_rolling_mean(df['GBP'], window=20)
    # rstd_gbp = stats_util.get_rolling_std(df['GBP'], window=20)
    # upper_band_gbp, lower_band_gbp = stats_util.get_bollinger_bands(sma20_gbp, rstd_gbp)
    #
    # # visualize data
    # ax_gbp = df['GBP'].plot(title="GBP - statistics", color='b', label="GBP exchange rates")
    # sma5_gbp.plot(label="SMA 5", color='c', linestyle='--', ax=ax_gbp)
    # sma20_gbp.plot(label="SMA 20", color='m', linestyle=':', ax=ax_gbp)
    # upper_band_gbp.plot(label="Upper Bollinger band", color='r', ax=ax_gbp)
    # lower_band_gbp.plot(label="Lower Bollinger band", color='g', ax=ax_gbp)
    # ax_gbp.set_xlabel("Date")
    # ax_gbp.set_ylabel("Price")
    # ax_gbp.legend(loc="upper right")
    # plt.show()


if __name__ == "__main__":
    test_run()
