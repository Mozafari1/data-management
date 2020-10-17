l = ['162.10.2.1', '162.10.2.1', '162.10.2.1', '192.34.1.10', '172.11.2.9']
d = {}
for v in l:
    d[v] = d.get(v, 0) + 1

for k, v in sorted(d.items()):
    print('%s - %s' % (k, v))
