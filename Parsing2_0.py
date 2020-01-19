import pandas as pd 
import numpy as np 
import pyAISm

raw_data = pd.read_csv("CCG_AIS_Log_2018-05-01.csv", sep="\\")
# print(raw_data)
df = raw_data.iloc[:,2]
# print(df)
# df_str = df.astype(str)
# print(df_str)

ais_data = df.apply(lambda x: x.pyAISm.decod_ais(df))
# ais_format = pyAISm.format_ais(ais_data)
# print(ais_format)
