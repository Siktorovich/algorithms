class Control:
    def __init__(self):
        self.start = 15
        self.tale = 30
        self.broken = False

    def increase(self, times):
        self.start += times
        self.prove()

    def decrease(self, times):
        self.tale -= times
        self.prove()

    def prove(self):
        if not self.broken:
            if self.start > self.tale:
                self.broken = True
                print(-1)
            else:
                print(self.tale)
        else:
            print(-1)


def main():
    control = Control()
    for _ in range(int(input())):
        temp_order, temp = map(str, input().split())
        if temp_order[:1] == '>':
            if int(temp) <= control.start <= control.tale and not control.broken:
                print(control.tale)
            else:
                control.increase(int(temp) - control.start)
        else:
            if int(temp) >= control.tale >= control.start and not control.broken:
                print(control.tale)
            else:
                control.decrease(control.tale - int(temp))


if __name__ == '__main__':
    for _ in range(int(input())):
        main()
        print()
