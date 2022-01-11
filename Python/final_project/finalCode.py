import pandas as pd
import matplotlib.pyplot as plt


def newCovidCasesGraph():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    fig, ax1 = plt.subplots() #create subplot
    ax1.set_xlabel('date') #set x axis
    ax1.plot(US_data_New['Date'], US_data_New["New_cases"], color="tab:red") #plot the date vs new data
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red') #set y axis
    plt.title("US New COVID Cases per Day (Figure 1)") #create title 
    fig.autofmt_xdate() #rotate date on x-axis
    fig.tight_layout() 
    plt.show()
#newCovidCasesGraph()

#Get Max COVID Case # and its date
def maxCaseDay():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    maxCases = US_data_New["New_cases"].max()
    maxIndex = US_data_New["New_cases"].idxmax()
    
    return US_data_New.loc[[maxIndex]]
print(maxCaseDay())
    
def getRate(lst):
    newLst = []
    for i in range(len(lst)):
        newLst.append((lst[i]/lst[0]-1)*100) #calculate percent change from intital 
    return newLst

#Plots Daily COVID cases vs. the rate of change of all Indexes from Jan 2020
def allStocks():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    
    sp500_data = pd.read_csv('SP500.csv') #pull in SP500 Data
    sp500_valid = sp500_data[sp500_data['SP500'] != '.'] #take out data where the market is closed indicated by "." in the data set
    sp500_valid["DATE"]=pd.to_datetime(sp500_valid.DATE) #covert to pythons datetime format
    sp500_valid["SP500"]=pd.to_numeric(sp500_valid.SP500) #convert string to integer 
    #print(sp500_valid.head())
    
    djia_data = pd.read_csv('DJIA.csv') #pull in DJIA Data
    djia_valid = djia_data[djia_data['DJIA'] != '.'] #take out data where the market is closed indicated by "." in the data set
    djia_valid["DATE"]=pd.to_datetime(djia_valid.DATE) #covert to pythons datetime format
    djia_valid["DJIA"]=pd.to_numeric(djia_valid.DJIA) #convert string to integer
    #print(djia_valid.head())
    
    rut_data = pd.read_csv('^RUT.csv') #pull in Russell 2000 Date
    rut_data["Date"]=pd.to_datetime(rut_data.Date) #covert to pythons datetime format
    rut_data["Close"]=pd.to_numeric(rut_data.Close) #convert string to integer
    rut_data_New = rut_data[["Date", 'Close']] #only include these 2 columns
    #print(rut_data_New.head())
    
    nasdaq_data = pd.read_csv('NASDAQCOM.csv') #pull in NASDAQ Data
    nasdaq_valid = nasdaq_data[nasdaq_data['NASDAQCOM'] != '.'] #take out data where the market is closed indicated by "." in the data set
    nasdaq_valid["DATE"]=pd.to_datetime(nasdaq_valid.DATE) #covert to pythons datetime format
    nasdaq_valid["NASDAQCOM"]=pd.to_numeric(nasdaq_valid.NASDAQCOM) #convert string to integer
    #print(nasdaq_valid.head())
    
    mergedData = sp500_valid.merge(US_data_New,left_on='DATE', right_on='Date') #merge SP500 and US covid data on date
    mergedData2 = djia_valid.merge(US_data_New,left_on='DATE', right_on='Date') #merge DJIA and US covid data on date
    mergedData3 = rut_data.merge(US_data_New,left_on='Date', right_on='Date') #merge Russell 2000 and US covid data on date
    mergedData4 = nasdaq_valid.merge(US_data_New,left_on='DATE', right_on='Date')
    
    y_sp500 = getRate(mergedData["SP500"].values.tolist()) #pull the sp500 close to list format
    y_djia = getRate(mergedData2["DJIA"].values.tolist()) #pull the djia close to list format
    y_rut = getRate(mergedData3["Close"].values.tolist())
    y_nasdaq = getRate(mergedData4["NASDAQCOM"].values.tolist())
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData["Date"],mergedData["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases Compared to Indexes Percent Change from Jan 2020 (Figure 2.1)")

    #create subplot of sp500, djia, russell, and nasdaq data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Percent Change from Jan 2020(%)')
    ax2.plot(mergedData["Date"], y_sp500, label = "S&P 500 Close", color='blue')
    ax2.plot(mergedData2["Date"], y_djia, label = "DJIA Close", color='green')
    ax2.plot(mergedData3["Date"], y_rut, label = "RUT2000 Close", color='purple')
    ax2.plot(mergedData4["Date"], y_nasdaq, label = "NASDAQCOM Close", color='orange')
    ax2.tick_params(axis='y')

    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()
#allStocks()    

