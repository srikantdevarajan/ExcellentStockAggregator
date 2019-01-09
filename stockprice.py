from yahoo_fin.stock_info import *
import csv
import datetime
import pandas as pd

Tickerstoget = []
with open('tickers.txt', 'r') as myFile:
    for line in myFile:
        lineInfo = line.strip()
        Tickerstoget.append(lineInfo)
counter = 0

isEmpty=True
csv_file=open('Stock_Tickers_From_Yahoo.csv', mode='a', newline='')
fieldnames = [ 'Todays Date','Ticker Symbol','1y Target Est', '52 Week Range', 'Ask','Volume','Beta (3Y Monthly)','Bid',"Day's Range",'EPS (TTM)','Earnings Date','Ex-Dividend Date','Forward Dividend & Yield','Market Cap','Open','PE Ratio (TTM)','Previous Close','Quote Price']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
try:
    df= pd.read_csv('Stock_Tickers_From_Yahoo.csv')
    print(df.empty)
except:
    writer.writeheader()
            

print(datetime.datetime.today().strftime('%Y-%m-%d'))
writer.writerow({fieldnames[0]:datetime.datetime.today().strftime('%Y-%m-%d')})

while counter < len(Tickerstoget):
	
    m1yTGTEST = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[2])
    yearRange = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[3])
    askValue = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[4])
    volume = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[5])
    BetaValue = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[6])
    bidValue = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[7])
    dayRange = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[8])
    epsTTM = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[9])
    earningsDate = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[10])
    exDivDate = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[11])
    forwardDiv = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[12])
    marketCap = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[13])
    openValue = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[14])
    peRatio = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[15])
    PreviousClose = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[16])
    closePrice = get_quote_table(Tickerstoget[counter], dict_result=True).get(fieldnames[17])
    tickercurrent = Tickerstoget[counter]
    writer.writerow({fieldnames[1]:tickercurrent,fieldnames[2]:m1yTGTEST,fieldnames[3]:yearRange,fieldnames[4]:askValue,fieldnames[5]:volume
    ,fieldnames[6]:BetaValue,fieldnames[7]:bidValue,fieldnames[8]:dayRange,fieldnames[9]:epsTTM,fieldnames[10]:earningsDate,fieldnames[11]:exDivDate,fieldnames[12]:forwardDiv,
    fieldnames[13]:marketCap,fieldnames[14]:openValue,fieldnames[15]:peRatio,fieldnames[16]:PreviousClose,fieldnames[17]:closePrice})
    counter += 1
csv_file.close()
