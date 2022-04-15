# THIS PROGRAM IS FOR THE INITIAL FILLING OF THE DATABASE

#IMPORTS
from xml.dom.minidom import Element
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
# import db.db as db
import mysql.connector

# Variables
## For JSON attributes
crp_c_id = "null"
crp_c_name = "null"
crp_c_symbol = "null"
crp_c_slug = "null"
crp_c_rank = "null"
crp_c_isactive = "null"
crp_c_first_historical_data = "null"
crp_c_last_historical_data = "null"
crp_p_hasplatform = False
crp_p_id = 9
crp_p_tokenaddress = "null"

flag_useapi = False
flag_debugmode = False

mydb = mysql.connector.connect(
  host="192.168.64.2",
  user="crp_agent",
  password="crp_agent",
  database="CRP"
)

#Call to CMC API

if flag_useapi:
  # url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
  parameters = {
    'start':'1' #,
    # 'limit':'5',
    #'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '0109303a-8059-45e5-9664-5e010ee892d7',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  # Export to JSON file
  a_file = open("export/data.json", "w")
  json.dump(data, a_file)
  a_file.close()

  a_file = open("export/data.json", "r")
  output = a_file.read()
  print(output)
  a_file.close()


# Import the generated JSON data
# Opening JSON file
f = open('export/data.json')
 
# returns JSON object as a dictionary
data = json.load(f)
 
# Iterating through the json list
if flag_debugmode:
  for i in data['data']:
      print(i)
 
# Closing file
f.close()


# Putted the data obj of var data into var extdata
extdata = data.get("data")

# Put attributes into variables
for crypto in extdata:
  crp_c_id = crypto.get("id")
  crp_c_name = crypto.get("name")
  crp_c_symbol = crypto.get("symbol")
  crp_c_slug = crypto.get("slug")
  crp_c_rank = crypto.get("rank")
  crp_c_isactive = crypto.get("is_active")
  crp_c_first_historical_data = crypto.get("first_historical_data")
  crp_c_last_historical_data = crypto.get("last_historical_data")
  print(crp_c_id, "\n", crp_c_name, "\n", crp_c_symbol, "\n", crp_c_slug, "\n", 
  crp_c_isactive, "\n", crp_c_first_historical_data, "\n", 
  crp_c_last_historical_data, "\n", crp_p_id, "\n", crp_p_tokenaddress)

  # Check, if Cryptocurrency has a platform, if yes, then save id and token_address into variables
  if crypto.get("platform"):
    crp_p_hasplatform = True
    extplatform = crypto.get("platform")
    crp_p_id = extplatform.get("id")
    crp_p_tokenaddress = extplatform.get("token_address")
    print(crp_p_id, "\n", crp_p_tokenaddress, "\n")

  mycursor = mydb.cursor()
  sql = "INSERT INTO CryptoMasterData (cmc_id, name, symbol, slug, rank, is_active, first_historical_data, last_historical_data, has_platform, platform_id, platform_token_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (crp_c_id, crp_c_name, crp_c_symbol, crp_c_slug, crp_c_rank, crp_c_isactive, crp_c_first_historical_data, crp_c_last_historical_data, crp_p_hasplatform, crp_p_id, crp_p_tokenaddress)
  mycursor.execute(sql, val)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  crp_p_hasplatform = False
