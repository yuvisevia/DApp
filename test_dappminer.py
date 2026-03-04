# test_dappminer.py
"""
Tests for DAppMiner module.
"""

import unittest
from dappminer import DAppMiner

class TestDAppMiner(unittest.TestCase):
    """Test cases for DAppMiner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DAppMiner()
        self.assertIsInstance(instance, DAppMiner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DAppMiner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
