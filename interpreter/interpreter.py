from interpreter.tokens_classes import *

class Interpreter:
    def __init__(self, tokens_tree):
        self.tokens_tree = tokens_tree
    

    def interpret(self, tokens_tree=None):
        if not tokens_tree:
            tokens_tree = self.tokens_tree

        
        if isinstance(tokens_tree, list):
            if len(tokens_tree) == 3:
                # gets the left and right tokens with recursion
                left_token = self.interpret(tokens_tree=tokens_tree[0])
                right_token = self.interpret(tokens_tree=tokens_tree[2])
                
                # operator is static and doesn't need recursion
                operator = tokens_tree[1]

                # gets the left and right token types
                left_type = left_token.type
                right_type = right_token.type

                # gets the left and right value in python builtin classes
                left_value = getattr(self, f"read_{left_type}")(left_token.value)
                right_value = getattr(self, f"read_{right_type}")(right_token.value)

                if operator.value == "+":
                    output = left_value + right_value
                elif operator.value == "-":
                    output = left_value - right_value
                elif operator.value == "*":
                    output = left_value * right_value
                elif operator.value == "/":
                    output = left_value / right_value
                else:
                    print(operator)
                    raise SyntaxError()

                if operator.value == "/":
                    return Float(output)
                else:    
                    return Integer(output) if "int" in {left_token.type, right_token.type} else Float(output)
                
        
        else:
            return tokens_tree
                
        
    
    # helper funcs:
    def read_int(self, value):
        return int(value)

    def read_float(self, value):
        return float(value)
    
    def read_variable(self, value):
        pass
    
    def read_string(self, value):
        return str(value)
    
    def read_list(self, value):
        return list(value)
    
    def read_dict(self, value):
        return list(value)
    