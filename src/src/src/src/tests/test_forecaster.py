from src.forecaster import DemandForecaster

def test_forecast():
    fc = DemandForecaster(base_twh=450, annual_growth=0.2, years=1)
    df = fc.forecast_monthly_mw()
    assert len(df) == 12
    assert df['Forecast_MW'].iloc[-1] > df['Forecast_MW'].iloc[0]
    print("Forecast test passed!")
