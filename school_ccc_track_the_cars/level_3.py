def main():
    data: str = read_file("input-3/level3-3.in")
    #data: str = read_file("input-3/test.in")

    rectangle_str = data.split("\n")[0]

    north: float = float(rectangle_str.split(",")[0])
    east: float = float(rectangle_str.split(",")[1])
    south: float = float(rectangle_str.split(",")[2])
    west: float = float(rectangle_str.split(",")[3])

    n: int = int(data.split("\n")[1])

    observations: list = []

    for index in range(n):
        observation_str: str = data.split("\n")[index+2]

        identity: str = observation_str.split(",")[0]
        time: str = observation_str.split(",")[1]
        latitude: float = float(observation_str.split(",")[2])
        longitude: float = float(observation_str.split(",")[3])

        if south <= latitude <= north and west <= longitude <= east:
            if identity not in observations:
                observations.append(identity)

    observations.sort()

    for observation in observations:
        print(observation, end=",")

    return


def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
