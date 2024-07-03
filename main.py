def shiftN(stringvalue, direction, N):
    # Shift left
    if direction == 0: 

    # Shift right
    if direction == 1:
    return stringvalue


def main():
    str = '001100'
    print(int(str, 2))
    rstr = shiftN(str, 0, 2)
    print(rstr)
    print(int(rstr, 2))

    rstr = '110000'
    rstr = shiftN(rstr, 1, 4)
    print(rstr)
    print(int(rstr, 2))


if __name__ == '__main__':
    main()
