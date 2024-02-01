
def largo_string(mi_string):
    largo = 0
    for n in mi_string:
        largo += 1
    return largo


texto = input("Introduce un texto: ")


largo_de_mi_string = largo_string(texto)


print("\n" + "El largo de mi string es de {}".format(largo_de_mi_string) + "\n")


def main():
    numero = int(input("Introduce un digito: "))

    potencia = int(input("Troduce la potencia: "))

    resultado = numero ** potencia

    print("El numero {}, elevado a {} es igual a {}".format(numero, potencia, resultado))


if __name__ == "__main__":
    main()