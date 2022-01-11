import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
dates = ["01/02/2020", "01/03/2020", "01/04/2020"]
x_values = [dt.datetime.strptime(d,"%m/%d/%Y").date() for d in dates]
print(x_values)
y_values = [1, 2, 3]

ax1 = plt.gca()
formatter = mdates.DateFormatter("%Y-%m-%d")

ax1.xaxis.set_major_formatter(formatter)

locator = mdates.DayLocator()

ax1.xaxis.set_major_locator(locator)
plt.plot(x_values, y_values)
plt.show()