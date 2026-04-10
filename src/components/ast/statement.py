from enum import Enum
from abc import ABC, abstractmethod

class Statement:
    """What is statement?
    In this calculator project, a statement is each line of math expression.
    In this case, it will consit of tree of math expression
    """
    def __init__(self) -> None:
        root_node
        

class Operations(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIVIDE = 3
    AND = 4
    OR = 5
    XOR = 6
    NOT = 7

class Expression(ABC): 
    @abstractmethod
    def __init__(self) -> None:
        self.signature:str = ""
        self.value:object = None
        self.prefix:str = ""

    @abstractmethod
    def run(self) -> None:
        pass

    def visualize(self, level:int=0) -> str:
        """Returns a string representation of the tree with indentation."""
        pass

class Expression_math(Expression):
    def __init__(self, operation:Operations, parameter1:Expression, parameter2:Expression):
        # Init attribute
        self.operation:Operations = operation
        self.parameter1:Expression = parameter1
        self.parameter2:Expression = parameter2
        self.signature:str = ""
        self.value:object = None
        self.prefix:str = ""
        # Checking Logic
        assert operation in Operations

        # Create a children
        self.children = [self.parameter1, self.parameter2]
        
        # Calculate SDT (Prefix & Value)
        self.run() # In actual SDT, we calculate during init
        
    def run(self) -> None:
        # evaluate child first
        for child in self.children:
            child.run()

        if(self.operation == Operations.PLUS):
            self.value = self.parameter1.value + self.parameter2.value
            self.prefix = f"+ {self.parameter1.prefix} {self.parameter2.prefix}"
        elif(self.operation == Operations.MINUS):
            self.value = self.parameter1.value - self.parameter2.value
            self.prefix = f"- {self.parameter1.prefix} {self.parameter2.prefix}"
        elif(self.operation == Operations.TIMES):
            self.value = self.parameter1.value * self.parameter2.value
            self.prefix = f"* {self.parameter1.prefix} {self.parameter2.prefix}"
        elif(self.operation == Operations.DIVIDE):
            self.value = self.parameter1.value / self.parameter2.value
            self.prefix = f"/ {self.parameter1.prefix} {self.parameter2.prefix}"
        elif(self.operation == Operations.AND):
            self.value = self.parameter1.value and self.parameter2.value
            self.prefix = f"^ {self.parameter1.prefix} {self.parameter2.prefix}"
        elif(self.operation == Operations.OR):
            self.value = self.parameter1.value or self.parameter2.value
            self.prefix = f"v {self.parameter1.prefix} {self.parameter2.prefix}"
        elif(self.operation == Operations.XOR):
            self.value = self.parameter1.value ^ self.parameter2.value
            self.prefix = f"x {self.parameter1.prefix} {self.parameter2.prefix}"
        else:
            raise ValueError(f"{self.operation=} is not supported.")
        
        self.signature = f"Expression: {self.operation.name} {self.parameter1.value} {self.parameter2.value}"

    def visualize(self, level:int=0) -> str:
        indent = "  " * level
        res = f"{indent}|-- {self.operation.name}\n"
        res += self.parameter1.visualize(level + 1)
        res += self.parameter2.visualize(level + 1)
        return res

    def __repr__(self) -> str:
        return self.signature

class Expression_number(Expression):
    def __init__(self, number:object, prefix:str=None) -> None:
        self.value:object = number
        self.prefix:str = prefix if prefix else str(number)
        self.signature:str= str(number)
        
    def run(self) -> None:
        pass

    def visualize(self, level:int=0) -> str:
        indent = "  " * level
        return f"{indent}|-- {self.signature} (Value: {self.value})\n"

    def __repr__(self) -> str:
        return f"Node({self.signature})"

class Expression_unary(Expression):
    def __init__(self, operation:Operations, parameter:Expression):
        self.operation:Operations = operation
        self.parameter:Expression = parameter
        self.children = [self.parameter]
        self.value:object = None
        self.prefix:str = ""
        self.run()

    def run(self) -> None:
        self.parameter.run()
        if self.operation == Operations.NOT:
            self.value = not self.parameter.value
            self.prefix = f"! {self.parameter.prefix}"
        
        self.signature = f"Unary({self.operation.name} {self.parameter.value})"

    def visualize(self, level:int=0) -> str:
        indent = "  " * level
        res = f"{indent}|-- {self.operation.name}\n"
        res += self.parameter.visualize(level + 1)
        return res

    def __repr__(self) -> str:
        return self.signature

if __name__ == "__main__":
    number1 = Expression_number(number=8)
    number2 = Expression_number(number=9)
    expr = Expression_math(Operations.MINUS, parameter1=number1, parameter2=number2)
    expr.run()
    # print(expr.hshow())
    print(expr.value)