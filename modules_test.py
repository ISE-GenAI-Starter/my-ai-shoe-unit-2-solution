## modules_test.py
##
## Created for TechExchange 2025, Software Development Studio with Google
##
## This file contains tests for modules.py.
##
## You will write these tests in Unit 2.

from streamlit.testing.v1 import AppTest
import unittest

app = AppTest.from_file("app.py")
app.run()
assert not app.exception

class TestModules(unittest.TestCase):
    def test_display_post(self):
        pass

# TODO(nyahway): Write a template for the test file.

if __name__ == "__main__":
    unittest.main()