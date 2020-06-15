import unittest


class MyUnitTests(unittest.TestCase):
    def setUp(self):
        print("In setUp...")

    def tearDown(self):
        print("Tearing Down the test.")
        print("~" * 10)

    @unittest.expectedFailure
    def test_3(self):
        print("in test_3")
        self.assertEqual(1 + 1, 3)

    @unittest.skip("Skipping test_2")
    def test_2(self):
        print("in test_2")
        self.assertEqual(1 + 1, 2)

    @unittest.skip("Skipping test_1")
    def test_1(self):
        print("in test_1")
        self.assertTrue(1 + 1 == 2)

    def will_not_be_called(self):
        print("this method will not be called automatically")


if __name__ == "__main__":
    unittest.main()
