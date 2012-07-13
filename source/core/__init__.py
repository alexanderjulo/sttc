from flask import Blueprint, abort

from source import app

from exceptions import IOError, OSError
import os

core = Blueprint('core', __name__)

def get_filenames():
	try:
		# TODO: make files directory configurable
		entries = os.listdir('files')
	except OSError as e:
		raise
	else:
		# TODO: filter entries
		return entries

# TODO: - cache this function
#       - maybe a default NullCache that doesn't cache at all
#       - but where should we initialize the cache?
def get_file_content(filename):
	try:
		# TODO: make files directory configurable
		f = open('files/' + filename)
	except IOError as e:
		raise
	else:
		file_content = f.read()
		f.close()
		return file_content

@app.route('/')
def index():
	try:
		filenames = get_filenames()
	except OSError:
		abort(500)
	else:
		# TODO: pass that to a template or something
		return str(filenames)

@app.route('/<path:filename>/')
def get_file(filename):
	try:
		# TODO: - render the file content using the configured renderer
		#       - maybe a default NullRenderer that returns what you put in
		#       - or pass it to a template
		file_content = get_file_content(filename)
	except IOError:
		abort(404)
	else:
		return file_content
