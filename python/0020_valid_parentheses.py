def is_valid(s: str) -> bool:
    stack = []
    brackets_map = {"(": ")", "[": "]", "{": "}"}
    for c in s:
        try:
            stack.append(brackets_map[c])
            continue
        except KeyError:
            pass

        try:
            if stack.pop() != c:
                return False
        except (KeyError, IndexError):
            return False

    return not bool(stack)
