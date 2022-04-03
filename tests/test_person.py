from re import L
import unittest
from src.person import Person,PersonDefaultSettings

class TestPerson(unittest.TestCase):
    def test_init(self):
        p = Person(0,0,0)

        self.assertEqual(p.money, 0)
        self.assertEqual(p.strength, 0)
        self.assertEqual(p.weight, 0)


    def test_random_person_defaults(self):

        pds = PersonDefaultSettings

        for i in range(0,1000):
            p1 = Person.random(pds.WEIGHT_RANGE,pds.MONEY_RANGE,pds.STRENGTH_RANGE)
            self.assertTrue(pds.WEIGHT_RANGE[0]<=p1.weight<=pds.WEIGHT_RANGE[1])
            self.assertTrue(pds.MONEY_RANGE[0]<=p1.money<=pds.MONEY_RANGE[1])
            self.assertTrue(pds.STRENGTH_RANGE[0]<=p1.strength<=pds.STRENGTH_RANGE[1])

            
        

