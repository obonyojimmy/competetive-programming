import unittest
from timesheet import sum_timesheet

class TestTimeSheetSum(unittest.TestCase):
    def test_november_timesheet(self):
        self.assertEquals(
            79, sum_timesheet("samples/november.txt"),
            "samples/november.txt"
        )
        
    def test_december_timesheet(self):
        self.assertEquals(
            68, sum_timesheet("samples/december.txt"), 
            "samples/december.txt"
        )
        
    def test_january_timesheet(self):
        self.assertEquals(
             82.5, sum_timesheet("samples/jan.txt"),
            "samples/jan.txt"
        )
        
    def test_february_timesheet(self):
        self.assertEquals(
            73.5, sum_timesheet("samples/feb.txt"),
            "samples/feb.txt"
        )
        
    def test_march_timesheet(self):
        self.assertEquals(
            80, sum_timesheet("samples/march.txt"),
            "samples/march.txt"
        )
        
    def test_april_timesheet(self):
        self.assertEquals(
            34.25, sum_timesheet("samples/april.txt"), 
            "samples/april.txt"
        )