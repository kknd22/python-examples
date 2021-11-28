import sys
import os
import subprocess
import shutil
import re

topdir = "topdir"
os.makedirs(topdir, exist_ok = True )
os.makedirs(topdir+'/child1', exist_ok = True )
os.makedirs(topdir+'/child2', exist_ok = True )
os.makedirs(topdir+'/20211118', exist_ok = True )
os.makedirs(topdir+'/20210929', exist_ok = True )

try :
  tf = open(topdir+"/top.txt", "w+")
  cf1 = open(topdir+"/child1/child1.txt", "w+")
  nf1 = open(topdir+"/20211118/err.log", "w+")
  nf2 = open(topdir+"/20210929/err.log", "w+")

  for i in range(3):
    tf.write("top level content {}\n".format(i))
    cf1.write("child 1 level content {}\n".format(i))
    nf1.write("number level content {}\n".format(i))
    nf2.write("number level content {}\n".format(i))
finally :
  tf.close()
  cf1.close()
  nf1.close()
  nf2.close()

ll = set()
for path, dir, fn in os.walk("./topdir") :
  for j in fn:
    if (j == "err.log") :
      ll.add(os.path.join(path, j))

print ("---------multi capture-------------------")
pattern = re.compile(r".*/(\d{8})/.+log")
for i in ll:
  for match in pattern.finditer(i):
    print (match.group(1))

print ("---------simple capture-------------------")
for i in ll:
  r = re.search(r".*/(\d{8})/.+log", i)
  print(r.group(1))    