#  Supported "type":  noargs, 3reg, 2reg_bc, 2reg_ab, 2reg_b, 2reg_bc_imm3, 1reg_c, 2reg_ac_imm16, 1reg_a_imm16, 1reg_imm16_c,imm16,1reg_c_imm16
 

instmnu =      {"nop"    :{"numops":0,"op1":"","op2":"","op3":"","size":1, "opcode":0x00 },
                "halt"   :{"numops":0,"op1":"","op2":"","op3":"","size":1, "opcode":0x01 },
                "sub"    :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x02 },
                "subc"   :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x03 },
                "add"    :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x04 },
                "addc"   :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x05 },
                "xor"    :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x06 },
                "or"     :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x08 },
                "and"    :{"numops":3,"op1":"rega","op2":"regb","op3":"regc","size":1, "opcode":0x0A },
                "not"    :{"numops":2,"op1":"regb","op2":"regc","op3":"","size":1, "opcode":0x0C },
                "storerw":{"numops":2,"op1":"rega","op2":"regb","op3":"","size":1, "opcode":0x10 },
                "storerb":{"numops":2,"op1":"rega","op2":"regb","op3":"","size":1, "opcode":0x11 },
                "cmp"    :{"numops":2,"op1":"rega","op2":"regb","op3":"","size":1, "opcode":0x12 },
                "cmpc"   :{"numops":0,"op1":"","op2":"","op3":"","size":1, "opcode":0x13 },
                "loadrw" :{"numops":2,"op1":"regb","op2":"regc","op3":"","size":1, "opcode":0x14 },
                "loadrb" :{"numops":2,"op1":"regb","op2":"regc","op3":"","size":1, "opcode":0x15 },
                "jmpr"   :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x18 },
                "jzr"    :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x19 },
                "jnzr"   :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x1A },
                "jcr"    :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x1B },
                "jncr"   :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x1C },
                "jvr"    :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x1D },       
                "jnvr"   :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x1E },
                "shl"    :{"numops":3,"op1":"regb","op2":"regc","op3":"imm3a","size":1, "opcode":0x22 },
                "shr"    :{"numops":3,"op1":"regb","op2":"regc","op3":"imm3a","size":1, "opcode":0x23 },
                "shlc"   :{"numops":3,"op1":"regb","op2":"regc","op3":"imm3a","size":1, "opcode":0x24 },
                "shra"   :{"numops":3,"op1":"regb","op2":"regc","op3":"imm3a","size":1, "opcode":0x25 },
                "getsp"  :{"numops":1,"op1":"regc","op2":"","op3":"","size":1, "opcode":0x2A },
                "putsp"  :{"numops":0,"op1":"","op2":"","op3":"","size":1, "opcode":0x2B },
                "mov"    :{"numops":2,"op1":"regb","op2":"regc","op3":"","size":1, "opcode":0x2C },
                "getpc"  :{"numops":1,"op1":"regc","op2":"","op3":"","size":1, "opcode":0x2D },
                "push"   :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x2E },
                "pop"    :{"numops":1,"op1":"regc","op2":"","op3":"","size":1, "opcode":0x30 },
                "callr"  :{"numops":1,"op1":"regb","op2":"","op3":"","size":1, "opcode":0x34 },
                "ret"    :{"numops":0,"op1":"","op2":"","op3":"","size":1, "opcode":0x38 },
                "subi"   :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x42 },
                "subic"  :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x43 },
                "addi"   :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x44 },
                "addic"  :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x45 },
                "xori"   :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x46 },
                "ori"    :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x48 },
                "andi"   :{"numops":3,"op1":"rega","op2":"imm16","op3":"regc","size":2, "opcode":0x4A },
                "storewi":{"numops":2,"op1":"rega","op2":"imm16","op3":"","size":2, "opcode":0x50 },
                "storebi":{"numops":2,"op1":"rega","op2":"imm16","op3":"","size":2, "opcode":0x51 },
                "loadwi" :{"numops":2,"op1":"imm16","op2":"regc","op3":"","size":2, "opcode":0x54 },
                "loadbi"  :{"numops":2,"op1":"imm16","op2":"regc","op3":"","size":2, "opcode":0x55 },
                "jmpi"    :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x58 },
                "jzi"     :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x59 },
                "jnzi"    :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x5A },
                "jci"     :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x5B },
                "jnci"    :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x5C },
                "jvi"     :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x5D },
                "jnvi"    :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x5E },
                "storewri":{"numops":2,"op1":"rega","op2":"imm16r","op3":"","size":2, "opcode":0x60 },
                "storebri":{"numops":2,"op1":"rega","op2":"imm16r","op3":"","size":2, "opcode":0x61 },
                "loadwri" :{"numops":2,"op1":"imm16r","op2":"regc","op3":"","size":2, "opcode":0x64 },
                "loadbri" :{"numops":2,"op1":"imm16r","op2":"regc","op3":"","size":2, "opcode":0x65 },
                "loadimm" :{"numops":2,"op1":"regc","op2":"imm16","op3":"","size":2, "opcode":0x66 },
                "jmpri"   :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x68 },
                "jzri"    :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x69 },
                "jnzri"    :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x6A },
                "jcri"    :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x6B },
                "jncri"   :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x6C },
                "jvri"   :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x06D },
                "jnvri"  :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x6E },
                "calli"  :{"numops":1,"op1":"imm16","op2":"","op3":"","size":2, "opcode":0x78 },
                "callri" :{"numops":1,"op1":"imm16r","op2":"","op3":"","size":2, "opcode":0x79 }
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
            if (ro.strip('-').isdecimal()):
                rni=int(ro)
            else:
                errortxt="Immediate number is not a decimal number"

    return (rni,errortxt)

     
