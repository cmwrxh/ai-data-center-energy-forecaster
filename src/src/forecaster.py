import numpy as np
import pandas as pd

class DemandForecaster:
    def __init__(self, base_twh=450, annual_growth=0.25, years=5, months_per_year=12):
        self.base_twh = base_twh  # 2025-ish global ~450 TWh
        self.annual_growth = annual_growth  # ~25% CAGR aggressive AI scenario
        self.years = years
        self.months = years * months_per_year

    def forecast_monthly_mw(self):
        # Convert TWh/year to average MW: TWh * 1e6 / 8760 hours
        base_mw = self.base_twh * 1e6 / 8760
        months = np.arange(self.months)
        growth_factor = (1 + self.annual_growth) ** (months / 12)
        monthly_mw = base_mw * growth_factor
        df = pd.DataFrame({
            'Month': pd.date_range(start='2026-01-01', periods=self.months, freq='M'),
            'Forecast_MW': monthly_mw
        })
        return df

    def annual_twh(self):
        return self.base_twh * (1 + self.annual_growth) ** np.arange(1, self.years + 1)
