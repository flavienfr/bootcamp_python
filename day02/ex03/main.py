from csvreader import CsvReader

if __name__ == "__main__":
	with CsvReader('good.csv', ',', True) as file:
		if file == None:
			print("File is corrupted")
		else:
			data = file.getdata()
			print (data, end = '')

			#header = file.getheader()
			#print(header, end = '')
