"""Build a dataframe in pandas."""

import pandas as pd


def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)

    # Create an empty dataframe with (consecutive dates only)
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("../data/SPY.csv",
                        index_col="Date",                   # by default integer is used as an index
                        parse_dates=True,
                        usecols=['Date', 'Adj Close'],      # we're interested in only 2 columns
                        na_values=['nan'])

    # Rename 'Adj Close' colummn to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})

    # (Inner) Join the two dataframes
    df1 = df1.join(dfSPY, how='inner')

    # alternatively, (Left) join the two dataframes using DataFrame.join()
    # and drop NaN Values
    #df1 = df1.join(dfSPY)
    #df1 = df1.dropna()

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("../data/{}.csv".format(symbol),
                              index_col="Date",  # by default integer is used as an index
                              parse_dates=True,
                              usecols=['Date', 'Adj Close'],  # we're interested in only 2 columns
                              na_values=['nan'])

        # Rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df1 = df1.join(df_temp)  # use default how='left'

    print(df1)


if __name__ == "__main__":
    test_run()

