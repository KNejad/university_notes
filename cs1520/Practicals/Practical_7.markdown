# Practical 7
Created Monday 07 March 2016

Question 1:
-----------

Write True or False for the following statements:

1- Assembly language identifiers are case-sensitive. (F)
2- Assembler directives execute at run time. (F)
3- A data label is followed by a colon (:), but a code label does not have a colon . (F)
4- The linker copies assembled procedures from the link library file. (T) 
5- When a program's source code is modified, it needn't to be assembled and linked again before it can be executed with the changes. (F)
6- The destination operand of a MOV instruction can be a segment register. (T)
7- Assembler directives must be written in lowercase letters .(F)
8- It's a good idea to use numeric addresses when writing instructions that access variables. (F)
9- Object file and MAP file are produced by the assembler. (T)


Question 2:
-----------

### Besides the stack pointer (SP), which other register points to variables on the stack'?:
BP

### Which flag is set when the result of an unsigned arithmetic operation is too large to fit into the destination?
Carry

### Which flag is set when the result of a signed arithmetic operation is either too large or too small to fit into the destination'?
Overflow

### Which flag is set when an arithmetic or logical operation generates a negative result'?
Sign


Question 3: Find the mistakes in the following assembly code:
-------------------------------------------------------------

#this is first assembly program ;#Thats not my comment; comments start with ; not #
.modle small                             ;model should be model not modle
.DATA
Msg1 dw 'welcome to Assembly',0
2msg db "this is my first quiz",'$'     ;data can't start with a number
Array1 db 3Bh,F5h,6Dh,'AB',3dup(?)     ;F5h must be 0F5h  and AB needs to be a word not a byte
                                     
Var1 dw 5Ah
$val db 256 ;can't have a number larger than 255
Var2 dd 7FF0h
Var3 db ?
.code
main:
Mov ds,@data            ;Must not mov immediate to segment   
Mov ax,var2
Mov dx,var1  
            
Mov Ah,4Ch
Int 21h
End main

