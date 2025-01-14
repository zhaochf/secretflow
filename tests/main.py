#!/usr/bin/env python3
# *_* coding: utf-8 *_*

""" Main test function """
import unittest

import xmlrunner
from absl import app


def main(argv):
    del argv
    suite = unittest.TestSuite()
    # Find all test files start with 'test'
    all_cases = unittest.defaultTestLoader.discover('./tests', 'test_*.py')
    for case in all_cases:
        # add all tests into suite
        suite.addTests(case)
    with open('./results.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output, failfast=True)
        runner.run(suite)


if __name__ == '__main__':
    app.run(main)
