RULE = [
    ['■■■', 0],
    ['■■ ', 0],
    ['■ ■', 0],
    ['■  ', 0],
    [' ■■', 0],
    [' ■ ', 0],
    ['  ■', 0],
    ['   ', 0]
]

LIST_MAP = {

}


def numToBinary(num):
    return f'{num:08b}'


def numToRule(num):
    for i, curr, in enumerate(num):
        RULE[i][1] = int(curr)


def arrToListMap(arr):
    for a in arr:
        LIST_MAP[a[0]] = '■' if a[1] == 1 else ' '


def start(num, string, countRows):
    if (num > 255):
        return False

    binaryNum = numToBinary(num)
    numToRule(binaryNum)

    arrToListMap(RULE)

    maxLength = len(string) + countRows
    res = wolfram(string, countRows, maxLength=maxLength)
    print(res)


def normalize(maxLength, string):
    diff = (maxLength * 2 - len(string)) // 2 + 1

    return f'{" " * diff}{string}{" " * diff}'


def wolfram(string, countRows, output='', j=1, maxLength=3):
    stringLength = len(string)
    string = f'  {string}  '

    stringLength = len(string)
    res = ''

    for i in range(stringLength - 2):
        res += f'{LIST_MAP[string[i: i+3]]}'

    string = normalize(maxLength, string)

    if (j < countRows + 1):
        output += f'{string}\n'
        return wolfram(res, countRows, output, j + 1, maxLength=maxLength)
    else:
        return output


str = '■'

number = 18
countRows = 100
start(number, str, countRows)
