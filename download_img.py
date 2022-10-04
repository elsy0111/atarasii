import requests

url = "https://www.asahi-net.or.jp/~yq3t-hruc/img/IE.gif"
file_name = "countries_img/IE.gif"

response = requests.get(url)
image = response.content

with open(file_name, "wb") as aaa:
    aaa.write(image)