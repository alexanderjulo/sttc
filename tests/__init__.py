import os
import unittest
import tempfile
import source

class FileTestCase(unittest.TestCase):

	def setUp(self):
		source.app.config['TESTING'] = True

	def tearDown(self):
		pass

def suite():
	suite = unittest.TestSuite()
	suite.addTest(unittest.makeSuite(FileTestCase))
	return suite

def run():
	test = unittest.TextTestRunner()
	result = test.run(suite())
	return result.wasSuccessful()
