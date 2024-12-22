st = input("Please input the string")
i = 0
j=0
l=0
n=len(st)
result=''
g=0
for k in range(1,n-1):
        if (st[k]==st[k-1]) or (st[k]==' ') or (result== st[i:j+1]):
                j=k-1
                
                if j-i+1>=l:
                        l=j-i+1
                        result=st[i:j+1]
                i=k

                if st[k]==' ':
                        i+=1
print(f'the longest substr is {result}')
                        
