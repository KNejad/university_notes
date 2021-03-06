# 1 - Assembly Language 1
Created Tuesday 19 January 2016


All assembly code: [Assembly Code](../../Assembly_Code.markdown)

Types of Language:
------------------
![](./1_-_Assembly_Language_1/pasted_image.png)

Intel 8086 Architecture:
------------------------
![](./1_-_Assembly_Language_1/pasted_image001.png)


### Execution Unit (EU):

#### Contains a circuit called the arithmetic and logic unit (ALU)
The ALU can perform arithmetic (+,-,*,/) and logic (AND, OR, NOT) operations
[Lectures:Logic:18 - ALU](../Logic/18_-_ALU.markdown)


Stack:
------
A stack is an area of memory which is used for storing data on a temporary basis.
The area of memory used for your program code is fixed, i.e. once the code is loaded into memory it does not grow or shrink. 
The size of the stack varies during program execution. We can store information on the stack and retrieve it later. 
Stack Pointer: keep track of where items are stored. Points to the top of the stack


### Registers:
Registers are places in the CPU where a number can be stored and manipulated. There are three sizes of registers: 8-bit, 16-bit and on 386 and above 32-bit.


### Types of Registers:

#### General purpose registers:
AX, BX, CX, DX
They are all 16-bit registers
The "H" and "L" suffix on the 8 bit registers stand for high byte and low byte. Meaning that when you call AL you get the 8 right most bits from the register AX


#### Segment registers:
CS, DS, ES, FS, GS, SS
Segment registers hold the segment address of various items. 
They are only available in 16 values. 
They can only be set by a general register or special instructions.


#### Index registers:
SI (source index), DI (destination index) and IP (instruction pointer), BP, SP
They some time used with a segment register to point to far address (in a 1Mb range).
Sometimes called pointer registers
16-bit registers 
Mainly used for string instructions


#### Stack registers:
BP and SP are stack registers
a stack is an area of memory which you can save and restore values to
a stack of plates -- Last On First Off (LOFO) or Last In First Out (LIFO)x
	


