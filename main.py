

def is_valid(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack=[]

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
            print("This is the stack: ", stack)

is_valid(s="()")
