"""Set up the AI and its goals"""
import json
import time

from colorama import Fore, Style

from autogpt import utils
from autogpt.config.ai_config import AIConfig
from autogpt.logs import logger
import my.oper_file as my_file_util


def prompt_user() -> AIConfig:
    """Prompt the user for input

    Returns:
        AIConfig: The AIConfig object containing the user's input
    """
    ai_name = ""
    # Construct the prompt
    logger.typewriter_log(
        "Welcome to Auto-GPT! ",
        Fore.GREEN,
        "run with '--help' for more information.",
        speak_text=True,
    )

    logger.typewriter_log(
        "Create an AI-Assistant:",
        Fore.GREEN,
        "Enter the name of your AI and its role below. Entering nothing will load"
        " defaults.",
        speak_text=True,
    )

    # Get AI Name from User
    logger.typewriter_log(
        "Name your AI: ", Fore.GREEN, "For example, 'Entrepreneur-GPT'"
    )

    # todo wangyl 创建目标
    my_file_util.write_step("0")
    tips = "Welcome to Auto-GPT! \nCreate an AI-Assistant: Set your AI name and role and goals."
    my_file_util.write_tips(tips)
    ai_info = my_file_util.read_ai_info()
    while len(ai_info) == 0:
        time.sleep(1)
        ai_info = my_file_util.read_ai_info()
    ai_info_json = json.loads(ai_info)
    ai_name = ai_info_json["ai_name"]
    if ai_name == "":
        ai_name = "Entrepreneur-GPT"

    logger.typewriter_log(
        f"{ai_name} here!", Fore.LIGHTBLUE_EX, "I am at your service.", speak_text=True
    )

    # Get AI Role from User
    logger.typewriter_log(
        "Describe your AI's role: ",
        Fore.GREEN,
        "For example, 'an AI designed to autonomously develop and run businesses with"
        " the sole goal of increasing your net worth.'",
    )
    ai_role = ai_info_json["ai_role"]
    if ai_role == "":
        ai_role = "an AI designed to autonomously develop and run businesses with the"
        " sole goal of increasing your net worth."

    # Enter up to 5 goals for the AI
    logger.typewriter_log(
        "Enter up to 5 goals for your AI: ",
        Fore.GREEN,
        "For example: \nIncrease net worth, Grow Twitter Account, Develop and manage"
        " multiple businesses autonomously'",
    )
    print("Enter nothing to load defaults, enter nothing when finished.", flush=True)
    ai_goals = ai_info_json["ai_goals"]
    if not ai_goals:
        ai_goals = [
            "Increase net worth",
            "Grow Twitter Account",
            "Develop and manage multiple businesses autonomously",
        ]
    # 清空本地AI配置
    my_file_util.write_ai_info("")

    return AIConfig(ai_name, ai_role, ai_goals)
