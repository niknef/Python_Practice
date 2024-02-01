#Ejercicio Converción Numero 1 (Grados)


print("----Este es un convertor de temperatura----")
gradosFa = int(input("Ingrese los grados Fahrenheit a convertir: "))
gradosCel = (gradosFa - 32)*5/9
print("{}° Fahrenheit son {}° Celsius".format(gradosFa,gradosCel))


#Ejercio Converción Numero 2 (Euro a Libra)



print("----Este es un convertor de moneda----")
libras = float(input("Ingrese la cantidad de Libras a convertir: "))
euro = 1.17
euros = libras * euro
respuesta = "Sus libras equivalen a ${} (Euros)".format(euros)
print(respuesta)