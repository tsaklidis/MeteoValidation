from database import TheDB
from scrape import meteo_forecast, station_conditions


db = TheDB()

m_data = meteo_forecast()
s_data = station_conditions()

db.insert_meteo(m_data)
db.insert_station(s_data)
