import sys
import subprocess
import shutil
import os
from typing import final

topdir = "topdir"
os.makedirs(topdir, exist_ok = True )
os.makedirs(topdir+'/child1', exist_ok = True )
os.makedirs(topdir+'/child2', exist_ok = True )
os.makedirs(topdir+'/20211118', exist_ok = True )

try :
  tf = open(topdir+"/top.txt", "w+")
  cf1 = open(topdir+"/child1/child1.txt", "w+")
  nf1 = open(topdir+"/20211118/err.log", "w+")

  for i in range(3):
    tf.write("top level content {}\n".format(i))
    cf1.write("child 1 level content {}\n".format(i))
    nf1.write("number level content {}\n".format(i))
finally :
  tf.close()
  cf1.close()
  nf1.close()

result = subprocess.run('''
  #ll=$(find topdir -type d -exec find {} -type f -name "err.log" \;)

  # echo -E $ll | sed -E "s|(.*)/([0-9]{8})/(.*)|\2|g" | uniq
  
  find topdir -type d -exec find {} -type f -name "err.log" \; | sed -E "s|(.*)/([0-9]{8})/(.*)|\2|" | uniq
 
  echo "abc123456fgh" | sed -E "s/(.*)([0-9]{6})(.*)/\2/"
  ''',
  shell=True, 
  check=True,
  executable='/bin/bash')

#print(result)
