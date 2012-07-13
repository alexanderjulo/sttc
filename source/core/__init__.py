from flask import Blueprint

mod = Blueprint('core', __name__)

from content import *
import routes