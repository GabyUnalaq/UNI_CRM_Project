import urllib.request
import json
import csv


# Info -----------------------------------------------------------------------------------------------------------------
DATA_BASE = 'http://crm.bpagency.ro/crm_data/data_base.json'
LOGIN_INFO = r'../data/login_data_base.csv'


# Methods --------------------------------------------------------------------------------------------------------------
def read_data_base():
    with urllib.request.urlopen(DATA_BASE) as url:
        data = json.loads(url.read().decode())
        return data


def write_data_base():
    print("Writing..")
    # TODO


def check_in_csv(username, password):
    with open(LOGIN_INFO) as login_csv:
        login_data = csv.reader(login_csv)
        for line in login_data:
            if username in line and password in line:
                return True
        return False
