import popen2
import re
import sys

cmd = "make %s" % " ".join(sys.argv[1:])
print "RUNNING: ", cmd

out, input = popen2.popen4(cmd)

results = out.readlines()

errors = re.compile(r'.*:.*:\s*([a-z]+):')

