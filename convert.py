import csv
import json

city_prons = {}
cities = []

# 市役所の名前であるかどうかを判断
def is_city_hall(facility_name):
    keywords = ["役場", "市役所"]
    for keyword in keywords:
        if facility_name.endswith(keyword) and facility_name != keyword:
            return True
    return False

# 市町村の発音はこのCSVから
# 道内179市町村 https://www.pref.hokkaido.lg.jp/link/shichoson
with open("shichoson.csv", "r", encoding="cp932") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        city_prons[row[0]] = row[1]

# lat, longはこのCSVから
# 北海道施設位置情報データベース【北海道】https://www.harp.lg.jp/opendata/dataset/227.html
with open("Hokkaido_OD_GeoDataBase2018.csv", "r", encoding="cp932") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        [facility_name, city_name, lat, long, _, _, _, _, _, _] = row
        if is_city_hall(facility_name):
            pron = city_prons[city_name]
            cities.append({"facility_name": facility_name, "city_name": city_name, "pron": pron, "lat": lat, "long": long})

# jsonとして吐き出す
with open("city_data.json", "w") as write_file:
    json.dump(cities, write_file)
