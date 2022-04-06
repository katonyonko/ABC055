from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="055"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc069_b".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  N=int(input())
  s=input()
  ans=-1
  d={0:'S', 1:'W'}
  for z,o in [[0,0],[0,1],[1,0],[1,1]]:
    tmp=[z,o]
    for i in range(N-2):
      if tmp[-1]==0:
        if s[i+1]=='o': tmp.append(tmp[-2])
        else: tmp.append(1^tmp[-2])
      else:
        if s[i+1]=='o': tmp.append(1^tmp[-2])
        else: tmp.append(tmp[-2])
    if tmp[0]==0 and (s[0]=='o' and tmp[1]==tmp[-1] or s[0]=='x' and tmp[1]!=tmp[-1]) or tmp[0]==1 and (s[0]=='o' and tmp[1]!=tmp[-1] or s[0]=='x' and tmp[1]==tmp[-1]):
      if tmp[-1]==0 and (s[N-1]=='o' and tmp[0]==tmp[N-2] or s[N-1]=='x' and tmp[0]!=tmp[N-2]) or tmp[-1]==1 and (s[N-1]=='o' and tmp[0]!=tmp[N-2] or s[N-1]=='x' and tmp[0]==tmp[N-2]): ans=tmp; break
    
  if ans==-1: print(ans)
  else: print(*[d[ans[i]] for i in range(N)],sep='')
  """ここから上にコードを記述"""

  print(test_case[__+1])