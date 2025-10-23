from unittest import TestCase
import TestAssignment

class Test(TestCase):
    def test_example(self):
        expected = 5
        actual = TestAssignment.example()
        self.assertEqual(expected,actual)
