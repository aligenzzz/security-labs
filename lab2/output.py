from colorama import Fore
import json


def yellow(content: str) -> str:
    return Fore.LIGHTYELLOW_EX + content + Fore.RESET

def red(content: str) -> str:
    return Fore.LIGHTRED_EX + content + Fore.RESET

def blue(content: str) -> str:
    return Fore.LIGHTBLUE_EX + content + Fore.RESET

def green(content: str) -> str:
    return Fore.LIGHTGREEN_EX + content + Fore.RESET

def dict_to_str(package: dict) -> str:
    return json.dumps(package, indent=4)
