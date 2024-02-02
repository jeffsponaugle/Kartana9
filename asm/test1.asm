; test the ALU and Flags

start:
        nop
        loadimm r0,0
        loadimm r1,1
        add r0,r1,r2    ; should have 1 in r2, zero flag cleared.
        loadimm r0,255
        add r0,r1,r2    ; should have 256 in r2, zero flag cleared.
        loadimm r1,1
        loadimm r0,1
        sub r1,r0,r2    ; should have 0 in r2, zero flag set
        loadimm r2,#aa55
        loadimm r0,#FFFF
        loadimm r1,1
        add r0,r1,r2    ; should have 0 in r2, zero flag, and carry flag
        cmpc            ; invert the carry flag, so it should be off.
        cmpc            ; invert it again so it should be on now.
        loadimm r0,0
        loadimm r1,1
        addc r0,r1,r2   ; r2 should be 2, since 1+0+CF = 2 CF will clear
        nop
        loadimm r0,#9000
        loadimm r1,#A000
        add r0,r1,r5     ;r5=#3000, ovf=1, cf=1
        loadimm r0,10
        loadimm r1,2
        sub r0,r1,r2    ; r2=8, ZF,CF,OV=0
        loadimm r0,10
        loadimm r1,11   
        sub r0,r1,r2    ; r2=FFFF, CF=1, OV=0, ZF=0
        nop
        subc r0,r1,r2   ; since carry flag should be 1 coming in, this should subtract and additional vluae, r2=fffe
        nop
        loadimm r0,#9000
        loadimm r1,#4000
        sub r0,r1,r2    ; r2=5000, CF=0, OV=1, ZF=0
        jmpi start
        
data:
        db 65,66,67,68,69,70,71,72,73,65,66,67,68,69,70,71,72,73,65,66,67,68,69,70,71,72,73
        db 65,67,-1,-2
        dw #aa55,#1122,#2233,#3344,#21,1,-1
        ds "Testing 1 2 3 This is a test string"



