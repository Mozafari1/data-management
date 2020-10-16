import csv
with open('r-file.csv', newline='') as f:
    reader = csv.DictReader(f)
    with open('w-file.csv', 'w', newline='')as wf:
        fieldnames = ['date_1', 'action', 'server_port',
                      'message', 'ssh', 'perform', 'ip', 'date_2']
        writer = csv.DictWriter(wf, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if(row['ip'] == 'already banned'):
                ips = row['ip']
                per = row['perform']
                temp = ips
                ips = per
                per = temp
                writer.writerow({'date_1': row['date_1'], 'action': row['action'], 'server_port': row['server_port'],
                                 'message': row['message'], 'ssh': row['ssh'], 'perform': per, 'ip': ips, 'date_2': row['date_2']})

            else:
                writer.writerow({'date_1': row['date_1'], 'action': row['action'], 'server_port': row['server_port'],
                                 'message': row['message'], 'ssh': row['ssh'], 'perform': row['perform'], 'ip': row['ip'], 'date_2': row['date_2']})
