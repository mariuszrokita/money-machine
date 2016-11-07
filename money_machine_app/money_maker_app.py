"""Build a dataframe in pandas."""
import pandas as pd
import matplotlib.pyplot as plt
import money_machine_app.io_util as util
import money_machine_app.math_util as math_util
import money_machine_app.stats_util as stats_util


def build_currency_dataframe(symbols, dates):
    df = util.get_currency_data(symbols, dates)
    return df


def build_stocks_dataframe(symbols, dates):
    df = util.get_stock_data(symbols, dates)
    return df


def compute_and_show_currency_statistics(df, symbols, window_1, window_2):
    for symbol in symbols:
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
        ax.legend(loc="upper left")

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

        # show maximized window
        plt.grid()
        plt.show()


def compute_and_show_stock_statistics(df, symbols, window_1, window_2):
    for symbol in symbols:
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
        ax.legend(loc="upper left")

        # # show intersection points between SMA-5 and SMA-20
        sma1_sma2_intersection_points = math_util.get_intersection_points(sma1, sma2)
        for intersect_point in sma1_sma2_intersection_points:
            plt.plot(intersect_point[0], intersect_point[1], 'mo')
            date_to_print = pd.to_datetime(str(intersect_point[0])).strftime("%d.%m.%Y")
            ax.text(intersect_point[0],                                                     # x-axis
                    intersect_point[1] * 1.01,                                              # y-axis
                    "{} ({})".format(round(intersect_point[1], 4), date_to_print),          # text
                    color="magenta",
                    fontsize=11)

        # show intersection points between stock quotation and Bollinger bands
        stock_values_for_analysis = df[symbol][-len(upper_band):]

        # print("x_values:")
        # print(x_values)
        # print("exchange_rates_for_analysis:")
        # print(exchange_rates_for_analysis)
        # print("len of exchange_rates_for_analysis, ", len(exchange_rates_for_analysis))
        # print("upper band:")
        # print(upper_band)
        # print("len of upper_band, ", len(upper_band))
        sq_ub_intersection_points = math_util.get_intersection_points(stock_values_for_analysis, upper_band)
        for intersect_point in sq_ub_intersection_points:
            plt.plot(intersect_point[0], intersect_point[1], 'ro')
            date_to_print = pd.to_datetime(str(intersect_point[0])).strftime("%d.%m.%Y")
            ax.text(intersect_point[0],                                                     # x-axis
                    intersect_point[1] * 1.01,                                              # y-axis
                    "{} ({})".format(round(intersect_point[1], 4), date_to_print),          # text
                    color="red",
                    fontsize=11)

        sq_lb_intersection_points = math_util.get_intersection_points(stock_values_for_analysis, lower_band)
        for intersect_point in sq_lb_intersection_points:
            plt.plot(intersect_point[0], intersect_point[1], 'go')
            date_to_print = pd.to_datetime(str(intersect_point[0])).strftime("%d.%m.%Y")
            ax.text(intersect_point[0],                                                     # x-axis
                    intersect_point[1] * 1.01,                                              # y-axis
                    "{} ({})".format(round(intersect_point[1], 4), date_to_print),          # text
                    color="green",
                    fontsize=11)

        # show maximized window
        plt.grid()
        plt.show()


def test_run():
    available_stock_symbols = ['GPW', 'KRU', 'JSW', 'ETFW20L.PL']
    available_currency_symbols = ['EUR', 'USD', 'GBP']

    # configure stock analysis
    analyse_stocks = 1
    stocks_time_frame = pd.date_range('2016-01-01', '2016-12-31')
    stocks_for_stats = ['KRU', 'JSW', 'ETFW20L.PL']
    stocks_window_1 = 10
    stocks_window_2 = 50

    # configure currency analysis
    analyse_currencies = 0
    currencies_time_frame = pd.date_range('2016-06-01', '2016-12-31')
    currencies_for_stats = ['EUR', 'USD', 'GBP']
    currencies_window_1 = 5
    currencies_window_2 = 20

    if analyse_stocks:
        df = build_stocks_dataframe(available_stock_symbols, stocks_time_frame)
        compute_and_show_stock_statistics(df,
                                          symbols=stocks_for_stats,
                                          window_1=stocks_window_1,
                                          window_2=stocks_window_2)

    if analyse_currencies:
        df = build_currency_dataframe(available_currency_symbols, currencies_time_frame)
        compute_and_show_currency_statistics(df,
                                             symbols=currencies_for_stats,
                                             window_1=currencies_window_1,
                                             window_2=currencies_window_2)

if __name__ == "__main__":
    test_run()
