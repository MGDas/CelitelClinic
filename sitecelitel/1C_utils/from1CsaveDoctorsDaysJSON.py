import requests
import json
from time import time

#получаем из 1С GetDoctorsDays.json и сохраняем на хостинг
def getDoctorsDays():
    print("Start getDoctorsDays")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetDoctorsDays', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetDoctorsDays.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
    	print("getDoctorsDays.json not found or error")
    	
    end = time()
    print("End getDoctorsDays")    
    print("Total time: ", end - start)
    
getDoctorsDays()