import os
import sqlite3
import datetime


class TheDB:

    def __init__(self):

        create_meteo_tbl = """CREATE TABLE IF NOT EXISTS meteo_data(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            month INTEGER,
                            day INTEGER,
                            time TEXT,
                            temperature REAL,
                            humidity REAL,
                            UNIQUE(month, day, time, temperature)
                            );"""

        create_station_tbl = """CREATE TABLE IF NOT EXISTS station_data(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            month INTEGER,
                            day INTEGER,
                            time TEXT,
                            temperature REAL,
                            humidity REAL,
                            UNIQUE(month, day, time, temperature)
                            );"""

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.conn = sqlite3.connect(dir_path + '/the_db.sqlite')
        self.cur = self.conn.cursor()

        self.cur.execute(create_meteo_tbl)
        self.cur.execute(create_station_tbl)
        self.conn.commit()

    def insert_meteo(self, meteo):
        for line in meteo:
            month, day = line['date'].split('-')
            try:
                self.cur.execute('INSERT INTO meteo_data (month, day, time, temperature, humidity) VALUES (?, ?, ?, ?, ?)',
                                 (month, day, line['time'], line['temperature'], line['humidity']))
                self.conn.commit()
            except sqlite3.IntegrityError:
                pass
                # print('Dublicate on Meteo: ', month, '-', day)

    def insert_station(self, station):
            try:
                d = datetime.datetime.now() 
                month = d.month
                day = d.day
                time = str(d.hour) + ':' + str(d.minute)
                self.cur.execute('INSERT INTO station_data (month, day, time, temperature, humidity) VALUES (?, ?, ?, ?, ?)',
                                 (month, day, time, station['temperature'], station['humidity']))
                self.conn.commit()
            except sqlite3.IntegrityError:
                pass
                # print('Dublicate on Station: ', month, '-', day)

    def __del__(self):
        self.conn.close()
