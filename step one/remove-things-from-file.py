infile = "logfile.txt"
outfile = "cleanlogfile.log"

delete_list = ["[", "]:", "]", "fail2ban.", " - "]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "         ")
        fout.write(line)
