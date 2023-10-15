def main():
    data: str = read_file("input-5/level5-4.in")
    data_split = data.split("\n")

    polygon_1_coords_n: int = int(data_split[0])

    polygon_1_points = []

    for index in range(polygon_1_coords_n):
        point_str: str = data_split[index + 1]

        latitude: float = float(point_str.split(",")[0])
        longitude: float = float(point_str.split(",")[1])

        polygon_1_points.append((latitude, longitude))

    polygon_2_coords_n: int = int(data_split[polygon_1_coords_n + 1])

    polygon_2_points = []

    for index in range(polygon_2_coords_n):
        point_str: str = data_split[polygon_1_coords_n + index + 2]

        latitude: float = float(point_str.split(",")[0])
        longitude: float = float(point_str.split(",")[1])

        polygon_2_points.append((latitude, longitude))

    m: int = int(data_split[polygon_1_coords_n + polygon_2_coords_n + 2])

    observations = []

    for index in range(m):
        position_str: str = data_split[polygon_1_coords_n + polygon_2_coords_n + 3 + index]
        identifier: str = position_str.split(",")[0]
        time: str = position_str.split(",")[1]
        latitude: float = float(position_str.split(",")[2])
        longitude: float = float(position_str.split(",")[3])

        observations.append((identifier, time, latitude, longitude))

    observations.sort(key=lambda x: x[1])

    p1_check = []
    success = []

    for observation in observations:
        identifier, time, latitude, longitude = observation

        # Check if time is in between the 9:30 and 10:45
        if "09:30:00" < time < "10:45:00":
            if identifier in success:
                continue

            if identifier not in p1_check:
                if check_if_in_polygon(polygon_1_points, latitude, longitude):
                    p1_check.append(identifier)

            if check_if_in_polygon(polygon_2_points, latitude, longitude):
                if identifier in p1_check:
                    success.append(identifier)

    success.sort()

    for identifier in success:
        print(identifier, end=",")


def check_if_in_polygon(polygon_points, latitude, longitude):
    inside: bool = False
    for i in range(len(polygon_points)):
        j = i - 1
        if (polygon_points[i][1] > longitude) != (polygon_points[j][1] > longitude):
            if latitude < (polygon_points[j][0] - polygon_points[i][0]) * (longitude - polygon_points[i][1]) / (
                    polygon_points[j][1] - polygon_points[i][1]) + polygon_points[i][0]:
                inside = not inside

    return inside


def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
