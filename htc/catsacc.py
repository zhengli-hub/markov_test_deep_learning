from os import listdir
from os.path import isfile, join

catsacc = "data/catsacc/stationary"
DG = 10
REP = 1


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[: -len(suffix)]
    return input_string


filenames = [
    remove_suffix(f, ".csv") for f in listdir(catsacc) if isfile(join(catsacc, f))
]

outputstr = ""

for rep in range(REP):
    for dg in range(DG):
        for name in filenames:
            outputstr += f"{name}, {dg}, {rep}\n"

with open("catsacc_dg10_rep1.txt", "w") as outfile:
    outfile.write(outputstr)
