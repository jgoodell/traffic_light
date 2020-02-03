import traffic_light

class TrafficLight(object):
    """Class definition of a traffic light.
    """
    def __init__(self):
        """Class initializer for TrafficLight instances."""
        self.red = None
        self.yellow = None
        self.green = None
        self.flashing = False

    def initialize_flashing(self, stop=True):
        if stop:
            self.green = False
            self.yellow = False
            self.red = True
            self.flashing = True
        else:
            self.green = False
            self.yellow = True
            self.red = False
            self.flashing = True

    def initialize_cycle(self, stop=True):
        """Traffic light cycle initializer.

        Keyword arguments:
        red -- Boolean value indicating light is on.
        yellow -- Boolean value indicating light is on.
        green -- Boolean value indicating light is on.
        flashing -- Boolean value indicating ligth is on.
        """
        if stop:
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
