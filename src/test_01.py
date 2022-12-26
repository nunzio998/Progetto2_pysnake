import time
import unittest
import numpy as np
from PIL import Image
from unittest import TestCase

from main import play

class TestSuite(TestCase):
    def test_01(self):
        self.assertEqual(test_passed("data/gamefile_01.json", "data/final_field_01.png", "data/expected_01.png", 4), "OK")

    def test_02(self):
        self.assertEqual(test_passed("data/gamefile_02.json", "data/final_field_02.png", "data/expected_02.png", 5), "OK")

    def test_03(self):
        self.assertEqual(test_passed("data/gamefile_03.json", "data/final_field_03.png", "data/expected_03.png", 14), "OK")

    def test_04(self):
        self.assertEqual(test_passed("data/gamefile_04.json", "data/final_field_04.png", "data/expected_04.png", 8), "OK")

    def test_05(self):
        self.assertEqual(test_passed("data/gamefile_05.json", "data/final_field_05.png", "data/expected_05.png", 29), "OK")

    def test_06(self):
        self.assertEqual(test_passed("data/gamefile_06.json", "data/final_field_06.png", "data/expected_06.png", 14), "OK")

    def test_07(self):
        self.assertEqual(test_passed("data/gamefile_07.json", "data/final_field_07.png", "data/expected_07.png", 49), "OK")

    def test_08(self):
        self.assertEqual(test_passed("data/gamefile_08.json", "data/final_field_08.png", "data/expected_08.png", 5), "OK")

    def test_09(self):
        # this is a hidden test
        pass

    def test_10(self):
        # this is a hidden test
        pass

    def test_11(self):
        # this is a hidden test
        pass

    def test_12(self):
        # this is a hidden test
        pass

    def test_13(self):
        # this test is aimed at evaluating the time elapsed to execute 10 times the gamefile_04.
        st = time.time()
        for i in range(10):
            play("data/gamefile_04.json")
        et = time.time()
        print(f"Elapsed time: { (et - st) * 1000 }ms")


def test_passed(game_file: str, final_field: str, expected_field: str, expected_len: int) -> str:
    length = play(game_file)
    if not length == expected_len:
        return f"Expected snake length is { expected_len }. We have { length } instead."

    if not are_equal(final_field, expected_field):
        return "Expected image differs from the computed one."

    return "OK"

def are_equal(final_field: str, expected_field: str) -> bool:
    a1 = load_image(final_field)
    a2 = load_image(expected_field)

    return np.array_equal(a1, a2)

def load_image(filename: str) -> np.ndarray:
    img = Image.open(filename)
    return np.array(img)

if __name__ == '__main__':
    unittest.main()