with open("input.txt") as f:
    numbers = [int(x.strip()) for x in f.readlines()]


def pt1():
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            if j > i:
                if num1+num2 == 2020:
                    return num1*num2

def pt2():
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers):
            for k, num3 in enumerate(numbers):
                if num1+num2+num3 == 2020:
                    return num1*num2*num3        
        
    
print("Part 1:", pt1())
print("Part 2:", pt2())




