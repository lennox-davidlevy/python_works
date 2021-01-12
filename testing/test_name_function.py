import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name(first="janis", last="joplin")
        self.assertEqual(formatted_name, "Joplin, Janis")

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(first="edgar", last="poe", middle="allen")
        self.assertEqual(formatted_name, "Poe, Edgar Allen")


if __name__ == "__main__":
    unittest.main()
