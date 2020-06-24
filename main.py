from huobi import RequestClient
from huobi.model import *

#TODO:deploy to server in japan
#TODO:compare the network latency between two domain api.huobi.pro and api-aws.huobi.pro, and then choose the better one for you.

request_client = RequestClient()

#system_status = request_client.get_system_status()
#print(system_status)

# Get the timestamp from Huobi server and print on console
timestamp = request_client.get_exchange_timestamp()
print(timestamp)

# # Get the latest btcusdt‘s candlestick data and print the highest price on console
# candlestick_list = request_client.get_latest_candlestick("btcusdt", CandlestickInterval.DAY1, 20)
# for item in candlestick_list:
#     print(item.high)