from flask import Blueprint

mod = Blueprint('core', __name__)

import content
import routes