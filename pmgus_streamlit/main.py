#####
import pandas as pd
import streamlit as st

#READ
trading_view_df = pd.read_csv('/Users/sudz4/Desktop/SPS_local/sps/x_pre_market_gap_up_screener/pmgus_inputs/tv_screen_gap-up_2025-01-10.csv')

#WRITE
st.write(trading_view_df)