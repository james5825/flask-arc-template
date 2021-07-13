from flask import Blueprint
from flask import jsonify

bp_api_a = Blueprint('api_a', __name__)

'''
example of return string
http://127.0.0.1:5000/apis/api1
'''
@bp_api_a.route('/api1')
def api1():
    return "demo api 1"

'''
example of return dictionary
http://127.0.0.1:5000/apis/api2
'''
@bp_api_a.route('/api2')
def api2():
    dic = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    return jsonify(dic)
