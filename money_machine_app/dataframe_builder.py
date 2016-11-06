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
    dates = pd.date_range('2016-06-01', '2016-12-31')
    # dates = pd.date_range('2014-01-01', '2016-12-31')

    # Choose currency symbols to read
    symbols = ['EUR', 'USD', 'GBP']

    # Get stock data
    df = build_dataframe(symbols, dates)

    ##################
    # statistics
    ##################
    symbols_stats = ['EUR', 'USD', 'GBP']
    # symbols_stats = ['EUR']

    daily_returns = stats_util.compute_daily_returns(df)
    print(daily_returns)

    for symbol in symbols_stats:
        window_1 = 5
        window_2 = 20
        sma1 = stats_util.get_rolling_mean(df[symbol], window=window_1)
        sma2 = stats_util.get_rolling_mean(df[symbol], window=window_2)
        rstd = stats_util.get_rolling_std(df[symbol], window=window_2)
        upper_band, lower_band = stats_util.get_bollinger_bands(sma2, rstd)

        # visualize data
        ax = df[symbol].plot(title="{} - statistics".format(symbol),
                             color='b',
                             label="{} exchange rates".format(symbol))
        sma1.plot(label="SMA {}".format(window_1), color='c', linestyle='--', ax=ax)
        sma2.plot(label="SMA {}".format(window_2), color='m', linestyle=':', ax=ax)
        upper_band.plot(label="Upper Bollinger band", color='r', ax=ax)
        lower_band.plot(label="Lower Bollinger band", color='g', ax=ax)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc="upper right")

        # # show intersection points between SMA-5 and SMA-20
        sma1_sma2_intersection_points = math_util.get_intersection_points(sma1, sma2)
        for intersect_point in sma1_sma2_intersection_points:
            plt.plot(intersect_point[0], intersect_point[1], 'mo')
            date_to_print = pd.to_datetime(str(intersect_point[0])).strftime("%d.%m.%Y")
            ax.text(intersect_point[0],                                                     # x-axis
                    intersect_point[1] + 0.005,                                             # y-axis
                    "{} ({})".format(round(intersect_point[1], 4), date_to_print),          # text
                    color="magenta",
                    fontsize=11)

        # show intersection points between exchange rates and Bollinger bands
        exchange_rates_for_analysis = df[symbol][-len(upper_band):]

        # print("x_values:")
        # print(x_values)
        # print("exchange_rates_for_analysis:")
        # print(exchange_rates_for_analysis)
        # print("len of exchange_rates_for_analysis, ", len(exchange_rates_for_analysis))
        # print("upper band:")
        # print(upper_band)
        # print("len of upper_band, ", len(upper_band))
        er_ub_intersection_points = math_util.get_intersection_points(exchange_rates_for_analysis, upper_band)
        for intersect_point in er_ub_intersection_points:
            plt.plot(intersect_point[0], intersect_point[1], 'ro')
            date_to_print = pd.to_datetime(str(intersect_point[0])).strftime("%d.%m.%Y")
            ax.text(intersect_point[0],                                                     # x-axis
                    intersect_point[1] + 0.005,                                             # y-axis
                    "{} ({})".format(round(intersect_point[1], 4), date_to_print),          # text
                    color="red",
                    fontsize=11)

        er_lb_intersection_points = math_util.get_intersection_points(exchange_rates_for_analysis, lower_band)
        for intersect_point in er_lb_intersection_points:
            plt.plot(intersect_point[0], intersect_point[1], 'go')
            date_to_print = pd.to_datetime(str(intersect_point[0])).strftime("%d.%m.%Y")
            ax.text(intersect_point[0],                                                     # x-axis
                    intersect_point[1] + 0.005,                                             # y-axis
                    "{} ({})".format(round(intersect_point[1], 4), date_to_print),          # text
                    color="green",
                    fontsize=11)

        plt.grid()
        plt.show()


if __name__ == "__main__":
    test_run()
