def main():
    friends = input().split()
    what_they_have = input().split()
    deck = list(range(2, int(friends[1]) + 1))
    given = []
    if int(friends[0]) < int(friends[1]):
        for item in what_they_have:
            new_item = int(item)
            if new_item > int(friends[1]):
                print('-1')
                return
            if deck[-1] <= new_item:
                print('-1')
                return
            for index, card in enumerate(deck):
                if card > new_item:
                    given.append(card)
                    deck.pop(index)
                    break
        print(*given)
    else:
        print('-1')


if __name__ == '__main__':
    main()
