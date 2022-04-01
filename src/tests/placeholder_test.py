# Automaattista testausta varten. Voi poistaa heti kun oikeita yksikkötestejä.
import unittest

class Test(unittest.TestCase):
    def test_placholder(self):
        self.assertEqual(True, True)
