def dfs(a,target,index,path,res):
    if len(path)==target:
        res.append(path)
        return 
    else:
        for i in range(index,len(a)):
            dfs(a,target,i+1,path+[a[i]],res)
def cs(a,target):
    res=[]
    dfs(a,target,0,[],res)
    return res
def ans(l):
    m=max(l)*len(l)
    s=sum(l)
    return m-s

def answer(a,target):
    mini=100000
    b=cs(a,target)
    for i in b:
        mini=min(mini,ans(i))
    return mini
t=int(input())
c=[]
for i in range(t):
    n,p=map(int,input().split())
    a=list(map(int,input().split()))
    c.append(answer(a,p))
for i in c:
    print(i)
