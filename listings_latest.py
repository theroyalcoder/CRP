# THIS PROGRAM IS FOR THE INITIAL FILLING OF THE DATABASE CRP, TABLE CryptoMarketData

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
crp_c_num_market_pairs = "null"
crp_c_tags = "null"
crp_c_max_supply = "null"
crp_c_circulating_supply = "null"
crp_c_total_supply = "null"
crp_c_self_reported_circulating_supply = "null"
crp_c_self_reported_market_cap = "null"
crp_c_last_updated = False
crp_c_price = 0
crp_c_volume_24h = "null"
crp_c_volume_change_24h = "null"
crp_c_percent_change_1h = "null"
crp_c_percent_change_24h = "null"
crp_c_percent_change_7d = "null"
crp_c_percent_change_30d = "null"
crp_c_percent_change_60d = "null"
crp_c_percent_change_90d = "null"
crp_c_market_cap = "null"
crp_c_market_cap_dominance = "null"
crp_c_fully_diluted_market_cap = "null"

flag_useapi = True
flag_debugmode = True

mydb = mysql.connector.connect(
  host="192.168.64.2",
  user="crp_agent",
  password="crp_agent",
  database="CRP"
)

#Call to CMC API

if flag_useapi:
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1' ,
    'limit':'5000'
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
    if flag_debugmode:
      print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  # Export to JSON file
  a_file = open("export/listings_latest.json", "w")
  json.dump(data, a_file)
  a_file.close()

  a_file = open("export/listings_latest.json", "r")
  output = a_file.read()
  if flag_debugmode:
    print(output)
  a_file.close()


# Import the generated JSON data
# Opening JSON file
f = open('export/listings_latest.json')
 
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
  crp_c_num_market_pairs = crypto.get("num_market_pairs")
  # crp_c_tags = crypto.get("tags")
  crp_c_max_supply = crypto.get("max_supply")
  crp_c_circulating_supply = crypto.get("circulating_supply")
  crp_c_total_supply = crypto.get("total_supply")
  crp_c_self_reported_circulating_supply = crypto.get("self_reported_circulating_supply")
  crp_c_self_reported_market_cap = crypto.get("self_reported_market_cap")
  crp_c_last_updated =crypto.get("last_updated")
  quotedata = crypto.get("quote")
  usddata = quotedata.get("USD")
  crp_c_price = usddata.get("price")
  crp_c_volume_24h = usddata.get("volume_24h")
  crp_c_volume_change_24h = usddata.get("volume_change_24h")
  crp_c_percent_change_1h = usddata.get("percent_change_1h")
  crp_c_percent_change_24h = usddata.get("percent_change_24h")
  crp_c_percent_change_7d = usddata.get("percent_change_7d")
  crp_c_percent_change_30d = usddata.get("percent_change_30d")
  crp_c_percent_change_60d = usddata.get("percent_change_60d")
  crp_c_percent_change_90d = usddata.get("percent_change_90d")
  crp_c_market_cap = usddata.get("market_cap")
  crp_c_market_cap_dominance = usddata.get("market_cap_dominance")
  crp_c_fully_diluted_market_cap = usddata.get("fully_diluted_market_cap")
  
  if flag_debugmode:
    print(crp_c_id, "\n", crp_c_num_market_pairs, "\n", crp_c_tags, "\n", crp_c_max_supply, "\n", crp_c_circulating_supply, "\n", crp_c_total_supply, "\n", 
    crp_c_self_reported_circulating_supply, "\n", crp_c_self_reported_market_cap, "\n", crp_c_last_updated, crp_c_price, "\n", crp_c_volume_24h, "\n", 
    crp_c_volume_change_24h, "\n", crp_c_percent_change_1h, "\n", crp_c_percent_change_24h, "\n", crp_c_percent_change_7d, "\n", crp_c_percent_change_30d, "\n", 
    crp_c_percent_change_60d, "\n", crp_c_percent_change_90d, "\n", crp_c_market_cap, "\n", crp_c_market_cap_dominance, "\n", crp_c_fully_diluted_market_cap)

  mycursor = mydb.cursor()
  sql = "INSERT INTO CryptoMarketData (cmc_id, num_market_pairs, tags, max_supply, circulating_supply, total_supply, self_reported_circulating_supply, self_reported_market_cap, last_updated, price, volume_24h, volume_change_24h, percent_change_1h, percent_change_24h, percent_change_7d, percent_change_30d, percent_change_60d, percent_change_90d, market_cap, market_cap_dominance, fully_diluted_market_cap) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
  val = (crp_c_id, crp_c_num_market_pairs, crp_c_tags, crp_c_max_supply, crp_c_circulating_supply, crp_c_total_supply, crp_c_self_reported_circulating_supply, 
  crp_c_self_reported_market_cap, crp_c_last_updated, crp_c_price, crp_c_volume_24h, crp_c_volume_change_24h, crp_c_percent_change_1h, crp_c_percent_change_24h, 
  crp_c_percent_change_7d, crp_c_percent_change_30d, crp_c_percent_change_60d, crp_c_percent_change_90d, crp_c_market_cap, crp_c_market_cap_dominance, crp_c_fully_diluted_market_cap)
  mycursor.execute(sql, val)
  mydb.commit()
  if flag_debugmode:
    print(mycursor.rowcount, "record inserted.")
  crp_c_last_updated = False
