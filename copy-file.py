import shutil
original = r'fail2ban.log.4'
target = r'logfile.txt'

shutil.copyfile(original, target)
