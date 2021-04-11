import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


papers["AB"].str.extractall('(ATCC.*\s)')
papers["AB"].str.extractall('(ATCC\s\w*\s)')
df = papers["AB"].str.extractall('(ATCC\s\w*\s)')
df = df.reset_index()
del df['match'] 
df.columns = ['ID', 'product']
df.head()

df_group = df.groupby('product')['ID'].nunique()
df_group.head()

df_group.to_csv('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/strain_tally.csv')






df.to_csv('C:/Users/james/Desktop/Projects/EarthOne/ATCC_product_info/Data/paper_strain.csv')

