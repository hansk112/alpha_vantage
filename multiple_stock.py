import asyncio
from alpha_vantage.async_support.timeseries import TimeSeries
import os

symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT']

# symbols = [
#     "AIA.NZ", "AIR.NZ", "ANZ.NZ", "ARG.NZ", "ATM.NZ", "AUG.NZ", "CEN.NZ", "CNU.NZ",
#     "EBO.NZ", "FBU.NZ", "FPH.NZ", "FRE.NZ", "GNE.NZ", "GMT.NZ", "IFT.NZ", "KMD.NZ",
#     "MCY.NZ", "MEL.NZ", "MET.NZ", "MFT.NZ", "MHJ.NZ", "NZR.NZ", "NZX.NZ", "PCT.NZ",
#     "POT.NZ", "RBD.NZ", "RYM.NZ", "SKC.NZ", "SKT.NZ", "SPK.NZ", "STU.NZ", "SUM.NZ",
#     "THL.NZ", "TPW.NZ", "TRA.NZ", "VCT.NZ", "VHP.NZ", "VTL.NZ", "WBC.NZ", "ZEL.NZ"
# ]


api_key = os.environ['ALPHA_ADVANTAGE']

async def get_data(symbol):
    ts = TimeSeries(key=api_key)
    data, _ = await ts.get_quote_endpoint(symbol)
    await ts.close()
    return data

loop = asyncio.get_event_loop()
tasks = [get_data(symbol) for symbol in symbols]
group1 = asyncio.gather(*tasks)
results = loop.run_until_complete(group1)
loop.close()
print(results)