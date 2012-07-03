#!/usr/bin/env python2.7

from flask.ext.script import Manager
from src import www

manager = Manager(www)

if __name__ == '__main__':
	manager.run()