import testfx1


class Aex:
    def __init__(self, num):
        self.otnum = num
        self.otnum2 = testfx1.sum_nums(3 , 2)

    def outval(self):
        return self.otnum + self.otnum2

'''
a = Aex(3)
print(a.outval())
'''