import sys

(hour, minutes, year, month, day) = (3,30,2019,9,25)

sys.stdout.write("%02d/%02d/%02d %02d:%02d\n" % (month, day, year, hour, minutes))
