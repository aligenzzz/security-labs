from colorama import Fore

def red(content: str) -> str:
    return Fore.LIGHTRED_EX + content + Fore.RESET

def blue(content: str) -> str:
    return Fore.LIGHTBLUE_EX + content + Fore.RESET