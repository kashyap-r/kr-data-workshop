# ============================================================
# Download NASDAQ-100 Historical Daily Data from Yahoo Finance
# ============================================================

# Install required packages (run once)
# pip install yfinance pandas tqdm

import pandas as pd
import yfinance as yf
from pathlib import Path
from tqdm import tqdm
import time
import os

# ------------------------------------------------------------
# CONFIGURATION
# ------------------------------------------------------------

# Get the current script's directory
# BASE_DIR = Path(__file__).resolve().parent.parent  # goes up from src/market-analysis to project root

try:
    BASE_DIR = Path(__file__).resolve().parent.parent
except NameError:
    # fallback if __file__ is not defined (e.g. Jupyter)
    BASE_DIR = Path.cwd()

# Define input/output paths relative to project root
INPUT_DIR = BASE_DIR / "data" / "input"
OUTPUT_DIR = BASE_DIR / "data" / "output"


CSV_FILE = "NASDAQ 100 Symbols.csv"   # Input CSV file
OUTPUT_DIR = "nasdaq100_data"         # Folder to save stock data
START_DATE = "2015-01-01"             # Historical data start date
END_DATE = None                       # None = today's date

# ------------------------------------------------------------
# CREATE OUTPUT DIRECTORY
# ------------------------------------------------------------

Path(OUTPUT_DIR).mkdir(exist_ok=True)

# ------------------------------------------------------------
# LOAD SYMBOLS
# ------------------------------------------------------------

df = pd.read_csv(CSV_FILE)

# Assumes the CSV has a column named 'Symbol'
# Change column name below if needed
symbols = df['Symbol'].dropna().unique().tolist()

print(f"Total symbols found: {len(symbols)}")

# ------------------------------------------------------------
# DOWNLOAD DATA
# ------------------------------------------------------------

failed_symbols = []

for symbol in tqdm(symbols):

    try:
        print(f"\nDownloading: {symbol}")

        # Download historical daily OHLCV data
        stock_data = yf.download(
            tickers=symbol,
            start=START_DATE,
            end=END_DATE,
            interval="1d",
            auto_adjust=True,
            progress=False,
            threads=False
        )

        # Skip empty data
        if stock_data.empty:
            print(f"No data found for {symbol}")
            failed_symbols.append(symbol)
            continue

        # Reset index to make Date a column
        stock_data.reset_index(inplace=True)

        # Save to CSV
        output_file = f"{OUTPUT_DIR}/{symbol}.csv"
        stock_data.to_csv(output_file, index=False)

        print(f"Saved: {output_file}")

        # Small delay to avoid rate limits
        time.sleep(0.5)

    except Exception as e:
        print(f"Failed for {symbol}: {e}")
        failed_symbols.append(symbol)

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

print("\n======================")
print("DOWNLOAD COMPLETE")
print("======================")

print(f"Successful: {len(symbols) - len(failed_symbols)}")
print(f"Failed: {len(failed_symbols)}")

if failed_symbols:
    print("\nFailed Symbols:")
    print(failed_symbols)