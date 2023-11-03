# Import these modules for webscraping
from bs4 import BeautifulSoup
import requests

# create a variable called (url = ) and a variable called (page = )
#using BeautifulSoup, parse the html text from the particular website
#create a variable (table = ) and using soup module find the table information
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
table = (soup.find_all('table')[1])

world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

#Import pandas modules for data analysis and storing the data in a pandas Data Frame
import pandas as pd
df = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data

df.to_csv(r'C:\Users\varma\Desktop\misc_files\companies.csv', index = False)


