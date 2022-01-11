import pandas as pd
import matplotlib.pyplot as plt

def getRate(lst):
    newLst = []
    for i in range(len(lst)):
        newLst.append((lst[i]/lst[0]-1)*100) #calculate percent change from intital 
    return newLst

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
    plt.title("US New COVID Cases Compared to Index Closing Price Daily (Figure 2.1)")

    #create subplot of sp500, djia, russell, and nasdaq data
    ax2 = ax1.twinx() #same x-axis, different y-axis
    ax2.set_ylabel('Close Price')
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
allStocks()