class TrafficLightController(object):
    """Class definition of a traffic light controller."""
    def __init__(self, lights=list(), stop=60, caution=20, go=60, caution_overlap=10, stop_overlap=3):
        """Class initializer for TrafficLightController instances.

        Keyword arguments:
        lights -- List of TrafficLight instances.
        stop -- Integer value indicating how long in seconds the stop sequence is.
        caution -- Integer value indicating how long in seconds the stop sequence is.
        go -- Integer value indicating how long in seconds the stop sequence is.
        caution_overlap = Integer value indicating long in seconds the caution overlap is.
        stop_overlap = Integer value indicating long in seconds the stop overlap is.
        """
        self.lights = lights
        self.stop = stop
        self.caution = caution
        self.go = go
        self.caution_overlap = caution_overlap
        self.stop_overlap = stop_overlap
