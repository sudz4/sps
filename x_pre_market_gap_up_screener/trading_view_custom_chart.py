import pandas as pd
from lightweight_charts import Chart


chart = Chart()

# Columns: time | open | high | low | close | volume
ohlcv_2_df = pd.read_csv('/Users/sudz4/Desktop/SPS_local/sps/x_pre_market_gap_up_screener/ohlcv_2.csv')
chart.set(ohlcv_2df)

chart.show(block=True)