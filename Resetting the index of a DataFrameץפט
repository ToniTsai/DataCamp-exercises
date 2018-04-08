import pandas as pd

# Read data
airquality = pd.read_csv('Data/airquality.csv')

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame = airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')


# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())
