import re
import requests
from bs4 import BeautifulSoup

from converter import month_to_num
# from converter import day_to_num


# Meteo has forecasts every 3 hours
# from 00:00
# to 03:00

meteo = "http://www.meteo.gr/cf.cfm?city_id=4"
emy = "http://www.emy.gr/emy/el/forecast/meteogramma_emy?perifereia=West%20Macedonia&poli=Kozani"
station = "http://penteli.meteo.gr/stations/kozani/"


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


def meteo_forecast():
    meteo_rsp = requests.get(meteo, headers=hdr)

    soup = BeautifulSoup(meteo_rsp.text, 'html.parser')

    # Meteo has multiple outerTable ids, here we get the first
    trapezi = soup.find("table", {"id": "outerTable"})

    rows = trapezi.findChildren(['tr'])

    forecast = []
    the_date = ''
    for row in rows:
        head_date = row.find("td", {"class": "forecastDate"})

        try:
            time = row.find("td", {"class": "fulltime"}).text.replace('\n', '')
            temperature = row.find("div", {"class": "tempcolorcell"}).text[:2]
            humidity = row.find("td", {"class": "humidity"}).text[:2]

            sample = {
                'date': the_date,
                'time': time,
                'temperature': temperature,
                'humidity': humidity,
            }
            forecast.append(sample)

        except AttributeError:
            if head_date:
                all_data = head_date.text.split(' ')

                week_day = all_data[0]
                day = re.findall(r'\d+', all_data[1])[0]
                month = re.findall("[Α-Ω]+", all_data[1])[0]

                # date = {
                #     'week_day': day_to_num(week_day),
                #     'day': day,
                #     'month': month_to_num(month)
                # }
                the_date = str(month_to_num(month)) + '-' + day

    return forecast


def station_conditions():
    st = requests.get(station)
    soup = BeautifulSoup(st.text, 'html.parser')
    trapezi = soup.find("table")
    rows = trapezi.findChildren(['tr'])

    t = rows[3].text.replace('\n', ' ')
    temperature = ','.join(re.findall(r'\d+', t))

    date = rows[2].text.replace('\n', '').strip().split(',')

    h = rows[4].text.replace('\n', ' ')
    hum = ','.join(re.findall(r'\d+', h))

    return {
        'temperature': temperature,
        'humidity': hum,
        'date': date[2],
        'time': date[1].strip()
    }
