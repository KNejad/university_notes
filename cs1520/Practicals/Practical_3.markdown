# Practical 3
Created Monday 08 February 2016

The sub program to display a character is sub program number 2h.
This number must be stored in the ah register.


Exercise 1:
-----------

.MODEL small
.code
Start:

MOV AH,08    ; Function to read a char from keyboard
INT 21h      ; the char saved in AL
MOV AH,02    ; Function to display a char  
MOV DL,AL    ; Copy a saved char in AL to DL to output it
INT 21h

MOV AH,4Ch   ; Function to exit
MOV AL,00    ; Return 00
INT 21h

Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program

END Start 			;End program


Exercise 2:
-----------

.MODEL small
.code
Start:

 MOV AH, 1                    ; read a character
 INT 21H

 MOV CL, AL                   ; save input character into CL

 MOV AH, 2                    ; carriage return
 MOV DL, 0DH          
 INT 21H

 MOV DL, 0AH                  ; line feed
 INT 21H

 MOV AH, 2                    ; display the character stored in CL   
 MOV DL, CL
 INT 21H

 MOV AH, 4CH                  ; return control to DOS
 INT 21H

Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program

END Start 			;End program


Exercise 3:
-----------
.MODEL small
.code
Start:

MOV AH,02    ; Function to display a char  
MOV DL, 48h    ; Copy a saved char in AL to DL to output it
INT 21h

MOV AH,02    ; Function to display a char  
MOV DL, 45h    ; Copy a saved char in AL to DL to output it
INT 21h

MOV AH,02    ; Function to display a char  
MOV DL, 4ch    ; Copy a saved char in AL to DL to output it
INT 21h

MOV AH,02    ; Function to display a char  
MOV DL, 4ch    ; Copy a saved char in AL to DL to output it
INT 21h

MOV AH,02    ; Function to display a char  
MOV DL, 4fh    ; Copy a saved char in AL to DL to output it
INT 21h


 MOV AH, 2                    ; carriage return
 MOV DL, 0DH          
 INT 21H

 MOV DL, 0AH                  ; line feed
 INT 21H

MOV AH,4Ch   ; Function to exit
MOV AL,00    ; Return 00
INT 21h

Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program

END Start 			;End program


Exercise 4:
-----------
.MODEL small
.code
Start:

MOV AH,08    ; Function to read a char from keyboard
INT 21h      ; the char saved in AL

MOV AH,02    ; Function to display a char  
MOV DL,AL    ; Copy a saved char in AL to DL to output it
INT 21h


mov CL,AL           ;move al to cl
xor CL, 00100000b   ;flip the 3rd bit so that capital becomes lowercase and vica versa


MOV AH,02      ;print a space 
MOV DL, 20h    
INT 21h


MOV AH,08    ; Function to read a char from keyboard
INT 21h      ; the char saved in AL

MOV AH,02    ; Function to display a char  
MOV DL,AL    ; Copy a saved char in AL to DL to output it
INT 21h

mov BL,AL           
xor BL, 00100000b   ;flip the 3rd bit so that capital becomes lowercase and vica versa



MOV AH, 2                    ; carriage return
MOV DL, 0DH          
INT 21H

MOV DL, 0AH                  ; line feed
INT 21H
	 
MOV AH,02    ; Function to display a char  
MOV DL,BL    
INT 21h


MOV AH,02      ;print a space 
MOV DL, 20h    
INT 21h


MOV AH,02    ; Function to display a char  
MOV DL,CL  
INT 21h

MOV AH,4Ch   ; Function to exit
MOV AL,00    ; Return 00
INT 21h

Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program

END Start 			;End program

