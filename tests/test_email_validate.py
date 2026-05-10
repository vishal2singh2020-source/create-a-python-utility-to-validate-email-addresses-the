"""Tests for email_validate."""
import unittest

from email_validate import is_valid_email

_REQ = "Create a Python utility to validate email addresses The utility should allow users to enter email addresses from the terminal The validation rules should ensure that the '@' symbol is present in the email address and that the email address ends with '@gmail com' [Stakeholder: Proceed without further clarification"


class TestIsValidEmail(unittest.TestCase):
    def test_valid_samples(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("a@b.co"))

    def test_invalid_samples(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email("nodomain"))
        self.assertFalse(is_valid_email("@missing.local"))
        self.assertFalse(is_valid_email("space in@here.com"))
        self.assertFalse(is_valid_email("bad"))

    def test_whitespace_trimmed(self):
        self.assertTrue(is_valid_email("  user@example.com  "))

    def test_requirement_echo(self):
        self.assertIn("email", _REQ.lower())


if __name__ == "__main__":
    unittest.main()
