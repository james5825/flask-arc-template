from datetime import date
from flask import Blueprint
from flask import jsonify
from database.read_data_file import *
from flask import request

from ml.arg_a import *

bp_api_c = Blueprint('api_c', __name__)

'''
example of return string
http://127.0.0.1:5000/apis/api99
'''
@bp_api_c.route('/api99')
def api99():
    return "demo api 999"
