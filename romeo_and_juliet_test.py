import unittest
from unittest.mock import patch, mock_open
import sys
import io
from romeo_and_juliet import *

class MockMap(Map):
    storyline = None
    play_executed = False

    def advance_scene(self, a_storyline):
        self.storyline = a_storyline
    def play(self):
        self.play_executed = True
        

class TestScene(unittest.TestCase):
    def test_print_description(self):
        a_scene = Scene(Map())
        # Capturing the standard output as a test harness.
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        a_scene.print_description()
        self.assertEqual(capturedOutput.getvalue(), dedent("""
            This scene is yet to be initialized\n
            """))
        # Releasing standard output.
        sys.stdout = sys.__stdout__
    
    def test_prompt_user(self):
        a_map = MockMap()
        a_scene = Scene(a_map)
        with patch("builtins.input", return_value = "yes"):
            a_scene.prompt_user()
            self.assertEqual(a_map.storyline, Storyline.CLASSIC)
        with patch("builtins.input", return_value = "no"):
            a_scene.prompt_user()
            self.assertEqual(a_map.storyline, Storyline.ALTERNATIVE)
        self.assertTrue(a_map.play_executed)

class TestTheMaskedBall(unittest.TestCase):
    def test_get_message(self):
        scene = TheMaskedBall(MockMap())
        self.assertEqual(scene.get_message(), """
            It was a starry night in Verona.
            Romeo, Benvolio, Mercutio, and others from the Montague
            household make their way to the Capulet Masked Ball with
            masks concealing their identities.
            As they enter the fest Romeo locks eyes with the most beautiful
            creature he has ever seen. He instantly falls in love.
            And they kiss.
            """)

    def test_get_prompt(self):
        scene = TheBalcony(MockMap())
        self.assertEqual(scene.get_prompt(), "Was that Juliet Capulet? Yes or No > ")
    

class TestTheBalcony(unittest.TestCase):
    def test_get_message(self):
        scene = TheBalcony(MockMap())
        self.assertEqual(scene.get_message(), """
            Just outside the Capulet orchard, Romeo hopes to see
            his beloved Juliet again after falling in love with her
            at first sight. Romeo stands in the shadows beneath Juliet's
            bedroom window, thinking she's alone, Juliet reveals her love for Romeo,
            and despairs over the feud between the two families. Romeo listens
            and steps out of the darkness. After professing their devotions,
            Juliet suggests they marry in secret.
            """)
    
    def test_get_prompt(self):
        scene = TheBalcony(MockMap())
        self.assertEqual(scene.get_prompt(), "Juliet just proposed to you. Do you say Yes or No > ")

class TestTheDuel(unittest.TestCase):
    def test_get_message(self):
        scene = TheDuel(MockMap())
        self.assertEqual(scene.get_message(), """
            During the heat of the day, Benvolio and Mercutio are
            loitering on the streets of Verona when Tybalt arrives
            looking for Romeo. Mercutio is deliberately provocative
            and tries to draw Tybalt into an argument so that they can fight.
            Romeo appears and Tybalt insults him, hoping he will respond 
            to the challenge, but Romeo refuses because he is marrying Juliet. 
            Tybalt and Mercutio draw their swords and fight. To stop 
            the battle, Romeo steps between them and Tybalt stabs 
            Mercutio under Romeo's arm. Mercutio's wound is fatal. 
            Blinded by rage over Mercutio's death, Romeo attacks 
            Tybalt and kills him.
            """)
    
    def test_get_prompt(self):
        scene = TheDuel(MockMap())
        self.assertEqual(scene.get_prompt(), "You just killed Tybalt. Do you flee? Yes or No > ")

class MockScene(Scene):
    was_entered = False
    def enter(self):
        self.was_entered = True

class TestMap(unittest.TestCase):
    def test_play(self):
        a_map = Map()
        mock_scene = MockScene(a_map)
        a_map.current_scene = mock_scene
        a_map.play()
        self.assertTrue(mock_scene.was_entered)      

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

if __name__ == '__main__':
    unittest.main()