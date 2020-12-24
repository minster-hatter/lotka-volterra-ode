from pandas import read_csv
from matplotlib.pyplot import subplots, savefig, close
from matplotlib.ticker import FormatStrFormatter
from numpy import arange

hbc = read_csv('hbc.csv')
print(hbc.head(10))

__, ax = subplots()
ax.plot(hbc['year'], hbc['hare'], color='black', marker='x', label='hare')
ax.plot(hbc['year'], hbc['lynx'], color='red', marker='o', label='lynx')
ax.legend()
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.xaxis.set_major_formatter(FormatStrFormatter('%1.0f'))
ax.set_xticks(arange(1900, 1921, 5))
savefig('lynx_hare_timeseries.png')
close()
