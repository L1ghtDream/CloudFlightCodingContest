def main():
    data = "sq Length=9 Iterations=2"
    length = int(data.split(" ")[1].split("=")[1])
    iterations = int(data.split(" ")[2].split("=")[1])

    print(f"{length} * 3", end="")
    output = length * 3
    length /= 3
    edges = 3

    for i in range(iterations):
        print(f" + ({length} * {edges})", end="")
        output += length * edges
        length /= 3
        edges *= 4

    print()
    print(output)


if __name__ == '__main__':
    main()
