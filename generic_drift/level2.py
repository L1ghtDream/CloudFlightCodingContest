def main():
    input_str = ""
    input_list_str = input_str.split(" ")
    input_list = []

    for str in input_list_str:
        input_list.append(int(str))

    input_list = input_list[1:]
    xi = input_list[-4]
    i = input_list[-3]
    xj = input_list[-2]
    j = input_list[-1]

    new_list = compute_inverse(input_list[0:-4], xi, i, xj, j)

    for element in new_list:
        print(element, end=" ")


def compute_inverse(data, xi, i, xj, j):
    if xi + xj == 1:
        to_invert = []
        for index in range(i, j):
            to_invert.append(data[index])

        inverted = list(reversed(to_invert))

        for index in range(i, j):
            data[index] = inverted[index - i] * -1

        return data

    if xi + xj == -1:
        to_invert = []
        for index in range(i+1, j+1):
            to_invert.append(data[index])

        inverted = list(reversed(to_invert))

        for index in range(i+1, j+1):
            data[index] = inverted[index - i -1] * -1

        return data

    return []

if __name__ == '__main__':
    main()
