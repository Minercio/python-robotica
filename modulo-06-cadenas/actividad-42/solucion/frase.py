lectura = "  el sensor mide distancia  "
limpia = lectura.strip()
mayusculas = limpia.upper()

print("mayusculas", mayusculas)
print("len(mayusculas)", len(mayusculas))

palabras = mayusculas.split()
print('"-".join(palabras)', "-".join(palabras))
