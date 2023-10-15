def main():
    input_str = "193 125 133 134 135 136 -52 -51 -50 -49 -48 -47 -46 -45 66 67 68 69 70 71 -38 -37 -36 -35 -34 -33 -32 -31 -30 -29 -132 -131 -130 -193 -192 -191 -190 -189 -188 -187 -186 -185 -184 -183 -182 -181 -180 -179 -178 -177 -176 -175 -174 -173 -172 -171 -170 -169 -77 -76 -75 -74 -73 -72 18 19 20 21 22 23 24 25 26 27 28 -164 -163 -65 -64 -63 -62 -61 -60 -59 -58 -57 -56 -55 -54 -53 39 40 41 42 43 44 159 160 161 162 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 -168 -167 -166 -165 126 127 128 129 86 87 88 89 90 91 92 93 94 95 96 -124 -123 -122 -121 -120 -119 -118 -117 -116 -115 -114 -113 -112 -111 -110 -109 -108 -107 -106 -105 -104 -103 -102 -101 -100 -99 -98 -97 153 154 155 156 157 158 -148 -147 -146 -145 -144 -143 -142 -141 -140 -139 -138 -137 -85 -84 -83 -82 -81 -80 -79 -78 -152 -151 -150 -149"
    input_list_str = input_str.split(" ")
    input_list = []

    for str in input_list_str:
        input_list.append(int(str))

    current_list = input_list[1:]

    steps = 0

    print(current_list)
    while current_list != sorted(current_list):

        next_score = 0
        next_list = []

        for pair in compute_oriented_pairs(current_list):
            new_list = compute_inverse(current_list, pair)
            score = computer_score(new_list)
            if score > next_score:
                next_score=score
                next_list=new_list


        current_list = next_list
        steps+=1
        print(current_list)


    print(steps)


def compute_oriented_pairs(data):
    data = data[:]

    output = []

    for index1 in range(len(data)):
        element1 = data[index1]
        for index2 in range(index1 + 1, len(data)):
            element2 = data[index2]
            if (element1 < 0 <= element2) or \
                    (element1 >= 0 > element2):
                if abs(abs(element1) - abs(element2)) == 1:
                    output.append((element1, index1, element2, index2))

    output.sort(key=lambda x: x[0])

    return output

def computer_score(data):
    data = data[:]
    return len(compute_oriented_pairs(data))

def compute_inverse(data, pair):
    data = data[:]

    xi = pair[0]
    i = pair[1]
    xj = pair[2]
    j = pair[3]

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
