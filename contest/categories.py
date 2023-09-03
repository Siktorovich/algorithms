import json


class Category:
    def __init__(self):
        self.next = []
        self.name = ''

    def set_parent(self, parents):
        self.parent = parents


def main():
    quan_strings = int(input())
    input_json = [input() for i in range(quan_strings)]
    print(json.loads(input_json))

if __name__ == '__main__':
    for _ in range(int(input())):
        main()