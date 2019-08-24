from sys import exit
from textwrap import dedent

class Scene(object):
    pass

class Director(object):
    pass

class TheMaskedBall(Scene):
    
    def enter(self):
        print(dedent("""
            It was a starry night in Verona.
            Romeo, Benvolio, Mercutio, and others from the Montague 
            household make their way to the Capulet Masked Ball with
            masks concealing their identities. 
            As they enter the fest Romeo locks eyes with the most beautiful
            creature he has ever seen. He instantly falls in love.
            """))

class TheBalcony(Scene):
    pass

class TheDuel(Scene):
    pass

class TheArrangement(Scene):
    pass

class TheApothecary(Scene):
    pass

class TheCapuletTomb(Scene):
    pass


class Map(object):

    scenes = {
        "the_masked_ball": TheMaskedBall(),
        "the_balcony": TheBalcony(),
        "the_duel": TheDuel(),
        "the_arrangement": TheArrangement(),
        "the_apothecary": TheApothecary(),
        "the_capulet_tomb": TheCapuletTomb()
    }

    current_scene = None

    def __init__(self):
        self.current_scene = self.scenes["the_masked_ball"]

    def get_current_scene(self):
        return self.current_scene

    def advance_scene(self):
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
        
        return self.current_scene

