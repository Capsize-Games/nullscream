import unittest

from nullscream import install_nullscream, uninstall_nullscream


class TestWhitelist(unittest.TestCase):
    def test_whitelist_noop(self):
        install_nullscream(whitelist=["math"], blacklist=["requests"])
        import requests
        self.assertTrue(requests.__doc__ == "This is a noop stand-in module.")
        self.assertTrue(hasattr(requests, "path"))

        import math
        self.assertFalse(math.__doc__ == "This is a noop stand-in module.")
        self.assertTrue(hasattr(math, "sin"))
        self.assertFalse(hasattr(math, "asdf"))

    def tearDown(self):
        uninstall_nullscream(blacklist=["requests"])


if __name__ == "__main__":
    unittest.main()
