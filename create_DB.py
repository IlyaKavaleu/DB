import csv
import json
import psycopg2
from password import password


class DataBase:
    def __init__(self, password):
        self.password = password

    def connect_to_db(self):
        conn = psycopg2.connect(
            dbname='shop_database',
            user='postgres',
            password=str(password),
            host='localhost',
            port=5432
        )
        cur = conn.cursor()
        return cur

    def selects(self, cur, enter):
        delimiter = '' * 160
        dates = []
        cur.execute(enter)
        clients = cur.fetchall()
        for client in clients:
            dates.append(client)
        return dates

    def to_csv(self, dates):
        if len(enter.split()) < 5:
            result = enter.split()[-1]
        else:
            result = f'{enter.split()[3]}_{enter.split()[6]}'
        filename = result

        with open(f'database_folder/{filename}.csv', 'w', newline='') as file:
            for data in dates:
                writer = csv.writer(file)
                writer.writerow(data)


enter = input('Enter select to DB: ')
db = DataBase(password)
dates = db.selects(db.connect_to_db(), enter)
db.to_csv(dates)
