import os
from exceptions import IOError, OSError, NotImplementedError
from source import app

RENDERMAP = {}

def get_filenames():
	if os.path.isdir(app.config['DEFAULT_CONTENT_DIR']):
		def _walk(dir, prefix=()):
			for name in os.listdir(dir):
				full_name = os.path.join(dir, name)
				if os.path.isdir(full_name):
					_walk(full_name, prefix + (name,))
				else:
					entries.append('/'.join(prefix + (name,)))
		entries = []
		_walk(app.config['DEFAULT_CONTENT_DIR'])
		# TODO: filter entries
		return entries
	else:
		return None

def get_file_content(filename):
	try:
		f = open(os.path.join(app.config['DEFAULT_CONTENT_DIR'], filename))
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
