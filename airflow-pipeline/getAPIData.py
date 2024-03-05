import requests 
import pandas as pd 


"""
Get API data from NZSX API
"""
response = requests.get("https://api.nzx.dev/ticker/1.0/nzsx/market")

print(response)