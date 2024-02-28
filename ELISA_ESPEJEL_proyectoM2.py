
# Programa para identificar la longitud de una palabra ingresada
while True:
        palabra = input("Ingrese una palabra: ")
        longitud = len(palabra)
        #Si la  la longitud de la palabra se encuentra en el rango de cuatro a ocho letras se genera la respuesta de la palabra es correcta
        if 4 <= longitud <= 8:
            print("La palabra es correcta.")
            break  # Termina el bucle si la palabra es correcta con el rango de cuatro a ocho letras
        #Si la palabra tiene menos de 4 letras imprime el mensaje "hacen falta letras y su longitud de palabras" 
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")
        #Si la palabra tiene más de 8 letras se indica un mensaje que diga: Sobran letras. Tiene N letras 
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")

#Programa Creado para la ubicación de un Cuadrante
            
# Pedimos al usuario que ingrese las coordenadas de cada punto

x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))


#Una vez conocidos los ejes se mostrara en que cuadrante se encuentra
if x == 0 or y == 0:
    print("Al menos una de las coordenadas es 0. Intente de nuevo.")
else:
    if x > 0 and y > 0:
        print("Cuadrante I")
    elif x < 0 and y > 0:
        print("Cuadrante II")
    elif x < 0 and y < 0:
        print("Cuadrante III")
    elif x > 0 and y < 0:
        print("Cuadrante IV")
    else:
        print("El punto está en un eje o en el origen y no pertenece a ningún cuadrante.")
