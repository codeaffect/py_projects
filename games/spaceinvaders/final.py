import csv

infile = "employees.csv"
outfile = "final.csv"

finalfile = []

w = open(outfile, "w+")
w.close()

with open(infile) as inputfile:
    line_row = csv.reader(inputfile, delimiter=",")
    result = ""

    for row in line_row:
        # print(row[0])
        names = row[0].split()
        if len(names) > 1:
            # print(names[0], "-", names[1])
            row[0] = ",".join({names[0], names[1]})
        result = ",".join(row)
        # print(result)
        finalfile.append(result)

print(*finalfile)
print("-----")

w = open(outfile, "a+")
for row in finalfile:
    print(row)
    w.write("%s\n" % row)
