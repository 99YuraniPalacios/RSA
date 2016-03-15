#         TRABAJO ALGORITMO RSA 
# Presentado por: Yurani Melisa Palacios Palacios 
# Estudiante Compuacion Cientifica "Primer Semestre" 
#   Presentado a: Docente Carlos Andres Vera Ciro 
#         Universidad de Medellin 
#                 2016 


# Problema 2

# Escriba una funcion (Python sugerido) que dada la clave publica de RSA y un mensaje compuesto de cuatro numeros codificados m1, m2, m3, m4 en el rango 0-9 desencripte el mensaje formado por estos cuatro numeros

# n1 , n2 , n3 , n4 = hackrsa (e, N, m1 , m2 , m3 , m4)


# DESARROLLO 

# Se pide la clave publica y los 4 numeros de el mensaje codificado, luego se buscan los numeros primos entre 2 y N para hallar p y q

# Despues de tener e,N la llave publica y d, N la llave privada, se empieza a desencriptar el mensaje


def hackrsa(e,N,n1,n2,n3,n4):
	for i in range(2,N):
		for j in range(2,N):
			if esprimo(i)==1 and esprimo(j)==1 and i*j == N:
				phi=(i-1) * (j-1)
	for d in range(phi*2):
		if e*d%phi== 1:
			d
	m1 = n1**d%N
	m2 = n2**d%N
	m3 = n3**d%N
	m4 = n4**d%N
	print "id_pub: (",e,",",N,")"
	print "id_priv: (",d,",",N,")"
	return m1, m2, m3, m4

	
# Para imprimir el mensaje decodificado imprimimos un mensaje para decir que este es el mensaje


m1, m2,m3,m4 = hackrsa(5,14,4,4,4,4)
print "Mensaje decodificado"
print "- ",m1,m2,m3,m4


