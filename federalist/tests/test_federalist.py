"""
This is the testing framework for

"""
import unittest

class FederalistTest(unittest.TestCase):
    """Doc string for unit test"""

    # TODO Implement test for loading Gutenberg URI
    # TODO Implement test for failing loading non-Gutenberg URI
    # TODO Implement test for loading local Gutenberg file
    # TODO Implement test for failing local non-Gutenberg file
    # TODO Implement test for loading css
    # TODO Implement test for failing non-css
    # TODO Implement test for stripping Gutenberg test

    def testLoadGut(self):
        """Tests that Gutenberg URIs are loaded properly.
        """
        book = GutBook("http://www.gutenberg.org/files/1404/1404-h/1404-h.htm") 
        title = "The Federalist Papers"

        self.assertEqual(GutBook.title,self.title, 'Titles are not equal. Test failed.')

if __name__ == "__main__":
    unittest.main()
