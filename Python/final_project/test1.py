import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

covid_data = pd.read_csv('WHO-COVID-19-global-data.csv')
#print(covid_data.head())
#print(covid_data["Country"]
dates = covid_data["Date"].tolist()
numCases = covid_data["Cumulative_cases"].tolist()
print(dates)
dates_list = []
US_data = covid_data[covid_data['Country_code'] == 'US']
US_cases = US_data["Cumulative_cases"].values.tolist()
print(US_data)

US_dates = US_data["Date"].values.tolist()
#print(covid_data.columns.values.tolist())

#dates_list = [dt.datetime.strptime(date,'%m/%d/%y').date() for date in dates]
dates_listUS = [dt.datetime.strptime(date,'%m/%d/%y').date() for date in US_dates]
x_values = mdates.date2num(dates_list)

fig, ax = plt.subplots()

#plt.plot(US_dates,US_cases)
ax.plot(dates_listUS, US_cases)
fmt_half_year = mdates.MonthLocator(interval=6)
fmt_month = mdates.MonthLocator()
ax.xaxis.set_minor_locator(fmt_month)
ax.xaxis.set_major_locator(fmt_half_year)

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
#plt.plot(US_dates,US_cases)
ax.xaxis.set_major_locator(mdates.MonthLocator())

fig.autofmt_xdate()
#plt.yscale(value, **kwargs)

plt.show()

# fig, ax = plt.subplots()
# ax.plot(dates_listUS, US_cases)

# # Make ticks on occurrences of each month:
# ax.xaxis.set_major_locator(mdates.MonthLocator())
# # Get only the month to show in the x-axis:
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
# # '%b' means month as locale’s abbreviated name
# plt.show()