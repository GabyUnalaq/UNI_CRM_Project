import os
import csv
from absl import logging, flags
import pandas as pd

login_data_path = r'C:/Facultate/CRM_PA/data/login_info.csv'

with open(login_data_path) as login_data:
    reader = csv.reader(login_data)
    for line in reader:
        print(line)
        if 'horju' in line:
            print('ok')
