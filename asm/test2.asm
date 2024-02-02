; test the ALU and Flags

start:
        nop
        loadimm r0,0
        storebi r0,#FFF0
        nop
        loadimm r0,16
        loadimm r3,1
        loadimm r1,sevseg   
lp:     loadbr  r1,r2
        storebi r2,#FFF0
        add r1,r3,r1
        sub r0,r3,r0
        jnzi lp
        jmpi start
        
sevseg:
        db #7E,#0C,#B6,#9E,#CC,#DA,#FA,#0E,#FE,#DE,#EE,#F8,#72,#BC,#F2,#E2




