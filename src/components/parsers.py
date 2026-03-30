# python -m components.parsers
from .lexica import MyLexer
from .memory import Memory
from sly import Parser

# Parser class for propositional logic expressions using sly library
class MyParser(Parser):
    debugfile = 'parser.out'  # File for parser debugging output
    start = 'statement'  # Starting grammar symbol
    # Get the token list from the lexer (required)
    tokens = MyLexer.tokens
    # Lower rows = higher eedence. So the parser reads it top → bottom.
    # precedence = (
    #     ('left', "+", MINUS),         (associativity, operator1, operator2, ...),
    #     ('left', TIMES, DIVIDE),      (associativity, operator1, operator2, ...),
    #     ('right', UMINUS),            (associativity, operator1, operator2, ...),
    #     ('left', OR, AND)             # Equal priority
    #     )

    # Operator precedence: AND has higher precedence than OR. Bottommost have higher priority. 
    # same line = same priority
    precedence = (
        ('left', OR),    # Left-associative OR
        ('left', AND),   # Left-associative AND (higher priority)
    )

    def __init__(self):
        self.memory:Memory = Memory()  # Initialize memory (not used in logic evaluator)

    # Variable assignment rule from template (not used in propositional logic evaluator)
    # rule meaning: statement → NAME = expr
    # @_('NAME ASSIGN expr')
    # def statement(self, p):
    #     var_name = p.NAME
    #     value = p.expr
    #     self.memory.set(variable_name=var_name,value=value, data_type=type(value))
    #     # Note that I did not return anything

    # Grammar rule: statement → expr
    # Returns the result of the expression
    @_('expr')
    # S -> E
    def statement(self, p) -> tuple:
        return p.expr

    # Grammar rule: expr → expr AND expr
    # Evaluates logical AND of two expressions
    @_('expr AND expr')
    def expr(self, p):
        # Extract boolean values from subexpressions
        value1 = p.expr0[0]
        value2 = p.expr1[0]

        # Extract prefix notations
        prefix1 = p.expr0[1]
        prefix2 = p.expr1[1]

        # Evaluate AND operation
        value = value1 and value2

        # Build prefix expression: ^ prefix1 prefix2
        prefix = "^ " + prefix1 + " " + prefix2

        print(f"Evaluating AND: {value1} ^ {value2} -> {value}")  # Debug output
        return value, prefix

    # Grammar rule: expr → expr OR expr
    # Evaluates logical OR of two expressions
    @_('expr OR expr')
    def expr(self, p):
        # Extract boolean values from subexpressions
        value1 = p.expr0[0]
        value2 = p.expr1[0]

        # Extract prefix notations
        prefix1 = p.expr0[1]
        prefix2 = p.expr1[1]

        # Evaluate OR operation
        value = value1 or value2

        # Build prefix expression: v prefix1 prefix2
        prefix = "v " + prefix1 + " " + prefix2

        print(f"Evaluating OR: {value1} v {value2} -> {value}")  # Debug output
        return value, prefix
    
    # Grammar rule: expr → TRUTH
    # Base case: single truth value (t or f)
    @_('TRUTH')
    def expr(self, p):
        print(f"Reading TRUTH token: {p.TRUTH}")  # Debug output
        # Convert 't' to True, 'f' to False; return tuple (bool, prefix)
        return p.TRUTH == 't', p.TRUTH


if __name__ == "__main__":
    # Test the parser with sample expressions
    lexer = MyLexer()
    # parser = MyParser()
    text = "f v f ^ t"  # Example: False OR (False AND True) -> False
    # text = "t v f ^ f" # Example: True OR (False AND False) -> True

    # Memory is not used because propositional logic evaluator does not require variable storage
    # memory = Memory() 
    parser = MyParser()
    # text = "1 + 2 + 3"  # Not used for logic
    result = parser.parse(lexer.tokenize(text))  # Parse and evaluate
    print(result)  # Output: (bool_value, prefix_notation)
    # print(memory)  # Not used


# from components.ast.statement import Expression, Expression_math, Expression_number, Operations
# class ASTParser(Parser):
#     debugfile = 'parser.out'
#     start = 'statement'
#     # Get the token list from the lexer (required)
#     tokens = MyLexer.tokens
#     eedence = (
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