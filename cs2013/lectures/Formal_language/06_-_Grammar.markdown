# 06 - Grammar
Created Tuesday 04 October 2016

A language is a set of strings over an alphabet.

Languages serve two purposes in computing:
------------------------------------------
Communicating instructions or information
Defining valid communications


Grammar:
--------
A set of production rules for strings in a formal language.
Grammars are 4-tuples consisting of Non Terminals (N), Terminals (T), Start Symbols (S) and Productions (P)
Non Terminals: A finite alphabet (ie X, Y, Z)
Terminals: Characters which cannot be substituted further (ie a, b, c)
Start Symbols: The initial symbol to produce the alphabet with (ie X) 
Productions: Available substitutions for characters to create stirngs (ie X -> aX: This means that X can be substituted by aX in our language)


Context-free Grammar (CFG):
---------------------------
The left side of all production rules are non terminal (ie a -> b instead of X -> b)
CFGs produce Context-free Languages (CFL)

