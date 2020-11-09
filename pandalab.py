import pandas as pd

weather = pd.read_csv('weather.csv')
weather = weather.set_index('DATE')
weather['PrecipitationIn']
weather['PrecipitationIn'].sum()
weather['PrecipitationIn']['2013-2-1':'2013-2-28'].sum()
weather_prec = weather[weather['PrecipitationIn'] > 0]

