def main():
    input_str = "6 3 1 6 5 -2 4"
    input_list_str = input_str.split(" ")
    input_list = []

    for str in input_list_str:
        input_list.append(int(str))

    input_list = input_list[1:]

    new_list = compute_oriented_pairs(input_list)

    print(new_list)

    print(len(new_list), end=" ")
    for pair in new_list:
        print(pair[0], end=" ")
        print(pair[1], end=" ")


def compute_oriented_pairs(list):
    output = []

    for index1 in range(len(list)):
        element1 = list[index1]
        for index2 in range(index1 + 1, len(list)):
            element2 = list[index2]
            if (element1 < 0 <= element2) or \
                (element1 >= 0 > element2):
                if abs(abs(element1) - abs(element2)) == 1:
                    output.append((element1, element2))

    output.sort(key=lambda x: x[0])

    return output


if __name__ == '__main__':
    main()
