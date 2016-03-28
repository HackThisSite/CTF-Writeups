with open("sorting-job.in", 'r') as fi:
    dump = fi.read()

splt = dump.split(',')

converted = sorted(map(int, splt), reverse=True)

res = ','.join(map(str, converted))

with open("sorting-job.out", 'w') as fo:
    fo.write(res + "\n")

