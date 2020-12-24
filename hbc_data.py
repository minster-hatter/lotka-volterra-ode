from numpy import arange, array
from pandas import DataFrame

year = arange(1900, 1921, 1)
lynx = array([4.0, 6.1, 9.8, 35.2, 59.4, 41.7, 19.0, 13.0, 8.3, 9.1, 7.4, 8.0,
              12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6])
hare = array([30.0, 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22.0, 25.4, 27.1,
              40.3, 57.0, 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7])
hbc = DataFrame({'year': year, 'lynx': lynx, 'hara': hare})
hbc.to_csv('hbc.csv')
