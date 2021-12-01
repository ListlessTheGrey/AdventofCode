def list():    
    with open("day1/input.txt", "r") as f:
        inputstring = f.read()
    inputlist = inputstring.split()
    inputlist = [int(x) for x in inputlist]    
    increasecount = 0
    length = len(inputlist)
    for i in range(length):
        if inputlist[i - 1] < inputlist[i]:
            increasecount += 1
        else:
            pass
    return increasecount


if __name__ == "__main__":
    print(list())
    
