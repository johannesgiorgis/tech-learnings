"""
Mock Demo
"""

import unittest
from unittest.mock import Mock, call


class MyClassA:
    """Class for mock demo"""

    def foo(self):
        """Return a number"""
        # Assume it does some lengthy computation here (not shown)
        return 100

    def foo2(self, num):
        """Return another number"""
        # Assume it does some lengthy computation here (not shown)
        return num + 200

    def compute(self):
        """Demonstrate use of mock objects"""
        x1 = self.foo()
        x2 = self.foo2(x1)
        print(f"x1 = {x1}, x2 = {x2}")
        result = x1 + x2
        print(f"In MyClassA.compute, result = x1 + x2 -> {result}")
        return result


class TestA(unittest.TestCase):
    """Write test cases for methods from class MyClassA"""

    def test_compute(self):
        """Unit test for MyClassA.compute"""
        a = MyClassA()

        # Create a mock object and mock methods of MyClassA
        mockObj = Mock()
        a.foo = mockObj.foo
        a.foo2 = mockObj.foo2

        # Assuming you know the return values, set those for the mocks
        a.foo.return_value = 100
        a.foo2.return_value = 300

        # Run the computation. Calls to foo and foo2 in compute method are
        # now replaced with mock object calls that return the desired value
        result = a.compute()

        # Verify the results
        self.assertEqual(result, 400)

        # Get info on how the mock objects are actually called by compute.
        test_call_list = mockObj.mock_calls
        print(f"test_call_list = {test_call_list}")

        # Compare it against some reference calling order
        reference_call_list = [call.foo(), call.foo2(100)]
        self.assertEqual(test_call_list, reference_call_list)

    def test_compute_with_patch(self):
        """Unit test for MyClassA.compute using mock.patch"""
        print("Running test_compute_with_patch...")
        print(__name__)
        with unittest.mock.patch(
            "test.mockdemo.MyClassA.foo", new=Mock(return_value=500)
        ):
            a = MyClassA()
            result = a.compute()

            # Verify the results. The test is expected to fail since we
            # are using a return value of 500 using MyClassA.foo!
            self.assertEqual(result, 400)

    def test_compute_with_patch_alternate(self):
        """Unit test for MyClassA.compute, using mock.patch

        .. note:: This uses 'mock.patch' but does not use the 'new' arg
        """
        print("Running test_compute_with_patch_alternate...")
        # mockObj = Mock()
        with unittest.mock.patch("test.mockdemo.MyClassA.foo") as foo_patch:
            foo_patch.return_value = 500
            a = MyClassA()
            result = a.compute()

            # Verify the results. The test is expected to fail since we
            # are using a return value of 500 using MyClassA.foo!
            self.assertEqual(result, 400)


if __name__ == "__main__":
    unittest.main()
