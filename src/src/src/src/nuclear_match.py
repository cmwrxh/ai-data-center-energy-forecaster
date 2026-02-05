def add_nuclear_baseload(forecast_df, nuclear_mw=500):
    forecast_df['Nuclear_MW'] = nuclear_mw
    forecast_df['Total_Clean_MW'] = forecast_df.get('Supply_MW', 0) + nuclear_mw
    forecast_df['Net_Gap_MW'] = forecast_df['Forecast_MW'] - forecast_df['Total_Clean_MW']
    return forecast_df
