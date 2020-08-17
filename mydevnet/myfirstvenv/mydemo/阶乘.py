i = 1
while i <= 9:

    j = 1
    while j <= i:
        mut = i * j
        print('%d*%d=%d'%(i , j , mut), end='  ')
        j+=1
    print("")
    i+=1