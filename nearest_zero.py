# 86116429

def nearest_zero_func():
    street_len = int(input())
    street = [int(x) for x in input().split()]

    len_between_zero = 0
    not_zero = 1

    for i in range(street_len):
        if street[i] == 0:
            if not_zero:
                for j in range(1, len_between_zero + 1):
                    street[i-j] = j
                not_zero = 0
            else:
                for j in range(1, (len_between_zero // 2) + 1):
                    street[i-j] = j
            len_between_zero = 0
        else:
            len_between_zero += 1
            street[i] = len_between_zero
    return street


if __name__ == '__main__':
    print(*nearest_zero_func())
