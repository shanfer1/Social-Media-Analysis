import csv
import json

def convertToJSON(csvfile,jsonfile):
	res = {}
	with open(csvfile, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for rows in csvReader:
			res[rows['username']] = rows
	with open(jsonfile, 'w', encoding='utf-8') as jsonf:
		jsonf.write(json.dumps(res, indent=4))

