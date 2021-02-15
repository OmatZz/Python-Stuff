def comppay(h,r):
    if h>40.0:
        pay=(h-40.0)*(1.5*r)+(40.0*r)
        return pay
    else:
        pay=h*r
        return pay
#input
hrs=input('Enter Hours ')
h=float(hrs)
rate=input('Enter Rate ')
r=float(rate)
p=comppay(h,r)
print('Pay',p)
