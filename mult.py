from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='6H4YYNQULX3JAJGZ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
pprint(data.head(2))