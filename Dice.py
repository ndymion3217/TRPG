import random as rd

class Dice:
    def __init__(self, dice, max):
        self.setDice(dice)
        self.setMax(max)
        self.rollResult = self.rollDice(self.getDice(), self.getMax())

    def setDice(self, num):
        self.dice = num

    def setMax(self, num):
        self.max = num

    def getDice(self):
        return self.dice

    def getMax(self):
        return self.max

    def rollDice(self, dice, max):
        result = []
        for case in range(dice):
            result.append(rd.randint(1, max))
        return result

    def getResult(self):
        result = 0
        for num in self.rollResult:
            result += num
        return result

class NumData:
    def __init__(self, data):
        self.setData(data)

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

a = Dice(2, 3)
print(a.getResult())