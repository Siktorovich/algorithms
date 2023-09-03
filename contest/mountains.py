def input_pictures(arr, height, wide, last):
    point_string = ''.join(['.' for _ in range(wide)])
    if not arr:
        for _ in range(height):
            mountain_string = input()
            arr.append(mountain_string)
            if last:
                print(mountain_string)
        return arr
    for _ in range(height):
        new_string = input()
        old_string = arr[_]
        if new_string == old_string:
            arr[_] = old_string
            if last:
                print(old_string)
            continue
        elif old_string == point_string:
            arr[_] = new_string
            if last:
                print(new_string)
            continue
        result_string = ''
        comparisons = list(zip(old_string, new_string))
        for i in range(len(comparisons)):
            if comparisons[i][0] == comparisons[i][1]:
                result_string += comparisons[i][0]
            else:
                if comparisons[i][0] == '.':
                    result_string += comparisons[i][1]
                elif comparisons[i][1] == '.':
                    result_string += comparisons[i][0]
                elif comparisons[i][0] != '.':
                    result_string += comparisons[i][0]
        arr[_] = result_string
        if last:
            print(result_string)
    return arr


def display_mountains(main_last):
    quantity_pict, height, wide = map(int, input().split())
    result = []
    for i in range(quantity_pict):
        last = (i == quantity_pict - 1)
        result = input_pictures(result, height, wide, last)
        if not last:
            input()
        elif not main_last:
            print()


if __name__ == '__main__':
    times = int(input())
    for _ in range(times):
        main_last = (_ == times - 1)
        display_mountains(main_last)
