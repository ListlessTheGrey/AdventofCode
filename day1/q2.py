def three():  
    with open("day1/input.txt", "r") as f:
        inputstring = f.read()
    inputlist = inputstring.split()
    inputlist = [int(x) for x in inputlist]
    increasecount = 0
    threelist = []
    length = len(threelist)
    for i in range(length):
        if threelist[i - 1] < threelist[i]:
            increasecount += 1
        else:
            pass
    return increasecount

def main():
    print(three())

if __name__ == "__main__":
    main()
    
