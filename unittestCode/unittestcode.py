import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart',80,18)
        s2 = Student('Lisa',100,18)
        self.assertEqual(s1.get_gtade(),'A')
        self.assertEqual(s2.get_gtade(),'A')
    def test_60_to_80(self):
        s1 = Student('Bart',60,18)
        s2 = Student('Lisa',70,18)
        self.assertEqual(s1.get_gtade(),'B')
        self.assertEqual(s2.get_gtade(),'B')
    def test_0_to_60(self):
        s1 = Student('Bart', 10, 18)
        s2 = Student('Lisa', 40, 18)
        self.assertEqual(s1.get_gtade(), 'C')
        self.assertEqual(s2.get_gtade(), 'C')
    def test_invais(self):
        s1 = Student('Bart', -1, 18)
        s2 = Student('Lisa', 101, 18)
        with self.assertRaises(ValueError):
            s1.get_gtade()
        with self.assertRaises(ValueError):
            s2.get_gtade()
    def test_age_0_to_18(self):
        s1 = Student('Bart', 90, 17)
        s2 = Student('Lisa', 90, 10)
        self.assertEqual(s1.get_age(), '未成年')
        self.assertEqual(s2.get_age(), '未成年')
    def test_age_18_to_25(self):
        s1 = Student('Bart', 90, 20)
        s2 = Student('Lisa', 90, 22)
        self.assertEqual(s1.get_age(), '中学生')
        self.assertEqual(s2.get_age(), '中学生')

    def test_age_25_to_100(self):
        s1 = Student('Bart', 90, 30)
        s2 = Student('Lisa', 90, 26)
        self.assertEqual(s1.get_age(), '社会人')
        self.assertEqual(s2.get_age(), '社会人')
    def test_age_invaos(self):
        s1 = Student('Bart', 90, -1)
        s2 = Student('Lisa', 90, 101)
        with self.assertRaises(ValueError):
            s1.get_age()
        with self.assertRaises(ValueError):
            s2.get_age()
if __name__ == '__main__':
    unittest.main()