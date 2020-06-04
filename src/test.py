



import unittest

from src.example import foo


class TestMultimethod(unittest.TestCase):

    #1.Run different functions for different types
    def test_type(self):

         self.assertEqual(foo(1,1),2)
         self.assertEqual(foo(1.0, 1.0), 0.0)
         self.assertEqual(foo('he', 'llo'), 'hello')
         self.assertEqual(foo('1', 10), '110')

    # 2.Optional and named parameters
    def test_optional(self):

        self.assertEqual(foo('1'), '110')
        self.assertEqual(foo('1',9), '19')

        self.assertEqual(foo(1.0,9,10), 20)
        self.assertEqual(foo(1.0), 21.0)
        self.assertEqual(foo(1.0,9),20)

    def test_named_object(self):
        self.assertEqual(foo(),3)



if __name__ == '__main__':
    unittest.main()
