"""q=" abcdefghijklmnopqrstuvwxyz"
ex=input("inter a letter").strip().lower()
print(q.find(ex))"""


y=[]
for i in range(97,123):
    y.append(chr(i))
print(y)
x=[x for x in range(26)]
di=dict.fromkeys(y)
for i in range(26):
    di[y[i]]=i+1
print(di)
while True:
    m=input("inter a letter")
    print(di[m.lower()])
    if m==('done'):
        break