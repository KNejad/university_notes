# Tutorial 1
Created Monday 25 January 2016


1. How many different numbers can be represented with 16 bits?
	a. 65536
2. Convert the following unsigned binary numbers to decimal. Show your work
	a. 1010~2  ~8+0+2+0=10
	b. 110110~2  ~32+16+4+2= 54
	c. 11110000~2 ~128+64+32+16=240
	d. 000100010100111~2 ~2048+128+32+4+2+1=2215




3. Convert the following unsigned binary numbers to hexadecimal. Show your work
	a. 1110B =14D = E
	b. 100100B = 36D = 24
	c. 11010111B = D7
	d. 01110101010100100B =EAA4



4. Convert the following hexadecimal numbers to decimal. Show your work
	a. A5H: 10*16 + 5=165
	b. 3BH: 3*16 + 11 =59
	c. FFFFH: 15*16^3 + 15*16^2 + 15*16 + 15= 65,535
	d. D0000000H: 14 * 16^7 = 3,758,096,384 



5. Convert the following hexadecimal numbers to unsigned binary. Show your work
	a. 4EH =  01001110
	b. 7CH=01111100
	c. ED3AH =1110110100111010
	d. 403FB001H =0100001111111011000000000001




6. How many bytes are in a 32-bit word? How many nibbles are in the word?

Answer: 4,  8

7. How many bytes are in a 64-bit word?

Answer: 8


8. Assembly Commands: write the assembly code
	a. Put 3 into register AX: mov ax 03d
	b. Add 2 to the contents of AX: ADD ax 2




9. Write instructions to:
	a. Load character ? into register bx: mov bx, ?
	b. Load space character into register cx: mov cx, ' '
	c. Load 26 (decimal) into register cx: mov cx, 26d
	d. Copy contents of ax to bx and dx: 

mov bx, ax 
mov dx, ax
	



10. What errors are present in the following :

mov ax 3d: doesn't know if 3d is hex number 3d or decimal 3
mov 23, ax: 23 is not a registry name
mov cx, ch: doesn't know if ch is a register or a number 
move ax, 1h: Should be 01h
add 2, cx: Should be add cx, 2
add 3, 6: no register
inc ax, 2: inc does not need the 2 it always increments by 1
	








