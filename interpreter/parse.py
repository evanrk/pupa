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
        return self.parse_block_token()
        
    # examples of parsing tree
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

    def parse_block_token(self):
        """parses block tokens like if, while, for, etc."""

        blocks = []
        if self.current_token.value in ("if", "while", "elif", "else"):
            while self.current_token.value in {"if", "while", "elif"}:
                keyword = self.current_token
                # skips the keyword because it's already been grabbed
                self.forward()
            
                blocks.extend([keyword] + self.parse_binary_level_value("{", self.parse_block_token, return_operator=False))
                # have to skip the outer }
                self.forward()
            
            if self.current_token.value == "else":
                keyword = self.current_token
                # skips the keyword because it's already been grabbed
                self.forward()
                
                # skip the {
                self.forward()

                blocks.extend([keyword] + [self.parse_block_token()])
                # have to skip the outer }
                self.forward()

        else:
            return self.parse_equals()
    
        return blocks

    def parse_equals(self):
        """parses the let and const keywords and the equal sign"""
        # NOTE: variable declaration should always be in the beginning of a line

        declarator = None

        # gets the declarator if there is one
        if self.current_token.value in {"let", "const"}:
            declarator = self.current_token
            self.forward()

        output = self.parse_binary_level_value({"="}, self.parse_boolean_operator)

        # if there is a declarator then it will put it in front, where it should, if its not, then it puts nothing
        return output if not declarator else [declarator] + output

    
    def parse_boolean_operator(self):
        return self.parse_binary_level_value({"and", "or"}, self.parse_comparator)


    def parse_comparator(self):
        """parses the comparators (<, >, etc.)"""
        return self.parse_binary_level_type("comparator", self.parse_addition_and_subtraction)


    def parse_addition_and_subtraction(self):
        """parses addition and subtraction operators"""
        return self.parse_binary_level_value({"+", "-"}, self.parse_multiplication_and_division)
    

    def parse_multiplication_and_division(self):
        """parses multiplication and division operators"""
        return self.parse_binary_level_value({"*", "/"}, self.read_current_token)


    def read_current_token(self):
        """reads and returns the current token"""    
        # handles token
        if self.current_token.type in {"int", "float", "variable", "bool"}: # or self.current_token.value in {"let", "const"}
            token = self.current_token
            self.forward()

        # handles parentheses
        elif self.current_token.value in {"("}:
            # skips opening parentheses
            self.forward()
            # creates new part because its essentially what a parentheses does
            token = self.parse_block_token() # TODO: fix later
            # skips closing parentheses
            self.forward()

        elif self.current_token.value in {"+", "-", "not"}:
            operator = self.current_token
            self.forward()
            output = self.parse_equals() # TODO: fix later
            return [operator, output]

        return token
    
    
    # helper funcs:
    def parse_binary_level_value(self, parse_values, output_func, return_operator=True):
        """parses a binary token based on the operator's value"""
        # parses left side
        left_side = output_func()

        while self.current_token.value in parse_values:
            operator = self.current_token
            self.forward()

            # parses right_side
            right_side = output_func()
            # output  
            # called left_side for conciseness; should be called output
            left_side = [left_side, operator, right_side] if return_operator else [left_side, right_side]
        
        return left_side

    # is separate from the other func for debugging
    def parse_binary_level_type(self, parse_type, output_func, return_operator=True):
        """parses a binary token based on the operator's type"""
        # parses left side   
        left_side = output_func()

        while self.current_token.type == parse_type:
            operator = self.current_token
            self.forward()

            # parses right_side
            right_side = output_func()
            # output  
            # called left_side for conciseness; should be called output
            left_side = [left_side, operator, right_side] if return_operator else [left_side, right_side]
        
        return left_side
            

    def forward(self):
        """moves the index forward and updates the character if it can"""
        self.index += 1
        if self.index < len(self.tokens):
            self.current_token = self.tokens[self.index]