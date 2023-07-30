class Token:
    debug_token_type = False

    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type
    
    def __repr__(self) -> str:
        
        return (f"{self.type}: " if Token.debug_token_type else "") + f"{self.value}"

 
# types
class Integer(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "int")

class Float(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "float")

class String(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "string")

class Boolean(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "bool")

class List(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "list")

class Dict(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "dict")


# operations
class Operator(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "operator")

class Boolean_Operator(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "boolean operator")

class Comparator(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "comparator")


# words
class Variable(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "variable")

class Reserved(Token):
    def __init__(self, value) -> None:
        super().__init__(value, "reserved")