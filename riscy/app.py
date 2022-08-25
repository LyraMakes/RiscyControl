#!/usr/bin/env python3

from typing import List, Tuple


x = "x"

MAX_SIZE = 0x800


table = []

stage1_table = []
stage2_dictionary = {}

bitmap = ["Add", "Nand", "Sli", "Rout", "Rin", "Rd", "Rs", "AddSub", "AddInc", "Rd1", "Rd0"]

sli_c1 = [
    [1, 1, x, x, 0, 0, x, x, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, x, x, 0, 1, x, x, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, x, x, 1, 0, x, x, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, x, x, 1, 1, x, x, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
]

sli_c3 = [
    [1, 1, x, x, 0, 0, x, x, 1, 1, " | ", 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 1, x, x, 0, 1, x, x, 1, 1, " | ", 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, x, x, 1, 0, x, x, 1, 1, " | ", 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, x, x, 1, 1, x, x, 1, 1, " | ", 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]
]

inc_c1 = [
    [1, 0, 0, 0, x, x, 0, 0, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, x, x, 0, 0, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, x, x, 0, 0, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, x, x, 0, 0, 0, 1, " | ", 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1]
]

inc_c3 = [
    [1, 0, 0, 0, x, x, 0, 0, 1, 1, " | ", 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, x, x, 0, 0, 1, 1, " | ", 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, x, x, 0, 0, 1, 1, " | ", 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, x, x, 0, 0, 1, 1, " | ", 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
]


def constructnumber(inp: List[int | str]) -> int:
    return int("".join(map(str, inp)), 2)


def splitline(line: List[int | str]) -> Tuple[int, int]:
    indx = line.index(" | ")
    return constructnumber(line[:indx]), constructnumber(line[indx + 1:])





def parsetable(table: List[List[int | str]]) -> None:
    for line in table:
        resolvex(line)



def resolvex(inp: List[int | str]) -> None:
    if not x in inp:
        stage1_table.append(inp)
        return
    
    xloc = inp.index(x)
    inp2 = [z for z in inp]
    inp3 = [z for z in inp]
    inp2[xloc] = 0
    inp3[xloc] = 1
    resolvex(inp2)
    resolvex(inp3)
    


def resolvestage1() -> None:
    for line in stage1_table:
        k, v = splitline(line)
        stage2_dictionary[k] = v


def constructstage1() -> None:
    print("sli_c1")
    parsetable(sli_c1)
    print("sli_c3")
    parsetable(sli_c3)
    print("inc_c1")
    parsetable(inc_c1)
    print("inc_c3")
    parsetable(inc_c3)


def constructstage2(NOP) -> None:
    for i in range(0, MAX_SIZE):
        if i not in stage2_dictionary:
            stage2_dictionary[i] = NOP


def print_dict(NOP) -> None:
    for addr in range(0, MAX_SIZE):
        print(hex(addr), ":", hex(stage2_dictionary[addr]))

    print("\n\nModified:")
    
        
    for addr in range(0, MAX_SIZE):
        if stage2_dictionary[addr] != NOP:
            print(hex(addr), ":", hex(stage2_dictionary[addr]))


def write_to_file(filename: str) -> None:
    with open(filename, "wb") as f:
        for addr in range(0, MAX_SIZE):
            f.write(bytes([stage2_dictionary[addr]]))



def mask_bits(mask: List[str]):
    for i in range(0, len(stage1_table)):
        new_line = stage1_table[i][:11]
        for j in range(11, len(stage1_table[i])):
            for k in range(0, len(mask)):
                if k == j - 11:
                    new_line.append(stage1_table[i][j])
                    break
        stage1_table[i] = new_line
    
    pass





constructstage1()

old_stage1_table = stage1_table[:]


# Create ALU Control Table
stage1_table = old_stage1_table[:]
NOP = 0b11111
mask_bits(["Add", "Nand", "Sli", "AddSub", "AddInc"])

resolvestage1()
constructstage2(NOP)

print_dict(NOP)
write_to_file("instruction_alu_control.bin")


# Create Register Control Table

stage1_table = old_stage1_table[:]
NOP = 0b001111
mask_bits(["Rout", "Rin", "Rd", "Rs", "Rd1", "Rd0"])

resolvestage1()
constructstage2(NOP)

print_dict(NOP)
write_to_file("instruction_register_control.bin")

