a=[0,1,2,3,4,5,6,7,8,9]
b=[]
c=0
while c!=10:
    b.append(list.pop(a))
    c=c+1
print(b)

a=[0,1,2,3,4,5,6,7,8,9]
b=[]
for i in range(0,10):
    b.append(list.pop(a))
print(b)
    
print('\n')

a=[]
c=0
while c!=100:
    a.append((1+c)**2)
    c=c+1
print(a)

a=[]
for i in range(1,101):
    a.append(i**2)
print(a)

print('\n')

a=[]
c=0
while c!=1000:
    a.append(c)
    c=c+1
b= sum(a)/(len(a))
print(b)

a=[]
for i in range(0,1000):
    a.append(i)
b= sum(a)/(len(a))
print(b)
