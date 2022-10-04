import csv

csv_file = open("img.csv", "r", encoding="UTF-8", errors="", newline="" )
#リスト形式
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="", quotechar='"', skipinitialspace=True)
f = list(f)[0]

print("file_num : ",len(f))

csv_file.close()

import requests

p = open('save_path.txt', 'w')

for i,url in enumerate(f):
    print("count :",i + 1)
    print("downloadning :",url)

    url_name = url.replace('https://www.asahi-net.or.jp/~yq3t-hruc/img/', '')
    file_name = "countries_img/" + url_name
    file_name_path = file_name + "\n"
    
    p.write(file_name_path)

    """
    response = requests.get(url)
    image = response.content

    with open(file_name, "wb") as hoge:
        hoge.write(image)
    """
p.close()