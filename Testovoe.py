s = input("Введите строку: ")
ps = input("Введите подстроку: ")
symb1 = '['
symb2 = ']'
a=[]
b=[]
c=0
q=0
for i in range(len(s)):
    if s[i]==symb1:
        a.append(i)
        q+=1
        c+=1

    elif s[i]==symb2:
        b.append(i)
        q-=1
        if q==0:
            z = a[0]
            y = b[c-1]
            q=999999
print(s.replace(s[z:y+1], ps))
