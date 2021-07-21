# /Order Endpoint
import requests as req
from auth import *

ENDPOINT = '/Order'

# GET ORDERS
res = req.get(BASE_URL+ENDPOINT,headers=HEADERS)
print( res.json() )

# CREATE ORDER
order =  {
    "orderNumber": "AN-1002",
    "contact": {"id": 34302790, "objectName": "Contact"},
    "orderDate": "21.07.2021",
    "status": 100,
    "header": "Angebot AN-1002",
    "version": 0,
    "smallSettlement": 1,
    "contactPerson": {"id": 614740, "objectName": "SevUser"},
    "taxRate": 19,
    "taxText": "Umsatzsteuer 19%",
    "taxType": "ss",
    "orderType": "AN",
    "currency": "EUR"
}
res = req.post(BASE_URL+'/Order',headers=HEADERS,json=order)
res