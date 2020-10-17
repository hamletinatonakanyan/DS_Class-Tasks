import numpy as np
import pandas as pd
import pytz
from datetime import datetime, timedelta, date
from pandas.tseries.offsets import Day,  Hour

#%%
# 1. Write a Pandas program to create...

#%%
# a) Datetime object for Jan 15 2012

dt_obj1 = pd.to_datetime('Jan 15 2012')
print(f'Datetime object for Jan 15 2012:  {dt_obj1}')

dt_obj2 = datetime(2012, 1, 15)
print(f'Datetime object for Jan 15 2012:  {dt_obj2}')

#%%
# b) Specific date and time of 9:20 pm

spec_dt = datetime(2020, 10, 15, 21, 20)
print(f'Specific date and time: {spec_dt}')


df1 = pd.DataFrame({'year': [2020],
                    'month': [10],
                    'day': [15],
                    'hour': [21],
                    'minute': [20]})

spec_date1 = pd.to_datetime(df1)
print(f'\n1. Specific date and time: {spec_date1}')


df2 = pd.DataFrame({'date': ['15 10 2020 21:20']})
spec_date2 = pd.to_datetime(df2['date'][0], format='%d %m %Y %H:%M')
print(f'\n2. Specific date and time: {spec_date2}')

#%%
# c) Local date and time

local_now = datetime.now(tz=None)
print('\nDate and time for now: ', local_now)

local_UTCnow = datetime.utcnow()
print('\nDate and current UTC: ', local_UTCnow)

#%%
# d) A date without time.

# creating datetime object
dt = datetime(2015, 10, 15)

# catching only date
date_only = dt.date()
print(f'\nDate without time: {date_only}')

#%%
# e) Current date.

current_date = date.today()
print('\nCurrent date is: ', current_date)

#%%
# f) Time from a datetime.

time_only = datetime(2012, 8, 20, 20, 40).time()
print(f'\nTime without day: {time_only}')

#%%
# g) Current local time.

current_local_time = datetime.utcnow().time()
print(f'\nCurrent local time: {current_local_time}')


#%%
# 2. Write a Pandas program to print the day after and before a specified date.
#    Also print the days between two given dates.

specified_day = datetime(2020, 9, 26).date()
print(f'\nSpecified day: {specified_day}')

day_after_specDay = specified_day + Day()
print(f'\nOne day after: {day_after_specDay.date()}')

day_before_specDay = specified_day + Day()
print(f'\nOne day before: {day_before_specDay.date()}')


# Printing the days between two given dates.
given_dates = ['2020, 9, 27', '2020, 10, 17']
print(f'\nGiven dates: {given_dates}')

days_between = pd.period_range(start=given_dates[0], end=given_dates[-1], freq='D')
print(f'\nThe days between given dates:\n{days_between}')


#%%
# 3. Write a Pandas program to create a date from a given year, month, day and another date from a given string format.

given_dt = pd.DataFrame({'year': [2020],
                         'month': [2],
                         'day': [25]})
print(f'\nGiven year, month and day:\n{given_dt}')

values_to_date = pd.to_datetime(dt)
print(f'\nGiven year, month and day to date:\n{values_to_date[0].date()}')

year_m_d = '10 Oct 2019'
print(f'\nGiven string: {year_m_d}')
string_to_date = pd.to_datetime(year_m_d, yearfirst=True)
print(f'\nString to date:\n{string_to_date}')


#%%
# 4. Write a Pandas program to create a date range using a start point date and a number of periods.

dates_through_range = pd.date_range(start='10/11/2010', periods=10)
print(f'\nDates printed through data_range function:\n{dates_through_range}')


#%%
# 5. Write a Pandas program to create a time series using three months frequency.

dt_range = pd.date_range('May 12 2005', periods=3, freq='M')
dt_range = dt_range.tz_localize('Asia/Yerevan')
time_series = pd.Series(['May', 'April', 'Jun'], index=dt_range)

print(f'\nTime series through data range function\n{time_series}')

#%%
# Create time series through period range function

tmsp_now = pd.Timestamp(datetime.now(), tz='Asia/Yerevan')
print(f'Today is: {tmsp_now}')

tmsp_range = pd.period_range(tmsp_now, periods=3, freq='H')
tmsp_range_to_series = pd.Series(['now', 'hour later', '2 hours later'], index=tmsp_range)
print(f'\nCurrent timezone series for 3 hours:\n{tmsp_range_to_series}')

#%%
pytz.all_timezones
