from datetime import date
from itertools import product


print("Hola impresión desde la consola") #Impresion de codigo

sum = 1 + 2 #Usando operadores
product= sum * 2
print(product)


date.today() #Usando fechas

print("La fecha de hoy es: "+str(date.today()))


print("Bienvenido al programa de bienvenida!") #Guardar informacion en variables
name=input("Introduzca su nombre: ")
print("Saludos "+name)

print("Programa de Calculadora")
primernum=input("Ingrese el primer numero: ")
segundonum=input("Ingrese el segundo numero: ")
print(int(primernum)+int(segundonum))