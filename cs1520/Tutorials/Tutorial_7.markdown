# Tutorial 7
Created Monday 07 March 2016

1. Determine the critical path of the following circuit.
--------------------------------------------------------

![](./Tutorial_7/pasted_image.png)

Use the gate delays given in the table below.

![](./Tutorial_7/pasted_image001.png)

### Answer:
The route that A B and C take will lead to a delay of 135Ps

 

2. Determine the short path for the circuit in Question 1 (using the same gate delays table).
---------------------------------------------------------------------------------------------

### Answer:
The shortest path is the route of g which is 30.


3. Given the input waveforms shown in the following, sketch the output Q of a D latch.
--------------------------------------------------------------------------------------
![](./Tutorial_7/pasted_image002.png)
![](./Tutorial_7/pasted_image003.png)






4. Given the input waveforms shown in the following, sketch the output Q of a D flip-flop
-----------------------------------------------------------------------------------------
![](./Tutorial_7/pasted_image004.png)
![](./Tutorial_7/pasted_image005.png)



5. The diagram below represents an important sequential circuit.
----------------------------------------------------------------
![](./Tutorial_7/pasted_image006.png)
Explain how it behaves using the inputs from table given below. As part of your answer, draw another table showing the values of CLK (L1), CLK (L2), D, Q (L1), N1, Q(L2) at each step.
![](./Tutorial_7/pasted_image007.png)
This is a D flip flop it is edge triggered meaning the output Q only changes to d when CLK is on the rising edge

time	CLK(L1)	CLK(L2)	D	Q(L1)	N1		Q(L2)
t0	1		0		0	Dprev	Dprev	Dprev
t1	1		0		1	0		0		0
t2	0		1		0	0		0		1
t3	1		0		0	0		0		1
t4	0		1		0	0		0		1

6. A home security system is either active or inactive. Pressing the SET key on a keypad makes the system active, while pressing the OFF key makes it inactive. Opening the front door of the house when the system is active triggers an audible alarm; closing the door stops the alarm. Draw the state diagram and state transition table for this simple finite state machine.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](./Tutorial_7/pasted_image009.png)c

State		Alarm Triggered	SET	OFF	Door Opening	Door Closing	New State	New Alarm State
Inactive		X				0	X	X			X			Off			Not Triggered
Inactive		X				1	X	X			X			On			Not Triggered
Active		No				0	0	X			X			On			Not Triggered
Active		No				1	0	X			X			On			Not Triggered
Active		Yes				0	0	Yes			No			On			Triggered		
..... Can't be bothered to continue		

