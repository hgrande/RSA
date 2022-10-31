# Algoritmo RSA  
# GENERACIÓN DE CLAVES
# a) Clave pública
# Elegimos dos números primos aleatorios. 
# Podemos utilizar el programa Generador de primos aleatorios
import random
limite_usuario = int(input("Introduce un valor máximo. Si no quieres especificarlo, pulsa 0 y trabajaremos sin límite máximo"))
if(limite_usuario == 0):
    limite = 100000
    
    
else:
    limite = limite_usuario
    
p = random.randrange(2,limite)
q = random.randrange(2,limite)
prim = 0
def primo(numero):
    divisores = []
    prim = 0 
    
    for i in range(2,numero):
        if(numero % i == 0 ):
        
            prim = prim + 1
            divisores.append(i)
            divisores_str = str(divisores)
            
        
    return prim       
   
# Mientras prim valga distinto de 0 , tenemos que seguir generando números
while(primo(p)!=0):
    p = random.randrange(2,limite)
    primo(p)
print(p)

while(primo(q)!=0):
    q = random.randrange(2,limite)
    primo(q)
print(q)



# Los multiplicamos

n = p*q
n_string = str(n)

# Calculamos z=(p-1)*(q-1)

z = (p-1)*(q-1)
print(z)

# Calculamos un k tal que 1<k<z primo con z (es decir, MCD(k,z) = 1)

for i in range(2,z):
    if ((z % i) != 0) :
        k = i
k_string = str(k)
print(k)

print("La clave pública es ("+n_string+","+k_string+")")

# b) Clave privada

# Necesitamos un j tal que k*j = 1(mod z) ; es decir, el resto de dividir k^j entre z es 1

j = k
resto = 0
while (resto != 1):
    j = j + 1
    resto = (k*j) % z
j_string = str(j)
print("La clave privada es "+j_string)

# Ciframos un mensaje

mensaje = int(input("Introduce el mensaje que quieras cifrar:"))
# El mensaje cifrado es el resto de dividir el mensaje elevado a k entre n
texto_cifrado = (mensaje ** k) % n
texto_cifrado_string = str(texto_cifrado)
print("Tu mensaje cifrado es "+texto_cifrado_string)

# Esto significa que si nuestro mensaje original era el número 14, vamos a enviarle al destinatario el número 20, 
# que es el número 14 cifrado con RSA utilizando la clave pública del destinatario. 
# Cualquier intermediario que «vea» pasar el 20 no podrá obtener, en un tiempo útil (por lo menos hasta ahora) 
# el valor 14 solo disponiendo del 20 y de la clave pública del destinatario, en este caso, n y k.

# Ahora, el destinatario utilizará la clave privada para descifrar el mensaje

texto_descifrado = (texto_cifrado ** j) % n 
texto_descifrado = str(texto_descifrado)

print("El texto descifrado es "+texto_descifrado)














