import json
from urllib.error import URLError
from urllib.request import urlopen
import requests
#import task1


URL = "https://openx.com/sellers.json"
try:
    response=requests.head(URL)
except Exception as e:
    print(f'NOT OK: {str(e)}')
else:
    if response.status_code ==200:
        print('OK')
    
