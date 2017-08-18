import pandas as pd
import tushare as ts

c = pd.DataFrame()

def test(content):

    # print(ts.get_industry_classified())

    # df = ts.profit_data(year=2017, top=60)
    # df.sort('shares', ascending=False)
    # print(df)

    # print(ts.get_today_all())
    content = ts.get_today_all()

    # print(ts.forecast_data(2017, 2))

    # print(ts.fund_holdings(2016, 4))

    # print(ts.sh_margin_details(start='2017-01-01', end='2017-04-19', symbol='601989'))

    # print(ts.get_stock_basics())

    # print(ts.get_latest_news())

    # print(ts.get_notices())

    # print(ts.guba_sina())
    print(content)


if __name__ == '__main__':
    test(c)