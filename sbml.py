#Samuel Sundararaman, 111352739

class Node:
    def __init__(self):
        print("init node")

    def evaluate(self):
        return 0

    def execute(self):
        return 0


# Object for numbers
class NumberNode(Node):
    def __init__(self, v):
        if ('.' in v):
            self.value = float(v)
        else:
            self.value = int(v)

    def evaluate(self):
        return self.value

    def negate(self):
        self.value = self.value*-1

    def exponent(self, v):
        self.value = self.value * (10**v.evaluate())

# Object for Booleans
class BooleanNode(Node):
    def __init__(self, v):
        if (v == 'True'):
            self.v = True
        else:
            self.v = False

    def evaluate(self):
        return self.v


class BooleanOpNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == 'or'):
            return self.v1.evaluate() or self.v2.evaluate()
        elif (self.op == 'and'):
            return self.v1.evaluate() and self.v2.evaluate()


class BooleanNotNode(Node):
    def __init__(self, v):
        self.v = v # expression

    def evaluate(self):
        if (self.v == 'True' or self.v.evaluate() == True):
            self.v = False
        else:
            self.v = True
        return self.v


# Object for String node
class StringNode(Node):
    def __init__(self, v):
        self.value = v.strip('(\")|(\')')

    def evaluate(self):
        word = self.value
        toReturn = "\'" + word + "\'"
        return toReturn


class SopNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        word = self.v1.evaluate().strip('(\")|(\')') + self.v2.evaluate().strip('(\")|(\')')
        test = StringNode(word)
        toReturn = test.evaluate()
        return toReturn


