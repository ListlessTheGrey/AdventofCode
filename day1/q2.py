def three():  
    with open("day1/input.txt", "r") as f:
        inputstring = f.read()
    inputlist = inputstring.split()
    inputlist = [int(x) for x in inputlist]
    increasecount = 0
    threelist = []
    length = len(inputlist)
    for i in range(length):
        try:
            threesum = inputlist[i] + inputlist[i + 1] + inputlist[i + 2]
            threelist.append(threesum)
        except:
            break
    threelength = len(threelist)
    for i in range(threelength):
        if threelist[i - 1] < threelist[i]:
            increasecount += 1
        else:
            pass
    return increasecount


if __name__ == "__main__":
    print(three())
    
