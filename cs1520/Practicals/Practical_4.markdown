# Practical 4
Created Monday 15 February 2016

Exercise 1:
-----------
.MODEL small
.code
Start:
	
MOV DL, 1100001b
	
print_a_to_z:
MOV AH,02      
INT 21h
add dl, 1
cmp dl , 1111011b
jne print_a_to_z
	
	
MOV AH,4Ch   ; Function to exit
MOV AL,00    ; Return 00
INT 21h
	
Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program
	
END Start 			;End program
	

