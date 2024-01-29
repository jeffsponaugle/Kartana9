#  Supported "type":  noargs, 3reg, 2reg_bc, 2reg_ab, 2reg_b, 2reg_bc_imm3, 1reg_c, 2reg_ac_imm16, 1reg_a_imm16, 1reg_imm16_c,imm16,1reg_c_imm16
 

instmnu =      {"nop"    :{"numops]":0,"op1":"","op2":"","op3":"","type":"noargs", "size":1, "opcode":0x00 },
                "halt"   :{"numops]":0,"op1":"","op2":"","op3":"","type":"noargs", "size":1, "opcode":0x01 },
                "sub"    :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x02 },
                "subc"   :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x03 },
                "add"    :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x04 },
                "addc"   :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x05 },
                "xor"    :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x06 },
                "or"     :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x08 },
                "and"    :{"numops]":3,"op1":"rega","op2":"regb","op3":"regc","type":"3reg", "size":1, "opcode":0x0A },
                "not"    :{"numops]":2,"op1":"regb","op2":"regc","op3":"","type":"2reg_bc", "size":1, "opcode":0x0C },
                "storerw":{"numops]":2,"op1":"rega","op2":"regb","op3":"","type":"2reg_ab", "size":1, "opcode":0x10 },
                "storerb":{"numops]":2,"op1":"rega","op2":"regb","op3":"","type":"2reg_ab", "size":1, "opcode":0x11 },
                "cmp"    :{"numops]":2,"op1":"rega","op2":"regb","op3":"","type":"2reg_ab", "size":1, "opcode":0x12 },
                "cmpc"   :{"numops]":0,"op1":"","op2":"","op3":"","type":"noargs", "size":1, "opcode":0x13 },
                "loadrw" :{"numops]":2,"op1":"regb","op2":"regc","op3":"","type":"2reg_bc", "size":1, "opcode":0x14 },
                "loadrb" :{"numops]":2,"op1":"regb","op2":"regc","op3":"","type":"2reg_bc", "size":1, "opcode":0x15 },
                "jmpr"   :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x18 },
                "jzr"    :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x19 },
                "jnzr"   :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x1A },
                "jcr"    :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x1B },
                "jncr"   :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x1C },
                "jvr"    :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x1D },       
                "jnvr"   :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x1E },
                "shl"    :{"numops]":3,"op1":"regb","op2":"regc","op3":"imm3a","type":"2reg_bc_imm3", "size":1, "opcode":0x22 },
                "shr"    :{"numops]":3,"op1":"regb","op2":"regc","op3":"imm3a","type":"2reg_bc_imm3", "size":1, "opcode":0x23 },
                "shlc"   :{"numops]":3,"op1":"regb","op2":"regc","op3":"imm3a","type":"2reg_bc_imm3", "size":1, "opcode":0x24 },
                "shra"   :{"numops]":3,"op1":"regb","op2":"regc","op3":"imm3a","type":"2reg_bc_imm3", "size":1, "opcode":0x25 },
                "getsp"  :{"numops]":1,"op1":"regc","op2":"","op3":"","type":"1reg_c", "size":1, "opcode":0x2A },
                "putsp"  :{"numops]":0,"op1":"","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x2B },
                "mov"    :{"numops]":2,"op1":"regb","op2":"regc","op3":"","type":"2reg_bc", "size":1, "opcode":0x2C },
                "getpc"  :{"numops]":1,"op1":"regc","op2":"","op3":"","type":"1reg_c", "size":1, "opcode":0x2D },
                "push"   :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x2E },
                "pop"    :{"numops]":1,"op1":"regc","op2":"","op3":"","type":"1reg_c", "size":1, "opcode":0x30 },
                "callr"  :{"numops]":1,"op1":"regb","op2":"","op3":"","type":"1reg_b", "size":1, "opcode":0x34 },
                "ret"    :{"numops]":0,"op1":"","op2":"","op3":"","type":"noargs", "size":1, "opcode":0x38 },
                "subi"   :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x42 },
                "subic"  :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x43 },
                "addi"   :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x44 },
                "addic"  :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x45 },
                "xori"   :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x46 },
                "ori"    :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x48 },
                "andi"   :{"numops]":3,"op1":"rega","op2":"imm16","op3":"regc","type":"2reg_a_imm16_c", "size":2, "opcode":0x4A },
                "storewi":{"numops]":2,"op1":"rega","op2":"imm16","op3":"","type":"1reg_a_imm16", "size":2, "opcode":0x50 },
                "storebi":{"numops]":2,"op1":"rega","op2":"imm16","op3":"","type":"1reg_a_imm16", "size":2, "opcode":0x51 },
                "loadwi" :{"numops]":2,"op1":"imm16","op2":"regc","op3":"","type":"1reg_imm16_c", "size":2, "opcode":0x54 },
                "loadbi"  :{"numops]":2,"op1":"imm16","op2":"regc","op3":"","type":"1reg_imm16_c", "size":2, "opcode":0x55 },
                "jmpi"    :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x58 },
                "jzi"     :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x59 },
                "jnzi"    :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x5A },
                "jci"     :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x5B },
                "jnci"    :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x5C },
                "jvi"     :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x5D },
                "jnvi"    :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x5E },
                "storewri":{"numops]":2,"op1":"rega","op2":"imm16","op3":"","type":"1reg_a_imm16", "size":2, "opcode":0x60 },
                "storebri":{"numops]":2,"op1":"rega","op2":"imm16","op3":"","type":"1reg_a_imm16", "size":2, "opcode":0x61 },
                "loadwri" :{"numops]":2,"op1":"imm16","op2":"regc","op3":"","type":"1reg_imm16_c", "size":2, "opcode":0x64 },
                "loadbri" :{"numops]":2,"op1":"imm16","op2":"regc","op3":"","type":"1reg_imm16_c", "size":2, "opcode":0x65 },
                "loadimm"   :{"numops]":2,"op1":"regc","op2":"imm16","op3":"","type":"1reg_c_imm16", "size":2, "opcode":0x66 },
                "jmpri"   :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x68 },
                "jzri"    :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x69 },
                "jnzi"    :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x6A },
                "jcri"    :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x6B },
                "jncri"   :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x6C },
                "jvri"   :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x06D },
                "jnvri"  :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x6E },
                "calli"  :{"numops]":1,"op1":"imm16","op2":"","op3":"","type":"imm16jmp", "size":2, "opcode":0x78 },
                "callri" :{"numops]":1,"op1":"imm16r","op2":"","op3":"","type":"imm16jmpr", "size":2, "opcode":0x79 }
                }


