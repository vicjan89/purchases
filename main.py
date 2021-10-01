import csv

FILENAME = r"C:\Users\rzi1\AppData\Roaming\JetBrains\PyCharmCE2021.2\scratches\ТМЦ.csv"
s=[]
with open(FILENAME, "r", newline="", encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        s.append(row)
print(s)
