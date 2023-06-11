# 86116480

def sleight_hand():
    fingers_by_one = int(input())
    arr = []

    for i in range(4):
        row = list(input())
        arr.append(row)

    dict_numbers = {}
    for row in arr:
        for item in row:
            if item != '.':
                dict_numbers[item] = int(dict_numbers.setdefault(item, 0)) + 1

    result = 0

    for key, value in dict_numbers.items():
        if fingers_by_one * 2 >= value:
            result += 1
    return result


if __name__ == '__main__':
    print(sleight_hand())
