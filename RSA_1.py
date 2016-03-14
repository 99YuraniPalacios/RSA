# TRABAJO ALGORITMO RSA 
# Presentado por: Yurani Melisa Palacios Palacios 
# Estudiante Compuacion Cientifica "Primer Semestre" 
# Presentado a: Docente Carlos Andres Vera Ciro 
# Universidad de Medellin 
# 2016 


# PROBLEMA 1 

# Escriba una funcion que dados dos numeros primos p y q genere las llaves publica y privada del algoritmo RSA:
# e, d, N = myrsa (p, q)


# Desarrollo::


# Funcion para encontar el minimo entre dos numeros

def minimo (x, y):
          if x<y:
              return x
          else:
              return y


# Funcion que nos defina el MCD (Minimo Comun Multiplo) de los dos numeros. 

def mcd(x, y):

	m = minimo (x,y)
	for i in range (m, 0,-1):
		if x%i == 0 and y%i ==0:
			return i


# Funcion que si dos numeros son coprimos arroja 1, sino 0.

def arecoprime (x,y):

        m= mcd (x,y)
	if m == 1:
		return 1
	else:
		return 0

# Funcion que muestra si un numero es primo, si lo es imprime 1 sino lo es imprie 0

def isprime (k):
     
    for i in range(2, k):
          if k % i == 0:
                  return 0

    return 1 

# Dos numeros primos "p" y "q".
# Calcular un numero "N" que es igual a la multiplicacion de los numeros primos "p" y "q".
# Calcular un numero mas, "phi_N" que es igual a la multiplicacion de (p-1) y (q-1).
# Escoger un numero "e" este debe cumplir dos condiciones ser menor que phi(n) y el MCD (e, phi_N) debe ser igual a 1. 
# Buscar un numero "d" que debe ser el inverso modular de "e".


# Definir los resultados de (N, e) y (N, d)

def myrsa (p, q):
          if isprime (p)==0 or isprime (q)==0:
              return " Los numeros no son primos "

          else :
              
             N = p * q
             phi_N = (p-1) * (q-1)

          for e in range(2, phi_N + 1):
	     		if arecoprime (phi_N, e) == 1:
				e
	  for d in range(0, phi_N * 3):
			if e * d % phi_N == 1:
				d  

          print "llave publica: (",e,",",N,")"
	  print "llave privada: (",d,",",N,")"

print myrsa (2, 7) 



















