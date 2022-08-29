#Se importan las funciones trigonometricas y otras
from math import sin, cos, tan, exp, log,sqrt
#Mensaje de bienvenida a la calculadora e integrantes del grupo.
def bienvenida():
  print ("¡Bienvenidos a la Calculadora en Python!")
  print ("")
  print(" ELABORADO POR: ")
  print("- Fabián Perdomo Sierra")
  print("- Oliver Dominguez")
  print("***SECCIÓN C***")
  print("")




def calculadora(e):
  while True:
#Nos dará las posiciones de los caracteres del string (EMPIEZA DE 0)
    cantidad = len(e)-1
#Lo que hicimos fue encontrar el primer espacio para poder validar las expresiones
    l = e.find(" ")
#La única forma que se validara la expresión es si todas estas condiciones se cumplen.
    if e[0] == ("(") and e[cantidad] == ")" and e[l] == " " and e[l+2] == " " and e[1] != " ":
#e2 en este caso se usa para encontrar el primer caracter de la segunda expresión
      e2 = l + 3
#e1 y e3 son las expresiones que se convirtieron a un tipo float. 
      e1 = float(e[1:l])
      e3 = float(e[e2:cantidad])
#Utilizamos condicionales para que pueda leer cual va a ser el operando que se estará usando en la calculadora.
      if e[l+1] == "+":
        print("Respuesta >> ", e1 + e3)
        e = input("Calculadora >> ") 
      elif e[l+1] == "-":
        print("Respuesta >> ", e1 - e3)
        e = input("Calculadora >> ")
      elif e[l+1] == "/":
#La división no se permite entre 0, usamos try-except. 
        try:
          print ("Respuesta >> ", e1 / e3)
          e = input("Calculadora >> ")
        except ZeroDivisionError:
          print ("ERROR! No se Permite la Division Entre 0")
          e = input("Calculadora >> ")
      elif e[l+1] == "*":
        print(e1 * e3)
        e = input("Calculadora >> ")
      elif e[l+1] == "%":
        print("Respuesta >> ", e1 % e3)
        e = input("Calculadora >> ")
#Sale del programa con break    
    elif e == "quit":
      print ("Saliendo...")
      break
#Todas las condiciones para que sea una expresión valida deben cumplirse o se irá al consecuente desplegando un error.
    else:
      print("¡ERROR! Expresión no válida. ")
      e = input("Calculadora >> ")
  
    
#El procedimiento principal que manda a llamar a los procedimientos. 
def main():
  bienvenida()
  e = input("Calculadora >> ") 
  calculadora(e)

main()
  