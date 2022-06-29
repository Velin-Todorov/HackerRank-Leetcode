def kangaroo(x1, v1, x2, v2):
    same_position = False

    while True:
        if x1 > x2:
            if v1 >= v2:
                return 'NO'

        if x2 > x1:
            if v2 >= v1:
                return 'NO'

        x1 += v1
        x2 += v2
        if x1 == x2:
            same_position = True
            break

    return 'YES'


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)