class Index(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # Index
        self.v2 = v2  # variable

    def evaluate(self):
        if(type(self.v2.evaluate())==str):
            word = self.v2.evaluate()
            toReturn = "\'" + word[self.v1.evaluate() + 1] + "\'"
            return toReturn
        else:
            array = self.v2.evaluate()
            return array[self.v1.evaluate()]




class StringFind(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # To find
        self.v2 = v2  # String

    def evaluate(self):
        if(type(self.v2.evaluate())==str):
            word = self.v2.evaluate()
            return self.v1.evaluate().strip('(\")|(\')') in word
        else:
            array = self.v2.evaluate()
            return self.v1.evaluate() in array

# Object to print a node
class PrintNode(Node):
    def __init__(self, v):
        self.value = v

    def evaluate(self):
        if (isinstance(self.value, ListNode)):
            self.value = self.value.evaluate()
        elif (type(self.value.evaluate()) is tuple):
            self.value = self.value.tupleString()
        elif (type(self.value.evaluate()) is list):
            self.value = list(self.value.evaluate()).__str__().replace(" ","")
        elif (type(self.value.evaluate()) is str):
            self.value = str(self.value.evaluate()).replace("\'","")
        else:
            self.value = self.value.evaluate()

        print(self.value)


# Object for math operations
class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if(type(self.v1.evaluate()) and type(self.v2.evaluate()) == str):
            return SopNode(self.v1, self.v2).evaluate()
        elif (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == '//' or self.op == 'div'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op == '%' or self.op == 'mod'):
            return self.v1.evaluate() % self.v2.evaluate()
        elif (self.op == '**'):
            return self.v1.evaluate() ** self.v2.evaluate()


# Object for comparison operations
class CompareNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '<'):
            return self.v1.evaluate() < self.v2.evaluate()
        elif (self.op == '>'):
            return self.v1.evaluate() > self.v2.evaluate()
        elif (self.op == '<='):
            return self.v1.evaluate() <= self.v2.evaluate()
        elif (self.op == '>='):
            return self.v1.evaluate() >= self.v2.evaluate()
        elif (self.op == '<>'):
            return self.v1.evaluate() != self.v2.evaluate()
        elif (self.op == '=='):
            return self.v1.evaluate() == self.v2.evaluate()


# Object for Tuples
class TupleNode(Node):
    def __init__(self, v1, v2):
        if ((v1 == None) and (v2 == None)):
            self.v1 = tuple()
        else:
            self.v = (v1, v2)

    def evaluate(self):
        return self.v

    def tupleString(self):
        return self.evaluate().__str__().replace(" " , "")


# Object to create tuples
class TupleArgNode(Node):
    def __init__(self, i, v):
        self.i = i  # Pre existing tuple
        self.v = v  # Element to add to tuple

    def evaluate(self):
        con = list(self.i.evaluate())
        con.append(self.v)
        return tuple(con)

    def tupleString(self):
        return self.evaluate().__str__().replace(" " , "")


class TupleElementNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # Index of element
        self.v2 = v2  # Tuple

    def evaluate(self):
        temp = self.v2
        return temp[self.v1]

# TODO: FIX LISTS
# Object for Lists
class ListNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        if (self.v == None):
            self.v = []
        elif type(self.v) == str:
            self.v = [self.v.strip('(\")|(\')')]
        elif type(self.v) == list:
            self.v = self.v
        elif type(self.v) == Index:
            self.v = self.v
            return [self.v.evaluate()]
        else:
            self.v = self.v
            return [self.v.evaluate()]
        return self.v


class ListPlusNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1.evaluate()
        if type(v2) == str:
            self.v2 = v2.strip('(\")|(\')')
        else:
            self.v2 = v2

    def evaluate(self):
        self.v1.append(self.v2)
        return self.v1


class ListConcatNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1.evaluate().strip('(\")|(\')')
        self.v2 = v2.evaluate().strip('(\")|(\')')

    def evaluate(self):
        return self.v1 + self.v2

class ListConsNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        return [self.v1.evaluate()]+self.v2.evaluate()


class ListFind(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # To find
        self.v2 = v2  # List

    def evaluate(self):
        array = self.v2
        for x in array:
            if x == self.v1:
                return True
        return False

class ListAssignmentNode(Node):
    def __init__(self, v1, v2, v3):
        self.v1 = v1  # variable
        self.v2 = v2  # index
        self.v3 = v3 # new value

    def evaluate(self):
        array = variable_values[self.v1.v1]
        array[self.v2.evaluate()] = self.v3.evaluate()
        variable_values[self.v1.v1] = array
        return self.v1

# TODO: Fix HW 4 Nodes
class BlockNode(Node):
    def __init__(self,sl):
        self.statementList = sl

    def evaluate(self):
        for statement in self.statementList:
            statement.evaluate()



variable_values = {}
variable_objects = {}
function_objects = {}

# TODO: Fix Variable node
class AssignmentNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def evaluate(self):
        variable_values[self.v1.v1] = self.v2.evaluate()
        return self.v1

class VariableNode(Node):
    def __init__(self, v1):
        self.v1 = v1
        variable_values[self.v1] = None
        variable_objects[self.v1] = self

    def evaluate(self):
        return variable_values[self.v1]

# TODO : If Node
class IfNode(Node):
    def __init__(self, v1, v2):
        self.condition = v1
        self.v = v2

    def evaluate(self):
        if(self.condition.evaluate()):
            return self.v.evaluate()
        else:
            return BlockNode(None)




# TODO : If Else Node
class IfElseNode(Node):
    def __init__(self, v1, v2, v3):
        self.condition = v1
        self.v1 = v2 # if to execute
        self.v2 = v3 # else to execute

    def evaluate(self):
        if (self.condition.evaluate()):
            return self.v1.evaluate()
        else:
            return self.v2.evaluate()


# TODO : While Node
class WhileNode(Node):
    def __init__(self, v1, v2):
        self.condition = v1
        self.v = v2

    def evaluate(self):
        while(self.condition.evaluate()):
            self.v.evaluate()


# TODO: Program Node
class ProgramNode(Node):
    def __init__(self,fun, call):
        self.functions = fun
        self.block = call

    def evaluate(self):
        self.block.evaluate()


# TODO: Function Node
class FunctionNode(Node):
    def __init__(self,name, arguments, block, expression):
        self.name = name
        self.args = arguments
        self.block = block
        self.final = ExpressionNode(expression)
        function_objects[self.name] = self

    def evaluate(self):
        return self.final

    def execute(self):
        self.block.evaluate()

# TODO: Function Call Node
class FunctionCallNode(Node):
    def __init__(self, name, parameters):
        self.name = name
        self.params = parameters

    def evaluate(self):
        global variable_values
        global variable_objects
        global function_objects
        old_vars = variable_values
        function = function_objects[self.name]

        new_vars = {}
        function_params = function.args
        for x in range(len(function_params)):
            new_vars[function_params[x]] = self.params[x].evaluate()

        old_vars = variable_values
        variable_values = new_vars
        function.execute()
        result = function.evaluate().evaluate()
        variable_values = old_vars
        return result

# TODO: Expression Node
class ExpressionNode(Node):
    def __init__(self,v):
        self.expression = v

    def evaluate(self):
        return self.expression.evaluate()


#  Add any other tokens
tokens = [
    'LPAREN', 'RPAREN',
    'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'SEMI', 'COMMA', 'POUND',
    'LBRACKET', 'RBRACKET',
    'POWER', 'CONS', 'DIV', 'MOD',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE', 'EXPONENT',
    'LCURLY', 'RCURLY', 'VAR', 'EQUALS'
]

# Tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_SEMI = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_POWER = r'\*\*'
t_CONS = r'::'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'<>'
t_DIV = r'//'
t_MOD = r'%'
t_POUND = r'\#'
t_EXPONENT = 'e'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_EQUALS = r'\='

# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'in': 'IN',
    'div': 'DIVWORD',
    'mod': 'MODWORD',
    'True': 'TRUE',
    'False': 'FALSE',
    'fun': 'FUN'
}

tokens = tokens + list(reserved.values())

def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    return t

# Number token for Number node
def t_NUMBER(t):
    r'(\d+(?:\.\d+)?)'
    try:
        t.value = NumberNode(t.value)
    except ValueError:
        print("SYNTAX ERROR")
        t.value = 0
    return t


# String token for string node
def t_STRING(t):
    r'(\"([^\\\n]|(\\.))*?\") | (\'([^\\\n]|(\\.))*?\')'
    try:
        t.value = StringNode(t.value)
    except ValueError:
        print("SYNTAX ERROR")
        t.value = ""
    return t


# Ignored characters
t_ignore = " \n\t"


def t_error(t):
    print("SYNTAX ERROR")


# Build the lexer
import ply.lex as lex

lex.lex(debug=0)

# Parsing rules, Lowest to highest
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
    ('right', 'CONS'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIV', 'MOD', 'DIVWORD', 'MODWORD'),
    ('right', 'UMINUS'),
    ('right', 'POWER', 'EXPONENT'),
    ('left', 'LBRACKET', 'RBRACKET'),
    ('left', 'POUND'),
    ('left', 'LPAREN', 'RPAREN')
)


# Parsing Rules
# Structure rules


# TODO: Finish all stuff for functions
# Function tokens
def p_program(t):
    """program : functions block"""
    t[0] = ProgramNode(t[1], t[2])

def p_program_block(t):
    """program : block"""
    t[0] = t[1]

def p_functions(t):
    """functions : functions function"""
    t[0] = t[1] + [t[2]]

def p_single_function(t):
    """functions : function"""
    t[0] = [t[1]]

def p_function(t):
    """
     function : FUN VAR LPAREN params RPAREN EQUALS block expression SEMI
    """
    t[0] = FunctionNode(t[2], t[4], t[7], t[8])

def p_params(t):
    """params : params COMMA VAR"""
    t[0] = t[1] + [t[3]]

def p_param(t):
    """ params : VAR"""
    t[0] = [t[1]]

def p_function_call_expression(t):
    """ expression : function_call"""
    t[0] = t[1]

def p_function_call(t):
    """function_call : VAR LPAREN args RPAREN"""
    t[0] = FunctionCallNode(t[1], t[3])

def p_args_list(t):
    """args : args COMMA expression"""
    t[0] = t[1] + [t[3]]

def p_args(t):
    """args : expression"""
    t[0] = [t[1]]


# Block token
def p_block(p):
    """
     block : LCURLY statement_list RCURLY
    """
    p[0] = BlockNode(p[2])

# Statement token
def p_statement_list_def(p):
    """
     statement_list : LCURLY statement_list RCURLY
    """
    p[0] = p[2]

def p_statement_list_list(p):
    """
     statement_list : statement_list statement_list
    """
    p[0] = p[1] + p[2]

def p_statement_list(p):
    """
     statement_list : statement_list statement
    """
    p[0] = p[1] + [p[2]]

def p_statement_list_val(p):
    """
    statement_list : statement
    """
    p[0] = [p[1]]

# Print grammar rule
def p_print_statement(p):
    """
    statement : PRINT LPAREN expression RPAREN SEMI
    """
    p[0] = PrintNode(p[3])

def p_statement(t):
    """statement : expression SEMI"""
    t[0] = t[1]

def p_empty(t):
    """block : LCURLY RCURLY"""
    t[0] = BlockNode([])

def p_empty_statement(t):
    """statement : LCURLY RCURLY"""
    t[0] = BlockNode([])

# TODO: If token
def p_if_statement(t):
    """statement : IF LPAREN expression RPAREN block"""
    t[0] = IfNode(t[3], t[5])

# TODO: If-Else token
def p_if_else_statement(t):
    """statement : IF LPAREN expression RPAREN block ELSE block"""
    t[0] = IfElseNode(t[3], t[5], t[7])

# TODO: While token
def p_while_statement(t):
    """statement : WHILE LPAREN expression RPAREN block"""
    t[0] = WhileNode(t[3], t[5])

# Assignment rule
def p_assignment(p):
    """statement : expression EQUALS expression SEMI"""
    p[0] = AssignmentNode(p[1], p[3])

# TODO: Fix variable
def p_variable(t):
    """expression : VAR"""
    if(t[1] in variable_values):
        t[0] = variable_objects[t[1]]
    else:
        t[0] = VariableNode(t[1])


def p_variable_index(t):
    """expression : expression index"""
    t[0] = Index(t[2], t[1])

def p_expression_group(t):
    """expression : LPAREN expression RPAREN"""
    t[0] = t[2]


# Number grammar rules
# Math Operation rules
def p_expression_binop(t):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DIV expression
                  | expression MOD expression
                  | expression POWER expression
                  | expression DIVWORD expression
                  | expression MODWORD expression"""

    t[0] = BopNode(t[2], t[1], t[3])

def p_expression_float(t):
    """expression : expression EXPONENT expression"""
    t[1].exponent(t[3])
    t[0] = t[1]

def p_expression_uminus(t):
    """expression : MINUS expression %prec UMINUS"""
    t[2].negate()
    t[0] = t[2]

def p_expression_factor(t):
    """expression : factor"""
    t[0] = t[1]


def p_expression_term(t):
    """expression : term"""
    t[0] = t[1]


def p_term_number(t):
    """term : NUMBER"""
    t[0] = t[1]


# String grammar rules
def p_expression_concat(t):
    """expression : factor PLUS expression"""
    t[0] = SopNode(t[1], t[3])


def p_factor_string(t):
    """factor : STRING"""
    t[0] = t[1]


def p_string_in(t):
    """expression : expression IN expression"""
    t[0] = StringFind(t[1], t[3])


# Comparison grammar rule for string and num
def p_expression_compare(t):
    """expression : expression LT expression
                  | expression LE expression
                  | expression GT expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression"""
    t[0] = CompareNode(t[2], t[1], t[3])


# Boolean grammar rules
def p_expression_boolean(t):
    """expression : boolean"""
    t[0] = t[1]


def p_boolean_true(t):
    """boolean : TRUE"""
    t[0] = BooleanNode(t[1])


def p_boolean_false(t):
    """boolean : FALSE"""
    t[0] = BooleanNode(t[1])


def p_expression_booleanop(t):
    """expression : expression OR expression
                  | expression AND expression"""
    t[0] = BooleanOpNode(t[2], t[1], t[3])


def p_expression_booleannot(t):
    """expression : NOT expression"""
    t[0] = BooleanNotNode(t[2])


# Tuple grammar rules
def p_expression_tuple(t):
    """expression : tuple"""
    t[0] = t[1]


def p_tuple(t):
    """tuple : LPAREN in_tuple RPAREN"""
    t[0] = t[2]


def p_emptytuple(t):
    """expression : LPAREN RPAREN"""
    t[0] = TupleNode(None, None)


def p_in_tuple(t):
    """in_tuple : in_tuple COMMA expression"""
    t[0] = TupleArgNode(t[1], t[3].evaluate())


def p_in_tuple2(t):
    """in_tuple : expression COMMA expression"""
    t[0] = TupleNode(t[1].evaluate(), t[3].evaluate())


def p_tuple_arg(t):
    """expression : POUND expression tuple"""
    t[0] = TupleElementNode(t[2].evaluate() - 1, t[3].evaluate())


# List rules
def p_list(t):
    """expression : list"""
    t[0] = t[1]

def p_expression_list(t):
    """list : LBRACKET in_list RBRACKET"""
    t[0] = t[2]


def p_emptylist(t):
    """expression : LBRACKET RBRACKET"""
    t[0] = ListNode(None)


def p_in_list(t):
    """in_list : expression"""
    t[0] = ListNode(t[1])


def p_in_list2(t):
    """in_list : in_list COMMA expression"""
    t[0] = ListPlusNode(t[1], t[3].evaluate())


def p_concat_list(t):
    """expression : expression PLUS list"""
    t[0] = ListConcatNode(t[1], t[3])


def p_list_cons(t):
    """expression : expression CONS expression"""
    t[0] = ListConsNode(t[1], t[3])

def p_list_in(t):
    """expression : expression IN list"""
    t[0] = ListFind(t[1].evaluate(), t[3].evaluate())

def p_index(t):
    """index : LBRACKET expression RBRACKET"""
    t[0] = t[2]


def p_variable_list(t):
    """expression : expression index EQUALS expression"""
    t[0] = ListAssignmentNode(t[1], t[2], t[4])


# Semantic error
def p_error(t):
    print("SEMANTIC ERROR")

import ply.yacc as yacc
import sys
yacc.yacc(debug = 0)

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = fd.read()

try:
    lex.input(code)
    while True:
        token = lex.token()
        if not token: break
        #print(token) # TODO: Uncomment to stop debug
    ast = yacc.parse(code)
    ast.evaluate()
except Exception:
    print("ERROR")
# except SemanticException:
#     print("SEMANTIC ERROR")
# except SyntaxException:
#     print("SYNTAX ERROR")
