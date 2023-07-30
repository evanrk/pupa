class Variables:
    def __init__(self):
        self.constant_variables = {}
        self.non_constant_variables = {}

    def add_non_constant_variable(self, name, data, type):
        if self.constant_variables.get(name): # if the variable already exists as a constant, you cant reset it
            raise ValueError("Already constant value") #TODO: fix
        
        # TODO: check type type:
        # elif self.non_constant_variables.get(name):


        else:
            self.non_constant_variables[name] = data
        # self.non_constant_variables[name] = data


    def add_constant_variable(self, name, data, type):
        if self.constant_variables.get(name):
            raise ValueError("Already constant value") #TODO: fix
        
        else:
            self.constant_variables[name] = data
        # self.constant_variables[name] = data


    def change_variable(self, name, data):
        if self.constant_variables.get(name):
            raise ValueError("Tried to change constant value")

        else:
            self.non_constant_variables[name] = data


    def get(self, data):
        constant_get = self.constant_variables.get(data)
        non_constant_get = self.non_constant_variables.get(data)

        print(self.non_constant_variables)

        if not (constant_get or non_constant_get):
            raise SyntaxError(f"Variable {data} does not exist")

        return constant_get if constant_get else non_constant_get

    
    def __repr__(self):
        return f"{self.constant_variables}\n{self.non_constant_variables}"

class Variable:
    def __init__(self, data, type):
        self.type = type
        self.data = data