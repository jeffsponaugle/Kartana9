; test the ALU and Flags

start:
        nop
        loadimm r0,0
        addi r0,1,r1
        addi r0,2,r2
        subi r2,1,r3
        subi r1,1,r4
        loadimm r7,#1000
        putsp r7
        getsp r6
        push r0
        push r1
        push r2
        push r3
        pop r0
        pop r1
        pop r2
        pop r3
        loadimm r0,0
        loadimm r5,#FF
  lp:   subi r5,1,r5
        cmp r5,r0
        jnzi lp




