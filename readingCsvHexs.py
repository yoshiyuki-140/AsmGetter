import os.path

def createHexListFromFile(csvFilePath:str):
    if os.path.splitext(csvFilePath)[-1] != '.csv':
        assert Exception("reading file must be csv format!")

    with open(csvFilePath,encoding='utf-8',mode='r') as f:
        hexList = [str(h) for h in f.read().strip('\n').split(',')]

    return hexList
