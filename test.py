print("Hy!")


def count_to_ten(fromz):
    from_orig = fromz
    for i in range(from_orig):
        fromz += 1
        print(f"{fromz - 1} added with 1 is {fromz}")
    return


if __name__ == '__main__':
    count_to_ten(10)
