; test the ALU and Flags

start:
        nop
        loadimm r0,0
        loadimm r1,1
        loadimm r2,2
        loadimm r3,3
        loadimm r7,#8120
        putsp r7
        putsp r7
        nop
        getsp r6
        getsp r6
        nop
        putsp r7
        nop
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




