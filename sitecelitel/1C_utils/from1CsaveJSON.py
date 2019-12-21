import requests
import json
from time import time


#получаем из 1С GetSpecialization.json и сохраняем на хостинг
def getSpecialization():
    print("Start getSpecialization")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetSpecialization', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetSpecialization.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getSpecialization.json not found or error")
    
    end = time()
    print("End getSpecialization")    
    print("Total time: ", end - start)
    
getSpecialization()


#получаем из 1С GetAgreements.json и сохраняем на хостинг
def getAgreements():
    print("Start getAgreements")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetAgreements', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetAgreements.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getAgreements.json not found or error")
        
    end = time()
    print("End getAgreements")    
    print("Total time: ", end - start)
    
getAgreements()


#получаем из 1С GetDepartments.json и сохраняем на хостинг
def getDepartments():
    print("Start getDepartments")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetDepartments', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetDepartments.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getDepartments.json not found or error")
        
    end = time()
    print("End getDepartments")    
    print("Total time: ", end - start)
    
getDepartments()


#получаем из 1С GetOrganizations.json и сохраняем на хостинг
def getOrganizations():
    print("Start getOrganizations")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetOrganizations', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetOrganizations.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getOrganizations.json not found or error")
        
    end = time()
    print("End getOrganizations")    
    print("Total time: ", end - start)
    
getOrganizations()


#получаем из 1С GetServiceGroups.json и сохраняем на хостинг
def getServiceGroups():
    print("Start getServiceGroups")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetServiceGroups', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetServiceGroups.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getServiceGroups.json not found or error")
        
    end = time()
    print("End getServiceGroups")    
    print("Total time: ", end - start)
    
getServiceGroups()


#получаем из 1С GetServices.json и сохраняем на хостинг
def getServices():
    print("Start getServices")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetServices', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetServices.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getServices.json not found or error")
        
    end = time()
    print("End getServices")    
    print("Total time: ", end - start)
    
getServices()


#получаем из 1С GetDoctors.json и сохраняем на хостинг
def getDoctors():
    print("Start getDoctors")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetDoctors', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetDoctors.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getDoctors.json not found or error")
        
    end = time()
    print("End getDoctors")    
    print("Total time: ", end - start)
    
getDoctors()


#получаем из 1С GetPriceTypes.json и сохраняем на хостинг
def getPriceTypes():
    print("Start getPriceTypes")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetPriceTypes', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetPriceTypes.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getPriceTypes.json not found or error")
        
    end = time()
    print("End getPriceTypes")    
    print("Total time: ", end - start)
    
getPriceTypes()

#получаем из 1С GetPrice.json и сохраняем на хостинг
def getPrices():
    print("Start getPrices")
    start = time()
     
    r = requests.get('http://91.205.128.70/MedicinePolic/hs/bitrixsite/GetPrices', auth=('vector', '112233'))

    if r.status_code == 200:
        data = r.json()
        with open('celitel05.ru/public_html/json/GetPrices.json', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=False, ensure_ascii=False, separators=(',', ':'))
    else:
        print("getPrices.json not found or error")
        
    end = time()
    print("End getPrices")    
    print("Total time: ", end - start)
    
getPrices()