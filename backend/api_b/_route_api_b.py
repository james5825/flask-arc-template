from datetime import date
from flask import Blueprint
from flask import jsonify
from database.read_data_file import *
from flask import request

from ml.arg_a import *

bp_api_b = Blueprint('api_b', __name__)

'''
example of return string
http://127.0.0.1:5000/apis/api3
'''
@bp_api_b.route('/api3')
def api3():
    return "demo api 3"

'''
example of return dictionary
http://127.0.0.1:5000/apis/api4
'''
@bp_api_b.route('/api4')
def api4():
    dic = {
        "brand": "TSLA",
        "model": "V",
        "year": 2002
    }
    return jsonify(dic)

'''
example of return dataframe with to_json
http://127.0.0.1:5000/apis/api5
'''
@bp_api_b.route('/api5')
def api5():
    return read_csv_demo().to_json(orient='records')


'''
example of read and return json object
http://127.0.0.1:5000/apis/api6
'''
@bp_api_b.route('/api6')
def api6():
    dic_data = read_json_demo()
    return jsonify(dic_data)

'''
example of utilize ml
http://127.0.0.1:5000/apis/api7
'''
@bp_api_b.route('/api7',  methods=['GET'])
def api7():
    return some_ml_7()

'''
example of utilize ml
http://127.0.0.1:5000/apis/api8?op1=tet1&op2=test2
'''
@bp_api_b.route('/api8',  methods=['GET'])
def api8():
    op1 = request.args.get('op1')
    op2 = request.args.get('op2')
    return some_ml_8(op1, op2)

'''
example of utilize ml
http://127.0.0.1:5000/apis/api9
postman>> POST>> Body>> raw>> JSON: {"op1":"str1", "op2": "str2"}
'''
@bp_api_b.route('/api9',  methods=['POST'])
def api9():
    content = request.json
    return some_ml_8(content["op1"], content["op2"])