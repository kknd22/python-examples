# A-C-2 = 2*(B-C)
# C = 2*B-A + 2
#
#  4,  1
#  6,  2
#  8,  3
# 10,  4

def solution(A, B):
  big = A
  small = B
  x = 'a'
  y = 'b'
  ll = []
    
  if A == B:
    for _ in range(int(A)):    
       ll.append('ab')
  else:
    if A < B :
      big = B
      small = A
      x = 'b'
      y = 'a'

    ll.append(x+x)
    C = 2*small - big + 2
    for _ in range(small-C):
      ll.append(y+x+x)
    for _ in range(C):
      ll.append(y+x)
   
  return ''.join(ll)
    
print(solution(6, 3))