import csv

with open("student.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID","Name","Age"])
    writer.writerow(["001","Ohmkar","23"])
    writer.writerow(["002","Reddy","25"])
    writer.writerow(["003","Sunny","24"])