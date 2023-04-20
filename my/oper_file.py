import os


auth_file_path = os.path.abspath("cache/input.txt")
openai_reply_file_path = os.path.abspath("cache/openai_reply.txt")
step_file_path = os.path.abspath("cache/step.txt")
ai_info_file_path = os.path.abspath("cache/ai_info.txt")
tips_file_path = os.path.abspath("cache/tips.txt")


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
    if os.path.exists(file_path):
        pass
    else:
        file_path = file_path.replace("/my", "")
    file = open(file_path, "w")
    # 写入字符串到文件
    file.write(text)
    # 关闭文件
    file.close()


def read_file(file_path):
    if os.path.exists(file_path):
        pass
    else:
        file_path = file_path.replace("/my", "")
    with open(file_path, "r") as f:
        data = f.read()
        return data


# 区分模式写入文件（未使用）
def write_file_with_mode(file_path, text, mode):
    if mode is None:
        mode = "w"
    # 打开文件，如果文件不存在则创建一个新文件， 模式分为覆盖写入:w，追加写入:a
    file = open(file_path, mode)
    # 写入字符串到文件
    file.write(text)
    # 关闭文件
    file.close()



