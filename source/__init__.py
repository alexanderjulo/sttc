from flask import Flask

app = Flask(__name__)
app.debug = True

from core import core
app.register_blueprint(core)

from admin import admin
app.register_blueprint(admin, prefix='/admin')
