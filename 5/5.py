import csv
import xml.etree.ElementTree as ET
import requests

rounding = 2

data_table = [["date", "usd", 'eur', "inr", 'uah']]
xml_roots = []

currencies = {"usd": "R01235", "eur": "R01239", "inr": "R01270", "uah": "R01720"}
for currency in currencies:
    currency_request = requests.get(
        'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/03/2020&date_req2=01/07/2020&VAL_NM_RQ={}'.format(
            currencies[currency]))
    xml_roots.append(ET.fromstring(currency_request.text))

for i in range(len(xml_roots[0])):
    row = [xml_roots[0][i].attrib['Date']]
    for root in xml_roots:
        value = float(root[i][1].text.replace(',', '.'))
        nominal = int(root[i][0].text)
        result_value = int((value/nominal)*10**rounding)/10**rounding
        row.append(result_value)
    data_table.append(row)

with open("./result.csv", 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_table)
