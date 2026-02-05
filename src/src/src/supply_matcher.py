from forecaster import DemandForecaster

def simple_solar_battery_match(forecast_df, solar_capacity_mw=1000, battery_hours=4):
    # Naive: solar provides daytime, battery shifts; assume 25% effective CF for solar+batt
    supply_mw = solar_capacity_mw * 0.25  # rough annual avg
    forecast_df['Supply_MW'] = supply_mw
    forecast_df['Gap_MW'] = forecast_df['Forecast_MW'] - supply_mw
    return forecast_df

# Example usage
if __name__ == "__main__":
    fc = DemandForecaster()
    df = fc.forecast_monthly_mw()
    matched = simple_solar_battery_match(df)
    print(matched.head())
