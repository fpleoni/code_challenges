from sys import exit
from textwrap import dedent
from enum import Enum

class Storyline(Enum):
    CLASSIC = "classic"
    ALTERNATIVE = "alternative"

class Scene(object):
    a_map = None
    
    def __init__(self, a_map):
        self.a_map = a_map

    def get_message(self):
        return """
            This scene is yet to be initialized
            """
    def get_prompt(self):
        return """
            This scene is yet to be initialized
            """
    
    def enter(self):
        self.print_description()
        self.prompt_user()
    
    def print_description(self):
        print(dedent(self.get_message()))

    def prompt_user(self):
        input_from_user = input(self.get_prompt()).lower()
        if input_from_user == "yes":
            self.a_map.advance_scene(Storyline.CLASSIC)
        elif input_from_user == "no":
            self.a_map.advance_scene(Storyline.ALTERNATIVE)
        self.a_map.play()

class TheMaskedBall(Scene):

    def get_message(self):
        return """
            It was a starry night in Verona.
            Romeo, Benvolio, Mercutio, and others from the Montague
            household make their way to the Capulet Masked Ball with
            masks concealing their identities.
            As they enter the fest Romeo locks eyes with the most beautiful
            creature he has ever seen. He instantly falls in love.
            And they kiss.
            """

    def get_prompt(self):
        return "Was that Juliet Capulet? Yes or No > "

class TheBalcony(Scene):

    def get_message(self):
        return """
            Just outside the Capulet orchard, Romeo hopes to see
            his beloved Juliet again after falling in love with her
            at first sight. Romeo stands in the shadows beneath Juliet's
            bedroom window, thinking she's alone, Juliet reveals her love for Romeo,
            and despairs over the feud between the two families. Romeo listens
            and steps out of the darkness. After professing their devotions,
            Juliet suggests they marry in secret.
            """
    
    def get_prompt(self):
        return "Juliet just proposed to you. Do you say Yes or No > "


class TheDuel(Scene):
    pass

class TheArrangement(Scene):
    pass

class TheApothecary(Scene):
    pass

class TheCapuletTomb(Scene):
    pass

class TheAlternativeEnding(Scene):
    pass

class Map(object):

    scenes = None
    current_scene = None

    def __init__(self):
        self.scenes = {
            "the_masked_ball": TheMaskedBall(self),
            "the_balcony": TheBalcony(self),
            "the_duel": TheDuel(self),
            "the_arrangement": TheArrangement(self),
            "the_apothecary": TheApothecary(self),
            "the_capulet_tomb": TheCapuletTomb(self),
            "the_alternative_ending": TheAlternativeEnding(self)
        }
        self.current_scene = self.scenes["the_masked_ball"]

    def get_current_scene(self):
        return self.current_scene

    def play(self):
        self.current_scene.enter()

    def advance_scene(self, storyline):
        if storyline == Storyline.CLASSIC:
            if self.current_scene == self.scenes["the_masked_ball"]:
                self.current_scene = self.scenes["the_balcony"]
            elif self.current_scene == self.scenes["the_balcony"]:
                self.current_scene = self.scenes["the_duel"]
            elif self.current_scene == self.scenes["the_duel"]:
                self.current_scene = self.scenes["the_arrangement"]
            elif self.current_scene == self.scenes["the_arrangement"]:
                self.current_scene = self.scenes["the_apothecary"]
            elif self.current_scene == self.scenes["the_apothecary"]:
                self.current_scene = self.scenes["the_capulet_tomb"]
            elif self.current_scene == self.scenes["the_capulet_tomb"]:
                raise Exception
        if storyline == Storyline.ALTERNATIVE:
            if self.current_scene == self.scenes["the_masked_ball"]:
                self.current_scene = self.scenes["the_alternative_ending"]
            elif self.current_scene == self.scenes["the_balcony"]:
                self.current_scene = self.scenes["the_alternative_ending"]
            elif self.current_scene == self.scenes["the_duel"]:
                self.current_scene = self.scenes["the_alternative_ending"]
            elif self.current_scene == self.scenes["the_arrangement"]:
                self.current_scene = self.scenes["the_alternative_ending"]
            elif self.current_scene == self.scenes["the_apothecary"]:
                self.current_scene = self.scenes["the_alternative_ending"]
            elif self.current_scene == self.scenes["the_alternative_ending"]:
                raise Exception

the_map = Map()
the_map.play()
