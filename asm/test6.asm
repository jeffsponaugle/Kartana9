; test the ALU and Flags

start:
        nop
        loadimm r0,#9000
        loadimm r1,#9000
        add r0,r1,r2
        addc r0,r1,r3
        loadimm r1,1
        shl r1,r1,1
        shl r1,r1,1
        shl r1,r1,1
        shl r1,r1,1
        shl r1,r1,4
        shr r1,r1,4
        shr r1,r1,1
        shr r1,r1,1
        shr r1,r1,1
        shr r1,r1,1
        loadimm r3,#8000
        shr r3,r3,1
        shr r3,r3,1
        shr r3,r3,1
        shr r3,r3,1
        loadimm r3,#8000
        shra r3,r3,1
        shra r3,r3,1
        shra r3,r3,1
        shra r3,r3,1        ; carry = 0
        loadimm r4,#FFFF
        shr r4,r4,1             ; should set carry
        shlc r4,r4,1
        shl r4,r4,1
        getpc r5
        loadimm r4,#F000
        putsp r4
        nop
        nop
        calli foo
        loadimm r0,#11
        storebi r0,[#FFF0]
        loadimm r0,#07
        storebi r0,[#FFF1]
        halt
 foo:          
        loadimm r0,#61
        storebi r0,[#FFF0]
        loadimm r0,#33
        storebi r0,[#FFF1]
        ret
