import flask
import json
from flask import request
import my.oper_file as file_util

"""
flask: web框架，通过flask提供的装饰器@server.route()将普通函数转换为服务登录接口
"""

# 创建一个服务,把当前这个python文件当做一个服务
server = flask.Flask(__name__)


# 获取响应数据
@server.route('/getResponse', methods=['get'])
def get_response():
    step = file_util.read_step()
    content = ""
    tips = ""
    need_auth = 0
    if step == "1":
        tips = "思考中..."
    elif step == "2":
        tips = "等待用户授权"
        content = file_util.read_openai_reply()
        need_auth = 1
    elif step == "3":
        tips = "执行命令中..."
    elif step == "4":
        tips = "执行结果"
        content = file_util.read_command_result()
    elif step == "99":
        tips = "是否继续执行？"
        content = file_util.read_tips()
        need_auth = 1
    elif step == "0":
        tips = "创建AI"
        content = file_util.read_tips()
        need_auth = 1
    resu = {"step": step, "content": content, "tips": tips, "needAuth": need_auth}
    return resu


@server.route('/authOperation', methods=['post'])
def auth_operation():
    user_input = ''
    # type【1: y 2: n 3: y -n 4: 自定义命令】
    operation_type = request.json.get('type')
    num = request.json.get('num')
    cust_command = request.json.get('custCommand')
    if operation_type == 1:
        user_input = 'y'
    elif operation_type == 2:
        user_input = 'n'
    elif operation_type == 3:
        user_input = 'y -' + str(num)
    else:
        user_input = cust_command
    file_util.write_auth(user_input)
    resu = {'code': 200, 'message': '操作成功!'}
    return json.dumps(resu, ensure_ascii=False)


@server.route('/createGoals', methods=['post'])
def create_goals():
    ai_name = request.json.get("aiName")
    ai_role = request.json.get("aiRole")
    ai_goals = request.json.get("aiGoals")
    info = {"ai_name": ai_name, "ai_role": ai_role, "ai_goals": ai_goals}
    file_util.write_ai_info(json.dumps(info))
    resu = {'code': 200, 'message': '操作成功!'}
    return json.dumps(resu, ensure_ascii=False)


@server.route('/getDetail', methods=['get'])
def get_detail():
    step = request.args.get("step")
    content = ""
    if step == "2":
        content = file_util.read_openai_reply()
    elif step == "4":
        content = file_util.read_command_result()
    return content


# @server.route("/operation", methods=['post'])
# def operation():
#     ai_name = request.json.get("aiName")
#     ai_role = request.json.get("aiRole")
#     ai_goals = request.json.get("aiGoals")
#     user_operation = request.json.get("operation")


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.代表不管几个网卡，任何ip都可以访问