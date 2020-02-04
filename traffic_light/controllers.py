class TrafficLightController(object):
    """Class definition of a traffic light controller."""
    
    def __init__(self, lights=list(), halt=60, caution=20, proceed=60, caution_overlap=10, halt_overlap=3):
        """Class initializer for TrafficLightController instances.

        Keyword arguments:
        lights -- List of TrafficLight instances.
        halt -- Integer value indicating how long in seconds the halt sequence is.
        caution -- Integer value indicating how long in seconds the caution sequence is.
        go -- Integer value indicating how long in seconds the proceed sequence is.
        caution_overlap = Integer value indicating long in seconds the caution overlap is.
        halt_overlap = Integer value indicating long in seconds the halt overlap is.
        """
        self.lights = lights
        self.halt = halt
        self.caution = caution
        self.proceed = proceed
        self.caution_overlap = caution_overlap
        self.halt_overlap = halt_overlap

    def cycle_lights(self):
        """Cycles the lights to the next sequence."""
        for light in self.lights:
            light.increment_cycle()

    def initialize(self):
        """Initialize the traffic lights into operation."""
        [each.initialize_cycle() for each in self.lights]

    @property
    def duration(self):
        """Returns the duration in seconds based on the state of the light. Typically
        called right after cycle_lights.
        """
        if self.lights[0].red:
            return self.halt
        elif self.lights[0].yellow:
            return self.caution
        elif self.lights[0].green:
            return self.proceed
        else:
            return 5
