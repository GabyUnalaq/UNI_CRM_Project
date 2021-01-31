"""
    Config class
    Authors: Gabriel Tomuta
"""

import urllib.request
import json
import csv


class Config(object):
    SVR_DATA_BASE = 'http://crm.bpagency.ro/crm_data/data_base.json'
    SVR_LOGIN_INFO = ''

    DATA_BASE = '../data/data_base.json'
    LOGIN_INFO = '../data/login_data_base.csv'

    # Methods ----------------------------------------------------------------------------------------------------------
    def read_data_base(self, server_read=False):
        if server_read:
            with urllib.request.urlopen(self.SVR_DATA_BASE) as url:
                data = json.loads(url.read().decode())
                return data
        else:
            with open(self.DATA_BASE) as json_file:
                data = json.load(json_file)
                return data

    def write_data_base(self, data, server_write=False):
        if server_write:
            print("Writing to server..")
            # TODO
        else:
            with open(self.DATA_BASE, 'w') as json_file:
                json.dump(data, json_file)

    def check_in_csv(self, username, password):
        with open(self.LOGIN_INFO) as login_csv:
            login_data = csv.reader(login_csv)
            for line in login_data:
                if username in line and password in line:
                    return True
            return False


def test_json():
    config = Config()
    data = config.read_data_base()
    print(data['criteria'])


if __name__ == "__main__":
    test_json()
