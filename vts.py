#!/usr/bin/env python

import cPickle
import os
import sys
import hashlib
import urllib
import urllib2

VT_API2_KEY='31aee15402b09192c5f0d9307edc2e6d2098ad5732b954bb12b4b6539caf39e2'
VT_REPORT_URL='https://www.virustotal.com/vtapi/v2/file/report'
"""
def Serialize(filename, object):
    try:
        fPickle = open(filename, 'wb')
    except:
        return False
    try:
        cPickle.dump(object, fPickle, -1)
    except:
        return False
    finally:
        fPickle.close()
    return True
def Timestamp(epoch=None):
    if epoch == None:
        localtime = time.localtime()
    else:
        localtime = time.localtime(epoch)
    return "%04%02%02-%02%02%02" % localtime[0:6]
"""
filename = sys.argv[1]

def GetHash(filename):
    try:
        hash = hashlib.md5(open(filename, 'rb').read()).hexdigest()
    except:
        print "Hash Calculation Failed"
    return hash

def VTRequestReport(searchHash):
    req = urllib2.Request(VT_REPORT_URL, urllib.urlencode({'resource': searchHash, 'apikey': VT_API2_KEY}))
    try:
        request = urllib2.urlopen(req)
    except:
        print request.getcode()
    try:
        data = request.read()
        print data
    except:
        print request.getcode()
        print "Could Not Read Return Data"

hashed = GetHash(filename)
print hashed
report = VTRequestReport(hashed)
print report

#def main():
 #   oParser = optparse.OptionParser(usage='usage: %prog [options] file \n'
