# 🧠 TradeBrain

**TradeBrain** is a deep learning-powered crypto and stock trading bot that uses LSTM models to forecast price movements and backtests strategies on historical data.

## 🚀 Features

- Fetch historical crypto/stock data
- LSTM-based price prediction
- Technical indicators (SMA, RSI, etc.)
- Backtesting of trading strategies
- Streamlit dashboard (coming soon)

## 🛠️ Tech Stack

- Python, pandas, NumPy
- TensorFlow/Keras (LSTM model)
- Backtrader (for strategy testing)
- Streamlit (dashboard UI)
- Matplotlib, Plotly (visualizations)

## 📁 Project Structure

```bash
src/
├── data_loader.py         # Download and cache data
├── preprocessing.py       # Data cleaning and indicators
├── lstm_model.py          # Deep learning model
├── backtest.py            # Strategy backtesting
└── utils.py               # Helper functions
