# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:12:48 2020

@author: jvan1
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
def get_HTML(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

def extract_line(header,soup):
    return re.findall('%s: +(.*)' %(header),soup.get_text())[0]

def save_info(soup,df=pd.DataFrame()):
    name = extract_line('Name',soup)
    purpose = extract_line('Purpose',soup)
    return df.append(pd.Series({'Name':name,'Purpose':purpose}),ignore_index=True)



if __name__ == '__main__':
    url = 'http://18.207.92.139:8000/random_company'
    output = pd.DataFrame()
    for i in range(50):
        soup = get_HTML(url)
        output = save_info(soup,df=output)
    output.to_csv('ListOfCompanies JVansant.csv')