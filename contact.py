# /Contact Endpoint
import requests as req
from auth import *

ENDPOINT = '/Contact'


# GET CONTACTS
res = req.get(BASE_URL+ENDPOINT, headers=HEADERS)
print(res.json())

# CREATE CONTACT
contact = {
  "name": "arthurdent",
  "customerNumber": "Customer-0815",
  "surename": "Arthur",
  "familyname": "Dent",
  "titel": "BEAST",
  "category": {
  "id": 3,
  "objectName": "Category"
},
  "description": "Rightful king of the seven kingdoms",
  "academicTitle": "Prof. Dr. rer. nat.",
  "gender": "male",
  "name2": "Targaryen",
  "birthday": "01.01.1970"
}
res = req.post(BASE_URL+ENDPOINT,headers=HEADERS,json=contact)
print(res.json())