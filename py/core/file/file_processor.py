import datetime
import os

# base file processor class.
## for all files in dir

class file_processor(object):
	def __init__(self, dir):
		self.dir = dir
		self.btime_coster = False
		self.bshow_name = False
		self.bfilecounter = False
		self.filecounter = 0

	def set_open_timecoster(self, btime_coster):
		self.btime_coster = btime_coster

	def set_open_filecounter(self, bfilecounter):
		self.bfilecounter = bfilecounter
	
	def set_open_showname(self, bshow_name):
		self.bshow_name = bshow_name

	def on_process(self):
		for root, dirs, files in os.walk(self.dir):
			for filename in files:
				if self.pass_file(root, filename):
					self.process_file(root, filename)
					if self.bfilecounter:
						self.filecounter = self.filecounter + 1
					if self.bshow_name:
						print "+ ", filename

	def before_process(self):
		pass

	def after_process(self):
		pass

	def pass_file(self, root , filename):
		return True

	def process(self):
		self.before_process()
		self.on_process()
		self.after_process()

	def process_file(self, root , filename ):
		pass

	def start(self):
		if not self.btime_coster:
			self.process()
		else:
			start_time = datetime.datetime.now()
			self.process()
			end_time = datetime.datetime.now()
			cost_time = end_time - start_time
			print "this process cost time", cost_time.seconds,"s."
		if self.bfilecounter:
			print "total: ", self.filecounter, " files."
