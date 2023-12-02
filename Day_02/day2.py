# Part 1
def part_1(data, bag):
    print(bag)
    sum_of_ids = 0
    for game in data:
        game_is_possible = True
        game_id = int(game.split(":")[0].split(" ")[1])
        sets_of_cubes = game.split(":")[1].split(";")
        for set_of_cubes in sets_of_cubes:
            cubes = [c.strip().split(" ") for c in set_of_cubes.split(",")]
            for cube in cubes:
                if bag[cube[1]] < int(cube[0]):
                    game_is_possible = False

        if game_is_possible:
            sum_of_ids += game_id

    return sum_of_ids


# Part Two
def part_2(data):
    sum = 0
    for game in data:
        few_cubes = {"red": 0, "green": 0, "blue": 0}
        sets_of_cubes = game.split(":")[1].split(";")
        for set_of_cubes in sets_of_cubes:
            cubes = [c.strip().split(" ") for c in set_of_cubes.split(",")]
            for cube in cubes:
                if few_cubes[cube[1]] < int(cube[0]):
                    few_cubes[cube[1]] = int(cube[0])
        sum_cubes = 1
        for item in few_cubes.values():
            sum_cubes *= item

        sum += sum_cubes

    return sum


if __name__ == "__main__":
    with open("Day_02/input_2.txt") as f:
        data = f.read().splitlines()
    print(part_1(data, {"red": 12, "green": 13, "blue": 14}))
    print(part_2(data))
