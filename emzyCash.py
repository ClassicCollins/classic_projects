import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from matplotlib import pyplot as plt

st.write("""
# EmzyCash
This is an investment platform that fascinates your interest on investment on financial asset such as stocks, bonds, 
options, forex & cryptos. This app is designed basically for stock investment.
\
I know you will like to invest in stock, sure everybody does but knowing the right stock and when to buy can be very 
tasking.That's why we created this platform to hold you by the hands and walk your though the rough road of investment.
Fell free to contact us at **ugwuozorcollinsemezie@gmail.com**
\
If you are still in doubt,not sure if stock is the right investment for you.Never worry, we do our best to clear
your worry.Well, it depends on a lot of factors
\
1. **Your risk appetite:** stock is less risky asset than crypto but more risky than bond. However,you should 
understand the higher the risk of loosing your investment, the higher the chances of doubling your investment.
\
2. **Your Age:** when you are young, we suggest 90% of your investment fund in stocks is good, and 10% in bonds. Crypto 
may come in depending on your risk appetite. As you approach retirement, increase your allocation to bonds.
\
3. **Timing:** we observed many people invest during bull markets (when stock market is booming) and sell during 
crashes(bearish market). Avoid this mistake. Buy when the market is low and sell when the market is high.The great thing
with getting the timing right is that you can benefit from market crashes. We also encourage investing on the side for 
long-term growth.
\
4. **Picking the right stock:** This is where you need professional services. Both fundamental and technical analysis
need to be carried out. There are a lot of other factors which can not be discussed in details here. 
feel free to connect with us **ugwuozorcollinsemezie@gmail.com** or whatsapp **+2348180094419**
\
I now invite you to check out our demo what is would be if you had invested in any of the company of your choice in the 
time past.
\
Enter a **ticker symbol** of any of the stock you want to examine in the text box. eg. GOOGL for Google, TSLA for Tesla, 
AAPL for Apple, etc. Use the slider to choose a **time interval** type the amount of time back from today that you
want to observe.
""")

timeChoices = {'Daily':['Days',365,'1d'],'Weekly':['Weeks',104,'1wk'],'Monthly':['Months',60,'1mo'],'Quarterly':['Quarters',48,'3mo']}
timeDf = pd.DataFrame(timeChoices)

# This takes input from the user on which stock ticker that they would like to look at and gives a sliding scale to choose how much data to look back at in months
tickerSymbol = st.text_input("Enter a ticker symbol: ", "TSLA")
timeChoiceSlider = st.select_slider("Choose the type of data you would like to pull: ", options=["Daily", "Weekly", "Monthly", "Quarterly"])
timeSlider = st.slider("Number of Previous %s" % timeDf[timeChoiceSlider][0], min_value=1, max_value = timeDf[timeChoiceSlider][1], value = timeDf[timeChoiceSlider][1], step = 1)

#Input ticker symbol sent to yfinance to get additional data long name of the company is pulled from the ticker
tickerData = yf.Ticker(tickerSymbol)

companyName = tickerData.info['longName']
if timeChoiceSlider == "Daily":
    days = timeSlider
    weeks = 0
    months = 0
elif timeChoiceSlider == "Weekly":
    days = 0
    weeks = timeSlider
    months = 0
elif timeChoiceSlider == "Monthly":
    days = 0
    weeks = 0
    months = timeSlider
else:
    days = 0
    weeks = 0
    months = timeSlider*3

#Pulling date from today for most updated info, and picks a starting date based on slider
endDay = date.today()
startDay = endDay - relativedelta(days=days, weeks = weeks, months = months)

#history data values pulled based on startDay, endDay and the ticker previously chosen.
tickerDf = tickerData.history(start=startDay, end=endDay, interval=timeDf[timeChoiceSlider][2])

st.write("""
Shown are the stock opening, closing, high, low, and volume on the day for %s.
""" % companyName)

#Open Price graphed
st.write("""
### Opening Price
""")
st.line_chart(tickerDf.Open)

#High Price graphed
st.write("""
### High Price
""")
st.line_chart(tickerDf.High)

#Low Price graphed
st.write("""
### Low Price
""")
st.line_chart(tickerDf.Low)

#Closing price graphed
st.write("""
### Closing Price
""")
st.line_chart(tickerDf.Close)

#Volume graphed
st.write("""
### Volume
""")
st.line_chart(tickerDf.Volume)

st.write("""
### Disclaimer:
*The best investment you can make with your money is to invest in yourself and in your knowledge. 
Make sure that you understand our disruptive future ahead before investing. We will not be liable for any lost in
investment*
""")


# tickerDF_greyed = tickerDf.Close[tickerDf.Date < startDay]

# #Close Price but using MatPlotLib
# fig, ax = plt.subplots()
# plt.plot(tickerDf.Close, color="green")
# plt.plot(tickerDF_greyed, color="blue")
# plt.title("Closing Prices for %s for the past %s months" % (tickerSymbol, monthsSlider))
# plt.xlabel("Closing Price")
# plt.ylabel("Time")
# ax.set_facecolor("gray")
# plt.grid(b=True, which='both',axis='both',c='blue')
# st.pyplot(fig)
# st.plotly_chart(fig)