def solution(A, B):
  ss = []
  def rec (X, Y):
    if ( abs(X-Y) < 2 ):
      if ss and (ss[-1] == 'a'):
        for _ in range(min(X,Y)):
          ss.append('b')
          ss.append('a')
      else : 
        for _ in range(min(X,Y)): 
          ss.append('a')
          ss.append('b')
      if X > Y:
        ss.append('a')
      elif Y > X:
        ss.append('b')
    else:
      if X > Y :
        ss.append('a')
        ss.append('a')
        if (Y > 0):
          ss.append('b')
          rec(X-2, Y-1)
        else:
          return
      else:
        ss.append('b')
        ss.append('b')
        if ( X > 0):
          ss.append('a')
          rec(X-1, Y-2)
        else:
          return
    
  rec(A,B) 
  return ''.join(ss)
    
print(solution(5, 3))