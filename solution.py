def precios(precio: int):
    # Cambiar el valor de esta variable como corresponde
   
    if precio < 4:
     print("Entra Gratis")
    elif precio >= 4 and precio <= 18 :
     print("Tiene que pagar 5 monedas")
    elif precio > 18: 
     print("Tiene que pagar 10 monedas")
    else:
     print("Usted es mayor de edad ")
     print("No puede entrar")
   
    

    return precio

print("Empresa de videos juegos el Mundo es perfecto")
precio = int(input("Introduzca la edad del jugador: "))
r = precios(precio)




def triangulo(n: int):
 

 return "\n".join([" "*(n-i)+"*"*(i+i-1) for i in range(1,n+1)])
 
 
numero = int(input('Introduce el número de filas del triángulo: '))
print(triangulo(numero))
