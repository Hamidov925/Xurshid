def ekub(x,y):
    ekub=1
    if x%y==0:
        return y

    for k in range(int(x/2),0,-1):
        if x%k==0 and y%k==0:
            return k
            break
        

print(ekub(6,4))
print(ekub(16,12))
