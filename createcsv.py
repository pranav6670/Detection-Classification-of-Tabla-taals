import os, csv

f = open('test.csv', 'r+')
w = csv.writer(f)
for path, dirs, files in os.walk('wavfiles'):
    for filename in files:
        w.writerow([filename])
