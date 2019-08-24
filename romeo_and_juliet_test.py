import unittest
import StringIO
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
        self.assertEqual(capturedOutput.getvalue(),
            "You've entered The Masked Ball\n")
        # Releasing standard output.
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()