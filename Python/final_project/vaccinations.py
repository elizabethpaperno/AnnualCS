import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#import datetime as dt

covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
print(US_data_New)
vaccine_data = pd.read_csv('owid-covid-data.csv') #pull in vaccination data from our world in data
vaccine_data = vaccine_data[vaccine_data['new_vaccinations'] != '']
USV_data = vaccine_data[vaccine_data['location'] == 'United States'] #filter for US data
USV_data["date"]=pd.to_datetime(USV_data.date) #covert to pythons datetime format
USV_data_New = USV_data[["date", 'new_vaccinations']] #only include these 2 columns

mergedData = USV_data_New.merge(US_data_New,left_on='date', right_on='Date')

dates_list = mergedData['Date'].values.tolist()
x_values = dates_list
#mdates.date2num(dates_list)
new_cases = mergedData["New_cases"].values.tolist()
new_vaccinations = mergedData['new_vaccinations'].values.tolist()

fig, ax1 = plt.subplots()

ax1.set_xlabel('date')
ax1.set_ylabel('new covid cases per day', color='tab:red')
ax1.plot(mergedData['Date'], mergedData["New_cases"])
# ax1.plot(x_values, new_cases, label = "New COVID Cases per day", color='tab:red')
ax1.tick_params(axis='y', labelcolor= 'tab:red')

fmt_half_year = mdates.MonthLocator(interval=6)
fmt_month = mdates.MonthLocator()
ax1.xaxis.set_minor_locator(fmt_month)
ax1.xaxis.set_major_locator(fmt_half_year)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
#plt.plot(US_dates,US_cases)
ax1.xaxis.set_major_locator(mdates.MonthLocator())



ax2 = ax1.twinx() #same x-axis, different y-axis
ax2.set_ylabel('new covid vaccinations per day')
ax2.plot(mergedData['Date'], mergedData['new_vaccinations'], label = "New COVID Vaccinations per day", color='tab:red')
ax2.tick_params(axis='y', labelcolor= 'tab:red')
fig.tight_layout()

#create legends for both line graphs (bc matplotlib is annoying)
# lines_1, labels_1 = ax1.get_legend_handles_labels()
# lines_2, labels_2 = ax2.get_legend_handles_labels()
# lines = lines_1 + lines_2
# labels = labels_1 + labels_2

fig.autofmt_xdate()
# ax1.legend(lines, labels, loc=0)

#ax1.set_xticklabels(labels=mergedData['Date'].index, rotation=70, rotation_mode="anchor", ha="right");
#ax1.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

plt.show()