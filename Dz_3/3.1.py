
with open("test_file.txt", "r") as f_r:
    data = f_r.readlines()
    for i in data:
        for j in i.split():
            f_r.write()

            #
            # if j.lower() == "one":
            #     data[data.index(i)] = "один"
            # elif j.lower() == "two":
            #     data[data.index(i)] = "два"
            # elif j.lower() == "three":
            #     data[data.index(i)] = "три"
            # elif j.lower() == "four":
            #     data[data.index(i)] = "чотири"


