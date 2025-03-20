import csv

input_file = "security_incidents.csv"
output_file = "security_incidents_modified.csv"

data = []

with open(input_file, mode="r", newline='') as file:
    reader = csv.reader(file)
    headers = next(reader)
    headers.append("Status")
    data.append(headers)

    for row in reader:
        row.append("pending")
        data.append(row)

with open(output_file, mode = "w", newline = '') as file:
       writer = csv.writer(file)
       writer.writerows(data)
       
print(f"Modified CSV file '{output_file}' has been created successfully.")
