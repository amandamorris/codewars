"""Description:

Write a function called validParentheses that takes a string of parentheses, and
determines if the order of the parentheses is valid. validParentheses should
return true if the string is valid, and false if it's invalid.

Examples: 
validParentheses( "()" ) => returns true 
validParentheses( ")(()))" ) => returns false 
validParentheses( "(" ) => returns false 
validParentheses( "(())((()())())" ) => returns true 
"""
#pseudocode: use a stack, push open parens on the stack, pop from stack for
#closed parens

def valid_parentheses(string):
    my_stack = []
    for char in string:
        if char == "(":
            my_stack.append(char)
            continue
        elif char == ")":
            if not my_stack:
                return False
            my_stack.pop()
            continue
    return my_stack == []
