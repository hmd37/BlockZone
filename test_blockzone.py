# test_blockzone.py
"""
Tests for BlockZone module.
"""

import unittest
from blockzone import BlockZone

class TestBlockZone(unittest.TestCase):
    """Test cases for BlockZone class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockZone()
        self.assertIsInstance(instance, BlockZone)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockZone()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
