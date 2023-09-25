class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        roll_index = 0
        for frameIndex in range(10):
            if self.isStrike(roll_index):
                result += self.strikeScore(roll_index)
                roll_index += 1
            elif self.isSpare(roll_index):
                result += self.spareScore(roll_index)
                roll_index += 2
            else:
                result += self.frameScore(roll_index)
                roll_index += 2
        return result

    def isStrike(self, roll_index):
        return self.rolls[roll_index] == 10

    def isSpare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strikeScore(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spareScore(self, roll_index):

        return 10 + self.rolls[roll_index + 2]

    def frameScore(self, roll_index):

        return self.rolls[roll_index] + self.rolls[roll_index + 1]