import unittest

from nullscream import install_nullscream, uninstall_nullscream


class TestBlacklist(unittest.TestCase):
    def test_blacklist_noop(self):
        install_nullscream(blacklist=["math"])
        import math
        self.assertTrue(math.__doc__ == "This is a noop stand-in module.")
        self.assertTrue(hasattr(math, "sin"))
        self.assertTrue(hasattr(math, "adsf"))

    def tearDown(self):
        uninstall_nullscream(blacklist=["math"])


if __name__ == "__main__":
    unittest.main()
