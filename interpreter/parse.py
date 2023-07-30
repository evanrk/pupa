class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index]

    # [5, +, 5, *, 5]
    # [5, +, [5, *, 5]]

    def parse(self):
        # if self.current_token.type in {"int", "float", "operator", "variable"}:
        #     return self.parse_equals()
        return self.parse_equals()
        
    # 5 + 5 * 5 + 5
    
    #     +
    #    / \
    #   /   +
    #  /   / \
    # 5   *   5
    #    / \
    #   5   5 


    # 5 * 5 + 5 + 5
    
    #           +
    #          / \
    #         +   5
    #        / \
    #       *   5
    #      / \
    #     5   5

    # IMPORTANT:
    # order of operations goes from bottom as most important and top as least important

    def parse_equals(self):
        # NOTE: variable declaration should always be in the beginning of a line

        if self.current_token.value in {"let", "const"}:
            declarator = self.current_token
            self.forward()

        return self.parse_binary_token_level({"="}, self.parse_addition_and_subtraction)


    def parse_addition_and_subtraction(self):
        return self.parse_binary_token_level({"+", "-"}, self.parse_multiplication_and_division)
    

    def parse_multiplication_and_division(self):
        return self.parse_binary_token_level({"*", "/"}, self.read_current_token)


    def read_current_token(self):
        if self.current_token.type in {"int", "float", "variable"}: # or self.current_token.value in {"let", "const"}
            token = self.current_token
            self.forward()

        if self.current_token.value == "(":
            # skips opening parentheses
            self.forward()
            # creates new part because its essentially what a parentheses does
            token = self.parse_equals()
            # skips closing parentheses
            self.forward()

        return token
    
    
    def parse_binary_token_level(self, parse_values, output_func):
        # parses left side
        left_side = output_func()

        while self.current_token.value in parse_values:
            operator = self.current_token
            self.forward()

            # parses right_side
            right_side = output_func()
            # output  
            left_side = [left_side, operator, right_side] # called left_side for conciseness; should be called output
        
        return left_side


    def forward(self):
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]