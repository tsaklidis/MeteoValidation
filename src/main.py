from database import TheDB
from scrape import meteo_forecast, station_conditions


db = TheDB()

m_data = meteo_forecast()
s_data = station_conditions()

meteo_info = db.insert_meteo(m_data)
station_info = db.insert_station(s_data)

print(meteo_info, station_info, sep='\n')
