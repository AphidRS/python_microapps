primero = input('Ingrese primer numero ')
try:
	primero = int(primero)
except:
	primero = 'chanchito feliz'

if primero == 'chanchito feliz':
	print('El valor ingresado no es entero')
	exit()


segundo = input('Ingrese segundo numero ')

try:
	segundo = int(segundo)
except:
	segundo = 'chanchito feliz'


if segundo == 'chanchito feliz':
	print('El valor ingresado no es entero')
	exit()

simbolo = input('ingrese operacion: ')

if simbolo == '+':
	print('Suma:', primero + segundo)
elif simbolo == '-':
	print('Resta:', primero - segundo)
elif simbolo == '*':
	print('Multiplicacion:', primero * segundo)
elif simbolo == '/':
	print('Division:', primero / segundo)
else:
	print('Simbolo no valido')

