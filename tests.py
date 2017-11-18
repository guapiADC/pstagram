import unittest
from pstagram import app;

class PstagramTest(unittest.TestCase):
    def setUp(self):
        print 'setup'

    def tearDown(self):
        print 'tearDown'

    def test1(self):
        print 'test1'


    def test2(self):
        print 'test2'