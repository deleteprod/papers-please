#!/usr/bin/env python3

import json
import requests
import pprint
import time

URL = "https://randomuser.me/api/"


def get_user(url=URL,count=2):
    for counter in range(1,count):
        result = json.loads(requests.get(url).text)

        marker = result['results'][0]['name']
        print("\n" + "Result No " + str(counter) + ": " + marker['title'] + " " + marker['first'] + " " + marker['last'])
        time.sleep(3)

        print("\n")

        output = print(pprint.pprint(result))

my_response = get_user()
