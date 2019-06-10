# Samuel Sundararaman, 111352739

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
        if (v == 'True' or v.evaluate() == True):
            self.v = False
        else:
            self.v = True

    def evaluate(self):
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


class StringIndex(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # Index
        self.v2 = v2  # String

    def evaluate(self):
        word = self.v2
        toReturn = "\'" + word[self.v1 + 1] + "\'"
        return toReturn


class StringFind(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # To find
        self.v2 = v2  # String

    def evaluate(self):
        word = self.v2
        return self.v1.strip('(\")|(\')') in word


# Object to print a node
class PrintNode(Node):
    def __init__(self, v):
        self.v = v

    def evaluate(self):
        print(self.v.evaluate())


# Object for math operations
class BopNode(Node):
    def __init__(self, op, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.op = op

    def evaluate(self):
        if (self.op == '+'):
            return self.v1.evaluate() + self.v2.evaluate()
        elif (self.op == '-'):
            return self.v1.evaluate() - self.v2.evaluate()
        elif (self.op == '*'):
            return self.v1.evaluate() * self.v2.evaluate()
        elif (self.op == '/'):
            return self.v1.evaluate() / self.v2.evaluate()
        elif (self.op == '//'):
            return self.v1.evaluate() // self.v2.evaluate()
        elif (self.op == '%'):
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


# Object to create tuples
class TupleArgNode(Node):
    def __init__(self, i, v):
        self.i = i  # Pre existing tuple
        self.v = v  # Element to add to tuple

    def evaluate(self):
        con = list(self.i.evaluate())
        con.append(self.v)
        return tuple(con)


class TupleElementNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # Index of element
        self.v2 = v2  # Tuple

    def evaluate(self):
        temp = self.v2
        return temp[self.v1]


# Object for Lists
class ListNode(Node):
    def __init__(self, v):
        if (v == None):
            self.v = []
        elif type(v) == str:
            self.v = [v.strip('(\")|(\')')]
        else:
            self.v = [v]

    def evaluate(self):
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


class ListIndex(Node):
    def __init__(self, v1, v2):
        self.v1 = v1  # Index
        self.v2 = v2  # List

    def evaluate(self):
        array = self.v2
        return array[self.v1]


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

class BlockNode(Node):
    def __init__(self,sl):
        self.statementList = sl

    def evaluate(self):
         for statement in self.statementList:
             statement.evaluate()

# TODO: Create assignment node

variable_values = {}
variable_objects = {}
class VariableNode(Node):
    def __init__(self, v1, v2):
            self.name = v1
            self.v = v2
            variable_objects[self.name] = self
            variable_values[self.name] = self.v.evaluate()

    def evaluate(self):
        return variable_values[self.name]

    def execute(self, v):
        self.v = v
        variable_values[self.name] = self.v.evaluate()
        return variable_objects[self.name]


# TODO : If Node
class IfNode(Node):
    def __init__(self, v1, v2):
        self.condition = v1
        self.v = v2

    def evaluate(self):
        if(self.condition.evaluate()):
            return self.v.evaluate()



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
        # while (self.condition.evaluate):
        #     if (self.condition.evaluate()):
        #         self.v.evaluate()
        #         variable_values.update()
        #         variable_objects.update()
        return(True)





# TODO: Add tokens for if, else, while, print
tokens = [
    'LPAREN', 'RPAREN',
    'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'SEMI', 'COMMA', 'POUND',
    'LBRACKET', 'RBRACKET',
    'POWER', 'CONS',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'DIV', 'MOD', 'LCURLY', 'RCURLY', 'VAR', 'EQUALS'

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
    'True': 'TRUE',
    'False': 'FALSE'
}

tokens = tokens + list(reserved.values())


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words
    return t

# Number token for Number node
def t_NUMBER(t):
    r'-?\d*(\d\.|\.\d)\d* | \d+'
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


# Boolean token
# def t_TRUE(t):
#     'True'
#     t = BooleanNode(t.value)
#     return t
#
#
# def t_FALSE(t):
#     'False'
#     t = BooleanNode(t.value)
#     return t
#

# Ignored characters
t_ignore = " \n\t"

def t_error(t):
    print("SYNTAX ERROR")


# Build the lexer
import ply.lex as lex

# Parsing rules, Lowest to highest
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'NOT'),
    ('left', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE'),
    ('right', 'CONS'),
    ('left', 'IN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIV', 'MOD'),
    ('right', 'UMINUS'),
    ('right', 'POWER'),
    ('left', 'LBRACKET', 'RBRACKET'),
    ('left', 'POUND'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'IF', 'WHILE','ELSE'),
    ('left', 'LCURLY', 'RCURLY')
)


# Parsing Rules
# TODO: Grammar rules for blocks and control statements

# Block token
def p_block(p):
    """
     block : LCURLY statement_list RCURLY
    """
    p[0] = BlockNode(p[2])

# Statement token
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

def p_statement(t):
    """statement : expression SEMI"""
    t[0] = t[1]

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
    if(isinstance(p[1], VariableNode)):
        p[0] = variable_objects[p[1].name].execute(p[3])
    else:
        p[0] = VariableNode(p[1], p[3])


def p_variable(t):
    """expression : VAR"""
    if(t[1] in variable_objects):
        t[0] = variable_objects[t[1]]
    else:
        t[0] = t[1]


# Print grammar rule
def p_print_statement(p):
    """
    statement : PRINT LPAREN expression RPAREN SEMI
    """
    p[0] = PrintNode(p[3])


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
                  | expression POWER expression"""
    t[0] = BopNode(t[2], t[1], t[3])


def p_expression_uminus(t):
    """expression : MINUS expression %prec UMINUS"""
    t[0] = -t[2]


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


def p_string_index(t):
    """expression : factor LBRACKET NUMBER RBRACKET"""
    t[0] = StringIndex(t[3].evaluate(), t[1].evaluate())


def p_string_in(t):
    """expression : expression IN expression"""
    t[0] = StringFind(t[1].evaluate(), t[3].evaluate())


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
    t[0] = ListNode(t[1].evaluate())


def p_in_list2(t):
    """in_list : in_list COMMA expression"""
    t[0] = ListPlusNode(t[1], t[3].evaluate())


def p_concat_list(t):
    """expression : expression PLUS list"""
    t[0] = ListConcatNode(t[1], t[3])


def p_index(t):
    """index : LBRACKET expression RBRACKET"""
    t[0] = t[2].evaluate()


def p_list_index(t):
    """list : expression index"""
    t[0] = ListIndex(t[2], t[1].evaluate())

def p_list_cons(t):
    """expression : expression CONS list"""
    node = ListNode(t[1].evaluate())
    t[0] = ListConcatNode(node, t[3])


def p_list_in(t):
    """expression : expression IN list"""
    t[0] = ListFind(t[1].evaluate(), t[3].evaluate())


# Semantic error
def p_error(t):
    print("SEMANTIC ERROR")


import ply.yacc as yacc
lex.lex(debug=0)
yacc.yacc(debug=0)


import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
# fd = open(sys.argv[1], 'r')
# TODO: Read entire file as one string
with open(sys.argv[1], 'r') as myfile:
    data = myfile.read().replace('\n', '')
root = yacc.parse(data)
root.evaluate()

