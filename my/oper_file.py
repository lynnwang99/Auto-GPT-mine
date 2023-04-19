import json

command_result_file_path = "/Users/wangyilian/PycharmProjects/Auto-GPT-mine/my/cache/command_result.txt"
auth_file_path = "/Users/wangyilian/PycharmProjects/Auto-GPT-mine/my/cache/input.txt"
openai_reply_file_path = "/Users/wangyilian/PycharmProjects/Auto-GPT-mine/my/cache/openai_reply.txt"
step_file_path = "/Users/wangyilian/PycharmProjects/Auto-GPT-mine/my/cache/step.txt"
ai_info_file_path = "/Users/wangyilian/PycharmProjects/Auto-GPT-mine/my/cache/ai_info.txt"
tips_file_path = "/Users/wangyilian/PycharmProjects/Auto-GPT-mine/my/cache/tips.txt"


def write_command_result(text):
    write_file(command_result_file_path, text)


def read_command_result():
    return read_file(command_result_file_path)


def read_auth():
    return read_file(auth_file_path)


def write_auth(text):
    write_file(auth_file_path, text)


def write_openai_reply(text):
    write_file(openai_reply_file_path, text)


def read_openai_reply():
    return read_file(openai_reply_file_path)


def write_step(text):
    write_file(step_file_path, text)


def read_step():
    return read_file(step_file_path)


def read_ai_info():
    return read_file(ai_info_file_path)


def write_ai_info(text):
    write_file(ai_info_file_path, text)


def write_tips(text):
    write_file(tips_file_path, text)


def read_tips():
    return read_file(tips_file_path)


def write_file(file_path, text):
    # 打开文件，如果文件不存在则创建一个新文件
    file = open(file_path, "w")
    # 写入字符串到文件
    file.write(text)
    # 关闭文件
    file.close()


def read_file(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        return data



