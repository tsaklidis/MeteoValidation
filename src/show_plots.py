import datetime
import matplotlib.pyplot as plt
import time
import sys

from database import TheDB


try:
    date = sys.argv[1]
except IndexError:
    t = time.time()
    date = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')
    # print('Provide a date in format YYYY-MM-DD')
    # print('Auto date set: ', date)

db = TheDB()


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


diffs = []
for met, st in zip(meteo['temps'], station['temps']):
    diffs.append(round(abs(met - st), 2))
try:
    dev = 'AVG deviation is: {0} (*C)'.format(
        round(sum(diffs) / len(diffs), 1))
except ZeroDivisionError:
    dev = 'AVG deviation is: 0 (*C)'

plt.title('Compare forecast for: ' + date + '\n' + dev, fontsize=10)
plt.ylabel('Temperature (*C)')
plt.xlabel('Time')
plt.grid(True)
plt.plot(meteo['dates'], meteo['temps'], station['dates'], station['temps'])
plt.legend(['Meteo.gr', 'Davis Station'], loc='best', fontsize=10)

plt.show()
