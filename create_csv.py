import os
import csv

FILENAME = os.getenv('FILENAME', 'users.csv')


def create_csv(response_data):
    user_csv = open(FILENAME, 'w')
    csv_writer = csv.writer(user_csv)
    count = 0

    for data in response_data:
        if count == 0:
            header = data.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(data.values())

    print('CSV Created...')
    user_csv.close()