def getsingleoperand(operandstring,operandnumber):
    errortxt=""
    match operandnumber:

        case 1:
            ro=operandstring.split(",")[0].strip()
           
        case 2:
            ro=operandstring.split(",")
            if (len(ro)>=2):
                ro=ro[1].strip()
            else:
                errortxt="Instruction needs 2 operands but found less than 2"
                ro=""
                return (0,errortxt)
        
        case 3:
            ro=operandstring.split(",")
            if (len(ro)>=3):
                ro=ro[2].strip()
            else:
                errortxt="Instruction needs 2 operands but found less than 2"
                ro=""
                return (0,errortxt)
    return (ro,errortxt)


def getregisternumber(operandstring,operandnumber):
    errortxt=""
    retval=0
    ro,errortxt = getsingleoperand(operandstring,operandnumber)

    if (ro.startswith("r")):
        rn=ro.split("r",1)[1]
        if (rn.isdecimal()):
            rni=int(rn)
            if (rni>=0 and rni<=7):
                retval = rni
            else:
                errortxt="Register number out of range 0-7"

        else:
            errortxt="Register number is not a decimal number"
    else:
        errortxt="Register does not start with an r:"+ro
    return (retval,errortxt)

def getimmnumber(operandstring,operandnumber):
    rni=0
    ro,errortxt = getsingleoperand(operandstring,operandnumber)
    if (len(errortxt)==0):
        # if the imm value starts with a pound sign, it is hex number
        if (ro.startswith("#")):
            rn=ro.split("#",1)[1]
            # rn is now the hex number with the pound sign removed
            rni=int(rn,16)
        else:
            if (ro.isdecimal()):
                rni=int(ro)
            else:
                errortxt="Immediate number is not a decimal number"

    return (rni,errortxt)

     
def ErrorExit(errortxt):
    print("TERMINATING: Error", errortxt)
    exit(1)

