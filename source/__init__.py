from flask import Flask

app = Flask(__name__)
app.debug = True

# some default configuration variables
DEFAULT_CONTENT_DIR='content'
CACHE_TYPE='null'
CACHE_DEFAULT_TIMEOUT=0

app.config.from_object(__name__)
app.config.from_pyfile('../config/main.py')

from flask.ext.cache import Cache
cache = Cache(app)

from core import core
app.register_blueprint(core)

from admin import admin
app.register_blueprint(admin, prefix='/admin')
