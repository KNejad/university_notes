# Tutorial 3
Created Monday 08 February 2016

1) Write instructions to clear bit 5 of the al register which contains 62h:
---------------------------------------------------------------------------
and al, 11101111


2) Write instructions to convert a lower-case letter ‘b’ to its upper case equivalent
-------------------------------------------------------------------------------------
and al, 11011111


3) Give three different instructions to clear the register ax. Explain which instruction is more efficient
----------------------------------------------------------------------------------------------------------
and ax, 00000000b
mov ax, 00d
sub ax, ffffh


4) Check a code segment to transfer control to label L, using a conditional jump instruction combined with the test instruction
-------------------------------------------------------------------------------------------------------------------------------

### (a) if bit 15 of ax is set
test ax, 15
jne l

### (b) if bit 7 of al is clear
test ax, 7
je l

### (c) if bits 2 and 4 of cx are clear
test cx, 2
je l1
l1:
test cx, 4
je l

### (d) if bit 5 of bl is clear
test bl, 5
je l


5) If al contains 63h, what is the value after rotating by one bit to the right ?
---------------------------------------------------------------------------------
1100011 => 1110001= 71h


6) Divide al (which contains 12) by 2 using the sar instruction:
----------------------------------------------------------------
sar al, 1


7) Write instruction to complement the al register (which contains 33h)
-----------------------------------------------------------------------
xor al, 11111111b
	

8) Write the shift instructions to multiply ax by 8 and bx by 32.
-----------------------------------------------------------------
sal ax, 3
sal ax, 5
	

9) Write the shift instructions to divide ax by 4 and dx by 16
--------------------------------------------------------------
sar ax, 2
sar ax, 4

