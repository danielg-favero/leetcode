def isValid(s: str) -> bool:
    """
    Given a string s containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, 
    determine if the input string is valid.

    An input string is valid if:

    - Open brackets must be closed by the same type of brackets.
    - Open brackets must be closed in the correct order.
    - Every close bracket has a corresponding open bracket of the same type.
    """
    stack = []

    # Estrategicamente a chave do `mapping` é elemento que fecha
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch in mapping:
            # Comparar pra ver se o elemento que abre na stack é o mesmo elemento que está no mapping
            if stack and stack[-1] == mapping[ch]:
                stack.pop()
            else:
                return False
        else:
            # Os únicos que podem ser adicionados são: (, { e [
            stack.append(ch)
    
    # Se ainda há elementos na stack, a string ainda é inválida
    return not len(stack)

print(isValid("()[]{}"))