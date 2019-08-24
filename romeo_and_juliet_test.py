import unittest
import StringIO
from unittest import mock
from unittest.mock import patch
import sys
from romeo_and_juliet import *


class TestStringMethods(unittest.TestCase):
    def test_initial_state(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
   
    def test_advance_scene(self):
       a_map = Map()
       self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
       a_map.advance_scene()
       self.assertIsInstance(a_map.get_current_scene(), TheBalcony)
       a_map.advance_scene()
       self.assertIsInstance(a_map.get_current_scene(), TheDuel)
       a_map.advance_scene()
       self.assertIsInstance(a_map.get_current_scene(), TheArrangement)
       a_map.advance_scene()
       self.assertIsInstance(a_map.get_current_scene(), TheApothecary)
       a_map.advance_scene()
       self.assertIsInstance(a_map.get_current_scene(), TheCapuletTomb)
       with self.assertRaises(Exception):
           a_map.advance_scene()

    def test_enter(self):
        a_scene = TheMaskedBall()
        # Capturing the standard output as a test harness.
        capturedOutput = StringIO.StringIO()
        sys.stdout = capturedOutput
        a_scene.enter()
        self.assertEqual(capturedOutput.getvalue(), dedent("""
            It was a starry night in Verona.
            Romeo, Benvolio, Mercutio, and others from the Montague
            household make their way to the Capulet Masked Ball with
            masks concealing their identities.
            As they enter the fest Romeo locks eyes with the most beautiful
            creature he has ever seen. He instantly falls in love.
            And they kiss.\n
            """))
        # Releasing standard output.
        sys.stdout = sys.__stdout__

    def test_promt_user(self):
        a_scene = TheMaskedBall()
        a_scene.prompt_user()
        with mock.patch("builtins.input", return_value = "yes"):
            assert a_scene.story_path == "classic"
        with mock.patch("builtins.input", return_value = "no"):
            assert a_scene.story_path == "alternative"

if __name__ == '__main__':
    unittest.main()