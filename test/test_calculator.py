import unittest
from code.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(34,23)

    def test_add(self):
        self.assertEqual(self.cal.add(),57,'add method is not workinng properly')
        self.assertNotEqual(self.cal.add(),54,'add method is not workinng properly')

    def test_sub(self):
        self.assertEqual(self.cal.sub(),11,'sub method is not working')
        self.assertNotEqual(self.cal.sub(),13,'sub method is not working')

    def test_mul(self):
        self.assertEqual(self.cal.mul(),782,'mul method is not working')
        self.assertNotEqual(self.cal.mul(),783,'mul method is not working')

    def test_div(self):
        self.assertEqual(self.cal.div(),1,'sub method is not working')
        self.assertNotEqual(self.cal.div(),2,'sub method is not working')

if __name__=='__main__':
    unittest.main()