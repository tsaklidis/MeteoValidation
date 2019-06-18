import sys
import matplotlib.pyplot as plt

from database import TheDB
try:
    date = sys.argv[1]
except IndexError:
    exit('Provide a date in format YYYY-MM-DD')

db = TheDB()
# [('00:00', 21.0), ('03:00', 19.0), ('06:00', 17.0), ('09:00', 23.0), ('12:00', 28.0), ('15:00', 30.0), ('18:00', 29.0), ('21:00', 24.0)] # noqa

meteo_rows = db.select_meteo(date)
station_rows = db.select_station(date)

meteo = {'temps': [], 'dates': []}
station = {'temps': [], 'dates': []}

for m in meteo_rows:
    meteo['dates'].append(m[0])
    meteo['temps'].append(m[1])

for s in station_rows:
    station['dates'].append(s[0])
    station['temps'].append(s[1])

plt.title('Meteo.gr VS Davis Station\nForecast for: ' + date)

plt.ylabel('Temperature (*C)')
plt.xlabel('Time')
plt.grid(True)


plt.plot(meteo['dates'], meteo['temps'], station['dates'], station['temps'])

# print(meteo)
# print(station)

try:
    plt.legend(['meteo.gr', 'Davis station'], loc='upper left')
    plt.show()
except KeyboardInterrupt:
    exit('Terminated by user')
