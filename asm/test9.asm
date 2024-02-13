; Output FF down to 00 on the 7 seg display.

start:
        
         nop
        ; setup the stack pointer to an area of RAM
        loadimm r0,#F000
        putsp r0
        ; clear display
        loadimm r0,#00FF
        storebi r0,[#FFF0]
        storebi r0,[#FFF1]
        ; We can test the conjector.  
        loadimm r0,6  ; Calling it with 6 should return 8 steps
        calli ccnt
        calli sevseg
        loadimm r0,14  ; Calling it with 14 should return 17 steps
        calli ccnt
        calli sevseg
        loadimm r0,48  ; Calling it with 48 should return 11 steps
        calli ccnt
        calli sevseg
        loadimm r0,63  ; Calling it with 14 should return 107 steps
        calli ccnt
        calli sevseg
        halt



; *************************************************************************************************************
; Calculate the number of loops needed to get to 1 using the Collatz Conjector 
; This routine takes a number passed in R0 and returns the number of collatz cycles needed to get to 1 in R0
; It will work with any number greater than 1
; *************************************************************************************************************
ccnt:
        push r1
        push r2
        push r3
        loadimm r1,0
ccntlp:
        ; lets check to see if r0 == 1
        loadimm r2,1
        cmp r2,r0
        jzi ccdone
        ; r0 is not 1, so lets do a cycle
        addi r1,1,r1            ; increment the count
        andi r0,#0001,r2        ; see if the number is even
        loadimm r3,0
        cmp r2,r3
        jzi cceven
        ; since the number is odd, we need to compute n*3 +1
        shl r0,r2,1     ; multiply r0 by 2 and store in r2
        add r0,r2,r2    ; add r0 to r2 to get r2=r0*3
        addi r2,1,r0    ; increment by 1, so now r0 has 3n+1
        jmpi ccntlp     ; lets loop
cceven:
        ; since the number is even, we can divide by 2
        shr r0,r0,1     ; /2
        jmpi ccntlp
ccdone:
        mov r1,r0   ; r1 has the count, so lets return that in r0
        pop r3
        pop r2
        pop r1
        ret


; Subroutine to display value on 7-seg display.  Pass value in R0.  Stack must be setup.
sevseg:
        push r1
        push r2
        push r3
        loadimm r2,sevsegd
        andi r0,#000F,r1
        add r1,r2,r1
        loadbr r1,r3
        storebi r3,[#FFF0]
        andi r0,#00F0,r1
        shr r1,r1,4
        add r1,r2,r1
        loadbr r1,r3
        storebi r3,[#FFF1]
        pop r3
        pop r2
        pop r1
        ret


        
sevsegd:
        ;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
        db #81,#F3,#49,#61,#33,#25,#05,#F1,#01,#21,#11,#07,#8D,#43,#0D,#1D
