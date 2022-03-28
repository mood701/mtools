import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), '../../core/file'))
from filter_processor import filter_processor

class fullname_printer(filter_processor):
	def __init__(self, datapath, lfilter):
		super(fullname_printer, self).__init__(datapath, lfilter)
		self.set_open_timecoster(True)
		self.set_open_filecounter(True)

	def process_file(self, root , filename ):
		print os.path.join(root,filename)

	def before_process(self):
		print 'before process'

	def after_process(self):
		print 'after process'

if __name__ == "__main__":
	fp = fullname_printer('../../..', ['.py'])
	fp.start()
