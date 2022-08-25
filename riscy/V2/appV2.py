#!/usr/bin/env python3

from typing import List, Tuple, Dict


x = "x"

MAX_SIZE = 0x800


table = []

stage1_table = []
stage2_dictionary = {}

bitmap = ["Add", "Nand", "Sli", "Rout", "Rin", "Rd", "Rs", "AddSub", "AddInc", "Rd1", "Rd0"]

sli_c1 = [
    (
        [1, 1, x, x, 0, 0, x, x, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 0
    }),

    (
        [1, 1, x, x, 0, 1, x, x, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 1
    }),

    (
        [1, 1, x, x, 1, 0, x, x, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 0
    }),

    (
        [1, 1, x, x, 1, 1, x, x, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 1
    })
]

sli_c3 = [
    (
        [1, 1, x, x, 0, 0, x, x, 1, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 0,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 0
    }),

    (
        [1, 1, x, x, 0, 1, x, x, 1, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 0,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 1
    }),

    (
        [1, 1, x, x, 1, 0, x, x, 1, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 0,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 0
    }),

    (
        [1, 1, x, x, 1, 1, x, x, 1, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 0,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 1
    })
]


inc_c1 = [
    (
        [1, 0, 0, 0, x, x, 0, 0, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 0
    }),

    (
        [1, 0, 0, 0, x, x, 0, 0, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 1
    }),

    (
        [1, 0, 0, 0, x, x, 0, 0, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 0
    }),

    (
        [1, 0, 0, 0, x, x, 0, 0, 0, 1], {
        "Add" : 1,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 0,
        "Rin" : 1,
        "Rd" : 0,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 1
    })
]

inc_c3 = [
    (
        [1, 0, 0, 0, x, x, 0, 0, 1, 1], {
        "Add" : 0,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 0
    }),

    (
        [1, 0, 0, 0, x, x, 0, 0, 1, 1], {
        "Add" : 0,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 0,
        "Rd0" : 1
    }),

    (
        [1, 0, 0, 0, x, x, 0, 0, 1, 1], {
        "Add" : 0,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 0
    }),

    (
        [1, 0, 0, 0, x, x, 0, 0, 1, 1], {
        "Add" : 0,
        "Nand" : 1,
        "Sli" : 1,
        "Rout" : 1,
        "Rin" : 0,
        "Rd" : 1,
        "Rs" : 1,
        "AddSub" : 1,
        "AddInc" : 1,
        "Rd1" : 1,
        "Rd0" : 1
    })
]


def constructnumber(inp: List[int | str]) -> int:
    return int("".join(map(str, inp)), 2)


def splitline(line: List[int | str]) -> Tuple[int, int]:
    indx = line.index(" | ")
    return constructnumber(line[:indx]), constructnumber(line[indx + 1:])





def parsetable(table: List[Tuple[List[int], Dict[str, int]]]) -> None:
    for line in table:
        resolvex(line)



def resolvex(inp: Tuple[List[int], Dict[str, int]]) -> None:
    if not x in inp:
        stage1_table.append(inp)
        return
    
    xloc = inp[0].index(x)
    inp2 = [z for z in inp[0]], inp[1]
    inp3 = [z for z in inp[0]], inp[1]
    inp2[0][xloc] = 0
    inp3[0][xloc] = 1
    resolvex(inp2)
    resolvex(inp3)
    


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


table_type = List[Tuple[List[int], Dict[str, int]]]
def mask_bits(mask: List[str]):
    s2 = {}

    for i in range(0, len(stage1_table)):
        key = constructnumber(stage1_table[i][0])
        value = constructnumber([v for k, v in stage1_table[i][1].items() if k in mask])
        
        s2[key] = value






constructstage1()

old_stage1_table = stage1_table[:]


# Create ALU Control Table
stage1_table = old_stage1_table[:]
NOP = 0b0001_1111
constructstage2(NOP)
mask_bits(["Add", "Nand", "Sli", "AddSub", "AddInc"])

print_dict(NOP)
write_to_file("instruction_alu_control.bin")


# Create Register Control Table

stage1_table = old_stage1_table[:]
NOP = 0b0000_1111
constructstage2(NOP)
mask_bits(["Rout", "Rin", "Rd", "Rs", "Rd1", "Rd0"])

print_dict(NOP)
write_to_file("instruction_register_control.bin")

