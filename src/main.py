import datetime
import time

from database import TheDB
from scrape import scrape_meteo, scrape_station

# Get the db functions
db = TheDB()
# The times we wan to save data
times = ['0:00', '3:00', '6:00', '9:00', '00:00', '03:00', '06:00', '09:00',
         '12:00', '15:00', '18:00', '21:00']

# Scrape the data from meteo and station
m_data = scrape_meteo()
s_data = scrape_station()

mins = 0  # Delay
while (s_data['time'] not in times):
    print(s_data['time'], ' Not in times, waiting')
    time.sleep(60)
    s_data = scrape_station()
    mins = mins + 1
    if mins > 10:  # Get data for 11 mins, if not in times, save what was given
        break
# Save any collected data
meteo_info = db.insert_meteo(m_data)
station_info = db.insert_station(s_data)

# Print some info.
# if cron is used any print() is saved to a file
t = time.time()
stamp = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S')

print('\n####### ', stamp, ' #######')
print(meteo_info, station_info, sep='\n')
print('################################\n')
