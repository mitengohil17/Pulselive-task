class Swapper:
    def __init__(self):
        self.rules = {3: "Pulse", 5: "Live", 7: "Sony", 11: "Sport"}

    def swapOne(self, num):
        result = ""
        for divisor, text in self.rules.items():
            if num % divisor == 0:
                result += text
        return result if result else str(num)

    def swapSome(self, nums):
        result = ""
        for num in nums:
            result += self.swapOne(num) + " "
        return result.strip()

    def swapRange(self, from_num, to_num):
        result = ""
        for num in range(from_num, to_num+1):
            result += self.swapOne(num) + " "
        return result.strip()
