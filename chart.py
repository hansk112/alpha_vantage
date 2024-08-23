from alpha_vantage.foreignexchange import ForeignExchange
from pprint import pprint
cc = ForeignExchange(key='6H4YYNQULX3JAJGZ')
# There is no metadata in this call
data, _ = cc.get_currency_exchange_rate(from_currency='NZD',to_currency='USD')
pprint(data)