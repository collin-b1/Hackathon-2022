import json
from datetime import date


def save_record(data):
    name = 'daily_record_' + date.today().strftime("%d%m%y") + '.json'
    with open(name, 'w') as file_handle:
        json.dump(data, file_handle)
