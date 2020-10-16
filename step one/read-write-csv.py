import csv
with open('r-file.csv', newline='') as f:
    reader = csv.DictReader(f)
    with open('w-file.csv', 'w', newline='')as wf:
        fieldnames = ['ip']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow({'ip': f"{row['ip']}"})
