vocales = [" "]
comas = [","]
puntos = ["."]
comentario_de_usuario = input("Comenta algo")
nespacios = 0
for letra in comentario_de_usuario:
    if letra in vocales:
         nespacios += 1
print("Espacios encontradoss: {}".format(nespacios))

ncomas = 0
for letra in comentario_de_usuario:
    if letra in comas:
         ncomas += 1
print("Comas encontradas: {}".format(ncomas))

npuntos = 0
for letra in comentario_de_usuario:
    if letra in puntos:
         npuntos += 1
print("Puntostrados: {}".format(npuntos))