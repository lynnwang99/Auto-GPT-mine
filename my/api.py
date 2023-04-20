import time

import flask
import json
from flask import request
import oper_file as file_util

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
    tips = file_util.read_tips()
    need_auth = 0
    if step == "1":
        pass
    elif step == "2":
        need_auth = 1
        content = file_util.read_openai_reply()
    elif step == "3":
        pass
    elif step == "4":
        content = file_util.read_command_result()
    elif step == "99":
        content = file_util.read_tips()
        need_auth = 1
    elif step == "0":
        content = file_util.read_tips()
        need_auth = 1
    if is_json(content):
        resu = {"step": step, "content": json.loads(content), "needAuth": need_auth}
    else:
        resu = {"step": step, "content": content, "needAuth": need_auth}
    return resu


@server.route('/authOperation', methods=['post'])
def auth_operation():
    file_util.write_openai_reply("")
    # 获取请求参数
    # type【1: y 2: n 3: y -n 4: 自定义命令】
    operation_type = request.json.get('type')
    num = request.json.get('num')
    cust_command = request.json.get('custCommand')
    ai_info = request.json.get("aiInfo")
    if ai_info is not None:
        # 需要创建AI
        ai_info = request.json.get("aiInfo")
        ai_name = ai_info["aiName"]
        ai_role = ai_info["aiRole"]
        ai_goals = ai_info["aiGoals"]
        info = {"ai_name": ai_name, "ai_role": ai_role, "ai_goals": ai_goals}
        file_util.write_ai_info(json.dumps(info))
    step = file_util.read_step()
    tips = ""
    need_create_ai = 0
    result_json = {}
    user_input = ''
    if operation_type == 1:
        user_input = 'y'
    elif operation_type == 2:
        user_input = 'n'
    elif operation_type == 3:
        user_input = 'y -' + str(num)
    else:
        # todo wangyl 暂时不支持自定义命令
        # user_input = cust_command
        user_input = 'y'
    file_util.write_auth(user_input)
    if step == "99" and operation_type == 2:
        tips = "Welcome to Auto-GPT! \nCreate an AI-Assistant: Set your AI name and role and goals."
        result_json["tips"] = tips
        need_create_ai = 1
    elif operation_type == 2:
        return {}
    else:
        openai_reply = file_util.read_openai_reply()
        while len(openai_reply) == 0:
            time.sleep(1)
            openai_reply = file_util.read_openai_reply()
            if is_json(openai_reply):
                result_json["reply"] = json.loads(openai_reply)
            else:
                result_json["reply"] = openai_reply
    result_json["need_create_ai"] = need_create_ai
    return result_json


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    server.run(debug=True, port=8888, host='0.0.0.0')  # 指定端口、host,0.0.0.代表不管几个网卡，任何ip都可以访问