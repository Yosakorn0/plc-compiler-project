# python -m components.parsers
from components.lexica import MyLexer
from components.memory import Memory
from sly import Parser

class MyParser(Parser):
    debugfile = 'parser.out'
    start = 'statement'
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    # Lower rows = higher precedence. So the parser reads it top → bottom.
    # precedence = (
    #     ('left', "+", MINUS),         (associativity, operator1, operator2, ...),
    #     ('left', TIMES, DIVIDE),      (associativity, operator1, operator2, ...),
    #     ('right', UMINUS),            (associativity, operator1, operator2, ...),
    #     )

    # same line = same priority
    precedence = (
        ('left', OR),
        ('left', AND), #higher priority
    )

    def __init__(self):
        self.memory:Memory = Memory()

    # Variable assignment rule from template (not used in propositional logic evaluator)
    # rule meaning: statement → NAME = expr
    # @_('NAME ASSIGN expr')
    # def statement(self, p):
    #     var_name = p.NAME
    #     value = p.expr
    #     self.memory.set(variable_name=var_name,value=value, data_type=type(value))
    #     # Note that I did not return anything

    @_('expr')
    # S -> E
    def statement(self, p) -> int:
        return p.expr

    # The example with literals
    @_('expr AND expr')
    # E -> E + E
    def expr(self, p):
        # You can refer to the token 2 ways
        # Way1: using array
        print(f"Evaluating AND: {p.expr0} ^ {p.expr1}")
        # Way2: using symbol name. 
        # Here, if you have more than one symbols with the same name
        # You have to indiciate the number at the end.
        return p.expr0 and p.expr1

    # The example with normal token
    @_('expr OR expr')
    def expr(self, p):
        print(f"Evaluating OR: {p.expr0} v {p.expr1}")
        return p.expr0 or p.expr1
    
    @_('TRUTH')
    def expr(self, p):
        print(f"Reading TRUTH token: {p.TRUTH}")
        return p.TRUTH == 't'


if __name__ == "__main__":
    lexer = MyLexer()
    # parser = MyParser()
    text = "f v f ^ t" # final output "f"
    # text = "t v f ^ f" # final output "t"

    # Memory is not used because propositional logic evaluator does not require variable storage
    # memory = Memory() 
    parser = MyParser()
    # text = "1 + 2 + 3"
    result = parser.parse(lexer.tokenize(text))
    print(result)
    # print(memory)



# from components.ast.statement import Expression, Expression_math, Expression_number, Operations
# class ASTParser(Parser):
#     debugfile = 'parser.out'
#     start = 'statement'
#     # Get the token list from the lexer (required)
#     tokens = MyLexer.tokens
#     precedence = (
#         ('left', "+", MINUS),
#         # ('left', TIMES, DIVIDE),
#         # ('right', UMINUS),
#         )

#     @_('expr')
#     def statement(self, p) -> int:
#         p.expr.run()
#         return p.expr.value

#     @_('expr "+" expr')
#     def expr(self, p) -> Expression:
#         parameter1 = p.expr0
#         parameter2 = p.expr1
#         expr = Expression_math(operation=Operations.PLUS, parameter1=parameter1, parameter2=parameter2)
#         return expr
    
#     @_('expr MINUS expr')
#     def expr(self, p) -> Expression:
#         parameter1 = p.expr0
#         parameter2 = p.expr1
#         expr = Expression_math(operation=Operations.MINUS, parameter1=parameter1, parameter2=parameter2)
#         return expr

#     @_('NUMBER')
#     def expr(self, p) -> Expression:
#         return Expression_number(number=p.NUMBER)
        
# if __name__ == "__main__":
#     lexer = MyLexer()
#     # parser = MyParser()
#     text = "9 + 2 + 3"
#     memory = Memory()
#     parser = ASTParser()
#     # text = "1 + 2 + 3"
#     result = parser.parse(lexer.tokenize(text))
#     print(result)
#     # print(memory)