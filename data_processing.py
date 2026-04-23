

import yfinance as yf
import pandas as pd

stocks = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS",
    "ICICIBANK.NS", "HINDUNILVR.NS", "SBIN.NS",
    "KOTAKBANK.NS", "LT.NS", "AXISBANK.NS"
]

all_data = []

for stock in stocks:
    
    data = yf.download(stock, start="2017-01-01", end="2024-01-01")
    

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    
    data.reset_index(inplace=True)
    
    data['Stock'] = stock
    
    data = data[['Date', 'Stock', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    all_data.append(data)

final_df = pd.concat(all_data, ignore_index=True)

final_df.to_csv("stock_data_clean.csv", index=False)

print("Clean dataset created successfully")



import pandas as pd

df = pd.read_csv("stock_data_clean.csv")

print(df.head())     # first 5 rows
print(df.tail())     # last 5 rows
print(df.shape)      # rows & columns
print(df.columns)    # column names



import pandas as pd

df = pd.read_csv("stock_data_clean.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by=['Stock', 'Date'])

df['Daily Return'] = df.groupby('Stock')['Close'].pct_change()

df['MA_10'] = df.groupby('Stock')['Close'].transform(lambda x: x.rolling(10).mean())
df['MA_50'] = df.groupby('Stock')['Close'].transform(lambda x: x.rolling(50).mean())

df['Volatility'] = df.groupby('Stock')['Daily Return'].transform(lambda x: x.rolling(10).std())

def risk_category(vol):
    if pd.isna(vol):
        return "No Data"
    elif vol < 0.01:
        return "Low Risk"
    elif vol < 0.02:
        return "Medium Risk"
    else:
        return "High Risk"

df['Risk Category'] = df['Volatility'].apply(risk_category)

df.to_csv("stock_data_final.csv", index=False)

print("Feature engineering completed")
print(df.head())



import pandas as pd

df = pd.read_csv("stock_data_final.csv")

df['Date'] = pd.to_datetime(df['Date'])

total_return = df.groupby('Stock')['Close'].apply(
    lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0]
)


avg_return = df.groupby('Stock')['Daily Return'].mean()


risk = df.groupby('Stock')['Daily Return'].std()

sharpe_ratio = avg_return / risk

portfolio_df = pd.DataFrame({
    'Total Return': total_return,
    'Average Return': avg_return,
    'Risk (Volatility)': risk,
    'Sharpe Ratio': sharpe_ratio
})


portfolio_df = portfolio_df.reset_index()


portfolio_df.to_csv("portfolio_summary.csv", index=False)

print("Portfolio analysis completed")
print(portfolio_df)


df = pd.read_csv("stock_data_final.csv")
print(df.columns) 

df = pd.read_csv("portfolio_summary.csv")
print(df.columns)