; Output FF down to 00 on the 7 seg display.

start:
        
        nop
        loadimm r0,#FF
        loadimm r1,#AA55
        loadimm r2,#55AA
        storebi r0,[#FFF0]
        storebi r0,[#FFF1]
lp:     calli sevseg
        subi r0,1,r0
        jnzi lp

        loadwi [#FFF0],r0
        calli sevseg
        shr r0,r0,8
        calli sevseg
        or r1,r2,r3
        and r1,r2,r3
        xor r1,r2,r3
        not r1,r1
        xor r1,r2,r3
        loadimm r1,#AA55
        ori r1,#5555,r2
        andi r1,#AAAA,r2
        xori r1,#55AA,r2
        
        jmpi start


; Subroutine to display value on 7-seg display.  Pass value in R0.  Stack must be setup.
sevseg:
        push r1
        push r2
        loadimm r2,sevsegd
        andi r0,#000F,r1
        add r1,r2,r1
        storebi r1,[#FFF0]
        andi r0,#00F0,r1
        shr r1,r1,4
        add r1,r2,r1
        storebi r1,[#FFF1]
        pop r2
        pop r1
        ret


        
sevsegd:
        ;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
        db #81,#F3,#49,#61,#33,#25,#05,#F1,#01,#21,#11,#07,#8D,#43,#0D,#1D



