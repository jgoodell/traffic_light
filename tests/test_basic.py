import unittest


import traffic_light


class TrafficLightTest(unittest.TestCase):
    def setUp(self):
        self.traffic_light01 = traffic_light.TrafficLight()
        self.traffic_light02 = traffic_light.TrafficLight()
        self.traffic_light_controller = traffic_light.TrafficLightController(
            lights=[self.traffic_light01, self.traffic_light02],
            halt=180,
            caution=20,
            proceed=200
        )

    def test_controller(self):
        try:
            self.traffic_light_controller.initialize()
        except Exception, error:
            raise AssertionError(str(error))
        
        try:
            self.traffic_light_controller.cycle_lights()
        except Exception, error:
            raise AssertionError(str(error))

        try:
            duration = self.traffic_light_controller.duration
        except Exception, error:
            raise AssertionError(str(error))

        assert duration == 200

    def test_display(self):
        self.traffic_light01.initialize_cycle(halt=True)
        try:
            str(self.traffic_light01)
        except Exception, error:
            raise AssertionError(str(error))

        self.traffic_light01.increment_cycle()
        try:
            str(self.traffic_light01)
        except Exception, error:
            raise AssertionError(str(error))

        self.traffic_light01.increment_cycle()
        try:
            str(self.traffic_light01)
        except Exception, error:
            raise AssertionError(str(error))

        self.traffic_light01.increment_cycle()
        try:
            str(self.traffic_light01)
        except Exception, error:
            raise AssertionError(str(error))

    def test_cycle(self):
        assert self.traffic_light01.red == None
        assert self.traffic_light01.yellow == None
        assert self.traffic_light01.green == None
        assert self.traffic_light01.flashing == False

        self.traffic_light01.initialize_cycle(halt=True)
        
        assert self.traffic_light01.red == True
        assert self.traffic_light01.yellow == False
        assert self.traffic_light01.green == False
        assert self.traffic_light01.flashing == False
        
        self.traffic_light01.increment_cycle()
        
        assert self.traffic_light01.red == False
        assert self.traffic_light01.yellow == False
        assert self.traffic_light01.green == True
        assert self.traffic_light01.flashing == False
        
        self.traffic_light01.increment_cycle()
        
        assert self.traffic_light01.red == False
        assert self.traffic_light01.yellow == True
        assert self.traffic_light01.green == False
        assert self.traffic_light01.flashing == False
        
        self.traffic_light01.increment_cycle()
        
        assert self.traffic_light01.red == True
        assert self.traffic_light01.yellow == False
        assert self.traffic_light01.green == False
        assert self.traffic_light01.flashing == False
        
        assert self.traffic_light02.red == None
        assert self.traffic_light02.yellow == None
        assert self.traffic_light02.green == None
        assert self.traffic_light02.flashing == False

        self.traffic_light02.initialize_cycle(halt=False)
        
        assert self.traffic_light02.red == False
        assert self.traffic_light02.yellow == True
        assert self.traffic_light02.green == False
        assert self.traffic_light02.flashing == False
        
        self.traffic_light02.increment_cycle()
        
        assert self.traffic_light02.red == True
        assert self.traffic_light02.yellow == False
        assert self.traffic_light02.green == False
        assert self.traffic_light02.flashing == False
        
        self.traffic_light02.increment_cycle()
        
        assert self.traffic_light02.red == False
        assert self.traffic_light02.yellow == False
        assert self.traffic_light02.green == True
        assert self.traffic_light02.flashing == False
        
        self.traffic_light02.increment_cycle()
        
        assert self.traffic_light02.red == False
        assert self.traffic_light02.yellow == True
        assert self.traffic_light02.green == False
        assert self.traffic_light02.flashing == False
        
    def test_flashing(self):
        assert self.traffic_light01.red == None
        assert self.traffic_light01.yellow == None
        assert self.traffic_light01.green == None
        assert self.traffic_light01.flashing == False

        self.traffic_light01.initialize_flashing(halt=True)
        
        assert self.traffic_light01.red == True
        assert self.traffic_light01.yellow == False
        assert self.traffic_light01.green == False
        assert self.traffic_light01.flashing == True

        assert self.traffic_light02.red == None
        assert self.traffic_light02.yellow == None
        assert self.traffic_light02.green == None
        assert self.traffic_light02.flashing == False

        self.traffic_light02.initialize_flashing(halt=False)
        
        assert self.traffic_light02.red == False
        assert self.traffic_light02.yellow == True
        assert self.traffic_light02.green == False
        assert self.traffic_light02.flashing == True

