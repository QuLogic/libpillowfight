#!/usr/bin/env python3
import unittest

from tests import tests_util
from tests import tests_ace

if __name__ == '__main__':
    unittest.main(tests_util, verbosity=2, exit=False)
    unittest.main(tests_ace, verbosity=2, exit=False)