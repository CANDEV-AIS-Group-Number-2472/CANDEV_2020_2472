import pyAISm
string = "\c:1525143369,C:359,s:P-Parke*6F\!AIVDM,1,1,8,B,15O<@N001sG:hgHL6F?m;T6D00S@,0*7C"
a = string.split("\\")
ais_data = pyAISm.decod_ais(a[2])
ais_format = pyAISm.format_ais(ais_data)
print(ais_format)
