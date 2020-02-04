import os

import traffic_light

class TrafficLight(object):
    """Class definition of a traffic light.
    """
    def __str__(self):
        """Instance Representation as a String"""
        if self.red:
            return open(
                __file__.split(
                    'traffic_light/data/text/red-default.txt'.split(os.path.sep)[0])[0] +\
                'traffic_light/data/text/red-default.txt', 'rb').read()
        elif self.yellow:
            return open(
                __file__.split(
                    'traffic_light/data/text/yellow-default.txt'.split(os.path.sep)[0])[0] +\
                'traffic_light/data/text/yellow-default.txt', 'rb').read()
        elif self.green:
            return open(
                __file__.split(
                    'traffic_light/data/text/green-default.txt'.split(os.path.sep)[0])[0] +\
                'traffic_light/data/text/green-default.txt', 'rb').read()
        else:
            return open(
                __file__.split(
                    'traffic_light/data/text/off-default.txt'.split(os.path.sep)[0])[0] +\
                'traffic_light/data/text/off-default.txt', 'rb').read()

    def __repr__(self):
        """Instance Representation"""
        return '<TrafficLight(red={red}, yellow={yellow}, green={green}, flashing={flashing})>'.format(red=self.red, yellow=self.yellow, green=self.green, flashing=self.flashing)
    
    def __init__(self):
        """Class initializer for TrafficLight instances."""
        self.red = None
        self.yellow = None
        self.green = None
        self.flashing = False

    def initialize_flashing(self, halt=True):
        """Initializes light into flashing mode.

        Keyword arguments:
        halt -- Boolean indicating if the light is flashing red or yellow.
        """
        if halt:
            self.green = False
            self.yellow = False
            self.red = True
            self.flashing = True
        else:
            self.green = False
            self.yellow = True
            self.red = False
            self.flashing = True

    def initialize_cycle(self, halt=True):
        """Traffic light cycle initializer.

        Keyword arguments:
        stop -- Boolean indicating if light is staring in red or yellow.
        """
        if halt:
            self.red = True
            self.yellow = False
            self.green = False
            self.flashing = False
        else:
            self.red = False
            self.yellow = True
            self.green = False
            self.flashing = False

    def increment_cycle(self):
        """Increments light into next sequence depending on current state. If
        flashing, the flashing stops and the light either moves to red or
        green depending on what condition the light is flashing red or yellow.
        Other wise green transitions to yellow, yellow to red and red to green.
        """
        if self.flashing:
            self.flashing = False
        if self.red:
            self.green = True
            self.red = False
        elif self.yellow:
            self.red = True
            self.yellow = False
        elif self.green:
            self.yellow = True
            self.green = False
        else:
            self.red = True
