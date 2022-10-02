"""
Created on Mon Feb  7 14:10:42 2022

@author: Okhrimchuk Roman
for Sierentz Global Merchants

Test task
"""

# TODO Import the necessary libraries
import pandas as pd
import datetime as dt

# TODO Import the dataset
path = r'./data/weather_dataset.data'
data = pd.read_csv(path, sep='\s{1,3}', engine='python')
# print(data.head())

# TODO  Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data['Date'] = pd.to_datetime(data[["Yr", "Mo", "Dy"]].astype(str).agg(' '.join, axis=1))
data = data.drop(columns=['Yr', 'Mo', 'Dy'])


# TODO Check if everything is okay with the data. Create functions to delete/fix rows with strange cases and apply them
def fix_dataset(data):
    location = [x for x in data.columns if x != 'Date']

    for i in location:
        data[i] = data[i].replace('\,|\.', '', regex=True)

    for i in location:
        data[i] = data[i].replace('^-?\w*\D\w*$|^\d{5,}$', 'NaN', regex=True)

    data[location] = data[location].astype(float) / 100


fix_dataset(data)


# TODO Write a function in order to fix date (this relate only to the year info) and apply it
def fix_dates(data):
    data['Date'] = data['Date'].map(lambda x: dt.datetime(x.year - 100 if x.year > 2000 else x.year, x.month, x.day))


fix_dates(data)

# TODO Set the right dates as the index. Pay attention at the data type, it should be datetime64[ns]
work_data = data.set_index('Date')
work_data.index.astype("datetime64[ns]")

# TODO Compute how many values are missing for each location over the entire record
missing_values = work_data.isnull().values.sum()
print(missing_values)

# TODO Compute how many non-missing values there are in total
non_missing_values = work_data.count().sum()
print(non_missing_values)

# TODO Calculate the mean windspeeds of the windspeeds over all the locations and all the times
mean_speed = work_data.mean().mean()
print(mean_speed)

# TODO Create a DataFrame called loc_stats and calculate the min, max and mean windspeeds and standard deviations of the windspeeds at each location over all the days
loc_stats = work_data.agg(['min', 'max', 'mean', 'std'])
# loc_stats=work_data.describe()
print(loc_stats)

# TODO Find the average windspeed in January for each location
avg_january = work_data[work_data.index.month == 1].mean()
print(avg_january)

# TODO Downsample the record to a yearly frequency for each location
sample_year = work_data.resample('A').mean()
print(sample_year)

# TODO Downsample the record to a monthly frequency for each location
sample_month = work_data.resample('M').mean()
print(sample_month)

# TODO Downsample the record to a weekly frequency for each location
sample_week = work_data.resample('W').mean()
print(sample_week)

# TODO Calculate the min, max and mean windspeeds and standard deviations of the windspeeds across all locations for each week (assume that the first week starts on January 2 1961) for the first 21 weeks
work_data_slice = work_data[(work_data.index.date > dt.date(1968, 1, 1)) & \
                            (work_data.index.date < dt.date(1968, 1, 3) + pd.Timedelta("147 day"))]

sample_21_week = work_data_slice.resample('W').mean().agg(['min', 'max', 'mean', 'std'])
# sample_21_week= work_data_slice.resample('W').mean().describe()
print(sample_21_week)
