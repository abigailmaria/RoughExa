# test_roughexa.py
"""
Tests for RoughExa module.
"""

import unittest
from roughexa import RoughExa

class TestRoughExa(unittest.TestCase):
    """Test cases for RoughExa class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughExa()
        self.assertIsInstance(instance, RoughExa)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughExa()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
