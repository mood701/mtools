import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), '../../core/file'))
from file_processor_async import processor_async

class fullname_printer(processor_async):
	def __init__(self, datapath):
		super(fullname_printer, self).__init__(datapath)
		self.set_count(fileparser_count=3)

	def before_process(self):
		print 'before process'

	def after_process(self):
		print 'after process'
	
	def on_fileparser(self, filepath):
		print('on_fileparser:{}'.format(filepath))
		return filepath
	
	def on_datahandler(self, rawdata):
		print('on_datahandler:{}'.format(rawdata))
		return rawdata
	
	def on_dataoutputer(self, outdata):
		print('on_dataoutputer:{}'.format(outdata))
		pass

if __name__ == "__main__":
	fp = fullname_printer('../../..')
	fp.start()
