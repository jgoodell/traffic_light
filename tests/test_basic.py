import unittest


import traffic_light


class TrafficLightTest(unittest.TestCase):
    def setUp(self):
        self.traffic_light01 = traffic_light.TrafficLight()
        self.traffic_light02 = traffic_light.TrafficLight()

    def test_cycle(self):
        assert self.traffic_light01.red == None
        assert self.traffic_light01.yellow == None
        assert self.traffic_light01.green == None
        assert self.traffic_light01.flashing == False

        self.traffic_light01.initialize_cycle(stop=True)
        
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

        self.traffic_light02.initialize_cycle(stop=False)
        
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

        self.traffic_light01.initialize_flashing(stop=True)
        
        assert self.traffic_light01.red == True
        assert self.traffic_light01.yellow == False
        assert self.traffic_light01.green == False
        assert self.traffic_light01.flashing == True

        assert self.traffic_light02.red == None
        assert self.traffic_light02.yellow == None
        assert self.traffic_light02.green == None
        assert self.traffic_light02.flashing == False

        self.traffic_light02.initialize_flashing(stop=False)
        
        assert self.traffic_light02.red == False
        assert self.traffic_light02.yellow == True
        assert self.traffic_light02.green == False
        assert self.traffic_light02.flashing == True

