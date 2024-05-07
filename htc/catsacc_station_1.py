from os import listdir
from os.path import isfile, join

catsacc = "../data_0330/catsacc_data/output_data/no_test/1"

DG = 20
REP_START = 0
REP_STOP = 20


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[: -len(suffix)]
    return input_string


filenames = [
    remove_suffix(f, ".npy") for f in listdir(catsacc) if isfile(join(catsacc, f))
]

filenames = sorted(filenames)

outputstr = ""

for rep in range(REP_START, REP_STOP):
    for dg in range(DG):
        for name in filenames:
            outputstr += f"{name}, {dg}, {rep}\n"

with open(f"catsacc_station_d1_dg{DG}_rep{REP_START}-{REP_STOP}.txt", "w") as outfile:
    outfile.write(outputstr)