def ErrorExit(errortxt):
    print("TERMINATING: Error", errortxt)
    exit(1)


import sys

srcfilename = sys.argv[1]

if (len(srcfilename)==0):
    ErrorExit("ERROR: Must specifiy source file name.")

srcfilenameroot = srcfilename.split(".")[0]
parsed = list()
labels = dict()
srcfilerecord = list()

try:
    srcfile = open(srcfilename ,"r")
except:
    ErrorExit("Could not open specified input file:"+srcfilename)

address = 0
maxaddress = 0
srcln = 1
print("*** Starting Phase 1 loop")
for srcline in srcfile:
    # we will save the source file in a list so we can generate a .lst output
    srcfilerecord.append(srcline)
    inst=""
    operand=""
    # for each line we read in, strip of extra spaces, convert to lower case and remove comments
    srcline = srcline.split(";",1)[0].expandtabs(1).strip().lower()
    # look for a lable
    if (srcline.count(":") != 0):
        # if there is a ':' there is a lable
        label = srcline.split(":",1)[0]
        if (len(label)>0):
            labels[label] = address
        if (len(srcline.split(":",1)) > 1):
            srcline = srcline.split(":",1)[1].strip()
        else:
            srcline = ""
    if (len(srcline)!=0):
        # there is an instruction to parse
        i = srcline.split(" ",1)
        inst = i[0].strip()

        try:
            size = instmnu[inst]["size"]
        except KeyError:
            ErrorExit("Invalid Instruction:"+inst+" ... From line:"+str(srcln))

        if (len(i)>1):
            # there is also an operand
            operand=i[1].strip()
        b0 = (0).to_bytes(2,byteorder='little')
        b1 = (0).to_bytes(2,byteorder='little')
        parseline = {"inst":inst, "operand":operand, "address":address , "size":size, "srcln":srcln, "iw0":0, "iw1":0, "w0":b0, "w1":b1}
        parsed.append(parseline)
        address = address + (2*size)
        if (address>maxaddress): maxaddress=address
    srcln = srcln + 1    
    # lets add what we have to the parsed table
    
print("*** Starting Phase 2 loop")

for parseinstdata in parsed:
    instruction = parseinstdata["inst"]
    operand = parseinstdata["operand"]
    srclinenumber = parseinstdata["srcln"]
    instaddr = parseinstdata["address"]

    opcode = instmnu[instruction]["opcode"]
    numops = instmnu[instruction]["numops"]
    instsize = instmnu[instruction]["size"]

    opnum = 1
    sela=0
    selb=0
    selc=0
    imm16val=0

    while ( numops >= 1):
        optype = instmnu[instruction]["op"+str(opnum)]
        match optype:
            case "rega":
                sela,errortxt = getregisternumber(operand,opnum)
                if (len(errortxt)!=0):
                    ErrorExit(errortxt)
            case "regb":
                selb,errortxt = getregisternumber(operand,opnum)
                if (len(errortxt)!=0):
                    ErrorExit(errortxt)
            case "regc":
                selc,errortxt = getregisternumber(operand,opnum)
                if (len(errortxt)!=0):
                    ErrorExit(errortxt)
            case "imm16":
                imm16val,errortxt = getimmnumber(operand,opnum)
                if (len(errortxt)!=0):
                    # if the imm16 value is not a number, it might be a label.
                    labelv,errortxt = getsingleoperand(operand,opnum)   
                    imm16val = labels[labelv]      
            case "imm3a":
                sela,errortxt = getimmnumber(operand,opnum)
            case "imm16r":
                imm16val,errortxt = getimmnumber(operand,opnum)
                if (len(errortxt)!=0):
                    # if the imm16 value is not a number, it might be a label.
                    labelv,errortxt = getsingleoperand(operand,opnum)   
                    imm16val = labels[labelv] 
                # since this is an imm16 relative instruction we will subtract (the current address+4)   
                imm16val = (imm16val-instaddr)-4
            
        numops = numops-1
        opnum = opnum+1
    inst_enc0 = ((opcode<<9) | (sela) | (selb<<3) | (selc<<6))
    inst_enc1 = imm16val
    parseinstdata["iw0"] = inst_enc0
    parseinstdata["w0"] = (inst_enc0).to_bytes(2,byteorder='little')
    parseinstdata["iw1"] = inst_enc1
    if (inst_enc1<0):
        parseinstdata["w1"] = (inst_enc1).to_bytes(2,byteorder='little',signed=True)
    else:
        parseinstdata["w1"] = (inst_enc1).to_bytes(2,byteorder='little',signed=False)

