class Token:
    debug_token_type = True

    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type
    
    def __repr__(self) -> str:    
        return (f"{self.type}: " if Token.debug_token_type else "") + f"{self.value}"

 
class Type(Token):
    def __init__(self, value, type) -> None:
        super().__init__(value, type)


# types
class Integer(Type):
    def __init__(self, value) -> None:
        super().__init__(value, "int")

class Float(Type):
    def __init__(self, value) -> None:
        super().__init__(value, "float")

class String(Type):
    def __init__(self, value) -> None:
        super().__init__(value, "string")

class Boolean(Type):
    def __init__(self, value) -> None:
        super().__init__(value, "bool")

class List(Type):
    def __init__(self, value) -> None:
        super().__init__(value, "list")

class Dict(Type):
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