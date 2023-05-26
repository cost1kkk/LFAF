import unittest
from cnf import CNFConvertor
from Grammar import RegularGrammar


vn = ['S','A','B','C','D','X']
vt = ['a','b']
p = {
'S' : ['dB','A'],
'A' : ['d','dS', 'aAdAB'],
'B' : ['aC','aS','AC'],
'C' : [''],
'E' : ['AS']
}
a = vt

correct = {
    'S' : ['d', 'DB', 'DS', 'FG'],
    'A' : ['d', 'DS', 'FG'],
    'B' : ['a', 'd', 'HS', 'DS', 'FG'],
    'D' : ['d'],
    'F' : ['HA'],
    'G' : ['DI'],
    'H' : ['a'],
    'I' : ['AB']
}



# Define a class TestMethods that inherits from unittest.TestCase
class TestMethods(unittest.TestCase):
    
    
    # Define a method called setUp that initializes two instances of classes and assigns them to instance variables
   
    def setUp(self):
        # Assign an instance of CNFConvertor class to the instance variable cnf_grammar with two arguments p and vn
        self.cnf_grammar = CNFConvertor(p,vn)
        # Assign an instance of RegularGrammar class to the instance variable reg_grammar with four arguments vn, vt, p, and a
        self.reg_grammar = RegularGrammar(vn,vt,p,a)





#The four test methods each test a different method of the CNFConvertor class. 


    # Define a method called test_eps_rem that checks if a method called RemoveEpsilon returns the expected result
  
    def test_eps_rem(self):
        # Use the assertEqual method of the unittest.TestCase class to check if RemoveEpsilon() method of cnf_grammar instance returns correct output
        self.assertEqual(self.cnf_grammar.RemoveEpsilon(),correct,'The epsilon was not removed correctly')

    # Define a method called test_unit_rem that checks if a method called ConvertCNF returns the expected result
    
    def test_unit_rem(self):
        # Use the assertEqual method of the unittest.TestCase class to check if ConvertCNF() method of reg_grammar instance returns correct output
        self.assertEqual(self.reg_grammar.ConvertCNF(),correct,'The unit production removal was not correct')

    # Define a method called test_unpr_rem that checks if a method called RemoveUnproductive returns the expected result
   
    def test_unpr_rem(self):
        # Assign correct value to the p instance variable of cnf_grammar instance
        self.cnf_grammar.p = correct
        # Use the assertEqual method of the unittest.TestCase class to check if RemoveUnproductive() method of cnf_grammar instance returns correct output
        self.assertEqual(self.cnf_grammar.RemoveUnproductive(),correct,'The unprodoctive removal went wrong')

    # Define a method called test_cln that checks if a method called Cleanup returns the expected result
  
    def test_cln(self):
        # Assign correct value to the p instance variable of cnf_grammar instance
        self.cnf_grammar.p = correct
        # Use the assertEqual method of the unittest.TestCase class to check if Cleanup() method of cnf_grammar instance returns correct output
        self.assertEqual(self.cnf_grammar.Cleanup(),correct,'The cleanup went wrong!')



# If this script is being run as the main program, execute unittest.main() function to run the tests in TestMethods class
if __name__ == '__main__':
    unittest.main()