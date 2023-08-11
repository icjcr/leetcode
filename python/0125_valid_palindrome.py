import re


def is_palindrome(s: str) -> bool:
    s = re.sub(r'[_\W]+', '', s).lower()
    return s == s[::-1]
