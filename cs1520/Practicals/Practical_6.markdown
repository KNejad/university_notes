# Practical 6
Created Monday 29 February 2016

The interrupt used for switching between screen modes, and for all graphics work is interrupt
10h.

Example 1:
----------

.MODEL small
.code
jmp start
;=========================================
; Basic program to draw a rectangle
;=========================================
mode db 18 ;640 x 480
x_start dw 100
y_start dw 100
x_end dw 540
y_end dw 380
colour db 1 ;1=blue
;=========================================
start:
mov ah,00 ;subfunction 0
mov al,mode ;select mode 18 (or 12h if prefer)
int 10h ;call graphics interrupt
;==========================
mov al,colour ;colour goes in al
mov ah,0ch
mov cx, x_start ;start drawing lines along x

drawhoriz:
mov dx, y_end ;put point at bottom
int 10h
mov dx, y_start ;put point on top
int 10h
inc cx ;move to next point
cmp cx, x_end ;but check to see if its end
jnz drawhoriz

drawvert: ;but check to see if its end
mov cx, x_start ;plot on left side
int 10h
mov cx, x_end ;plot on right side
int 10h
inc dx ;move down to next point
cmp dx, y_end ;check for end jnz drawvert
jnz drawvert

;==========================
readkey:
mov ah,00
int 16h ;wait for keypress
;==========================
end:
mov ah,00 ;again subfunc 0
mov al,03  ;text mode 3
int 10h ;call int
mov ah,04ch
mov al,00 ;end program normally
int 21h 

Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program

END Start 			;End program


Example 2:
----------

.MODEL small
.code
jmp start
;==============================
; Draws a horiz and vert line
;==============================
startaddr dw 0a000h ;start of video memory
colour db 1
;==============================
start:
mov ah,00
mov al,19
int 10h ;switch to 320x200 mode
;=============================
horiz:
mov es, startaddr ;put segment address in es
mov di, 32000 ;row 101 (320 * 100)
add di, 75 ;column 76
mov al,colour ;cannot do mem-mem copy so use reg
mov cx, 160 ;loop counter
hplot:
mov es:[di],al ;set pixel to colour
inc di ;move to next pixel
loop hplot
vert:
mov di, 16000 ;row 51 (320 * 50)
add di, 160 ;column 161
mov cx, 100 ;loop counter
vplot:
mov es:[di],al
add di, 320 ;mov down a pixel
loop vplot
;=============================
keypress:
mov ah,00
int 16h ;await keypress
end:
mov ah,00
mov al,03
int 10h
mov ah,4ch
mov al,00 ;terminate program
int 21h

Exit:
mov ax, 4c00h
int 21h 			;call DOS. Terminate program

END Start 			;End program






Exercise 1:
-----------
Could not complete.


