
import datetime as dt
from turtle import color
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mpl_finance import candlestick2_ochl

#define timeframe
start = dt.datetime(2019,1,1)
end = dt.datetime(2020,2,2)

#load the data
FinanceData = web.DataReader('FB','yahoo',start,end)

print(FinanceData)

#Restructure Data

FinanceData = FinanceData[['Open','High','Low','Close']]
FinanceData.reset_index(inplace=True)
FinanceData['Date'] = FinanceData['Date'].map(mdates.date2num)

print(FinanceData.head())

#Plotting the data

ax = plt.subplot()
ax.grid(True)
ax.set_axisbelow(True)
ax.set_title('Facebook Share Price',color='white')
ax.set_facecolor('black')
ax.figure.set_facecolor('#121212')
ax.tick_params(axis='x',colors='white')
ax.tick_params(axis='y',colors='white')

ax.xaxis_date()



candlestick2_ochl(ax, FinanceData.Open,FinanceData.Close,FinanceData.High,FinanceData.Close, width=0.5,colorup='#00ff00')
plt.show()