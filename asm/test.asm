; newline comment

start:
        nop
        loadimm r0,0
        loadimm r1,1
        add r0,r1,r2
        add r1,r2,r3
        add r2,r3,r4
        add r3,r4,r5
        add r4,r5,r6
        add r5,r6,r7
        loadimm r0,#aa55
        shr r0,r1,1
        shr r1,r2,1
        shr r2,r3,1
        shr r3,r4,1
        shr r4,r5,1
        loadimm r6,#55aa
        shr r6,r6,2
        shr r6,r6,2
        shr r6,r6,2
        shr r6,r6,2
mid:    loadimm r3,16
        loadimm r2,1
        sub r3,r2,r3
        jnzri mid
        loadimm r4,#1234
mid2:   shr r4,r4,1
        jnzri mid
        loadimm r5,#aa
        loadwi #FFF0,r6
        storewi r6,#FFF0
        jmpi start
        
data:
        db 65,66,67,68,69,70,71,72,73,65,66,67,68,69,70,71,72,73,65,66,67,68,69,70,71,72,73
        db 65,67,-1,-2
        dw #aa55,#1122,#2233,#3344,#21,1,-1


