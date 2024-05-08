import os

openacc = "data_0507/lyft_data/1s_npy"
DG = 20
REP = 1

filenames = os.listdir(openacc)

outputstr = ""

for rep in range(REP):
    for dg in range(DG):
        for name in filenames:
            outputstr += f"{name}, {dg}, {rep}\n"

with open("lyft_0507_dg20.txt", "w") as outfile:
    outfile.write(outputstr)
