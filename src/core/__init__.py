from flask import Blueprint, abort

from src import app

from exceptions import IOError

core = Blueprint('core', __name__)

# TODO: - cache this function
#       - maybe a default NullCache that doesn't cache at all
#       - but where should we initialize the cache?
def get_file_content(filename):
	try:
		# TODO: make files directory configurable
		f = open('files/' + filename)
	except:
		raise IOError
	else:
		file_content = f.read()
		f.close()
		return file_content

@app.route('/<filename>')
def get_file(filename):
	try:
		# TODO: - render the file content using the configured renderer
		#       - maybe a default NullRenderer that returns what you put in
		file_content = get_file_content(filename)
	except IOError:
		abort(404)
	else:
		return file_content
