import csv

csv_file = open("img.csv", "r", encoding="UTF-8", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="", quotechar='"', skipinitialspace=True)
f = list(f)[0]
print(f)