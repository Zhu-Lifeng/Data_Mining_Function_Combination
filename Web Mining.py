# Opening HTML content
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
!pip3 install beautifulsoup4
!pip3 install lxml

url = "https://www.hubertiming.com/results/2017GPTR"
html = urlopen(url)

# Parsing HTML content
soup = BeautifulSoup(html, 'lxml')
#The soup object allows you to extract interesting information about the website we are scraping such as getting the title of the page or the text of the webpage
title = soup.title
text = soup.get_text()

soup.find_all('a')
# extract all the hyperlinks within the webpage

all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))
# extract and print out only hyperlinks

rows = soup.find_all('tr') 
# print out table rows only

for row in rows:
    row_td = row.find_all('td')  
    # the 'td' tag in html code denotes a table cell
str_cells = str(row_td)
cleantext = BeautifulSoup(str_cells, "lxml").get_text()
# extract the text without html tags

# Create an empty list where the table header will be stored
header_list = []

# Find the 'th' html tags which denote table header
col_labels = soup.find_all('th')
col_str = str(col_labels)
cleantext_header = BeautifulSoup(col_str, "lxml").get_text()  # extract the text without HTML tags
header_list.append(cleantext_header) # Add the clean table header to the list

# Create an empty list where the table will be stored
table_list = []

# For every row in the table, find each cell element and add it to the list
for row in rows:
    row_td = row.find_all('td')
    row_cells = str(row_td)
    row_cleantext = BeautifulSoup(row_cells, "lxml").get_text()  # extract the text without HTML tags
    table_list.append(row_cleantext)  # Add the clean table row to the list

df_header = pd.DataFrame(header_list)
df_header2 = df_header[0].str.split(',', expand=True) # split the "0" column into multiple columns at the comma position

df_table = pd.DataFrame(table_list)
df_table2 = df_table[0].str.split(',', expand=True)
# convert the table list into a pandas dataframe

# Remove uneccesary characters
df_table2[0] = df_table2[0].str.strip('[')
df_table2[0] = df_table2[0].str.strip(']')
df_table2[1] = df_table2[1].str.strip(']')
df_table2[7] = df_table2[7].str.strip(']')
df_table2[2] = df_table2[2].str.strip('\r\n\r\n ')

# Remove all rows with any missing values
df_table3 = df_table2.dropna(axis=0, how='any')

# We remove uneccessary characters from the header
df_header2[0] = df_header2[0].str.strip('[')
df_header2[7] = df_header2[7].str.strip(']')

# We concatenate the two dataframes
frames = [df_header2, df_table3]
df = pd.concat(frames)

df2 = df.rename(columns=df.iloc[0]) # We assign the first row to be the dataframe header
df3 = df2.drop(df2.index[0]) # We drop the replicated header from the first row of the dataframe
