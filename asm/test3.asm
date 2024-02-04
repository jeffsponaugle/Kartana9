; test the ALU and Flags

start:
        nop
        loadimm r0,#FE
        storebi r0,[#FFF0]
        nop
        loadimm r0,15
        loadimm r1,sevseg
        loadimm r3,1
lp:     add r1,r0,r2        ; r2 is address in sevseg for the value we want
        loadbr  [r2],r4       
        storebi r4,[#FFF0]
        sub r0,r3,r0
        jnzi lp
        jmpi start
        
sevseg:
        ;    0   1   2   3   4   5   6   7   8   9   a   b   c   d   e   f
        db #81,#F3,#49,#61,#33,#25,#05,#F1,#01,#21,#11,#07,#8D,#43,#0D,#1D



