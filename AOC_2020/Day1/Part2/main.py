import math

with open("AOC_2020\\Day1\\Part2\\inputD1P2.txt", 'r') as f:
    dt = f.read().replace("\n", " ").split()


def find_sum():


    for x in dt:
        for y in dt:
            for z in dt:
                x = int(x)
                y = int(y)
                z = int(z)
                sum = x + y + z

                if sum == 2020:
                    return f"The three numbers that sum to {sum} are: {x}, {y}, and {z}; and their product is {x * y * z}"


print(find_sum())