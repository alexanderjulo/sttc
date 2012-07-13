from flask import abort
from . import mod
from content import get_filenames, get_file_object

@mod.route('/')
def index():
	filenames = get_filenames()
	if filenames:
		return str(filenames)
	else:
		abort(500)

@mod.route('/<path:filename>/')
def get_file(filename):
	file = get_file_object(filename)
		# TODO: - render the file content using the configured renderer
		#       - maybe a default NullRenderer that returns what you put in
		#       - or pass it to a template
	if file:
		return file.html
	else:
		abort(404)
