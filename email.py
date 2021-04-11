import pandas as pd
import matplotlib.pyplot as plt
import re
import csv

product_info = pd.read_excel('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/strain_info.xlsx')
strain = product_info['Strain'].astype(str)

strain = strain.str.split("ATCC").str[-1]
strain = strain.str.replace('\)', '') # delete ')'
strain = strain.str.replace('\-', '') # delete '-'
strain

#read json file with information on papers that use ATCC and transpose the entire dataframe
papers = pd.read_json('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/papers.json').T


papers["AB"] = papers["AB"].astype(str)
papers["AB"] = papers["AB"].str.replace('\(R\)', '') #delete '(R)'
papers["AB"] = papers["AB"].str.replace('\(', ' ') # delete parentheses 
papers["AB"] = papers["AB"].str.replace('\)', ' ')
papers["AB"] = papers["AB"].str.replace('\.', ' ') 
papers["AB"] = papers["AB"].str.replace('\,', ' ') 

#find a way to extract product names
papers["AB"].str.extractall('(ATCC\s\w*\s)')

product = papers["AB"].str.extractall('(ATCC\s\w*\s)')
product = product.reset_index()
del product['match'] 
product.columns = ['ID', 'product']
product.head()

date = papers["LR"]
date = date.reset_index()
date.columns = ['ID', 'date']
date.head()

email = papers["AD"].str.extractall('(\w+@\w+\.\w+)')
email = email.reset_index()
del email['match']
email.columns = ['ID', 'email']
email.head()

country = papers["AD"].str.split().str[-1]
country = country.str.extractall('(\w+\.\')')
country = country.reset_index()
del country['match']
country.columns = ['ID', 'country']
country['country'] = country['country'].str.replace('\.\'', '')
country

AD = papers["AD"]
AD = AD.reset_index()
AD.columns = ['ID', 'AD']
AD.head()

pd1 = pd.merge(product, date, how='left', on='ID')
pd1
pd2 = pd.merge(pd1, email, how='left', on='ID')
pd2
pd3 = pd.merge(pd2, country, how='left', on='ID')
pd3
pd4 = pd.merge(pd3, AD, how='left', on='ID')
pd4


#make a tally for each product
df_group = product.groupby('product')['ID'].nunique()
df_group.head()
df_group.to_csv('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/strain_tally.csv')


#export the email data
pd3.to_csv('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/contact_info.csv')





df.to_csv('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/paper_strain.csv')

