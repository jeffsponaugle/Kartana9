; newline comment
start:
        nop
        loadimm r0,32
        loadimm r1,77
        add r0,r1,r2
 mid:   add r7,r2,r3   ; mid comment
        add r2,r3,r4
        or r1,r2,r6
        not r6,r7
        shl r1,r2,5
        cmpc
        and r1,r2,r6
        cmp r5,r4
        subi r3,227,r4
        jmpi mid
        jmpi start
        jmpr r5
        jmpri frd
        push r5
        jmpi start
 frd:   pop r2
        jmpri mid
        storewi r1,4567
        loadwi #1453,r5



