import csv
import json

csv_file_path = 'data.csv'
json_file_path = 'data.json'

# Read CSV data into a list of dictionaries
csv_data = []
with open(csv_file_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        csv_data.append(row)

# Write JSON data to file
with open(json_file_path, 'w') as json_file:
    json.dump(csv_data, json_file, indent=4)
