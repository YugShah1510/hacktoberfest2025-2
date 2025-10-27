n = int(input())
d= int(input())
s=0
while n>0:
    dig=n%10
    if dig==d:
        s+=1
    
    n=n//10
print(s)
