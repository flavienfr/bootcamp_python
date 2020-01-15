class CsvReader():

	def __init__(self, file, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.file = file
		self.sep = sep
		self.header = header
		self.top = skip_top
		self.bot = skip_bottom
		self.n_line = 0
	
	#def is_empty(self, lst):
	#	for elem in lst:
	#		pass
	#	return False

	def getheader(self):
		if self.header:
			return self.file.readline()

	def getdata(self):
		data = ''
		n_elem = len(self.file.readline().split(self.sep))
		for line in self.file:
			if (len(line.split(self.sep))) != n_elem:
				return None
			#check = line.split(self.sep)
			#if self.is_empty(check):
			#	return None
			if self.header and self.n_line == 0:
				pass
			elif self.top != 0:
				if self.n_line in range(self.bot, self.top):
					data += line
			else:
				data += line
			self.n_line += 1
		return data

	def __enter__(self):
		try:
			self.file = open(self.file, 'r')
			return self
		except (FileNotFoundError, IOError):
			self.file = None

	def __exit__(self, type, value, traceback):
		if self.file:
			self.file.close()
