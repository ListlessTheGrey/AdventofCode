def position():
    horizontal = depth = 0
    with open("day2/input.txt", "r") as f:
        inputstring = f.read()
        inputlist = inputstring.split()
        for i in range(len(inputlist)):
            if inputlist[i] == 'forward':
                horizontal += int(inputlist[i + 1])
            elif inputlist[i] == 'up':
                depth -= int(inputlist[i + 1])
            elif inputlist[i] == 'down':
                depth += int(inputlist[i + 1])
                print(inputlist[i])
                print(inputlist[i + 1])
            else:
                pass
        print(horizontal)
        print(depth)
        return horizontal * depth


if __name__ == "__main__":
    print(position())
