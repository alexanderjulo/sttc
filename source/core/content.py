import os
from exceptions import IOError, OSError
from source import app, cache

@cache.memoize()
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

@cache.memoize()
def get_file_content(filename):
	try:
		f = open(os.path.join(app.config['DEFAULT_CONTENT_DIR'], filename))
	except IOError:
		return None
	else:
		file_content = f.read()
		f.close()
		return file_content