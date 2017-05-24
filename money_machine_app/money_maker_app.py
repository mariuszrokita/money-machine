"""
Main application file.
"""

import matplotlib.pyplot as plt
import pandas as pd
import sys
from datetime import date

import utils.io_util as util
import utils.math_util as math_util
import utils.stats_util as stats_util

import downloaders.stocks_data_downloader as sdd
import downloaders.currency_data_downloader as cdd


def build_currency_dataframe(symbols, dates):
    df = util.get_currency_data(symbols, dates)
    return df


def build_stocks_dataframe(symbols, dates):
    df = util.get_stock_data(symbols, dates)
    return df


def compute_and_show_currency_stats(df, symbols, window_1, window_2):
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


def compute_and_show_stock_stats(df, symbols, window_1, window_2):
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


def get_last_date_of_current_year():
    """Return a string representing the last date of current year in ISO 8601 format, 'YYYY-MM-DD'."""
    return date(year=date.today().year, month=12, day=31).isoformat()


def get_latest_stocks(symbols, start_date, end_date):
    for symbol in symbols:
        sdd.download_data(stock_symbol=symbol, start_date=start_date, end_date=end_date)


def get_latest_currencies(symbols, start_date, end_date):
    for symbol in symbols:
        cdd.download_data(currency_symbol=symbol, start_date=start_date, end_date=end_date)


def analyse_currencies(currency_symbols):
    # configuration
    currencies_time_frame = pd.date_range('2016-01-01', '2017-12-31')
    currencies_window_1 = 5
    currencies_window_2 = 20

    df = build_currency_dataframe(currency_symbols, currencies_time_frame)
    compute_and_show_currency_stats(df,
                                    symbols=currency_symbols,
                                    window_1=currencies_window_1,
                                    window_2=currencies_window_2)


def analyse_stocks(stock_symbols):
    # configuration
    stocks_time_frame = pd.date_range('2016-01-01', '2017-12-31')
    stocks_window_1 = 15  # popular pairs: 15 and 45, 10 and 50.
    stocks_window_2 = 45

    # WIG is mandatory because it's used to determine trading dates
    symbols = ['WIG'] + stock_symbols
    df = build_stocks_dataframe(symbols, stocks_time_frame)
    compute_and_show_stock_stats(df,
                                 symbols=symbols,
                                 window_1=stocks_window_1,
                                 window_2=stocks_window_2)


def analyse_etfs(etf_symbols):
    etfs_time_frame = pd.date_range('2016-01-01', '2017-12-31')
    etfs_window_1 = 10
    etfs_window_2 = 50

    # WIG is mandatory because it's used to determine trading dates
    symbols = ['WIG'] + etf_symbols
    df = build_stocks_dataframe(symbols, etfs_time_frame)
    compute_and_show_stock_stats(df,
                                 symbols=etf_symbols,
                                 window_1=etfs_window_1,
                                 window_2=etfs_window_2)


if __name__ == "__main__":
    print("debugging")
    print("0: ", sys.argv[0])
    print("1: ", sys.argv[1])
    print("2: ", sys.argv[2])

    analysis_type = sys.argv[1]
    if analysis_type:
        data = sys.argv[2]

        if analysis_type == "CURRENCY":
            currencies = data.split(";")
            analyse_currencies(currencies)

        if analysis_type == "STOCK":
            stock_symbols = data.split(";")
            analyse_stocks(stock_symbols)

        if analysis_type == 'ETF':
            etf_symbols = data.split(';')
            analyse_etfs(etf_symbols)
