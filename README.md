# AI Data Center Energy Forecaster (2026 Edition)

Simple Python tool to forecast monthly/annual power demand from AI-driven hyperscale data centers and simulate matching to clean energy (solar+batteries, nuclear baseload).

**2026 Reality Check**  
- Global data centers: ~415–500 TWh in 2024–2025 → projected ~600–800+ TWh by 2026–2028 (IEA base: doubling to 945 TWh by 2030, AI as main driver at 30% annual growth for accelerated servers).  
- US: ~180–200 TWh in 2024 (4% of total electricity) → 426 TWh by 2030 (+133%).  
- Trends: AI inference/training exploding; grids strained; push for renewables + SMRs + behind-the-meter power.

Goal: Scenario modeling to show gaps & clean supply options.

MIT Licensed.
## Quick Start (Colab or local)
```bash
pip install -r requirements.txt
streamlit run app.py   # interactive dashboard
