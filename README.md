# Kartana9
A simple 16-bit CPU implemented completely in a collection of ATF15XX CPLDs.

This is an implemenation of a simple 16-bit CPU design using ATF5XX CPLDs on a single  4-layer PCBs.   

The goal was to pick a simple instruction set that would allow for simple assembly language programs.  With a 16 bit address bus capable of addressing 64K of memory it was important for the ISA to support relative offsets and fully relocatable code.  While the first iteration does not have a multiply or divide instruction, some features in the shifting mechanism have been enhanced to make it easy to implment.

![](/images/IMG_6812.jpeg)

## Instruction Set Architecture

The instruction set is a RISC-like 3 operand load-store design with support for 8 general purpose 16 bit registers as well as two special purpose registers (Stack Pointer and Program Counter)   The internal data path is 16-bits wide, as are the registers and the external data path.  Access to external memory can be either 8 or 16 bits wide with automatic byte shifting to support loading 8 bit values odd and even addresses. 

Signed and Unsigned comparisons are supported, as are 'with carry' and 'without carry'  math operations.  

Stack operations are also supported for single register push and pops.

Call/Return functionality is support with return address storage on the stack.

Instructions fall in to 2 size catagories:  
  - Single Word Instructions (16 bits in width)
  - Double Word Instructions (32 bits in width)

Instruction Execution time also falls into two catagories:
  - Single Cycle execution (most of the instructions)
  - Two Cycle execution 

The fastest instructions have 1 fetch cycle and 1 execution cycle, while the slowest instruction has 2 fetch cycles and 2 executions cycles. I would expect average throughput to be ~2.2 cycles/instruction.  The design should support operation up to ~ 10 Mhz.

Instruction Set:

![](/InstructionsA.jpg)
![](/InstructionsB.jpg)

Most ALU operations are 3 operand, and there are no restrictions on those operands.  Each can be any of the 8 general purpose registers, and they do not need to be unique.

As an example:

`XOR R1,R1,R1`

would clear the R1 register, since an XOR against the same value results in zero.

The ALU operations ADD and SUB have variants that use the carry flag, and a side effect was added to the OR/XOR/AND/NOT operation to clear the carry flag.   You can use an instruction like OR R1,R1,R1 to make no changes except the CF clear.  There is also a Carry-Flag invert instruction to support fast integer multiplications.

Load and Store operations use either an immediate address, a relative immediate address,  or an address in a register.  Both Load and Store have BYTE and WORD varients.  Memory access occurs in a single cycle (the execution cycle).  This is the largest single limit on total processor speed, since both data and instruction access require memory access times to be ~ 1/2 the clock speed. (~50ns at 10MHZ).   To go faster it would require some fetch/execution pipelining and extension of the execute cycle for some instructions.

The shift instructions include the standard logical right and left as well as arithmetic right. There is an additional shift left with CARRY FILL, an instruction that can be used in some division algorythms.

The JUMP operations is to an address in a register, a direct immeditate addresss, or a reltive address (for relocatable code).  CALL (subroutine) operations also support register, a direct immeditate addresss, or a reltive address.

All decode and operation logic is direct sequential logic implemented inside the CPLDs with no microcode.  

## Physcial Implementation

The CPU is implemented on a 4-layer PCBs using ATF1508 CPLDs.  

- A primary CPU PCB that has the entire CPU, plus display/logic analyzer outputs.

  ![](/images/IMG_7430.jpeg)

  ![](/images/IMG_7434.jpeg)

A second PCB implements the 'computer' support around the CPU including boot FLASH and System RAM.

  ![](/images/IMG_7431.jpeg)

  ![](/images/IMG_7435.jpeg)

Both of these PCBs go into slots on a generic microprocessor test platform that I use for different CPU designs.

 ![](/images/IMG_7428.jpeg)

## Schematics

There are DIPTRACE format schmatics in the CPUKIT_ASBUILT/schematics folder. 

## CPLD

The CPLD source code is located in the CPUKIT_ASBUILT/PLD folder.

## Operations

[Youtube Video](https://youtu.be/H3OF3yWDvbs)






