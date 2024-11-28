class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self



md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)

y = md.add(15,7,4).subtract(1,4,9).result
print(y)  



