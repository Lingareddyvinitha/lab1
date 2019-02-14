import random
def matrix_multiplication(r,g):
  m=len(r)
  n=len(r[0])
  a=len(g)
  b=len(g[0])
  s=[]
  s=[[random.random()for col in range(b)]for row in range(m)]
  if(n==a):
    for i in range(len(r)):
      for j in range(len(g[0])):
        s[i][j]=0
        for k in range(len(g)):
          s[i][j] += r[i][k]*g[k][j]
        print s[i][j],'\t',
      print
  else:
    print "multiplication is not possible"
r=input('enter matrix1')   #ex:r=[[1,2,3],[2,3,3]]
g=input('enter matrix2')
matrix_multiplication(r,g)