parsed = list()
labels = dict()

srcfile = open("test.asm","r")
address = 0
srcln = 1
for srcline in srcfile:
    addrinc = 0
    inst=""
    operand=""
    # for each line we read in, strip of extra spaces, convert to lower case and remove comments
    srcline = srcline.split(";")[0].expandtabs(1).strip().lower()
    # look for a lable
    if (srcline.count(":") != 0):
        # if there is a ':' there is a lable
        label = srcline.split(":")[0]
        if (len(label)>0):
            labels[label] = address
            print(address,"lable=",label)
        if (len(srcline.split(":")) > 1):
            srcline = srcline.split(":")[1].strip()
        else:
            srcline = ""
    if (len(srcline)!=0):
        # there is an instruction to parse
        i = srcline.split(" ",1)
        inst = i[0]
        size = instmnu[inst]["size"]
        print(address,"inst",inst)
        if (len(i)>1):
            # there is also an operand
            operand=i[1].strip()
            print("operand",operand)
        parseline = {"inst":inst, "operand":operand, "address":address , "size":size, "srcln":srcln, "iw0":0, "iw1":0}
        parsed.append(parseline)
        address = address + (2*size)
    srcln = srcln + 1    
    # lets add what we have to the parsed table
    
print(labels)
print(parsed)
print("*** Starting Phase 2 loop")

