from file_processor import file_processor

# file processor class with filter.
## can choose handle file pass filter or not

class filter_processor(file_processor):
	def __init__(self, datapath, lfilter):
		super(filter_processor, self).__init__(datapath)
		self.lfilter = lfilter
		self.bfilter_pass = True

	def open_filter_pass(self, bfilter_pass):
		self.bfilter_pass = bfilter_pass

	def pass_file(self, root , filename):
		in_filter = False
		for filter in self.lfilter:
			if filename.endswith(filter):
				in_filter = True
				break
		
		return self.bfilter_pass == in_filter