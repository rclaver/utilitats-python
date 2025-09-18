#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Parsing

Para crear una función que tome una cadena y produzca un AST, dividimos el análisis en tres etapas.
   tokenize - turns a string into tokens
   reader   - take the tokens and group them
   parser   - turn the segmented parts into Abstract Syntax Trees (AST)

La idea es transformar la cadena "(+ 1 2)" para obtener un AST como éste:

parser(reader(tokenize("(+ 1 1)")))

La forma del AST puede ser cualquier estructura de datos que decidamos. Utilizaremos expresiones de Scheme
muy simples (llamadas s-exp). La cadena anterior podría verse así en Scheme:

(apply-exp
 (var-exp +)
 ((lit-exp 1) (lit-exp 2)))

Una expresión compuesta por un operador ('+') y dos expresiones literales 1 y 2 como operandos.

Llamamos a la sintaxis de la cadena Sintaxis Concreta en comparación con la Sintaxis Abstracta del AST.
Scheme es un lenguaje sencillo compuesto de listas, símbolos, cadenas y números. Todo lo que contiene el lenguaje
se puede analizar en esos componentes, por lo que escribir un analizador de Scheme es bastante fácil.
https://notebook.community/dsblank/ProgLangBook/Chapter%2005%20-%20Interpreting%20Scheme%20in%20Python
'''

'''
Tokenize
========
Para analizar S-Calc primero definimos el nivel más bajo del proceso, el tokenizador:
   ejemplo:
      In [2]:
         tokenizer("""(this    is (a)
         3.14
         ((list))""")

      Out[2]:
         ['(', 'this', 'is', '(', 'a', ')', '3.14', '(', '(', 'list', ')', ')']
'''
def tokenizer(string):
   """
   Takes a string and segments it into parts. We break strings up by brackets, and whitespace.
   Returns a Python list of strings.
   """
   retval = []
   current = ""
   for i in range(len(string)):
      if string[i] in ["(", "[", ")", "]"]:
         if current:
            retval.append(current)
         current = ""
         retval.append(string[i])
      elif string[i] in [" ", "\t", "\n"]:
         if current:
            retval.append(current)
         current = ""
      else:
         current += string[i]
   if current:
      retval.append(current)
   return retval


'''
Reader
======
The reader will take the tokenized expression (texp) and produced grouped results.
   ejemplo
      In [5]:
         reader(tokenizer("""(this    is (a) 3.14 ((list))""")

      Out[5]:
         ['this', 'is', ['a'], '3.14', [['list']]]
'''
def reader(texp):
   """
   Takes the output of the tokenizer, and creates lists of lists of items. Numbers are represented as numbers.
   """
   current = None
   stack = []
   for item in texp:
       if item.isdigit():
          if current is not None:
             current.append(eval(item))
          else:
             current = eval(item)
       elif item in ["[", "("]:
          if current is not None:
             stack.append(current)
          current = []
       elif item in ["]", ")"]:
          if stack:
             stack[-1].append(current)
             current = stack.pop(-1)
          else:
             pass
       else:
          if current is not None:
             current.append(item)
          else:
             current = item
   return current


'''
Parser
======
The final process of Step 1 is to take the output of the reader and parse it into an AST.
For our first S-Calc expression, we just need to handle "(+ 1 2)". That is, we need to handle three things:
    numbers - any kind of number
    variables, like "+" - anything not a number
    application - starts with a parenthesis

'''
EmptyList = "()"

def cons(item1, item2):
   return [item1, item2]

def car(exp):
   return exp[0]

def cdr(exp):
   return exp[1]

def cadr(exp):
   return exp[1][0]

def cddr(exp):
   return exp[1][1]

def caddr(exp):
   return exp[1][1][0]

def List(*args):
   "Create a linked-list of items"
   retval = EmptyList
   for arg in reversed(args):
      retval = cons(arg, retval)
   return retval

def lit_exp(value):
   return List("lit-exp", value)

def var_exp(symbol):
   return List("var-exp", symbol)

def app_exp(f, args):
   return List("apply-exp", f, args)

def parser(rexp):
   # Reads in a Python list of things, and returns an AST.
   if isinstance(rexp, int):
      return lit_exp(rexp)
   elif isinstance(rexp, str):
      return var_exp(rexp)
   else:
      return app_exp(parser(rexp[0]), List(*map(parser, rexp[1:])))


'''
Interpreter

Esta función toma una expresión AST y la interpreta (da un resultado). Llamaremos 'evaluator' a nuestro intérprete.
Nuevamente, como solo tenemos números, símbolos y aplicaciones, solo necesita manejar esos tres elementos.
Para ayudar con la depuración, también agregaremos una aplicación de impresión.
'''
def evaluator(expr):
   if car(expr) == "lit-exp":
      return cadr(expr)
   elif car(expr) == "var-exp":
      return cadr(expr) ## for now, return symbol
   elif car(expr) == "apply-exp":
      return evaluator_apply(evaluator(cadr(expr)),
                        Map(evaluator, caddr(expr)))
   else:
      raise Exception("invalid ast: %s" % expr)

def evaluator_apply(op, operands):
   if op == "print":
      Print(operands)
   elif op == "+":
      return car(operands) + cadr(operands)
   else:
      raise Exception("unknown apply operator: %s" % op)

def Map(f, slist):
   if slist == EmptyList:
      return EmptyList
   else:
      return cons( f(car(slist)), Map(f, cdr(slist))) ## recursive!

def Print(slist):
   if slist == EmptyList:
      return
   else:
      print(car(slist))
      Print(cdr(slist))
