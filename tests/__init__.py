import os
import shutil
import unittest
import tempfile
import source

class STTCTestCase(unittest.TestCase):

	def setUp(self):
		source.app.config['TESTING'] = True
		self.dir = tempfile.mkdtemp()
		source.app.config['CONTENT_DIR'] = self.dir
		self.subdir = tempfile.mkdtemp(dir=self.dir)
		self.files = []
		self.files.append(tempfile.mkstemp(suffix='.md', dir=self.dir))
		self.files.append(tempfile.mkstemp(suffix='.md', dir=self.subdir))
		self.app = source.app.test_client()
		
	def test_index(self):
		filenames = []
		for fd, filename in self.files:
			filenames.append(filename[len(self.dir)+1:-len(filename.split('.')[-1])-1])
		result = self.app.get('/')
		assert sorted(filenames) == sorted(eval(result.data))

	def tearDown(self):
		shutil.rmtree(self.dir)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(STTCTestCase))
	return suite

def run():
	test = unittest.TextTestRunner()
	result = test.run(suite())
	return result.wasSuccessful()
