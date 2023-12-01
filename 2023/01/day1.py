def solve (lines):
    sum = 0
    for line in lines:
        print(line)
        for element in line:
            if element.isdigit():
                print(element)
                sum += int(element) * 10
                break
        line = line [::-1]
        print("reverse")
        for element in line:
            if element.isdigit():
                print(element)
                sum += int(element)
                break
    print(sum)

def transform():
    input = open("input_j.txt", "r")
    lines = [line.rstrip() for line in input]
    res = []
    for line in lines:
        numbers = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
        for number in numbers:
            while(line.find(number) != -1):
                line = line [:line.find(number)+1] + numbers[number] + line [line.find(number)+1:]
                print(line)
        res.append(line)
    return res

if __name__ == '__main__':
    solve(transform())