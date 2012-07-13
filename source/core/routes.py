from flask import abort
from source import cache
from source.core import mod, get_filenames, find_file, get_file_object

@mod.route('/')
@cache.memoize()
def index():
	filenames = get_filenames()
	if filenames:
		return str(filenames)
	else:
		abort(500)

@mod.route('/<path:url>/')
@cache.memoize()
def get_file(url):
	filename = find_file(url)
	if not filename:
		abort(404)
	# TODO: - render the file content using the configured renderer
	#       - maybe a default NullRenderer that returns what you put in
	#       - or pass it to a template
	return get_file_object(filename).html