# **** Create the listing file ****
    
try:
    listfile = open(srcfilenameroot+".lst","w")
except:
    ErrorExit("Could not open list file - "+srcfilenameroot+".lst")
# create three bytearrays, one for the regular binary file, one for the low byte file and one for the high byte file
# we will make the bytearray the size based the max address used rounded up to the nearest 32/16 bytes.
binimage = bytearray(((int(maxaddress/16))+1)*32)
binimagel = bytearray(((int(maxaddress/16))+1)*16)
binimageh = bytearray(((int(maxaddress/16))+1)*16)
listfile.write("*** List File:"+srcfilename+"\r\n")
parsedindex=0
srclineindex=1

for srcline in srcfilerecord:
    if (parsedindex < len(parsed)):
        if (parsed[parsedindex]["srcln"] != srclineindex):
            # we will continue to print the source output in list file until we get to a src line that has
            # an enrty in the parsed list.  Since the parsed list is ordered by srcline, we only need to do
            # one compare until we find a match, then increment to the next parsed list item
            lst="{:3d}                           {:40.40s}".format(srclineindex,srcline)
        else:
            # if the srcline and srcln are the same
            w0low=parsed[parsedindex]["w0"][0]
            w0high=parsed[parsedindex]["w0"][1]
            address=parsed[parsedindex]["address"]
            binimage[address]=w0low
            binimage[address+1]=w0high
            binimagel[address>>1]=w0low
            binimageh[address>>1]=w0high
            if(parsed[parsedindex]["size"]==1):
                lst="{:3d} {:2.2s}{:2.2s}                     {:40.40s}".format(srclineindex,hex(w0high)[2:].rjust(2, "0"),hex(w0low)[2:].rjust(2, "0"),srcline)
            else:
                w1low=parsed[parsedindex]["w1"][0]
                w1high=parsed[parsedindex]["w1"][1]
                binimage[address+2]=w1low
                binimage[address+3]=w1high
                binimagel[(address>>1)+1]=w1low
                binimageh[(address>>1)+1]=w1high
                lst="{:3d} {:2.2s}{:2.2s} {:2.2s}{:2.2s}                {:40.40s}".format(srclineindex,hex(w0high)[2:].rjust(2, "0"),hex(w0low)[2:].rjust(2, "0"),hex(w1high)[2:].rjust(2, "0"),hex(w1low)[2:].rjust(2, "0"),srcline)
            parsedindex = parsedindex + 1
        listfile.write(lst.rstrip()+"\r\n")
        srclineindex = srclineindex +1

listfile.close()

# output binary files

binfile=open(srcfilenameroot+".bin","wb")
binfileh=open(srcfilenameroot+".binh","wb")
binfilel=open(srcfilenameroot+".binl","wb")
binfile.write(binimage)
binfilel.write(binimagel)
binfileh.write(binimageh)
binfile.close()
binfileh.close()
binfilel.close()

    
 


#binfile=open(srcfilenameroot+".bin","w")
#binfileh=open(srcfilenameroot+".binh","w")
#binfilel=open(srcfilenameroot+".binl","w")



    #print("[",hex(instaddr),"]",parseinstdata["inst"],opcode,"0x"+hex(inst_enc0)[2:].rjust(4,"0"), ",0x"+hex(inst_enc1)[2:].rjust(4,"0") )
                



    





               



