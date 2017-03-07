import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filtra_urls = getattr(undertest, 'filtra_urls', None)

class AcceptanceTests(unittest.TestCase):

    def test_exemplo(self):
        p1 = ['www.uol.com','www.google.com','http://mail.google.com']
        assert filtra_urls(p1) == ['www.google.com','http://mail.google.com']

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
