print("Conversion de Fº a Cº")
x = int(input("Intruduce la temperatura en Fª: "))
print(x)
print("la temperatura en Cº es: ")
y = ((x-32)*5)/9
print(y)

print("Conversion de Libra a Euro")
x = float(input("introduce el valor de la moneda en Libras: "))
print(x)
print("El valor de la moneda en Euros es: ")
y = float(x*1.16)
print(y)


#---------------------------------------
print("¡Bienvenido a mi conversor de libras a euros!")

numero1 = int(input("Introduce el monto de libras: "))
numero2 = float(input("Introduce el cambio: "))

a = numero1*numero2

print("Tu cambio es: {}".format(a))
print("Estamos a tu orde!")