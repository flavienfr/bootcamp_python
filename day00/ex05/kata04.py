import sys

(day, ex, n1, n2, n3 ) = ( 0, 4, 132.42222, 10000, 12345.67)
sys.stdout.write("day_%02d, ex_%02d : " % (day, ex))
print("%.2f, " % round(n1,2), end = '')
print("%.2e, " % n2, end = '')
print("%.2e" % n3)
