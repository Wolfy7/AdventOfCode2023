import unittest
from Day_03 import day3


class TestDay3(unittest.TestCase):
    def test_part_1(self):
        data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

        result = day3.part_1(data)
        self.assertEqual(4361, result)

    def test_part_2(self):
        data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

        result = day3.part_2(data)
        self.assertEqual(467835, result)


if __name__ == "__main__":
    unittest.main()
