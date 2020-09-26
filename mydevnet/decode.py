ip='192.168.50.1/30'

a=ip.split('.')
print(a)

b = str(int(a[3][:-3]) +1 )

new= a[0]+'.'+a[1]+'.'+a[2]+'.'+b+'/30'

print(new)