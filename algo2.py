class Mystery:
    def mystery(self, n):
        count = 0
        if n % 2 == 0:
            for i in range(1, n, 1):
                for j in range(int(n/2), n, 1):
                    count += 1
        else:
            for k in range(int(n/4)):
                for m in range(n):
                    count += 1
        print("the count is {}".format(count))

a = Mystery()
a.mystery(10)
a.mystery(20)
a.mystery(30)
a.mystery(40)
a.mystery(50)
a.mystery(11)
a.mystery(21)
a.mystery(31)
a.mystery(41)
a.mystery(51000000001)
a.mystery(51000000000)

