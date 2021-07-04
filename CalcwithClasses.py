class Calculator:
    def __init__(self, *args):
        self.numbers = args

    def sum(self) -> float:
        num = self.numbers
        sum: int = 0
        for a in num:
            try:
               sum = sum + a
            except Exception as e:
                print(e)

        return sum

    def diff(self) -> float:
        num = self.numbers
        diff: int = 0
        for a in num:
            diff = int(a) - diff
        return diff

    def multiply(self) -> float:
        num = self.numbers
        mul: int = 1
        for a in num:
            try:
                mul = mul * int(a)
            except Exception as e:
                print(e)
        return mul

