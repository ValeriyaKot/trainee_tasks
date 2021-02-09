import json
import csv

# my_table = [["first_name", "second_name", "Grade"],
#           ['Alex', 'Brian', 'A'],
#           ['Tom', 'Smith', 'B']]
#
# my_file = open('test.csv', 'w')
# with my_file:
#     writer = csv.writer(my_file)
#     writer.writerows(my_table)

res = []
with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        res.append(row)
    print(res)

with open('test.json', 'w') as f:
    json.dump(res, f)


