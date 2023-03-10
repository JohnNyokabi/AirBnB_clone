#!/usr/bin/python3
"""Unit test for the file storage class
"""
import unittest
import pep8
from models import review
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """TestReviewClass tests suite for use of the review class
Args:
    unittest (): properties for unit testing
"""

    maxDiff = None

    def setUp(self):
        """Return to "" class attributes"""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    def test_module_doc(self):
        """check for module documentation"""
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """check for class documentation"""
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_doc(self):
        """check for method documentation"""
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

    def test_pep8(self):
        """test base and test_base for pep8 conformance"""
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/review.py'
        file2 = 'tests/test_models/test_review.py'
        result = style.check_file([file1], [file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")

    def test_is_instance(self):
        """Test if review is instance of basemodel"""
        my_review = Review()
        self.assertTrue(isinstance(my_review, BaseModel))

    def test_field_types(self):
        """test user field attributes"""
        my_review = Review()
        self.assertTrue(type(my_review.place_id) == str)
        self.assertTrue(type(my_review.user_id) == str)
        self.assertTrue(type(my_review.text) == str)


if __name__ == '__main__':
    unittest.main()
