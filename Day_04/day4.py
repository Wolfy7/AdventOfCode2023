# Part 1
def part_1(data):
    result = 0

    for card in data:
        winning_numbers, numbers = card.split(":")[1].split("|")
        numbers_intersection = set(winning_numbers.strip().split(" ")) & set(numbers.strip().split(" "))
        numbers_intersection.discard("")
        if(numbers_intersection):
            points = 0
            for number in numbers_intersection:
                if(points == 0):
                    points = 1
                else:
                    points *= 2
            result += points

    return result

from collections import defaultdict

# Part Two
def part_2(data):
    cards = defaultdict(lambda: 1)
    for index, card in enumerate(data):
        card_name = int(card.split(":")[0].replace("Card", "").strip())
        winning_numbers, numbers = card.split(":")[1].split("|")
        numbers_intersection = set(winning_numbers.strip().split(" ")) & set(numbers.strip().split(" "))
        numbers_intersection.discard("")
        for _ in range(cards[card_name]):
            for copie in range(1, len(numbers_intersection)+1):
                cards[index + 1 + copie] += 1
    return sum(cards.values())


if __name__ == "__main__":
    with open("Day_04/input_4.txt") as f:
        data = f.read().splitlines()
    print(part_1(data))
    print(part_2(data))
