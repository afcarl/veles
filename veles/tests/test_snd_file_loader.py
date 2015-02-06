"""
Created on May 21, 2013

Copyright (c) 2013 Samsung Electronics Co., Ltd.
"""

import logging
import unittest

from veles.loader.libsndfile_loader import SndFileLoader


class Test(unittest.TestCase):

    def tearDown(self):
        pass

    def testSndFileLoader(self):
        loader = SndFileLoader()
        data = loader.decode_file(
            "/home/markhor/Development/speech_files/sawyer.flac")
        logging.info("%d samples at %d Hz" % (data["data"].size,
                                              data["sampling_rate"]))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    # import sys;sys.argv = ['', 'Test.testSndFileLoader']
    unittest.main()