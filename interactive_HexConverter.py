#coding:utf-8
# Author : Yoshiyuki Kurose

def showAsmFromOpeCode(H: str):
    # If you specified lang == 'en', this function will show english message.

    # Example:
    # H == "ab4f"
    #
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

    sv = str(bin(int('0x'+H, 16))).lstrip('0b')
    vstr = f"HEX -> {hex(int('0x'+H,16))}:\nBIN -> {f'{sv[:-13]}_{sv[-13:-9]}_{sv[-9:-5]}_{sv[-5:-1]}'.zfill(19)}"
    print(vstr)
    for opC in list(opeCodeDict.keys()):
        if opC == sv[:-13].zfill(4):
            print(f"ASM -> {opC}:{opeCodeDict[opC]}")

def main():
    while True:
        H = input("4桁以内で16進数を入力してください\n例:1f5c\n終了するためには'q'を入力してください\n >> ")
        if len(H) > 4:
            raise Exception("Inputted value must be with 4 digit!")
        exitCommand = ['q', 'Q', 'exit', 'EXIT']
        if H in exitCommand:
            break
        showAsmFromOpeCode(H)


if __name__ == "__main__":
    main()
