# Tutorial 10
Created Monday 28 March 2016

1) Implement the following functions using a single 16x3 ROM. Use dot notation to indicate the ROM contents:-
-------------------------------------------------------------------------------------------------------------


i. X = AB + BC'D + A'B'

ii. Y = AB + BD
iii. Z = A + B + C + D

### Answer:

![](./Tutorial_10/pasted_image.png)

2) Specify the size of a ROM that you could use to program the following combinational circuit: A 16-bit adder/subtractor with Cin and Cout:
--------------------------------------------------------------------------------------------------------------------------------------------


### Answer:
Number of inputs = 2 x 16 + 1 = 33
Number of outputs = 16 + 1 = 17
Thus, this would require a 2^33^ * 17-bit ROM.
	

3) The extraterrestrial life project team has just discovered aliens living at the bottom of Loch Ness. They need to construct a circuit to classify the aliens by potential planet of origin based on measured features available from the NANSA probe: greenness, brownness, sliminess, and ugliness. Careful consultation with xenobiologists lead to the following conclusions:
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



a. If the alien is green and slimy or ugly, brown, and slimy, it might be from Mars.
b. If the alien is ugly, brown, and slimy, or green and neither ugly nor slimy, it might be from Venus.
c. If the alien is brown and neither ugly nor slimy or is green and slimy, it might be from Jupiter.


Note that this is an inexact science; for example, a life form which is mottled green and brown and is slimy but not ugly might be from either Mars or Jupiter.
Program a 4x4x3 PLA to identify the alien. 
You may use dot notation.
![](./Tutorial_10/pasted_image001.png)

