from flask import Flask

www = Flask(__name__)

from serve import serve
www.register_blueprint(serve)

from admin import admin
www.register_blueprint(admin, prefix='/admin')
