#funciones de suma y resta (en proceso multiplicacion y division)
def sum(num1,num2):
    sum=num1+num2
    return sum
def res(num1,num2):
    res=num1-num2
    return res
def mult(num1,num2):
    mult=num1*num2
    return mult
def div(num1,num2):
    div=num1/num2
    return div
#input desired operation (en proceso multiplicacion y division)
op=input("Hola, soy una calculadora owo, que operacion deseas realizar (suma o resta): ")
if op!='suma'or'resta':
    print('Eso no lo hago ono!')
if op=='suma':
    print('Has escojido suma')
    num=input('Numero 1: ')
    num1=float(num)
    numd=input('Numero 2: ')
    num2=float(numd)
    suma=sum(num1,num2)
    print('Resultado:',suma)
if op=='resta':
    print('Has escojido resta')
    num=input('Numero 1: ')
    num1=float(num)
    numd=input('Numero 2: ')
    num2=float(numd)
    resta=res(num1,num2)
    print('Resultado:',resta)
