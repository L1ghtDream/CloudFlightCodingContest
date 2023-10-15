def main():
    data = "sq Length=531441 Iterations=9"
    length = int(data.split(" ")[1].split("=")[1])
    iterations = int(data.split(" ")[2].split("=")[1])

    print(f"{length} * 4", end="")
    output = length * 4
    length /= 3
    edges = 4

    for i in range(iterations):
        print(f" + ({length} * {edges} * 2)", end="")
        output += length * edges * 2
        length /= 3
        edges *= 5

    print()
    print(output)


if __name__ == '__main__':
    main()
