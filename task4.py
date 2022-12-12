import csv

with open('data/in.csv', 'r') as rf:
    res, err = 0, 0
    r_object = csv.reader(rf, delimiter=',')
    for row in r_object:
        try:
            res += float(row[int(row[0])])
        except:
            err += 1

print(res, err, sep=',')

