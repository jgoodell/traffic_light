import unittest


import traffic_light


class BasicTest(unittest.TestCase):
    def test_happy_path(self):
        assert traffic_light.TrafficLight(red=60, yellow=20, green=60)
        assert traffic_light.TrafficLightController(lights=list())
