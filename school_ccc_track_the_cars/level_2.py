def main():
    data: str = read_file("input-2/level2-4.in")
    #data: str = read_file("input-2/test.in")


    n: int = int(data.split("\n")[0])

    max_latitude: float = 0
    max_latitude_index: int = 0

    max_longitude: float = 0
    max_longitude_index: int = 0

    observations: list = []

    for index in range(n):
        observation_str: str = data.split("\n")[index+1]

        identity: str = observation_str.split(",")[0]
        time: str = observation_str.split(",")[1]
        latitude: float = float(observation_str.split(",")[2])
        longitude: float = float(observation_str.split(",")[3])

        observations.append((identity, time, latitude, longitude))

        if latitude > max_latitude:
            max_latitude = latitude
            max_latitude_index = index

        if longitude > max_longitude:
            max_longitude = longitude
            max_longitude_index = index

    print(observations[max_latitude_index][0], end=",")
    print(observations[max_latitude_index][1], end=",")
    print(observations[max_longitude_index][0], end=",")
    print(observations[max_longitude_index][1], end="")

    return


def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
