from flask import Blueprint, abort

from source import app, cache

from exceptions import IOError, OSError
import os

core = Blueprint('core', __name__)

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

@app.route('/')
def index():
	filenames = get_filenames()
	if filenames:
		return str(filenames)
	else:
		abort(500)

@app.route('/<path:filename>/')
def get_file(filename):
	file_content = get_file_content(filename)
		# TODO: - render the file content using the configured renderer
		#       - maybe a default NullRenderer that returns what you put in
		#       - or pass it to a template
	if file_content:
		return file_content
	else:
		abort(404)
