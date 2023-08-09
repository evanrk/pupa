from interpreter.data.tokens_classes import *

class Tokenizer:
    # basic chars
    digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    safe_chars = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "_"}
    
    # operations
    operators = {"+","-","*", "/","(",")","="}

    # syntax
    skip_chars = {" "}
    break_chars = {"{", "}"}
    
    # boolean
    booleans = {"true", "false"}
    boolean_operators = {"and", "or", "not"}
    comparators = {">", "<", ">=", "<=", "!=", "=="}

    # built-in types
    types = {"String", "int", "float", "Array", "Set", "Dict"}

    # reserved keywords
    variable_declarators = {"let", "const"}
    reserved = {"if", "elif", "else", "while", "for", "in"}

    def __init__(self, text):
        self.text = text
        self.index = 0
        self.char = self.text[self.index]

        self.tokens = []

    def make_tokens(self):
        while self.index < len(self.text):
            if self.char in self.skip_chars:
                self.forward()
            
            elif self.char in self.break_chars:
                self.tokens.append(Break_Character(self.char))
                self.forward()

            elif self.char in Tokenizer.digits:
                self.tokenize_number()
            
            elif self.char in Tokenizer.operators or self.char in Tokenizer.comparators or self.char == "!":
                self.tokenize_operator()

            elif self.char in Tokenizer.safe_chars:
                self.tokenize_keyword()

        return self.tokens


    def tokenize_number(self):
        """Creates a token if it's either an integer or float"""
        token = ""
        while (self.char in Tokenizer.digits) and self.index < len(self.text):
            token += self.char
            self.forward()
        

        if self.char == ".": # __.__ is a float -- is still one token
            token += "."
            self.forward()    
            while (self.char in Tokenizer.digits) and self.index < len(self.text):
                token += self.char
                self.forward()
            
            self.tokens.append(Float(token))
            return

        self.tokens.append(Integer(token))


    def tokenize_operator(self):
        operator = self.char
        self.forward()


        if (operator + self.char) in self.comparators: # some boolean operators are two-long
            self.tokens.append(Comparator(operator + self.char)) 
            self.forward() # have to go forward because this char was just used

        elif operator in self.comparators:
            self.tokens.append(Comparator(operator))
            # dont go forward because it wasn't used
        
        else:
            self.tokens.append(Operator(operator))
            # also dont go forward because it wasn't used


    def tokenize_keyword(self):
        """Creates a token for a keyword (variable name or reserved words)"""
        token = ""
        while (self.char in Tokenizer.safe_chars) and self.index < len(self.text):
            token += self.char
            self.forward()

        if token in self.booleans:
            self.tokens.append(Boolean(token))

        elif token in self.reserved:
            self.tokens.append(Reserved(token))
        
        elif token in self.variable_declarators:
            self.tokens.append(Variable_Declarator(token))

        else:
            self.tokens.append(Variable(token))


    # helper funcs:
    def forward(self):
        self.index += 1
        if self.index < len(self.text):
            self.char = self.text[self.index]