# Practical 8
Created Monday 14 March 2016

(Q1) Write True or false for the following statements of 8086 assembly language:
--------------------------------------------------------------------------------


1. For any two integers n and m, ((n XOR m) XOR m) produces n. (T)
2. The TEST instruction does not alter the destination operand. (T)
3. The OR instruction can be used to set an operand's value to zero. (F)
4. The Loop instruction jumps to a label when the Zero flag is clear. (F)
5. The JO instruction is used after an operation involving signed integers. (T)
6. The NOT instruction reverses the sign of a number. (F)
7. The XOR instruction can be used to toggle (complement) the bits in a number. (T)
8. The OR instruction modifies the Sign, Zero, and Parity flags according to the value of the destination operand.(T)
9. The JG instruction is used when comparing unsigned integers. (F)
10. The PROC directive begins a procedure and END directive ends a procedure. (F)
11. It is possible to call a procedure inside an existing procedure.(T)
12. Given the same task to accomplish, a nonrecursive procedure usually uses less memory than a recursive one (T)



(Q2) Choose the correct answer:
-------------------------------


1. Will the following code jump to the label named Target?

Mov ax,-15
cmp aX,10
ja Target

->a) Yes 
b) No 
c) ja is unsigned and can't be used


2. The implement of the following pseudocode in assembly language is:

if( bx < cx )
X = 1;

->a) Cmp bx,cx
Jnb next
Mov x,1
Next:
b) cmp bx,cx
jb next
mov x,1
next:
c) cmp cx,bx
jb next
jmp end
next: mov x,1
End:
d) (a) and (c)


3. Which instruction that multiplies the contents of BX by 8?


-> a) Shl bx,3 
b) shr bx,3 
c) ror bx,3 
d) rol bx,4


4. A sequence of instructions that shift three memory words to the right by 1 bit position.

Use the following data definition is:
Array WORD 8CF4h,0B678h,92Ach


-> a) Shr array+4,1
Rcr array+2,1
Rcr array,1
b) shl array+4,1
rcl array+2,1
rcl array,1
c) shr array+4,1
rol array+2,1
rol array,1
d)shl array+4,1
ror array+2,1
ror array,1


NOTE:
RCL
Rotate left (with carry)
RCR
Rotate right (with carry)



5. The content of AX register after the following operation is :

Mov ax,5000h
Mov dx,100h
Div bx

a) 0400h 
b) 0500h 
c) 5400h 
-> d) div will cause a divide overflow so AX can't be determined


6. The implement of the following pseudocode in assembly language is:

if( bx > cx )
X = 1;

a) Cmp bx,cx
Ja next
Mov x,1
Next:
->b) cmp bx,cx
jna next
mov x,1
next:
c) cmp cx,bx
ja next
jmp end
next: mov x,1
End:
d) (b) and (c)


7. Which instruction that divides the contents of BX by 8?


a) Shl bx,3 
-> b) shr bx,3 
c) ror bx,3 
d) rol bx,4


8. the value of AL after these instruction has executed:

mov al,0D4h
rcr al,2

a) 1110 1010 
->b) 0111 0101 # I think this is wrong it should be 00110101
c) 1111 0101 
d) 0110 1010


9. The content of AH register after the following operation is :

Mov ax,95h
Mov bl,10h
Div bl
->a) 05h 
b) 09h 
c) 00h 
d) none of the above

