def catAndMouse(x, y, z):
    catA = x
    catB = y
    mouseC = z

    difference_C_A = abs(mouseC - catA)
    difference_C_B = abs(mouseC - catB)

    if difference_C_A > difference_C_B:
        return 'Cat B'

    elif difference_C_A < difference_C_B:
        return 'Cat A'

    return 'Mouse C'


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()
        x = int(xyz[0])
        y = int(xyz[1])
        z = int(xyz[2])

        print(catAndMouse(x, y, z))