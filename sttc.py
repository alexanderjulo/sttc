#!/usr/bin/env python2.7

from flask.ext.script import Manager
from source import app

manager = Manager(app)

@manager.command
def test():
	"""Run the tests to ensure that the platform as working as expected."""
	import tests
	# executes the test, if the tests pass this it returns 0 to the command line
	# otherwise it returns 1, this is especially useful for commit hooks and similar
	if tests.run():
		exit(0)
	else:
		exit(1)

if __name__ == '__main__':
	manager.run()