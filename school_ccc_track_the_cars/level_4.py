def main():
    data: str = read_file("input-4/level4-4.in")
    #data: str = read_file("input-4/test.in")

    n: int = int(data.split("\n")[0])

    points = []

    for index in range(n):
        point_str: str = data.split("\n")[index+1]

        latitude: float = float(point_str.split(",")[0])
        longitude: float = float(point_str.split(",")[1])

        points.append((latitude, longitude))

    m: int = int(data.split("\n")[n+1])

    count:int =0

    for index in range(m):
        position_str: str = data.split("\n")[index+n+2]
        latitude: float = float(position_str.split(",")[0])
        longitude: float = float(position_str.split(",")[1])

        # check if the point is inside the polygon
        inside: bool = False
        for i in range(len(points)):
            j = i - 1
            if (points[i][1] > longitude) != (points[j][1] > longitude):
                if latitude < (points[j][0] - points[i][0]) * (longitude - points[i][1]) / (points[j][1] - points[i][1]) + points[i][0]:
                    inside = not inside

        if inside:
            count+=1

    print(count, end=" ")


def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
