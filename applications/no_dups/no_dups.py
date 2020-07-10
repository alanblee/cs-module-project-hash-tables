def no_dups(s):
    splitStr = s.split()
    strSet = set(splitStr)
    outputStr = ""

    for str in splitStr:
        if str in strSet:
            outputStr += str + " "
            strSet.remove(str)

    # remove the extra space
    outputStr = outputStr[:-1]
    return outputStr


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
