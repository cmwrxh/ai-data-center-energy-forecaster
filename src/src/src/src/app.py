import streamlit as st
from src.forecaster import DemandForecaster
from src.supply_matcher import simple_solar_battery_match
from src.nuclear_match import add_nuclear_baseload
import plotly.express as px

st.title("AI Data Center Power Forecaster 2026+")

growth = st.slider("Annual Growth Rate (%)", 10, 40, 25) / 100
fc = DemandForecaster(annual_growth=growth)
df = fc.forecast_monthly_mw()

solar = st.number_input("Solar + Battery Capacity (MW)", 500, 5000, 2000)
nuclear = st.number_input("Nuclear Baseload (MW)", 0, 2000, 500)

df = simple_solar_battery_match(df, solar_capacity_mw=solar)
df = add_nuclear_baseload(df, nuclear_mw=nuclear)

fig = px.line(df, x='Month', y=['Forecast_MW', 'Total_Clean_MW', 'Net_Gap_MW'],
              title="Demand vs Clean Supply Scenarios")
st.plotly_chart(fig)

st.dataframe(df)
