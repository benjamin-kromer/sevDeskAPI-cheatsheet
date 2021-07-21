from dotenv import load_dotenv
import os
load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
#YOU CAN FIND YOUR API TOKEN IN SETTINGS-->USERS-->YOURUSER-->API TOKEN https://my.sevdesk.de/#/admin/userManagement
BASE_URL = 'https://my.sevdesk.de/api/v1'
HEADERS = {'Authorization':API_TOKEN,'Content-Type':'application/json','Accept':'application/json'}