#####################################################
# Tyler Hedegard
# 6/1/2016
# Thinkful Data Science
# Stats
#####################################################

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()
data = [i.split(',') for i in data]

column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print("Alcohol mean: {}".format(df['Alcohol'].mean()))
# 5.4436363636363634
print("Alcohol median: {}".format(df['Alcohol'].median()))
# 5.63
# If all numbers occur equally often, stats.mode() will return the smallest number
print("Alcohol mode: {}".format(stats.mode(df['Alcohol'])))
# 4.02

print("Alcohol range: {}".format(max(df['Alcohol']) - min(df['Alcohol'])))
# 2.4500000000000002
print("Alcohol standard deviation: {}".format(df['Alcohol'].std()))
# 0.79776278087252406
print("Alcohol variance: {}".format(df['Alcohol'].var()))
# 0.63642545454546284

print("Tobacco mean: {}".format(df['Tobacco'].mean()))
# 3.6181818181818186
print("Tobacco median: {}".format(df['Tobacco'].median()))
# 3.53
print("Tobacco mode: {}".format(stats.mode(df['Tobacco'])))
# 2.71

print("Tobacco range: {}".format(max(df['Tobacco']) - min(df['Tobacco'])))
# 1.8499999999999996
print("Tobacco standard deviation: {}".format(df['Tobacco'].std()))
# 0.59070835751355388
print("Tobacco variance: {}".format(df['Tobacco'].var()))
# 0.3489363636363606
