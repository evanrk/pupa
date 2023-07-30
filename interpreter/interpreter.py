from interpreter.data.tokens_classes import *
from interpreter.data.variables import *

class Interpreter:
    def __init__(self, tokens_tree, data):
        self.tokens_tree = tokens_tree
        self.data = data

    def interpret(self, tokens_tree=None):
        if not tokens_tree:
            tokens_tree = self.tokens_tree

        
        if isinstance(tokens_tree, list):
            # handle non-constant variable
            if tokens_tree[0].value == "let":
                variable = tokens_tree[1]
                right_side = self.interpret(tokens_tree=tokens_tree[3])

                self.data.add_non_constant_variable(variable.value, right_side, right_side.type)
                return self.data # TODO: change to not print out

            # handle constant variable
            elif tokens_tree[0].value == "const":
                variable = tokens_tree[1]
                right_side = self.interpret(tokens_tree=tokens_tree[3])

                self.data.add_constant_variable(variable.value, right_side, right_side.type)
                return self.data # TODO: change to not print out

            elif len(tokens_tree) == 2:
                # unary evaluation:

                operator = tokens_tree[0]
                # gets the token next to the operator with recursion
                right_side = self.interpret(tokens_tree=tokens_tree[1])

                right_type = right_side.type
                right_value = getattr(self, f"read_{right_type}")(right_side.value)

                if operator.type == "operator":
                    
                    # gets the type of the output
                    if right_type == "int":
                        output_type = Integer
                    elif right_type == "float":
                        output_type = Float
                    elif right_type == "bool":
                        output_type = Boolean
                    
                    # processes the output
                    if operator.value == "+":
                        if output_type in {Integer, Float}:
                            output = right_value
                        elif output_type == Boolean:
                            output = right_value

                    elif operator.value == "-":
                        if output_type in {Integer, Float}:
                            output = -right_value
                        elif output_type == Boolean:
                            output = not right_value
                    
                elif operator.value == "not":
                    output = not right_value


                # handle switching type back to token_type
                if output_type == Boolean:
                    if output == True:
                        return output_type("true")
                    else:
                        return output_type("false")
                else:
                    return output_type(output)                


            elif len(tokens_tree) == 3:
                # operator is static and doesn't need recursion
                operator = tokens_tree[1]

                right_token = self.interpret(tokens_tree=tokens_tree[2])
                
                # the left token is a special case because of the equal sign
                # if there's an equal sign, you don't want to compute what the variable is (don't do recursion)
                if operator.value == "=":
                    self.data.change_variable(tokens_tree[0].value, right_token)
                    return self.data # TODO: change to not print out
                else:
                    # gets the left and right tokens with recursion
                    left_token = self.interpret(tokens_tree=tokens_tree[0])

                
                # gets the left and right token types
                left_type = left_token.type
                right_type = right_token.type


                # gets the left and right value in python builtin classes
                left_value = getattr(self, f"read_{left_type}")(left_token.value)
                right_value = getattr(self, f"read_{right_type}")(right_token.value)



                # no other way to do it without a bunch of if statements :(

                # add
                if operator.value == "+":
                    if left_type == "int" and right_type == "int":
                        output_type = Integer
                    else:
                        output_type = Float
                    
                    output = left_value + right_value
                
                # subtract
                elif operator.value == "-":
                    if left_type == "int" and right_type == "int":
                        output_type = Integer
                    else:
                        output_type = Float
                    
                    output = left_value - right_value
                
                # multiply
                elif operator.value == "*":
                    if left_type == "int" and right_type == "int":
                        output_type = Integer
                    else:
                        output_type = Float
                    
                    output = left_value * right_value
                
                # divide
                elif operator.value == "/":
                    output_type = Float
                    
                    output = left_value / right_value
                

                # all comparators have the same output type
                elif operator.type == "comparator":
                    output_type = Boolean
                    
                    # less than
                    if operator.value == "<":
                        output = left_value < right_value
                    
                    # greater than
                    elif operator.value == ">":
                        output = left_value > right_value
                    
                    # less than or equal to
                    elif operator.value == "<=":
                        output = left_value <= right_value
                    
                    # greater than or equal to
                    elif operator.value == ">=":
                        output = left_value >= right_value
                    
                    # equal to
                    elif operator.value == "==":
                        output = left_value == right_value
                    
                    # not equal to
                    elif operator.value == "!=":
                        output = left_value != right_value
                    
                # and
                elif operator.value == "and":
                    output_type = Boolean
                    output = left_value and right_value
                # or
                elif operator.value == "or":
                    output_type = Boolean
                    output = left_value or right_value

                # if its not in here, there's a problem
                else:
                    raise SyntaxError(f"{operator} not handled")

                # handle switching type back to token_type
                if output_type == Boolean:
                    if output == True:
                        return output_type("true")
                    else:
                        return output_type("false")
                else:
                    return output_type(output)
                
        
        else:
            if tokens_tree.type == "variable":
                return self.read_variable(tokens_tree.value)

            return tokens_tree
                
        
    
    # helper funcs:
    def read_int(self, value):
        return int(value)

    def read_float(self, value):
        return float(value)
    
    def read_bool(self, value):
        if value == "true":
            return True
        elif value == "false":
            return False
        else:
            raise ValueError()

    def read_variable(self, value):
        data = self.data.get(value)
        return data

    def read_string(self, value):
        return str(value)
    
    # def read_list(self, value):
    #     return list(value)
    
    # def read_dict(self, value):
    #     return list(value)
    