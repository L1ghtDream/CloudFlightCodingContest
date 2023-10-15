def main():
    data: str = read_file("input-1/level1-4.in")

    rectangle_str = data.split("\n")[0]

    north: float = float(rectangle_str.split(",")[0])
    east: float = float(rectangle_str.split(",")[1])
    south: float = float(rectangle_str.split(",")[2])
    west: float = float(rectangle_str.split(",")[3])

    m: int = int(data.split("\n")[1])

    count: int = 0

    for index in range(m):
        position_str: str = data.split("\n")[index+2]
        latitude: float = float(position_str.split(",")[0])
        longitude: float = float(position_str.split(",")[1])

        if south <= latitude <= north and west <= longitude <= east:
            count += 1

    print(count, end=" ")

    return


def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
