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
        if (v == 'true'):
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
        if (v == 'true' or v.evaluate() == True):
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
        self.value = v

    def execute(self):

        if (type(self.value.evaluate()) is tuple):
            self.value = self.value.tupleString()
        elif (type(self.value.evaluate()) is list):
            self.value = list(self.value.evaluate()).__str__().replace(" ","")
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
        if (self.op == '+'):
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


# Object for Lists
class ListNode(Node):
    def __init__(self, v):
        if (v == None):
            self.v = []
        elif type(v.evaluate()) == str:
            self.v = [v.strip('(\")|(\')')]
        elif type(v) == list:
            self.v = v
        else:
            self.v = [v.evaluate()]

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

class ListConsNode(Node):
    def __init__(self, v1, v2):
        self.v1 = v1.evaluate()
        self.v2 = v2.evaluate()

    def evaluate(self):
        return [self.v1]+self.v2



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


# TOD: Add any other tokens
tokens = (
    'LPAREN', 'RPAREN',
    'NUMBER', 'STRING',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'SEMI', 'COMMA', 'POUND',
    'TRUE', 'FALSE',
    'LBRACKET', 'RBRACKET',
    'POWER', 'CONS',
    'AND', 'OR', 'NOT',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE',
    'IN', 'DIV', 'MOD', 'DIVWORD', 'MODWORD', 'EXPONENT'
)

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
t_AND = 'and'
t_OR = 'or'
t_NOT = 'not'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'<>'
t_IN = 'in'
t_DIV = r'//'
t_DIVWORD = 'div'
t_MOD = r'%'
t_POUND = r'\#'
t_MODWORD = 'mod'
t_EXPONENT = 'e'


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


# Boolean token
def t_TRUE(t):
    'true'
    t.value = BooleanNode(t.value)
    return t


def t_FALSE(t):
    'false'
    t.value = BooleanNode(t.value)
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
# Print grammar rule
def p_print_smt(t):
    """
    print_smt : expression SEMI
    """
    t[0] = PrintNode(t[1])



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
    t[0] = t[1]


def p_boolean_false(t):
    """boolean : FALSE"""
    t[0] = t[1]


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


def p_index(t):
    """index : LBRACKET NUMBER RBRACKET"""
    t[0] = t[2].evaluate()


def p_list_index(t):
    """list : list index"""
    t[0] = ListIndex(t[2], t[1].evaluate())


def p_list_cons(t):
    """expression : expression CONS expression"""
    t[0] = ListConsNode(t[1], t[3])


def p_list_in(t):
    """expression : expression IN list"""
    t[0] = ListFind(t[1].evaluate(), t[3].evaluate())


# Semantic error
def p_error(t):
    print("SEMANTIC ERROR")


import ply.yacc as yacc

yacc.yacc(debug=0)

import sys

if (len(sys.argv) != 2):
    sys.exit("invalid arguments")
fd = open(sys.argv[1], 'r')
code = ""
lines = []
for line in fd:
    lines += line.split(r'\;')
for line in lines:
    code = line
    try:
        lex.input(code)
        while True:
            token = lex.token()
            if not token: break
            #print(token)
        ast = yacc.parse(code)
        ast.execute()
    except Exception:
        print("SEMANTIC ERROR")
