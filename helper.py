from constants import *

def add_escapes(s : str) -> str:
    res = ''
    for i in range(len(s)):
        res += s[i] if s[i] not in SYMBOLS else '\\' + s[i]

    return res
