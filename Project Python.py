import matplotlib.pyplot as plt
import pandas
import yfinance as yf
gamestop= yf.Ticker("GME")
data_gamestop = gamestop.history(period="MAX")
data_gamestop.reset_index(inplace=True)
data_gamestop = data_gamestop.head()
print(data_gamestop)
x = data_gamestop["Date"]
y = data_gamestop["Open"]
plt.plot(x,y)
plt.show()




