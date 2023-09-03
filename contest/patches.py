def change_patch(origin_patch):
    start, end, letters = map(str, input().split())
    origin_patch = origin_patch[:int(start)-1] + letters + origin_patch[int(end):]
    return origin_patch


def main():
    origin_patch = input()
    for _ in range(int(input())):
        new_patch = change_patch(origin_patch)
        origin_patch = new_patch
    print(origin_patch)


if __name__ == '__main__':
    main()
