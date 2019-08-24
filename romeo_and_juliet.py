from sys import exit
from textwrap import dedent
from enum import Enum

class Storyline(Enum):
    CLASSIC = "classic"
    ALTERNATIVE = "alternative"

class Scene(object):
    pass

class Director(object):
    pass

class TheMaskedBall(Scene):

    story_path = None

    def enter(self):
        print(dedent("""
            It was a starry night in Verona.
            Romeo, Benvolio, Mercutio, and others from the Montague
            household make their way to the Capulet Masked Ball with
            masks concealing their identities.
            As they enter the fest Romeo locks eyes with the most beautiful
            creature he has ever seen. He instantly falls in love.
            And they kiss.
            """))

    def prompt_user(self):
        input_from_user = input("Was that Juliet Capulet? Yes or No > ").lower()
        if input_from_user == "yes":
            self.story_path = "classic"
        elif input_from_user == "no":
            self.story_path = "alternative" 
        return self.story_path

class TheBalcony(Scene):
    
    story_path = None

    def enter(self):
        print(dedent("""
            Just outside the Capulet orchard, Romeo hopes to see
            his beloved Juliet again after falling in love with her
            at first sight. Romeo stands in the shadows beneath Juliet's
            bedroom window, thinking she's alone, Juliet reveals her love for Romeo,
            and despairs over the feud between the two families. Romeo listens
            and steps out of the darkness. After professing their devotions,
            Juliet suggests they marry in secret.
            """))
    

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

    scenes = {
        "the_masked_ball": TheMaskedBall(),
        "the_balcony": TheBalcony(),
        "the_duel": TheDuel(),
        "the_arrangement": TheArrangement(),
        "the_apothecary": TheApothecary(),
        "the_capulet_tomb": TheCapuletTomb(),
        "the_alternative_ending": TheAlternativeEnding()
    }

    current_scene = None

    def __init__(self):
        self.current_scene = self.scenes["the_masked_ball"]

    def get_current_scene(self):
        return self.current_scene

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
        
        return self.current_scene

