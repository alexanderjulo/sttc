import os
from glob import glob
from random import randrange
from exceptions import IOError, OSError, NotImplementedError
from source import app

RENDERMAP = {}

def get_filenames():
	if os.path.isdir(app.config['CONTENT_DIR']):
		entries = []
		for dirpath, dirnames, filenames in os.walk(app.config['CONTENT_DIR']):
			entries.extend(filenames)
		# TODO: filter entries
		return entries
	else:
		return None

def find_file(url):
	possible_filenames = glob(os.path.join(app.config['CONTENT_DIR'], url + '.*'))
	if len(possible_filenames) == 1:
		return possible_filenames[0][len(app.config['CONTENT_DIR'])+1:]
	else:
		# "who wants to put both files into one directory anyway. we thought:
		# if someone is this dumb, our script should handle that in similar manner
		# bl1nk, #sttc @ freenode, 2012-07-13 19:27
		return possible_filenames[randrange(0, len(possible_filenames)-1)]

def get_file_content(filename):
	try:
		f = open(os.path.join(app.config['CONTENT_DIR'], filename))
	except IOError:
		return None
	else:
		file_content = f.read()
		f.close()
		return file_content
		
def get_file_type(filename):
	extension = filename.split('.')[-1]
	try:
		return RENDERMAP[extension]
	except KeyError:
		return None
		
def get_file_object(filename):
	file = get_file_type(filename)
	if file:
		return file(filename)
	else:
		return None
		
class File(object):
	def __init__(self, filename):
		raise NotImplementedError
		
	def __html__(self):
		return self.html
		
	def __getitem__(self, item):
		return self.meta[item]

class MarkdownFile(File):
	
	from markdown import Markdown
	
	def __init__(self, filename):
		self.content = get_file_content(filename)
		self._parse()
		
	def _parse(self):
		self.md = self.Markdown(extensions=['meta'])
		self.html = self.md.convert(self.content)
		self.meta = self.md.Meta

RENDERMAP['md'] = MarkdownFile
