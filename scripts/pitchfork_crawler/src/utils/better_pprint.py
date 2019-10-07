from colorama import Back, Fore, Style
from pprint import pformat


def pprint(obj, global_ident=4, color=Fore.GREEN, **kwargs):
    lines = pformat(obj, **kwargs).split("\n")
    for line in lines:
        print(color + " " * global_ident + line + Style.RESET_ALL)
