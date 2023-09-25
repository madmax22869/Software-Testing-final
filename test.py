import unittest
import BowlingGame


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """Set up BowlingGame for testing"""
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """Test 'all zeros' score for BowlingGame.py"""
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def testAllOnes(self):
        """Test 'all ones' score for BowlingGame.py"""
        self.rollMany(1, 20)
        self.assertEqual(20, self.game.score())

    def testOneSpare(self):
        """Test 'one spare' score for BowlingGame.py"""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def testOneStrike(self):
        """Test 'one strike, one frame < 10 and rest of zeros' score for BowlingGame.py"""
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def testPerfectGame(self):
        """Test 'all strikes' score for BowlingGame.py"""
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def testManySpare(self):
        """Test 'all spares' score for BowlingGame.py"""
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    def rollMany(self, pins, rolls):
        """Append some number(pins) to rolls[] list from BowlingGame.py number of times (rolls)"""
        for i in range(rolls):
            self.game.roll(pins)
					

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.