import csv
file_name="filehandling/csv-handling/data2.csv"
'''with open(file_name, mode="a") as file:
    writer = csv.writer(file)
    for i in range(1):
        writer.writerow(["This is a row writen by developer","this one also"])'''
with open(file_name, mode="r") as file:
    row = csv.reader(file)
    for i in row:
        for j in i:
            print(j)

            


