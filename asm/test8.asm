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
        ; RAM starts of 0x8000, and we will start our table of primes there.
        ; The sieve table has an entry for each number from 0-255.
        ; Let us zero out that entire table
        loadimm r1,255  ; size of the sieve table (0-255)
        loadimm r7,#8000 ; pointer to the sieve table
        loadimm r0,0
lp1:    add r1,r7,r2
        storerb r0,r2
        subi r1,1,r1
        jnzi lp1
        loadimm r0,1
        storerb r0,r7   ; 0 is not prime
        addi r7,1,r7
        storerb r0,r7   ; 1 is not prime
        addi r7,1,r7
        ; lets mark all of the even numbers as not prime
        loadimm r0,2
        calli mark
        ; lets now mark all of the odd numbers up to the sqrt of 256
        loadimm r1,17
        loadimm r0,3
lp2:    calli mark
        addi r0,2,r0
        cmp r1,r0
        jnci lp2

disp:
; this routine will display all of the primes
        push r0
        push r1
        push r2
        push r3
        push r4
        loadimm r0,0        ; the current number we are looking at
        loadimm r2,#8100    ; the end address of the table
        loadimm r3,0        ; the flag for a number being prime

displp:
        addi r0,1,r0        ; increment the number we are looking for
        addi r0,#8000,r1    ; r1 = the address to get
        cmp r2,r1           ; if we are at the end address, we are done
        jzi dispdone
        loadbr r1,r4        ; get the value from the table
        cmp r3,r4
        jzi displp          ; if the memory location is not zero, this is not a prime, so go to the next one
        calli sevseg         ; if it is prime, print on the 7 segment display
        jmpi displp
dispdone:   
        pop r4
        pop r3
        pop r2
        pop r1  
        pop r0
        ret



; this routine will take r0 and use is as the increment the mark the sieve
mark:       
        push r1
        push r2
        push r3
        loadimm r1,1
        loadimm r2,#8100
        loadimm r3,#8000
mk2:
        add r3,r0,r3
        storerb r1,r3
        cmp r2,r3
        jnci mk2
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



