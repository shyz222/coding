# 実行時間5sに対しO(n^5)=10^10程度なので全探索で求める
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(0,n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            for l in range(k+1,n):
                for m in range(l+1,n):
                    if a[i]+a[j]+a[k]+a[l]+a[m]==1000:
                        ans+=1
print(ans)