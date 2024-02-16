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
        loadimm r1,254  ; size of the sieve table (0-255)
        loadimm r7,#8000 ; pointer to the sieve table
        loadimm r0,0
lp1:    add r1,r7,r2
        storerw r0,r2
        subi r1,2,r1
        jnzi lp1

        loadimm r0,1
        storerb r0,r7   ; 0 is not prime
        addi r7,1,r7
        storerb r0,r7   ; 1 is not prime

        ; lets mark all of the even numbers as not prime
        loadimm r0,2
        calli mark
        ; lets now mark all of the odd numbers up to the sqrt of 256
        loadimm r1,17
        loadimm r0,3
lp2:    calli mark
        addi r0,2,r0
        cmp r1,r0
        jci lp2
        calli disp
        jmpi start

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
        add r3,r0,r3            ; increment the address by the sieve amount
        storerb r1,r3           ; mark as not prime (1)
        cmp r2,r3               ; check to see if we are at or past the end of the table
        jci mk2
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


; the hex primes
;  2 3 5 7 B D 11 13 17 1D 1F 25 29 2B 2F 35 3B 3D 43 47 49 4F 53 59 61 65 67 6B 6D 71 7F 83 89 8B 95 97 9D A3 
;  A7 AD B3 B5 BF C1 C5 C7 D3 DF E3 E5 E9 EF F1 FB 
;
;  101 107 10D 10F 115 119 11B 125 133 137 139 13D 14B 151 15B 
;  15D 161 167 16F 175 17B 17F 185 18D 191 199 1A3 1A5 1AF 1B1 1B7 1BB 1C1 1C9 1CD 1CF 1D3 1DF 1E7 1EB 1F3 1F7 
;  1FD 209 20B 21D 223 22D 233 239 23B 241 24B 251 257 259 25F 265 269 26B 277 281 283 287 28D 293 295 2A1 2A5 
;  2AB 2B3 2BD 2C5 2CF 2D7 2DD 2E3 2E7 2EF 2F5 2F9 301 305 313 31D 329 32B 335 337 33B 33D 347 355 359 35B 35F 
;  36D 371 373 377 38B 38F 397 3A1 3A9 3AD 3B3 3B9 3C7 3CB 3D1 3D7 3DF 3E5 3F1 3F5 3FB 3FD 407 409 40F 419 41B 
;  425 427 42D 43F 443 445 449 44F 455 45D 463 469 47F 481 48B 493 49D 4A3 4A9 4B1 4BD 4C1 4C7 4CD 4CF 4D5 4E1 
;  4EB 4FD 4FF 503 509 50B 511 515 517 51B 527 529 52F 551 557 55D 565 577 581 58F 593 595 599 59F 5A7 5AB 5AD 
;  5B3 5BF 5C9 5CB 5CF 5D1 5D5 5DB 5E7
