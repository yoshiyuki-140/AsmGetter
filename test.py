opeCodeDict = {
    '0000': 'and',
    '0001': 'nor',
    '0010': 'add',
    '0011': 'sub',
    '0100': 'addi',
    '0101': 'sll',
    '0110': '',
    '0111': '',
    '1000': 'nop',
    '1001': 'halt',
    '1010': '',
    '1011': '',
    '1100': 'lw',
    '1101': 'sw',
    '1110': 'jnz',
    '1111': 'j'}

TestHexList = [0x8000, 0x40c3, 0x4109, 0x38e0, 0xf001, 0x9000]


def showAsmFromOpeCode(hexList: list):
    for i, v in enumerate(hexList):
        sv = str(bin(v)).lstrip('0b')
        vstr = f"{i+1}:\nHEX -> {hex(hexList[i])}:\nBIN -> {f'{sv[:-13]}_{sv[-13:-9]}_{sv[-9:-5]}_{sv[-5:-1]}'.zfill(19)}"
        print(vstr)
        for opC in list(opeCodeDict.keys()):
            if opC == sv[:-13].zfill(4):
                print(f"ASM -> {opC}:{opeCodeDict[opC]}")


if __name__ == '__main__':
    showAsmFromOpeCode(TestHexList)
