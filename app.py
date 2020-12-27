from flask import Flask, request, jsonify
from book_cp import compare_price

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/result.html')
def result():
    return app.send_static_file('result.html')

# 比价接口, post参数格式json, 需要isbn书号
@app.route('/compare',methods=['post'])
def compare():
    q_json = request.get_json() #得到post提交过来的json

    # 检查请求参数是否完整
    if 'isbn' not in q_json:
        return jsonify(msg="缺失isbn参数")

    # 返回比价查询的结果
    return jsonify(compare_price(q_json["isbn"]))

app.run()