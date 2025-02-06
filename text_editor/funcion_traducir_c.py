def traducir_c_a_python(codigo_c):
    lineas = codigo_c.split("\n")
    codigo_python = []
    
    for linea in lineas:
        # Eliminar punto y coma al final
        linea = linea.strip().rstrip(";")

        # Reemplazar palabras clave
        for clave, valor in conversion_dict.items():
            linea = linea.replace(clave, valor)

        # Convertir printf y scanf
        if "print" in linea:  # printf -> print
            linea = linea.replace('print(', 'print(')
        if "input" in linea:  # scanf -> input
            linea = linea.replace('input(', 'input(')

        codigo_python.append(linea)

    return "\n".join(codigo_python)
