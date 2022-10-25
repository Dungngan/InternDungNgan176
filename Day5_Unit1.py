import requests
from lxml import html
from bs4 import BeautifulSoup
import re
import openpyxl
import datetime
import csv
import pandas as pd

url = 'https://www.us-cert.gov/ncas/alerts'

def parserHtml (url):
    res=requests.get(url)
    try:
        res.raise_for_status()
    except:
        print('Error url')
    soup =BeautifulSoup(res.text,'html.parser')
    return soup

regexId =re.compile(r'Alert \((.*)\)')
regexRelease1 =re.compile(r'Original release date: (.*)')
regexRelease3 =re.compile(r'Original release date: ([^|]*)')
regexRevised  =re.compile(r': (.*)')

pageTag = parserHtml(url).select('.date-listing')
tag = pageTag[0].select('a')[0].get('href')
year = pageTag[0].select('a')[0].getText()

alertTag = parserHtml(url).select('.views-field.views-field-title')

alertLink_list = []
idAlert_list = []
alertName_list = []
releaseDate_list = []
lastRevised_list = []

for tag in range(len(alertTag)):
    alertLink = 'https://www.cisa.gov/uscert' + alertTag[tag].select('a')[0].get('href')  # getlink aleart
    alertLink_list.append(alertLink)

    mySoup1 = parserHtml(alertLink)

    alertId = mySoup1.select('#page-title')
    ID_alert = regexId.search(alertId[0].getText()).group(1)  # value id
    idAlert_list.append(ID_alert)

    alertName = mySoup1.select('#page-sub-title')
    name = alertName[0].getText()  # value name
    alertName_list.append(name)

    releaseDate = mySoup1.select('.submitted.meta-text')

    dateString = releaseDate[0].contents
    lenS = len(dateString)
    if lenS == 1:  # string date same :'Original release date: June 07, 2022'
        releaseDate1 = regexRelease1.search(releaseDate[0].getText().strip()).group(1)
        lastRevised1 = releaseDate1
        # Done
    else:  # string date same:'Original release date: June 07, 2022 | Last revised: June 10, 2022'
        releaseDate1 = regexRelease3.search(releaseDate[0].getText().strip()).group(1)
        lastRevised1 = regexRevised.search(dateString[2].strip()).group(1)
    lastRevised_list.append(lastRevised1)
    releaseDate_list.append(releaseDate1)

df=pd.DataFrame(list(zip(idAlert_list,alertName_list,releaseDate_list,lastRevised_list,alertLink_list)),columns=['Id','Name','Release Date','Last Revised','Link'])
df
df.to_csv("lesson5_write.csv")