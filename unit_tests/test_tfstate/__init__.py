# -*- coding: utf-8 -*-

# Python stdlib
import unittest

# Unit tests
from unit_tests.test_tfstate import test_base, test_provider


def suite():
    suite = unittest.TestSuite()
    suite.addTests(test_base.suite())
    suite.addTests(test_provider.suite())
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
