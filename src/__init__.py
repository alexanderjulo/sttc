from flask import Flask

app = Flask(__name__)

from serve import serve
app.register_blueprint(serve)

from admin import admin
app.register_blueprint(admin, prefix='/admin')
