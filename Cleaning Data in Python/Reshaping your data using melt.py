import pandas as pd

# Read data
airquality = pd.read_csv('Data/airquality.csv')

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame = airquality, id_vars=['Month', 'Day'])

# Print the head of airquality_melt
print(airquality_melt.head())
