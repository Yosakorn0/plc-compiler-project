# python -m components.parsers
from .lexica import MyLexer
from .memory import Memory
from sly import Parser
from .ast.statement import Expression, Expression_math, Expression_number, Operations

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
    # Evaluates logical AND of two expressions and returns an AST node
    @_('expr AND expr')
    def expr(self, p):
        # Create a binary operation node for AND
        node = Expression_math(operation=Operations.AND, parameter1=p.expr0, parameter2=p.expr1)
        print(f"AST Node Created: {node.operation.name} (Value: {node.value})")
        return node

    # Grammar rule: expr → expr OR expr
    # Evaluates logical OR of two expressions and returns an AST node
    @_('expr OR expr')
    def expr(self, p):
        # Create a binary operation node for OR
        node = Expression_math(operation=Operations.OR, parameter1=p.expr0, parameter2=p.expr1)
        print(f"AST Node Created: {node.operation.name} (Value: {node.value})")
        return node
    
    # Grammar rule: expr → TRUTH
    # Base case: single truth value (t or f) returns an AST leaf node
    @_('TRUTH')
    def expr(self, p):
        # Convert 't' to True, 'f' to False
        val = (p.TRUTH == 't')
        # Create a leaf node representing the truth value
        node = Expression_number(number=val, prefix=p.TRUTH)
        print(f"AST Leaf Created: {p.TRUTH} (Value: {val})")
        return node


if __name__ == "__main__":
    # Test the parser with sample expressions
    lexer = MyLexer()
    # parser = MyParser()
    text = "f v f ^ t"  # Example: False OR (False AND True) -> False
    # text = "t v f ^ f" # Example: True OR (False AND False) -> True

    # Memory is not used because propositional logic evaluator does not require variable storage
    # memory = Memory() 
    parser = MyParser()
    result_node = parser.parse(lexer.tokenize(text))
    
    if result_node:
        print(f"\nFinal Value: {result_node.value}")
        print(f"Final Prefix: {result_node.prefix}")
        print("\nVisual Tree Structure:")
        print(result_node.visualize())


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