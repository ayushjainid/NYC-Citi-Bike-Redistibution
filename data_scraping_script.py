import requests
import time
import sys

start = time.time()
lastTimeStamp = 0

while(True):
    try:
        x = requests.get('https://gbfs.citibikenyc.com/gbfs/en/station_status.json')
        print()
        json = x.json()
        if(json["last_updated"] != lastTimeStamp):
            file = open(f'files/{json["last_updated"]}_station_status.json', "wb")
            file.write(x.content)
            file.close()
        lastTimeStamp = json["last_updated"]
        end = time.time()
        time.sleep(4)
        if(end - start > 86400):
            sys.exit()
    except:
        time.sleep(300)
