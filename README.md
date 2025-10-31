# TradingBot  
A Python-based trading automation framework leveraging news sentiment & technical signals.

## 🚀 Overview  
This tool allows you to build an automated trading workflow that:  
- ingests news sentiment (via a module like `finbert_utils.py`)  
- generates buy / sell decisions (via `buy_or_sell.py`)  
- executes / simulates trades (via `tradingbot.py`)  
- uses configuration through environment variables (`.env.example`) for API keys, broker credentials, and trading parameters  

It’s designed as a starting point for quant/swing-traders who want to combine textual sentiment (news) with technical triggers.

## 📁 Project Structure  
```
├─ .env.example             # sample environment variables file  
├─ buy_or_sell.py           # logic to decide buy vs sell based on sentiment & signal  
├─ finbert_utils.py         # helper functions for news sentiment analysis (e.g., FinBERT)  
├─ tradingbot.py            # main bot engine: connects to broker/API, places or simulates trades  
├─ README.md                # project documentation (you’re here)  
└─ .gitignore               
```

## 🧰 Key Components  
- **Environment Config**: via `.env` (copy from `.env.example`) you’ll configure your broker API keys, news-API keys, trading account settings, risk parameters.  
- **News Sentiment Module** (`finbert_utils.py`): fetches and processes textual news items; computes sentiment scores that feed into decision logic.  
- **Decision Logic** (`buy_or_sell.py`): given sentiment + technical indicators, outputs recommendations (buy, hold, sell).  
- **Bot Engine** (`tradingbot.py`): orchestrates the end-to-end cycle: fetch data → compute signals → decide → place trade or simulate; supports backtesting or live trading paths.

## 📝 Getting Started  
1. Clone the repo:  
   ```bash
   git clone https://github.com/sohan-shingade/TradingBot.git
   cd TradingBot
   ```  
2. Install dependencies (adjust for your environment, e.g., `pip install -r requirements.txt`).  
3. Copy and configure your environment variables:  
   ```bash
   cp .env.example .env  
   # then edit .env to set your API keys, broker credentials, risk parameters etc.
   ```  
4. Configure your trading parameters (e.g., target tickers, timeframe, stop-loss / take-profit thresholds) inside the bot or via config variables.  
5. Run in simulation/backtest mode first:  
   ```bash
   python tradingbot.py --mode backtest --ticker XYZ  
   ```  
   Then when comfortable, switch to live or paper trading mode:  
   ```bash
   python tradingbot.py --mode live --ticker XYZ  
   ```  

## ✅ Features  
- Combines **textual sentiment** (news) with **technical signals** for decision-making  
- Modular design makes it easy to swap in your own sentiment model or broker API  
- Environment variable driven: keeps credentials/config outside code  
- Supports backtest → live transition workflow  

## ⚠️ Important Notes & Caveats  
- **This is not financial advice.** Use this bot at your own risk. The markets carry losses.  
- Make sure to **paper-trade** thoroughly before going live — historical backtests do not guarantee future performance.  
- Ensure your broker API and trading account permissions are configured correctly (e.g., margin, leverage, risk limits).  
- News sentiment models (like FinBERT) can have biases; treat any output as one signal among many.  
- Monitor for exceptions / slippage / connectivity issues in live mode.

## 🔧 Customization Ideas  
- Plug in **your own sentiment source**: Twitter, Reddit, RSS feeds, earnings transcripts.  
- Add **industry-specific news categories**, macro news, or event detection (earnings, Fed announcements).  
- Enhance the decision logic with **swing-trading rules** (e.g., your Bollinger Band squeeze + MACD histogram exit rules).  
- Integrate **risk management** modules: position sizing, stop-losses, dynamic exposure based on volatility.  
- Use your knowledge of swing trading to extend the bot beyond intraday setups (you’ve indicated you prefer swing trades).  
- Connect to your preferred broker’s API (you mentioned the use of `ibapi` for IB KR) if migrating away from generic brokers.

## 🧠 Why This Approach?  
You’re combining *qualitative* signals (news sentiment) with *quantitative/technical* triggers — which is aligned with modern **quantamental** strategy thinking. Given your interest in swing-trading and conditional inputs (news + industry + macro), this architecture offers a scaffold to integrate all of those layers.

## 📚 Next Steps & Enhancements  
- Expand the news-conditioning scope: ticker-specific news, industry-level and macro-level (interest rates, employment data).  
- Introduce **news revision detection logic** (you’ve researched BLS jobs report revisions) and feed that into signal generation.  
- Add **post-earnings drift (PEAD)** module, focusing on companies with low analyst coverage, to align with your research interest.  
- Incorporate performance metrics tracking: Sharpe ratio, drawdown, win-rate, expectancy, to evaluate your swing strategy with this bot.  
- Set up **logging**, **alerting**, **dashboarding** (e.g., via Power BI / Tableau or a simple web UI) so you can monitor bot health and trading performance.

## 📄 License  
Specify your license here (e.g., MIT, Apache 2.0) — if none exists, consider adding one so others know how they may reuse the code.
