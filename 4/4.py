import csv
import json

with open("./items.json", "r") as json_file:
    data = json_file.read()

json_data = json.loads(data)
csv_table_list = [["item", "country", "year", "sales"]]

for json_item in json_data:
    item = json_item['item']
    for country in json_item['sales_by_country']:
        for year in json_item['sales_by_country'][country]:
            sales = json_item['sales_by_country'][country][year]
            csv_table_list.append([item, country, year, sales])

with open("./items.csv", "w") as file:
    csv_writer = csv.writer(file)
    for row in csv_table_list:
        csv_writer.writerow(row)