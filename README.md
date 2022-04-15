# Cryptocurrency Rating Program (CRP)

## Idee
- Beim starten des Programmes wird ein Anfrage zu CoinMarketCap (CMC) ausgeführt und die grössten Schwankungen der letzten 24h werden heruntergeladen und in eine Datenbank gespeichert. Diese Daten können dann von uns via Metabase analysiert werden.

## Konzept
- Es soll Filtermöglichkeiten geben, bevor man einen API Call macht (sonst werden unnötig Calls verschwendet)
- Das erhaltene JSON muss geparsed werden und danach in eine DB gesiepchert werden (ERM machen)

## Datenbank
### Tabellen
Cryptocurrency (CC) Master Data
CC Historical Data
CC Rating


## Welche APIs brauchen wir (Listen nicht abschliessend)
- Metadata V2 https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyInfo
- Listings Latest https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest


### Nur ab Startup Plan
- Trending Gainers & Losers: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingGainerslosers
- Trending Latest: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingLatest
- Trending Most Visited: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyTrendingMostvisited
- OHLCV Historical v2: https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyOhlcvHistorical
- Price Performance Stats v2: https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyPriceperformancestatsLatest
