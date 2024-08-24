from alpha_vantage.timeseries import TimeSeries
import os

api = os.environ['ALPHA_ADVANTAGE']
ts = TimeSeries(key=api)
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
print(data)