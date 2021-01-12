import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

print(msft.major_holders)