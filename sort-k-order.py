# find the kth most frequent words in a string

str = '''
  a a a a a 
  b b b b b b b
  c c c c c c c c
  d d d d d
  e e e
'''
def getKthHighFrequencyWord(s, k):
  strList = s.split()
  dic = {}
  
  for item in strList :
    if item in dic :
      dic[item] = dic[item] + 1
    else:
      dic[item] = 1
  
  sortedTuple = sorted(dic.items(), reverse=True, key= lambda x: x[1])
  wordList=[]
  print(type(sortedTuple))
  index = 0
  for key, v in sortedTuple:
    print ("{}, {}".format(key, v))
    if index < k:
      wordList.append(key)
    index = index + 1
  return wordList

print(getKthHighFrequencyWord(str, 2))  