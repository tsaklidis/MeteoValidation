import os
import sqlite3
import datetime
import time


class TheDB:

    def __init__(self):

        create_meteo_tbl = """CREATE TABLE IF NOT EXISTS meteo_data(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            month INTEGER,
                            day INTEGER,
                            time TEXT,
                            temperature REAL,
                            humidity REAL,
                            recorded TEXT,
                            UNIQUE(month, day, time, temperature)
                            );"""

        create_station_tbl = """CREATE TABLE IF NOT EXISTS station_data(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date TEXT,
                            time TEXT,
                            temperature REAL,
                            humidity REAL,
                            recorded TEXT,
                            UNIQUE(date, time, temperature)
                            );"""

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(dir_path + '/the_db.sqlite')
        self.cur = self.conn.cursor()

        self.cur.execute(create_meteo_tbl)
        self.cur.execute(create_station_tbl)
        self.conn.commit()

    def insert_meteo(self, meteo):
        new = 0
        for line in meteo:
            month, day = line['date'].split('-')
            try:
                t = time.time()
                stamp = datetime.datetime.fromtimestamp(
                    t).strftime('%Y/%m/%d %H:%M:%S')

                self.cur.execute('INSERT INTO meteo_data (month, day, time, temperature, humidity, recorded) VALUES (?, ?, ?, ?, ?, ?)',  # noqa
                                 (month, day, line['time'], line['temperature'], line['humidity'], stamp))  # noqa
                self.conn.commit()
                new = new + 1
            except sqlite3.IntegrityError:
                pass
        if new:
            return"METEO: New records: " + str(new)
        else:
            return"METEO: Nothing new"

    def insert_station(self, station):
        try:
            t = time.time()
            stamp = datetime.datetime.fromtimestamp(t).strftime('%Y/%m/%d %H:%M:%S')  # noqa

            self.cur.execute('INSERT INTO station_data (date, time, temperature, humidity, recorded) VALUES (?, ?, ?, ?, ?)',  # noqa
                             (station['date'], station['time'], station['temperature'], station['humidity'], stamp))  # noqa
            self.conn.commit()
            record = 'STATION: New data saved'
        except sqlite3.IntegrityError:
            record = 'STATION: Nothing new'

        return record

    def __del__(self):
        self.conn.close()
