# 🪙 SG Coin Tracker
**Market Intelligence Module | Powered by CoinGecko API**
A streamlined Python utility developed for real-time tracking of high-cap digital assets and strategic holdings. This tool is optimized for low-resource environments like **Termux**, providing a clean, terminal-based alternative to heavy web-based dashboards.

### 🛠️ Technical Architecture
The script interacts with the **CoinGecko V3 REST API** to pull live valuation data.
 * **Endpoint:** /simple/price
 * **Data Format:** JSON (JavaScript Object Notation)
 * **Integration:** Utilizes the requests library for secure HTTP handshake and data retrieval.
### 📋 Monitored Assets
The tracker is currently configured to monitor a diversified watchlist, including:
 * **Layer 1s:** Bitcoin (BTC), Ethereum (ETH), Solana (SOL), Cardano (ADA)
 * **Infrastructure:** Chainlink (LINK), Kaspa (KAS), Render (RNDR)
 * **Emerging/Utility:** Hedera (HBAR), Ripple (XRP), Qubic (QUBIC), and others.
### 🚀 Setup & Usage
**1. Install Dependencies**
Ensure you have the requests library installed in your Python environment:
```bash
pip install requests

```
**2. Execution**
Run the tracker directly from your terminal:
```bash
python sg_coin_tracker.py

```
### 🛡️ About the Developer
Maintained by **sgeorge83** as part of a personal financial sovereignty and technical automation portfolio. This project demonstrates practical applications of Python in market data analysis and API integration.
> **Note:** This tool is for informational purposes. Market data is fetched from public endpoints and should be used as a reference for personal hobbyist tracking.
