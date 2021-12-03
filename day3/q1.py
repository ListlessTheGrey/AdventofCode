def convert(entry):
    binarystring = ''.join([str(int) for int in entry])
    return int(binarystring, 2)


def binary():
    decimallist1 = []
    decimallist2 = []
    with open("day3/input.txt", "r") as f:
        inputstring = f.read()
        inputlist = inputstring.split() 
        for x in range(len(inputlist[0])):
            count0 = count1 = 0
            for y in range(len(inputlist)):
                if inputlist[y][x] == "0":
                    count0 += 1
                else:
                    count1 += 1
            if count0 > count1:
                decimallist1.append(0)
            else:
                decimallist1.append(1)
            if count0 < count1:
                decimallist2.append(0)
            else:
                decimallist2.append(1)
    gammarate = convert(decimallist1)
    epsilonrate = convert(decimallist2)
    return gammarate * epsilonrate


if __name__ == "__main__":
    print(binary())
    
