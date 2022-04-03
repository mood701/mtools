import datetime
import os
import queue
import threading
import sys


# base processor class.
## for all files in dir async

# producer-consumer
## fileparser --rawdata--> datahandler --data--> dataoutputer

# Will exec sys.exit() when all task done.
## do everything after process in after_process

class processor_async(object):
	def __init__(self, dir):
		self.dir = dir
		self.set_count()
		self.filequeue = queue.Queue()
		self.fileparsers = []
		self.rawqueue = queue.Queue()
		self.datahanders = []
		self.dataqueue = queue.Queue()
		self.dataoutputers = []
		self.dir = dir
	
	def set_count(self, fileparser_count=1, datahander_count = 5, dataouputer_count = 1):
		self.fpcount = fileparser_count
		self.dhcount = datahander_count
		self.docount = dataouputer_count
	
	def fileparser(self, filequeue, rawqueue):
		while True:
			filepath = filequeue.get()
			resraw = self.on_fileparser(filepath)
			if resraw:
				rawqueue.put(resraw)
			filequeue.task_done()
	
	def datahandler(self, rawqueue, dataqueue):
		while True:
			rawdata = rawqueue.get()
			outdata = self.on_datahandler(rawdata)
			if outdata:
				dataqueue.put(outdata)
			rawqueue.task_done()
	
	def dataoutputer(self, dataqueue):
		while True:
			outdata = dataqueue.get()
			self.on_dataoutputer(outdata)
			dataqueue.task_done()

	def on_fileparser(self, filepath):
		pass
	
	def on_datahandler(self, rawdata):
		pass
	
	def on_dataoutputer(self, outdata):
		pass

	def create_threads(self):
		for i in range(self.fpcount):
			t = threading.Thread(target=self.fileparser, \
				args=(self.filequeue, self.rawqueue), name="fileparser_t {}".format(i))
			t.daemon = True
			self.fileparsers.append(t)
			t.start()
		
		for i in range(self.dhcount):
			t = threading.Thread(target=self.datahandler, \
				args=(self.rawqueue, self.dataqueue), name="datahandler_t {}".format(i))
			t.daemon = True
			self.datahanders.append(t)
			t.start()
		
		for i in range(self.docount):
			t = threading.Thread(target=self.dataoutputer, \
				args=(self.dataqueue,), name="dataoutputer_t {}".format(i))
			t.daemon = True
			self.dataoutputers.append(t)
			t.start()

	def waitfinished(self):
		self.filequeue.join()
		self.rawqueue.join()
		self.dataqueue.join()


	def process(self):
		self.create_threads()

		for root, dirs, files in os.walk(self.dir):
			for filename in files:
				if self.pass_file(root, filename):
					self.filequeue.put(root+filename)
		
		self.create_threads()
		self.waitfinished()


	def before_process(self):
		pass

	def after_process(self):
		pass

	def pass_file(self, root , filename):
		return True

	def start(self):
		self.before_process()
		self.process()
		self.after_process()
		sys.exit()