#Plots Daily COVID cases vs. SP500 close
def sp500():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    
    sp500_data = pd.read_csv('SP500.csv') #pull in SP500 Data
    sp500_valid = sp500_data[sp500_data['SP500'] != '.'] #take out data where the market is closed indicated by "." in the data set
    sp500_valid["DATE"]=pd.to_datetime(sp500_valid.DATE) #covert to pythons datetime format
    sp500_valid["SP500"]=pd.to_numeric(sp500_valid.SP500) #convert string to integer 
    #print(sp500_valid.head())
    
    mergedData = sp500_valid.merge(US_data_New,left_on='DATE', right_on='Date') #merge SP500 and US covid
    
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData["Date"],mergedData["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases Compared to SP500 Close Price Daily (Figure 2.2)")
    
    #create subplot of sp500 data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Close Price', color='blue')
    ax2.plot(mergedData["Date"], mergedData["SP500"], label = "S&P 500 Close", color='blue')
    
    ax2.tick_params(axis='y', labelcolor='blue')

    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()
#sp500()

#Plots Daily COVID cases vs. DJIA close
def djia():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    
    djia_data = pd.read_csv('DJIA.csv') #pull in DJIA Data
    djia_valid = djia_data[djia_data['DJIA'] != '.'] #take out data where the market is closed indicated by "." in the data set
    djia_valid["DATE"]=pd.to_datetime(djia_valid.DATE) #covert to pythons datetime format
    djia_valid["DJIA"]=pd.to_numeric(djia_valid.DJIA) #convert string to integer
    #print(djia_valid.head())
    
    mergedData2 = djia_valid.merge(US_data_New,left_on='DATE', right_on='Date') #merge DJIA and US covid data on date
    
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData2["Date"],mergedData2["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases Compared to DJIA Close Price Daily (Figure 2.3)")

    #create subplot of djia data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Close Price', color = 'green')
    ax2.plot(mergedData2["Date"], mergedData2["DJIA"], label = "DJIA Close", color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()   
#djia()
    
#Plots Daily COVID cases vs. Russell close
def rut():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    
    rut_data = pd.read_csv('^RUT.csv') #pull in Russell 2000 Date
    rut_data["Date"]=pd.to_datetime(rut_data.Date) #covert to pythons datetime format
    rut_data["Close"]=pd.to_numeric(rut_data.Close) #convert string to integer
    rut_data_New = rut_data[["Date", 'Close']] #only include these 2 columns
    #print(rut_data_New.head())

    mergedData3 = rut_data.merge(US_data_New,left_on='Date', right_on='Date') #merge Russell 2000 and US covid data on date
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData3["Date"],mergedData3["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases Compared to Russell 2000 Closing Price Daily (Figure 2.4)")

    #create subplot of russell data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Close Price', color="purple")
    ax2.plot(mergedData3["Date"], mergedData3["Close"], label = "RUT2000 Close", color='purple')
    ax2.tick_params(axis='y', color="purple")

    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()
#rut()   

#Plots Daily COVID cases vs. Nasdaq close
def nasdaq():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    
    nasdaq_data = pd.read_csv('NASDAQCOM.csv') #pull in NASDAQ Data
    nasdaq_valid = nasdaq_data[nasdaq_data['NASDAQCOM'] != '.'] #take out data where the market is closed indicated by "." in the data set
    nasdaq_valid["DATE"]=pd.to_datetime(nasdaq_valid.DATE) #covert to pythons datetime format
    nasdaq_valid["NASDAQCOM"]=pd.to_numeric(nasdaq_valid.NASDAQCOM) #convert string to integer
    #print(nasdaq_valid.head())
    
    mergedData4 = nasdaq_valid.merge(US_data_New,left_on='DATE', right_on='Date')
    
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData4["Date"],mergedData4["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases Compared to NASDAQ Price Daily (Figure 2.5)")

    #create subplot of sp500, djia, russell, and nasdaq data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Close Price', color='orange')
    ax2.plot(mergedData4["Date"], mergedData4["NASDAQCOM"], label = "NASDAQCOM Close", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()
#nasdaq()    
    
# Plots monthly unemployment rate (as a scatter plot) and new daily COVID cases (line) on the same x-axis and differetly scaled y-axis    
def unemploy():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    #print(US_data_New.head())
    
    unemp_data = pd.read_csv('UNRATE.csv') #pull in unemployment Data
    unemp_data["DATE"]=pd.to_datetime(unemp_data.DATE) #covert to pythons datetime format
    unemp_data["UNRATE"]=pd.to_numeric(unemp_data.UNRATE) #convert string to integer
    #print(unemp_data.head())
    
    mergedData5 = unemp_data.merge(US_data_New, how='right', left_on='DATE', right_on='Date') #merge right to keep all of the daily cases
    #print(mergedData3)
    
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData5["Date"],mergedData5["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases Compared to Unemployment Rate (Figure 3)")

    #create subplot of unemp data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Unemployment Rate (percent)', color = 'tab:olive')
    ax2.scatter(mergedData5["Date"], mergedData5["UNRATE"], label = "Unemployment Rate Monthly", color='tab:olive') #scaatter plot bc points are missing as it is monthly
    ax2.tick_params(axis='y', labelcolor='tab:olive')
    
    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()
    
#unemploy()
    
#get unemployment percent for the dates listed
def getUnemployAtMonth():
    unemp_data = pd.read_csv('UNRATE.csv') #pull in unemployment Data
    unemp_data["DATE"]=pd.to_datetime(unemp_data.DATE) #covert to pythons datetime format
    unemp_data["UNRATE"]=pd.to_numeric(unemp_data.UNRATE) #convert string to integer
    get_df=unemp_data[unemp_data["DATE"] == "2020-03-1"]
    get_df2=unemp_data[unemp_data["DATE"] == "2021-05-1"]
    return  get_df, get_df2
print(getUnemployAtMonth())

#get max unemployment rate in data
def getHighestUnemp():
    unemp_data = pd.read_csv('UNRATE.csv') #pull in unemployment Data
    unemp_data["DATE"]=pd.to_datetime(unemp_data.DATE) #covert to pythons datetime format
    unemp_data["UNRATE"]=pd.to_numeric(unemp_data.UNRATE) #convert string to integer
    maxRate = unemp_data["UNRATE"].max()
    maxIndex = unemp_data["UNRATE"].idxmax()
    return unemp_data.loc[[maxIndex]]
print(getHighestUnemp())

    
# Plots US New COVID Cases vs New US Vaccinations Daily on the same x-axis, and differently scaled y-axises
def vaccinations():
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv') #pull in COVID data from WHO
    US_data = covid_data[covid_data['Country_code'] == 'US'] #filter for US data
    US_data["Date"]=pd.to_datetime(US_data.Date) #covert to pythons datetime format
    US_data_New = US_data[["Date", 'New_cases']] #only include these 2 columns
    
    vaccine_data = pd.read_csv('owid-covid-data.csv') #pull in vaccination data from our world in data
    print(vaccine_data.head())
    USV_data = vaccine_data[vaccine_data['location'] == 'United States'] #filter for US data
    USV_data["date"]=pd.to_datetime(USV_data.date) #covert to pythons datetime format
    USV_data_New = USV_data[["date", 'new_vaccinations']] #only include these 2 columns

    mergedData5 = USV_data_New.merge(US_data_New,left_on='date', right_on='Date')
    print(mergedData5)

    fig, ax1 = plt.subplots()
    
    ax1.set_xlabel('date')
    ax1.set_ylabel('US New Daily COVID Cases', color='tab:red')
    ax1.plot(mergedData5["Date"],mergedData5["New_cases"], label = "New COVID Cases", color='tab:red')
    ax1.tick_params(axis='y', labelcolor= 'tab:red')
    plt.title("US New COVID Cases vs New US Vaccinations Daily (Figure 4)")
    
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('New Vaccinations in US per Day', color='tab:blue')
    ax2.plot(mergedData5["Date"], mergedData5["new_vaccinations"], label = "New Vaccinations", color='tab:blue')
    ax2.tick_params(axis='y', labelcolor='tab:blue')

    #create legends for both line graphs (bc matplotlib is annoying)
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines = lines_1 + lines_2
    labels = labels_1 + labels_2
    ax1.legend(lines, labels, loc=0)
    
    #format axises
    fig.tight_layout()
    fig.autofmt_xdate()
    plt.show()
#vaccinations()  
    
    
# Plots all search trends for various topics on the same graph
def trends():
    trends_data = pd.read_csv('multiTimeline.csv') #pull in unemployment Data
    trends_data["Week"]=pd.to_datetime(trends_data.Week) #covert to pythons datetime format
    trends_data = trends_data.replace(to_replace="<1", value="0") #make "<1" equal to 0 bc otherwise it cannot be handeled 
    trends_data["Coronavirus"]=pd.to_numeric(trends_data.Coronavirus) #convert string to integer
    trends_data["Music"]=pd.to_numeric(trends_data.Music)
    trends_data["Sports"]=pd.to_numeric(trends_data.Sports)
    trends_data["Weather"]=pd.to_numeric(trends_data.Weather)
    trends_data = trends_data[trends_data['Vaccine'] != '<1'] #filter for US data
    trends_data["Vaccine"]=pd.to_numeric(trends_data.Vaccine)
    #print(trends_data.head())
    
    #plot dates, vs music, covid, sports, vaccine, and music search interest
    plt.plot(trends_data["Week"], trends_data["Coronavirus"], color="tab:cyan", label="Searches for Topic Coronavirus")
    plt.plot(trends_data["Week"], trends_data["Music"], color="m", label="Searches for Topic Music")
    plt.plot(trends_data["Week"], trends_data["Sports"], color="tab:gray", label="Searches for Topic Sports")
    plt.plot(trends_data["Week"], trends_data["Weather"], color="black", label="Searches for Topic Weather")
    plt.plot(trends_data["Week"], trends_data["Vaccine"], color="palegreen", label="Searches for Topic Vaccine")
    plt.title("Search Trends for Popular topics vs COVID and Vaccine (Figure 5)")
    plt.ylabel("Search Interest (relative to the highest point)")
    plt.xlabel("date")
    
    plt.legend()
    plt.show()   
#trends()    