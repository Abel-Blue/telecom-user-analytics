
import pandas as pd
import numpy as np
import unittest
import os
import sys

sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))

from data_preProcessing import data_preProcessing_script

df = pd.DataFrame({'numbers': [2, 4, 6, 7, 9], 'letters': ['a', 'b', 'c', 'd', 'e'],
                   'floats': [0.2323, -0.23123, np.NaN, np.NaN, 4.3434]})


class TestCases(unittest.TestCase):
    def test_class_creation(self):
        data_preProcessing = data_preProcessing_script(df)
        self.assertEqual(df.info(), data_preProcessing.df.info())


if __name__ == '__main__':
    unittest.main()
