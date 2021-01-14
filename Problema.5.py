with open("input.txt","r") as f:
    a=f.readline()
for i in a:
    #a)
    if (ord(i)>=65) and (ord(i)<=90):
        with open("literaA.txt","a") as f:
            f.write(str(i))
    #b)
    elif (ord(i)>=48) and (ord(i)<=57):
        with open("cifre.txt","a") as f:
            f.write(str(i))
    #c)
    elif((ord(i)>=33)and(ord(i)<=47))or((ord(i)>=58)and(ord(i)<=64))or((ord(i)>=91)and(ord(i)<=96))or((ord(i)>=123)and(ord(i)<=127)):
        with open("operatori.txt","a") as f:
            f.write(str(i))
    #d)
    else:
        with open("literaB.txt","a") as f:
            f.write(str(i))
