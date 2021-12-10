#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import grades
import math

class Grade_Test(unittest.TestCase):
    def test_total_returns_total_of_list(self):
        result = grades.total([1,10,22])
        self.assertEqual(result,33,"The total function should return 33")
    
    def test_total_returns_0(self):
        result = grades.total([])
        self.assertEqual(result,0,"The total function should return 0")
    
    def test_average_one(self):
        result = grades.average([2,5,9])
        self.assertAlmostEqual(result,5.33333,5)
    
    def test_average_two(self):
        result = grades.average([2,15,22,9])
        self.assertAlmostEqual(result,12.0000,4)
        
    def test_average_returns_nan(self):
        result = grades.average([])
        self.assertIs(result,math.nan)
        
    def test_median_returns_two(self):
        result = grades.median([2,5,1])
        self.assertEqual(result,2,"The median function should return 2")


    def test_median_returns_two_point_five(self):
        result = grades.median([5,2,1,3])
        self.assertEqual(result,2.5,"The median function should return 2.5")
    
    def test_median_0(self):
        with self.assertRaises(ValueError):
            result = grades.median([])
        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)        


# In[ ]:





# In[ ]:




