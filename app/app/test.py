"""
Sample test file
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subs_numbers(self):
        """Test that two numbers are subtracted and returned"""
        res = calc.subs(3, 8)
        self.assertEqual(res, -5)
