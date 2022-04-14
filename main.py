
#IMPORTS
from xml.dom.minidom import Element
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

#Call to CMC API
url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/category'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
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

#Testdata
#data = "{'status': {'timestamp': '2022-04-13T20:57:59.170Z', 'error_code': 0, 'error_message': None, 'elapsed': 1, 'credit_count': 1, 'notice': None}, 'data': [{'id': 2758, 'name': 'awx8lo2spn', 'symbol': '2jqgpm10i7r', 'slug': '6qu9961yr6', 'cmc_rank': 4896, 'num_market_pairs': 30, 'circulating_supply': 8968, 'total_supply': 1397, 'max_supply': 1670, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['j8ksgm5xqqd', 'yi43k3vb0oj', 'pte5kbeksra', '6jxjybdv26b', 'ny1vq5bfukp', 'ykbajbyfypf', 'mgbfw318a4c', 'dv05m628o69', '1gyk07zp3u9', '821v8o6my9a'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.10757352817137567, 'volume_24h': 5500, 'volume_change_24h': 0.6705434606063458, 'percent_change_1h': 0.06903150248637369, 'percent_change_24h': 0.6796043030888173, 'percent_change_7d': 0.901232761741873, 'market_cap': 0.5488234493862516, 'market_cap_dominance': 9310, 'fully_diluted_market_cap': 0.9137395079056796, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 8887, 'name': 'nje18e2rvr', 'symbol': 'qx4069ft51', 'slug': '6luwbrynme', 'cmc_rank': 4775, 'num_market_pairs': 1796, 'circulating_supply': 1632, 'total_supply': 3556, 'max_supply': 2602, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['y5byxmiqdab', 'm6yv3z82bd', 'uec1yolnym', 'h996k032do', 'ycd9wiakfc', 'wvoni8cv5k', 'hhvll3z37d', '2vyzvoeup4u', 'qbxvliu0vm', 'uikfp7lbceh'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.7867656551941962, 'volume_24h': 7485, 'volume_change_24h': 0.22694340950419978, 'percent_change_1h': 0.608900322767306, 'percent_change_24h': 0.365061162295941, 'percent_change_7d': 0.6194026880058214, 'market_cap': 0.10009024780159703, 'market_cap_dominance': 7628, 'fully_diluted_market_cap': 0.08243439337341818, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 6846, 'name': 'v1oo261vbu9', 'symbol': 'm3a52ll8gv', 'slug': 'b3w4jnir6nk', 'cmc_rank': 4460, 'num_market_pairs': 5869, 'circulating_supply': 8423, 'total_supply': 5961, 'max_supply': 2508, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['i4vepmja60l', '532fknsr6yc', 'lqd6ge8n2kq', 'ycr497oysp', '6049k5s2ogy', 'eta31y8vy1', 'pn6vna05fed', '0xiwz3ovvc1', 'lmdbsq2ald', '131s769iabs'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.47333930775249344, 'volume_24h': 4500, 'volume_change_24h': 0.9687237729683973, 'percent_change_1h': 0.033025568686274376, 'percent_change_24h': 0.7534102496376487, 'percent_change_7d': 0.10610292270354638, 'market_cap': 0.2884249175561635, 'market_cap_dominance': 8530, 'fully_diluted_market_cap': 0.43283438564692833, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 7582, 'name': 'a3268cutejw', 'symbol': 'lrmxhlmz3g', 'slug': '5yqlvsqtlp', 'cmc_rank': 4592, 'num_market_pairs': 4926, 'circulating_supply': 5785, 'total_supply': 7611, 'max_supply': 6946, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['02l8occhm7bv', '6g1gwi78km', 'f3ikbrtyo6p', 'vhvhjbh8iyc', 'ngwmu66apf', 'vmslxfqe1hf', '4w15zngniee', 'ssajsg8zyll', '70g6l58yeyq', 'famqsd4t0f'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.7320736527628906, 'volume_24h': 5117, 'volume_change_24h': 0.1916317983527973, 'percent_change_1h': 0.5539919435345964, 'percent_change_24h': 0.322463742602906, 'percent_change_7d': 0.4363194335826355, 'market_cap': 0.2650303239484142, 'market_cap_dominance': 4006, 'fully_diluted_market_cap': 0.9802058784906889, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 3584, 'name': 'izympxe952', 'symbol': 'f6enn41mji7', 'slug': 'ov06xd4g30s', 'cmc_rank': 1847, 'num_market_pairs': 4788, 'circulating_supply': 1701, 'total_supply': 1537, 'max_supply': 1991, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['qaufd7jyl3q', 'dzj7euihkmg', '3wu0evqrs7a', 'i8zxy4oyxj', 'yqot945rqrn', 'rpzdx5395ep', '09blgt9098ww', 'k3h2kwlfqsk', 'hoksajc7j8l', 'k8froc1yiwl'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.8316301287708991, 'volume_24h': 7909, 'volume_change_24h': 0.7313534792772269, 'percent_change_1h': 0.7525227898277898, 'percent_change_24h': 0.4555029939061497, 'percent_change_7d': 0.36370777019536615, 'market_cap': 0.2814279056830731, 'market_cap_dominance': 5335, 'fully_diluted_market_cap': 0.27140504396118525, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 1493, 'name': 'yqazsqf0tyg', 'symbol': '6b7dibf8u5s', 'slug': '2o17bxxcjis', 'cmc_rank': 6188, 'num_market_pairs': 1005, 'circulating_supply': 4504, 'total_supply': 8877, 'max_supply': 7493, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['yqdwuwnve5i', '26a32uruec9', 'gv2lop3po3o', 'k4gtkfso73o', '5zpjo8k71om', 'yof9x76kh', '22eix7b16nd', 'f1uxyshdi1v', 'pax7ossanw', 'zmffe3m4c7'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.8054954412111606, 'volume_24h': 5058, 'volume_change_24h': 0.9549516119256265, 'percent_change_1h': 0.5732015258189405, 'percent_change_24h': 0.14704874317646577, 'percent_change_7d': 0.5651186889489033, 'market_cap': 0.8576671400208702, 'market_cap_dominance': 8014, 'fully_diluted_market_cap': 0.05396319711771391, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 2658, 'name': 'q01jjask51', 'symbol': 'xxm0oavkl2i', 'slug': '73dil3uugor', 'cmc_rank': 8824, 'num_market_pairs': 5187, 'circulating_supply': 8880, 'total_supply': 412, 'max_supply': 1802, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['eqgeubfvjmf', 'ao59bscrnaw', 'o47xt4y1z3m', '12eox8t2gba9', 'boombp0j4dh', 'c89uk8rxxrt', 'b4ndp628hyq', 'qu6imhonhzm', 'k1y3l8zw0cs', 'fhz3vr3aias'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.2973860113669766, 'volume_24h': 881, 'volume_change_24h': 0.9658363675292294, 'percent_change_1h': 0.475219797518611, 'percent_change_24h': 0.8375994379268952, 'percent_change_7d': 0.35761820724361626, 'market_cap': 0.390148512089044, 'market_cap_dominance': 7930, 'fully_diluted_market_cap': 0.9206728056704561, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 4240, 'name': 'f357kmfnhyo', 'symbol': 'bsl8wg1b6rs', 'slug': 'z6d314uma9i', 'cmc_rank': 5998, 'num_market_pairs': 7254, 'circulating_supply': 9834, 'total_supply': 4513, 'max_supply': 2880, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['qc2ebev6r9f', 's6svlzov3e', '8uumc0h4hwo', 'muwzcfu567p', 'f5fuvnrfh0r', 'kkd22w4fb5b', 'i3ivg29t6q', 'p3ozvpfm2j', 'txuiwg1cg2r', 'oq92gpf9k3'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.07605164139119736, 'volume_24h': 5331, 'volume_change_24h': 0.4624594363299277, 'percent_change_1h': 0.9115414727773052, 'percent_change_24h': 0.2634670568143769, 'percent_change_7d': 0.19866247146914606, 'market_cap': 0.8919130070085648, 'market_cap_dominance': 120, 'fully_diluted_market_cap': 0.9954834103637826, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 7559, 'name': 'eskuouceokl', 'symbol': 'kqsmnvwh6en', 'slug': 'rif27dd84er', 'cmc_rank': 5651, 'num_market_pairs': 9233, 'circulating_supply': 3737, 'total_supply': 8909, 'max_supply': 565, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['8bmvck8l96', '12rhi1yzru1', 'zcp8aro1xl', 'lhowt0992d9', 'ga1ugl0f8mo', '1up49uwyvec', '3nh9v9dqze7', 'mdpo1jll61j', 'l065xk5n8rf', 'i83kciugh0n'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.9181017874740187, 'volume_24h': 2586, 'volume_change_24h': 0.8664992400053377, 'percent_change_1h': 0.7483492048650875, 'percent_change_24h': 0.02220408987738698, 'percent_change_7d': 0.9608728065057124, 'market_cap': 0.1468002599433753, 'market_cap_dominance': 2616, 'fully_diluted_market_cap': 0.30567504890941755, 'last_updated': '2022-04-13T20:57:59.170Z'}}}, {'id': 8610, 'name': 't5zd4ogezx', 'symbol': 'r3075pip2g', 'slug': '35m9wdzhq9k', 'cmc_rank': 8104, 'num_market_pairs': 6427, 'circulating_supply': 2361, 'total_supply': 6139, 'max_supply': 3721, 'last_updated': '2022-04-13T20:57:59.170Z', 'date_added': '2022-04-13T20:57:59.170Z', 'tags': ['qm598y656y', 'bi85tsdbvs9', '4jc94akthsg', 'a7jzpkzbje8', '18kl0yv0god', 'lg2apt9cl9j', 'gw6ssdyawsn', 'otcb33wz5l', 'b0j4bpukhbd', 'qs2inpm6mt'], 'platform': None, 'self_reported_circulating_supply': None, 'self_reported_market_cap': None, 'quote': {'USD': {'price': 0.36973150754693673, 'volume_24h': 236, 'volume_change_24h': 0.9719343932579072, 'percent_change_1h': 0.7644713210787843, 'percent_change_24h': 0.1431219725771804, 'percent_change_7d': 0.13486728331391107, 'market_cap': 0.48947185064577314, 'market_cap_dominance': 6457, 'fully_diluted_market_cap': 0.9198855401341979, 'last_updated': '2022-04-13T20:57:59.170Z'}}}]}"
formattedData = data

"""
for element in data:
  if element == '{':
    formattedData+=element+"\n"
  elif element == '}':
    formattedData+=element+"\n"
  elif element == ',':
    formattedData+=element+"\n"
  else:
    formattedData+=element
"""

#print(formattedData)

#Export formattedData to Text document
with  open("export/export.txt", "w") as file:
	content = data
	file.write(content)
	file.close()
