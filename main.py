import json,os,urllib.request as r
O=10**5
V=(0,100,320,330,500,900,0)
A=(-33,-31,-18,-14,14,18,31,33);Y=(-17,-15,15,17);Z=(-16,-1,1,16);F=Y+Z
D=(0,0,(A,0),(Y,1),(Z,1),(Y+Z,1),(F,0))
B=[0]*128;S=1;C=0;E=-1;M=0;K=[0,0];N=0;W={};H=0;G=0
class X(Exception):pass
def a(p,s,q):
 global M
 v=abs(p)
 M+=(q if p>0 else -q)*(V[v]+(6-abs((s&7)-3)-abs((s>>4)-3))*(3-6*(v==6)))
def k(s,y):
 for o in (15,17):
  t=s-o*y
  if not t&136 and B[t]==y:return 1
 for ds,v in ((A,2),(F,6)):
  for d in ds:
   t=s+d
   if not t&136 and B[t]==v*y:return 1
 for d in Y+Z:
  t=s
  while 1:
   t+=d
   if t&136:break
   c=B[t]
   if c:
    if c*y in (5,3 if d in Y else 4):return 1
    break
 return 0
def g():
 m=[];s=S
 for q,p in enumerate(B):
  if q&136 or not p or p*s<0:continue
  v=p if p>0 else -p
  if v==1:
   d=16*s;u=q+d;z=7*(s>0)
   if not B[u]:
    m+=[q|(u<<7)|(v<<14)for v in((2,3,4,5)if(u>>4)==z else(0,))]
    if (q>>4)==1+5*(s<0) and not B[u+d]:m.append(q|((u+d)<<7))
   for u in (q+d-1,q+d+1):
    if u&136:continue
    c=B[u]
    if c*s<0 or u==E:m+=[q|(u<<7)|(v<<14)for v in((2,3,4,5)if(u>>4)==z else(0,))]
  else:
   ds,sl=D[v]
   for d in ds:
    u=q
    while 1:
     u+=d
     if u&136:break
     c=B[u]
     if c*s>0:break
     m.append(q|(u<<7))
     if c or not sl:break
 for b,x,e,r in ((1,4,1,3),(2,4,-1,-4),(4,116,1,3),(8,116,-1,-4)):
  if C&b and B[x]==6*s and B[x+r]==4*s and not B[x+e] and not B[x+2*e] and (e>0 or not B[x-3]) and all(not k(n,-s) for n in (x,x+e,x+2*e)):m.append(x|((x+2*e)<<7))
 return m
def y(m,u=None):
 global S,C,E,M
 if u is not None:m,c,d,e,C,E,M,k0,k1=u
 f=m&127;t=(m>>7)&127;r=m>>14
 w=t+1 if t>f else t-2;v=t-1 if t>f else t+1
 if u is None:
  p=B[f];c=B[t];d=-1;e=0
  if not c and t==E and (p==1 or p==-1):d=t-16*S;e=B[d]
  u=(m,c,d,e,C,E,M,K[0],K[1])
  a(p,f,-1)
  if c:a(c,t,-1)
  if d>=0:a(e,d,-1);B[d]=0
  n=r*S if r else p;a(n,t,1);B[f]=0;B[t]=n
  if abs(p)==6 and abs(t-f)==2:
   q=B[w];a(q,w,-1);a(q,v,1);B[w]=0;B[v]=q
  if abs(p)==6:K[p<0]=t
  for b2,s2 in ((1,7),(2,0),(4,119),(8,112),(3,4),(12,116)):
   if f==s2 or t==s2:C&=~b2
  E=f+16*S if abs(p)==1 and abs(t-f)==32 else -1
  S=-S
  return u
 n=B[t];B[t]=c;B[f]=-S if r else n
 if d>=0:B[d]=e
 if abs(B[f])==6 and abs(t-f)==2:B[w]=B[v];B[v]=0
 S=-S;K[0]=k0;K[1]=k1
def o(m):
 if m==H:return 1<<20
 c=B[(m>>7)&127]
 if c:return V[abs(c)]*10
 return 0
def f(d,x,z,l):
 global N,H,G
 N+=1
 if N>=O:raise X
 s=M*S+10
 h=k(K[S<0],-S)
 if d<=0 and not h:
  if s>=z:return z
  if s>x:x=s
 e=(tuple(B),S,C,E)if d>0 else 0;w=W.get(e,0)
 b=-10**6;w2=0;n=0
 H=w
 for m in sorted(g(),key=o,reverse=True):
  t2=(m>>7)&127;c=B[t2]
  if abs(c)==6:continue
  if not h and not c and t2!=E and(d<=0 or d==1 and n and s+150<x):continue
  u=y(m)
  if k(K[S>0],S):y(0,u);continue
  n+=1;r=-f(d-1,-z,-x,l+1);y(0,u)
  if r>b:
   b=r;w2=m
   if r>x:
    x=r
    if x>=z:break
 if not n:
  if h:return -10**5+l
  return 0 if d>0 else x
 if d>0:W[e]=w2
 if l==0:G=w2
 return b
def R():
 global N
 N=0;W.clear();b=0
 for d in range(1,99):
  try:
   f(d,-10**6,10**6,0)
   b=G or b
  except X:break
 return b
def d(n):
 global B,S,C,E,M,K
 B=[0]*128;p=n.split();s=112;M=0;K=[0,0]
 for c in p[0]:
  if c=='/':s-=24
  elif c.isdigit():s+=int(c)
  else:
   x=(1+'PNBRQK'.find(c.upper()))*(1 if c<'a' else -1)
   B[s]=x;a(x,s,1)
   if abs(x)==6:K[x<0]=s
   s+=1
 S=1 if p[1]=='w' else -1;C=sum(1<<j for j in map('KQkq'.find,p[2]) if j>=0)
 E=-1
 if p[3]!='-':E=(int(p[3][1])-1)*16+ord(p[3][0])-97
def p(t,j):
 try:return json.load(r.urlopen(r.Request(os.environ["MAKEFUN_ENV_URL"]+t,data=json.dumps(j).encode(),headers={"content-type":"application/json"})))
 except r.HTTPError:return {"status":"http"}
if __name__=="__main__":
 Q=lambda x:chr(97+(x&7))+str((x>>4)+1)
 while 1:
  e=p("/game",{})
  if e["status"]=="done":break
  while e["status"]=="your_move":
   d(e["fen"]);b=R();t=e["legal_moves"]
   s=Q(b&127)+Q(b>>7&127)+('nbrq'[(b>>14)-2]if b>>14 else '')if b else t[0]
   t=[s]+[x for x in t if x!=s]
   for s in t:
    e=p("/move",{"game":e["game"],"move":s})
    if e.get("status")!="http":break
