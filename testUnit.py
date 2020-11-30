import unittest
class TestStudyPark(unittest.TestCase):
    def testLogIn(self):
        self.assertEqual(TestStudyPark.Login(self,22g2ff31), 22g2ff31 )
    def testName(self):
        self.assertEqual(TestStudyPark.ChangeName())
    def testPass(self):