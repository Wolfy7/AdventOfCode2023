import unittest
import day1


class TestDay1(unittest.TestCase):
    def test_part_1(self):
        data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet""".splitlines()

        result = day1.part_1(data)
        self.assertEqual(142, result)

    def test_part_2(self):
        data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen""".splitlines()

        result = day1.part_2(data)
        self.assertEqual(281, result)


if __name__ == "__main__":
    unittest.main()
