import csv
import pyAISm
import ais

with open ('TEST.csv', 'r') as csv_data:
	csv_reader = csv.reader(csv_data)

	for line in csv_reader:
		print(line)
		if line[2] != '!AIVDM':
		 	line[2] = '!AIVDM'
		 	line[0] = ''
		 	line[1] = ''
		 	print(line[2])
		 	print(line)
		 	# ID = line[2]+","+line[3]+","+line[4]+","+line[5]+","+line[6]+","+line[7]+","+line[8]
		 	# print(ID)
with open('CCG_AIS_Log_2018-05-01_DECODE.nmea', 'w') as updatedData:
	updatedData_writer = csv.writer(updatedData)
	
	updatedData_writer.writerow(line)

with open('DECODE.csv','r') as file:
	for aline in file:
		# try:
			msg = aline.lstrip(",")
			print(msg)
		# 	ais_data = pyAISm.decod_ais(msg)  # Return a dictionnary
		# 	print('data:')
		# 	print(ais_data)

		# 	ais_format = pyAISm.format_ais(ais_data)  # A more human readable dictionnary
		# 	print(ais_format)  # Accessing the value of the key
		# except pyAISm.UnrecognizedNMEAMessageError as e:
		# 	print (e)
		# except pyAISm.BadChecksumError as e:
		# 	print (e)
		# except Exception as e:
		# 	print (e)
		# print('End of file')