for parseinstdata in parsed:
    opcode = instmnu[parseinstdata["inst"]]["opcode"]
    operand = parseinstdata["operand"]
    srclinenumber = parseinstdata["srcln"]
    operandtype =  instmnu[parseinstdata["inst"]]["type"]
    instsize = instmnu[parseinstdata["inst"]]["size"]
    instaddr = parseinstdata["address"]
    match operandtype:

        # for instructions that have no arguments we just need to compute to instruction encoding from the opcode
        case "noargs":
            inst_enc0 = (opcode<<9)
            parseinstdata["iw0"] = inst_enc0
            print(hex(instaddr),"[noargs]",parseinstdata["inst"],opcode,hex(inst_enc0))


        # for instructions with 3 registers, we need to get each register number, then build the instuction encoding
        case "3reg":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            secondreg,errortxt = getregisternumber( operand,2)
            if (len(errortxt)!=0):
                 ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            thirdreg,errortxt = getregisternumber( operand,3)
            if (len(errortxt)!=0):
                 ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            inst_enc0 = ((opcode<<9) | (firstreg) | (secondreg<<3) | (thirdreg<<6))
            parseinstdata["iw0"] = inst_enc0
            print(hex(instaddr),"[3reg]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0") )
            
        # for instructions with just a single imm16 value, that value is either a direct address or a lable that points to a direct address for a jump or call instruction
        case "imm16jmp":
            imm16val,errortxt = getimmnumber(operand,1)
            if (len(errortxt)==0):
                # if the imm16 field is a number (decimal or hex), we can use it to build the final instruction encoding
                destadd = imm16val
            else:
                # if there was an error, it is possible the operand is a label.  Lets check to see if it is.
                destadd = labels[operand]
            inst_enc0 = (opcode<<9)
            inst_enc1 = destadd  
            parseinstdata["iw0"] = inst_enc0
            parseinstdata["iw1"] = inst_enc1     
            print(hex(instaddr),"[imm16jmp]",parseinstdata["inst"],opcode, "dest add",destadd, "0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",0x"+hex(inst_enc1)[2:].rjust(4,"0") )

        case "imm16jmpr":
            imm16val,errortxt = getimmnumber(operand,1)
            if (len(errortxt)==0):
                # if the imm16 field is a number (decimal or hex), we can use it to build the final instruction encoding
                destadd = imm16val
            else:
                # if there was an error, it is possible the operand is a label.  Lets check to see if it is.
                destadd = labels[operand]
            inst_enc0 = (opcode<<9)
            inst_enc1dec = ((destadd-instaddr)-4)
            inst_enc1bytes = inst_enc1dec.to_bytes(2,byteorder='little',signed=True) 
            parseinstdata["iw0"] = inst_enc0
            parseinstdata["iw1"] = inst_enc1   

            print(hex(instaddr),"[imm16jmpr]",parseinstdata["inst"],opcode, "dest add",destadd, "0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",",inst_enc1dec,inst_enc1bytes)


        # for instructions with a register (c) and an imm16 value.  For loadimm instruction
        case "1reg_c_imm16":
            firstreg,errortxt = getregisternumber(operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            imm16val,errortxt = getimmnumber(operand,2)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            
            # if the imm16 field is a number (decimal or hex), we can use it to build the final instruction encoding
            inst_enc0 = (opcode<<9) | (firstreg<<6)
            inst_enc1 = imm16val
            parseinstdata["iw0"] = inst_enc0
            parseinstdata["iw1"] = inst_enc1  
            print(hex(instaddr),"[1reg_c_imm16]",parseinstdata["inst"],opcode, "imm val",imm16val, "0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",0x"+hex(inst_enc1)[2:].rjust(4,"0") )
        case "1reg_imm16_c":
            firstreg,errortxt = getregisternumber(operand,2)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            imm16val,errortxt = getimmnumber(operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            
            # if the imm16 field is a number (decimal or hex), we can use it to build the final instruction encoding
            inst_enc0 = (opcode<<9) | (firstreg<<6)
            inst_enc1 = imm16val
            parseinstdata["iw0"] = inst_enc0
            parseinstdata["iw1"] = inst_enc1  
            print(hex(instaddr),"[1reg_imm16_c]",parseinstdata["inst"],opcode, "imm val",imm16val, "0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",0x"+hex(inst_enc1)[2:].rjust(4,"0") )

        case "2reg_bc":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            secondreg,errortxt = getregisternumber( operand,2)
            if (len(errortxt)!=0):
                 ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            inst_enc0 = ((opcode<<9) | (firstreg<<3) | (secondreg<<6))
            parseinstdata["iw0"] = inst_enc0
            print(hex(instaddr),"[2reg_bc]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0") )

        case "2reg_ab":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            secondreg,errortxt = getregisternumber( operand,2)
            if (len(errortxt)!=0):
                 ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            inst_enc0 = ((opcode<<9) | (firstreg) | (secondreg<<3))
            parseinstdata["iw0"] = inst_enc0
            print(hex(instaddr),"[2reg_ab]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0") )


        case "1reg_b":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            inst_enc0 = ((opcode<<9) | (firstreg<<3))
            parseinstdata["iw0"] = inst_enc0
            print(hex(instaddr),"[1reg_b]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0") )

        case "2reg_bc_imm3":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            secondreg,errortxt = getregisternumber( operand,2)
            if (len(errortxt)!=0):
                 ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            imm3val,errortxt = getimmnumber(operand,3)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))    
            if ((imm3val>7) or (imm3val<0)):
                ErrorExit("Parse Error: Immediate value can only by 0-7 for this instruction"+" at src line="+str(srclinenumber)) 
            inst_enc0 = ((opcode<<9) | (firstreg<<3) | (secondreg<<6) | (imm3val)) 
            print(hex(instaddr),"[2reg_bc_imm3]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0") )
        case "1reg_c":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            inst_enc0 = ((opcode<<9) | (firstreg<<6))
            parseinstdata["iw0"] = inst_enc0
            print(hex(instaddr),"[1reg_c]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0") )
        case "2reg_a_imm16_c":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            secondreg,errortxt = getregisternumber( operand,3)
            if (len(errortxt)!=0):
                 ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            imm16val,errortxt = getimmnumber(operand,2)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            
            inst_enc0 = ((opcode<<9) | (firstreg) | (secondreg<<6) )
            inst_enc1 =  imm16val
            print(hex(instaddr),"[2reg_a_imm16_c]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",0x"+hex(inst_enc1)[2:].rjust(4,"0") )
        case "1reg_a_imm16":
            firstreg,errortxt = getregisternumber( operand,1)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            imm16val,errortxt = getimmnumber(operand,2)
            if (len(errortxt)!=0):
                ErrorExit("Parse Error:"+errortxt+" at src line="+str(srclinenumber))
            inst_enc0 = ((opcode<<9) | (firstreg) )
            inst_enc1 =  imm16val
            print(hex(instaddr),"[1reg_a_imm16]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",0x"+hex(inst_enc1)[2:].rjust(4,"0") )







               



