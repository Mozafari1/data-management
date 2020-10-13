import shutil

infile = "cleanlogfile.log"
outfile = "cleanestlogfile.log"
original = r'cleanestlogfile.log'
target = r'cleanlogfile.log'

delete_list = ["already"]
with open(infile) as fin, open(outfile, "w+") as fout:
    for line in fin:
        for word in delete_list:
            line = line.replace(word, "         already")
        fout.write(line)


shutil.copyfile(original, target)
