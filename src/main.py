import datetime
import time

from database import TheDB
from scrape import meteo_forecast, station_conditions


db = TheDB()
times = ['00:00', '03:00', '06:00', '09:00',
         '12:00', '15:00', '18:00', '21:00']

m_data = meteo_forecast()
s_data = station_conditions()

while (s_data['time'] not in times):
    print('Not in times, waiting my time')
    time.sleep(60)
    s_data = station_conditions()

meteo_info = db.insert_meteo(m_data)
station_info = db.insert_station(s_data)

t = time.time()
stamp = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S')

print('####### ', stamp, ' #######')
print(meteo_info, station_info, sep='\n')
print('################################\n\n')
