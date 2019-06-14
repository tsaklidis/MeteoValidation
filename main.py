from database import TheDB
from scrape import meteo_forecast, station_conditions


meteo_db = MeteoDB()
station_db = StationDB()

m_data = meteo_forecast()
s_data = station_conditions()

meteo_db.insert(m_data)
station_db.insert(s_data)

