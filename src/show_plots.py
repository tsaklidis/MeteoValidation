import datetime
import matplotlib.pyplot as plt
import time
import sys

from database import TheDB


try:
    date = sys.argv[1]  # Different day than today
except IndexError:
    t = time.time()
    date = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d')

try:
    show = sys.argv[2]  # Any text saves the plot to image
except IndexError:
    show = False

db = TheDB()

# Get the raw data from db
meteo_rows = db.select_meteo(date, True) # Set this to false in order to get the last forecast
station_rows = db.select_station(date)

meteo = {'temps': [], 'dates': []}
station = {'temps': [], 'dates': []}

# Prepare data for plot
for m in meteo_rows:
    meteo['dates'].append(m[0])
    meteo['temps'].append(m[1])

for s in station_rows:
    station['dates'].append(s[0])
    station['temps'].append(s[1])

# Prepare data for deviation
diffs = []
for met, st in zip(meteo['temps'], station['temps']):
    # If station and meteo dates do not match, deviation is wrong.
    # Example:
    # meteo = {'temps': [18, 17], 'dates': ['12:00', '18:00']}
    # station = {'temps': [18, 25, 17], 'dates': ['12:00', '15:00', '18:00']}
    diffs.append(round(abs(met - st), 2))

# Create deviation info
try:
    avg_dev = 'AVG deviation +/- {0}*C\n'.format(round(sum(diffs) / len(diffs), 1))
    max_dev = 'MAX deviation +/- {0}*C\n'.format(max(diffs))
    min_dev = 'MIN deviation +/- {0}*C'.format(min(diffs))
except ZeroDivisionError:
    avg_dev = 'AVG deviation is: 0 (*C)'

# Create the plot
# Also add data to plot
# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, yn)

# plt.title('Compare forecast for: ' + date + '\n' + avg_dev + max_dev + min_dev, fontsize=10)
plt.title('Compare forecast for: ' + date + '\n' + avg_dev, fontsize=9)
plt.ylabel('Temperature (*C)')
plt.xlabel('Time')
plt.grid(True)

# Do not show time but all samples
# plt.plot(meteo['temps'])
# plt.plot(station['temps'])

plt.plot(meteo['dates'], meteo['temps'], 'ro', station['dates'], station['temps'])
plt.legend(['Meteo.gr', 'Davis Station'], loc='best', fontsize=10)

# Display or save the plot
if show:
    t = time.time()
    stamp = datetime.datetime.fromtimestamp(t).strftime('%Y%m%d_%H:%M:%S')

    plt.savefig(str(stamp) + '.png')
else:
    plt.show()
