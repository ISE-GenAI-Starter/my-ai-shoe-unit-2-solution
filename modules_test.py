#############################################################################
# modules_test.py
#
# This file contains tests for modules.py.
#
# You will write these tests in Unit 2.
#############################################################################

from streamlit.testing.v1 import AppTest
import unittest
from modules import display_post, display_activity_summary, display_genai_advice, display_recent_workouts

app = AppTest.from_file("app.py")
app.run()
assert not app.exception

# Write the tests below
# TODO(Nyah): POST do image urls display? is it okay if there's no image?
# Calling it multiple times with different args doesn't change the previous one
# All data is displayed

class TestDisplayPost(unittest.TestCase):
    """Tests the display_post function."""

    def test_foo(self):
        """Tests foo."""
        pass


class TestDisplayActivitySummary(unittest.TestCase):
    """Tests the display_activity_summary function."""

    def test_foo(self):
        """Tests foo."""
        pass


class TestDisplayGenAiAdvice(unittest.TestCase):
    """Tests the display_genai_advice function."""

    def test_foo(self):
        """Tests foo."""
        pass


class TestDisplayRecentWorkouts(unittest.TestCase):
    """Tests the display_recent_workouts function."""

    def test_foo(self):
        """Tests foo."""
        pass


if __name__ == "__main__":
    unittest.main()