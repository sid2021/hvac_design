import os
import csv

basedir = os.path.abspath(os.path.dirname(__file__))

pipe_dict = []

with open(os.path.join(basedir, "pipes.csv"), encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=";")
    for row in csv_reader:
        pipe_dict.append(row)

# print(type(pipe_dict))
# print(pipe_dict)

diameters = []

for pipe in pipe_dict:
    if pipe["type"] == "carbon_steel":
        diameters.append(pipe["di"])

print(diameters)
print(diameters[0]["k"])
