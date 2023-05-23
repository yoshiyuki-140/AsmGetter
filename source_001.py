#coding:utf-8


import os

def createHexList(csvFilePath:str):
    if os.path.splitext(csvFilePath) != '.csv':
        assert Exception("reading file must be csv format!")

    with open(csvFilePath,encoding='utf-8',mode='r') as f:
        hexList = [str(h) for h in f.read().strip('\n').split(',')]

    return hexList

hexList = [0x8000,0x40c3,0x4109,0x38e0,0xf001,0x9000]
hexList = createHexList('./hexList001.csv')

opeCodeDict = {
        '0000':'and',
        '0001':'nor',
        '0010':'add',
        '0011':'sub',
        '0100':'addi',
        '0101':'sll',
        '0110':'',
        '0111':'',
        '1000':'nop',
        '1001':'halt',
        '1010':'',
        '1011':'',
        '1100':'lw',
        '1101':'sw',
        '1110':'jnz',
        '1111':'j'}

# print(list(opeCodeDict.keys()))
for i,v in enumerate(hexList):
    sv = str(bin(v)).lstrip('0b')
    vstr = f"{i+1}:{f'{sv[:-13]}_{sv[-13:-9]}_{sv[-9:-5]}_{sv[-5:-1]}'.zfill(19)}"
    print(vstr)
    for opC in list(opeCodeDict.keys()):
        if opC == sv[:-13].zfill(4):
            print(f"{opC}:{opeCodeDict[opC]}")

