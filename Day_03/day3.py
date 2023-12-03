from string import punctuation


# Part 1
def part_1(data):
    symbols = list(punctuation)
    symbols.remove(".")
    # print(symbols)
    sum = 0
    for y, line in enumerate(data):
        number = ""
        for x, char in enumerate(line):
            if char == "." or char in punctuation or x == len(line) - 1:
                if not number:
                    continue

                if char.isdigit():
                    number += char

                positions = []
                for row in [-1, 0, 1]:
                    for column in range(x - len(number) - 1, x + 1):
                        if (
                            (y == 0 and row == -1)
                            or column == -1
                            or (y + row) >= len(data)
                            or column > len(line)
                        ):
                            continue
                        positions.append((y + row, column))

                characters = [data[y][x] for y, x in positions if data[y][x] in symbols]
                if characters:
                    sum += int(number)
                number = ""
            else:
                number += char

    return sum


# Part Two
def part_2(data):
    symbols = list(punctuation)
    symbols.remove(".")
    # print(symbols)
    sum = 0
    gears = {}
    for y, line in enumerate(data):
        number = ""
        for x, char in enumerate(line):
            if char == "." or char in punctuation or x == len(line) - 1:
                if not number:
                    continue

                if char.isdigit():
                    number += char

                positions = []
                for row in [-1, 0, 1]:
                    for column in range(x - len(number) - 1, x + 1):
                        if (
                            (y == 0 and row == -1)
                            or column == -1
                            or (y + row) >= len(data)
                            or column > len(line)
                        ):
                            continue
                        positions.append((y + row, column))

                characters = [
                    [data[y][x], (y, x)] for y, x in positions if data[y][x] in symbols
                ]
                if characters:
                    if characters[0][0] == "*":
                        gears.setdefault(characters[0][1], []).append(int(number))
                number = ""
            else:
                number += char

    for gear, numbers in gears.items():
        if len(numbers) == 2:
            sum += numbers[0] * numbers[1]

    return sum


if __name__ == "__main__":
    with open("Day_03/input_3.txt") as f:
        data = f.read().splitlines()
    print(part_1(data))
    print(part_2(data))
