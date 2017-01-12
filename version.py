#!/usr/bin/env python

import requests
print requests.__version__

response = requests.get("https://raw.githubusercontent.com/nlovas/cmput404lab1/master/version.py")

print response.text
print response.status_code
