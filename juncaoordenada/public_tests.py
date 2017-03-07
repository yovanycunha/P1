import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
juncao_ordenada = getattr(undertest, 'juncao_ordenada', None)

class PublicTests(unittest.TestCase):

   def test_1_base(self):
     l1 = [8, 12, 78, 79, 511]
     l2 = [7, 8, 121, 302]
     assert juncao_ordenada(l1, l2) == [7, 8,8,12,78,79,121,302,511]
     assert l1 == [8, 12, 78, 79, 511]
     assert l2 == [7, 8, 121, 302]
   

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
