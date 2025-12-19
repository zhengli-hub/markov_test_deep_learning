from os import listdir
from os.path import isfile, join

catsacc = "data_0507/catsacc_data/no_test_120s/"

DG = 20
REP_START = 0
REP_STOP = 1


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[: -len(suffix)]
    return input_string


filenames = [f for f in listdir(catsacc) if isfile(join(catsacc, f))]

filenames = sorted(filenames)

outputstr = ""

for rep in range(REP_START, REP_STOP):
    for dg in range(DG):
        for name in filenames:
            outputstr += f"{name}, {dg}, {rep}\n"

with open(f"htc/catsacc_0512_dg20.txt", "w") as outfile:
    outfile.write(outputstr)
