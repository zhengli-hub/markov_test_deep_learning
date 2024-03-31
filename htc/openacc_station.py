from os import listdir
from os.path import isfile, join

openacc = "../data_0330/openacc_data/output_data/eigenvalue_test/0.1_500"
DG = 30
REP = 1


def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[: -len(suffix)]
    return input_string


filenames = [
    remove_suffix(f, ".npy") for f in listdir(openacc) if isfile(join(openacc, f))
]

filenames = sorted(filenames)

outputstr = ""

for rep in range(REP):
    for dg in range(DG):
        for name in filenames:
            outputstr += f"{name}, {dg}, {rep}\n"

with open("openacc_station_dg30_rep1.txt", "w") as outfile:
    outfile.write(outputstr)
