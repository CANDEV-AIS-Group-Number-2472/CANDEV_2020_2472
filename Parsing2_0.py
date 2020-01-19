import pandas as pd 
import numpy as np 
import pyAISm

raw_data = pd.read_csv("CCG_AIS_Log_2018-05-01.csv" ,sep="\\")
# print(raw_data)
df = raw_data.iloc[:,2]
print(df)

data = pd.DataFrame(columns=['type','repeat','mmsi','status','turn','speed','knots','accuracy','lon','lat','course','heading','second','maneuver','raim','radio']) 
for row in df:
	if type(row) == float:
		pass
	else:
		decoded = pyAISm.decod_ais(row)
		formating = pyAISm.format_ais(decoded)
		data.append(formating, ignore_index=True)
decoded_data = data.to_csv("CCG_AIS_Log_2018-05-01_DECODED.csv")