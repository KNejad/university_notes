# 05 - Output
Created Tuesday 04 October 2016

Moore Machines:
---------------
A finite-state machine whose output values are determined solely by its current state. 
6-tuple (Q,I,T,E,Γ,O)
Γ is the output alphabet
O is a set of pairs (a function : Q → Γ) defining the output corresponding to each state of the machine.
The output is shown in the state bubble


Mealy Machines:
---------------
A finite-state machine whose output values are determined both by its current state and the current inputs.
6-tuple (Q,I,T,E,Γ,O)
Γ is the output alphabet
O is a set of pairs (a function : Q → Γ) defining the output corresponding to each state of the machine.
The input and output are shown on transition line
	
A mealy machine can be converted to a moore machine and the reverse

Other Variations:
-----------------
Markov models: FSAs whose edges have probabilities 
Hidden Markov models: FSAs with hidden edges
	

