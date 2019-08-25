import unittest
from unittest.mock import patch, mock_open
import sys
import io
from romeo_and_juliet import *


class TestStringMethods(unittest.TestCase):
    def test_initial_state(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
   
    def test_advance_scene_classic(self):
       a_map = Map()
       self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
       a_map.advance_scene(Storyline.CLASSIC)
       self.assertIsInstance(a_map.get_current_scene(), TheBalcony)
       a_map.advance_scene(Storyline.CLASSIC)
       self.assertIsInstance(a_map.get_current_scene(), TheDuel)
       a_map.advance_scene(Storyline.CLASSIC)
       self.assertIsInstance(a_map.get_current_scene(), TheArrangement)
       a_map.advance_scene(Storyline.CLASSIC)
       self.assertIsInstance(a_map.get_current_scene(), TheApothecary)
       a_map.advance_scene(Storyline.CLASSIC)
       self.assertIsInstance(a_map.get_current_scene(), TheCapuletTomb)
       with self.assertRaises(Exception):
           a_map.advance_scene(Storyline.CLASSIC)

    def test_advance_scene_alternative_one(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
        a_map.advance_scene(Storyline.ALTERNATIVE)
        self.assertIsInstance(a_map.get_current_scene(), TheAlternativeEnding)
        with self.assertRaises(Exception):
            a_map.advance_scene(Storyline.ALTERNATIVE)
    
    def test_advance_scene_alternative_two(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheBalcony)
        a_map.advance_scene(Storyline.ALTERNATIVE)
        self.assertIsInstance(a_map.get_current_scene(), TheAlternativeEnding)
        with self.assertRaises(Exception):
            a_map.advance_scene(Storyline.ALTERNATIVE)

    def test_advance_scene_alternative_three(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheBalcony)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheDuel)
        a_map.advance_scene(Storyline.ALTERNATIVE)
        self.assertIsInstance(a_map.get_current_scene(), TheAlternativeEnding)
        with self.assertRaises(Exception):
            a_map.advance_scene(Storyline.ALTERNATIVE)

    def test_advance_scene_alternative_four(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheBalcony)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheDuel)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheArrangement)
        a_map.advance_scene(Storyline.ALTERNATIVE)
        self.assertIsInstance(a_map.get_current_scene(), TheAlternativeEnding)
        with self.assertRaises(Exception):
            a_map.advance_scene(Storyline.ALTERNATIVE)               

    def test_advance_scene_alternative_five(self):
        a_map = Map()
        self.assertIsInstance(a_map.get_current_scene(), TheMaskedBall)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheBalcony)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheDuel)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheArrangement)
        a_map.advance_scene(Storyline.CLASSIC)
        self.assertIsInstance(a_map.get_current_scene(), TheApothecary)
        a_map.advance_scene(Storyline.ALTERNATIVE)
        self.assertIsInstance(a_map.get_current_scene(), TheAlternativeEnding)
        with self.assertRaises(Exception):
            a_map.advance_scene(Storyline.ALTERNATIVE) 

    def test_enter_masked_ball(self):
        a_scene = TheMaskedBall(Map())
        # Capturing the standard output as a test harness.
        capturedOutput = io.StringIO()
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

    def test_prompt_user_masked_ball(self):
        a_scene = TheMaskedBall(Map())
        with patch("builtins.input", return_value = "yes"):
            assert  a_scene.prompt_user() == "classic"
        with patch("builtins.input", return_value = "no"):
            assert a_scene.prompt_user() == "alternative"

    def test_enter_balcony(self):
        a_scene = TheBalcony(Map())
        # Capturing the standard output as a test harness.
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        a_scene.enter()
        self.assertEqual(capturedOutput.getvalue(), dedent("""
            Just outside the Capulet orchard, Romeo hopes to see
            his beloved Juliet again after falling in love with her
            at first sight. Romeo stands in the shadows beneath Juliet's
            bedroom window, thinking she's alone, Juliet reveals her love for Romeo,
            and despairs over the feud between the two families. Romeo listens
            and steps out of the darkness. After professing their devotions,
            Juliet suggests they marry in secret.\n
        """))
        # Releasing standard output.
        sys.stdout = sys.__stdout__

    def test_prompt_user_balcony(self):
        a_scene = TheBalcony(Map())
        with patch("builtins.input", return_value = "yes"):
            assert a_scene.prompt_user() == "classic"
        with patch("builtins.input", return_value = "no"):
            assert a_scene.prompt_user() == "alternative"

if __name__ == '__main__':
    unittest.main()